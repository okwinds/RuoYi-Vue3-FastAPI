#!/usr/bin/env python3
"""
生成 Endpoint → Controller → Service.method 的静态映射（尽量不依赖运行时）。

设计目标：
- 仅用 Python 标准库，避免 import FastAPI app 带来的副作用/环境依赖。
- 通过 AST 解析 controller 源码，提取：
  - APIRouterPro/APIRouter 的 prefix
  - 路由装饰器（get/post/put/delete/patch）的 method + path + summary
  - handler 函数中直接调用的 Service/Dao/Util 的方法名（启发式）

注意：
- 这是“可复刻索引”用途的静态工具，输出用于快速定位实现入口。
- 解析规则是启发式：例如 service 调用可能发生在 helper、依赖注入或多层封装中；
  这种情况会在输出中体现为 service_calls 为空，需要人工补充。
"""

from __future__ import annotations

import argparse
import ast
import datetime as _dt
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


HTTP_METHOD_ATTRS = {"get", "post", "put", "delete", "patch"}
ROUTER_FACTORY_NAMES = {"APIRouterPro", "APIRouter"}


@dataclass(frozen=True)
class RouteItem:
    http_method: str
    full_path: str
    summary: str | None
    controller_file: str
    router_var: str
    handler_func: str
    service_calls: tuple[str, ...] = field(default_factory=tuple)


def _is_str_const(node: ast.AST) -> bool:
    return isinstance(node, ast.Constant) and isinstance(node.value, str)


def _get_str_const(node: ast.AST, default: str | None = None) -> str | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return default


def _join_paths(prefix: str, path: str) -> str:
    prefix = prefix or ""
    path = path or ""
    if not prefix and not path:
        return "/"
    if not prefix:
        joined = path
    elif not path:
        joined = prefix
    else:
        if prefix.endswith("/") and path.startswith("/"):
            joined = prefix + path[1:]
        elif not prefix.endswith("/") and not path.startswith("/"):
            joined = f"{prefix}/{path}"
        else:
            joined = prefix + path
    # normalize
    while "//" in joined:
        joined = joined.replace("//", "/")
    if not joined.startswith("/"):
        joined = "/" + joined
    return joined


class _ServiceCallCollector(ast.NodeVisitor):
    def __init__(self) -> None:
        self.calls: list[str] = []

    def visit_Call(self, node: ast.Call) -> None:
        # 捕获形如 X.y(...) 的调用
        func = node.func
        if isinstance(func, ast.Attribute) and isinstance(func.value, ast.Name):
            class_name = func.value.id
            method_name = func.attr
            # 只收集“类.方法”这种稳定可读的调用点
            self.calls.append(f"{class_name}.{method_name}")
        self.generic_visit(node)


def _is_relevant_class_name(class_name: str) -> bool:
    """
    过滤“实现入口”相关调用点，降低噪音。

    目标：
    - 主要保留 Service/Dao/Util（以及少量本仓库约定的 Util）
    - 排除 logger/ResponseUtil/datetime/uuid 等通用调用
    """

    noisy = {
        "logger",
        "ResponseUtil",
        "datetime",
        "uuid",
        "os",
        "json",
    }
    if class_name in noisy:
        return False
    if class_name.endswith(("Service", "Dao", "Util")):
        return True
    return False


def _extract_router_prefixes(module: ast.Module) -> dict[str, str]:
    """
    从 module 顶层语句中提取 router_var -> prefix 的映射。
    """
    prefixes: dict[str, str] = {}
    for node in module.body:
        if not isinstance(node, ast.Assign):
            continue
        if len(node.targets) != 1 or not isinstance(node.targets[0], ast.Name):
            continue
        var_name = node.targets[0].id
        call = node.value
        if not isinstance(call, ast.Call):
            continue
        func = call.func
        if not isinstance(func, ast.Name) or func.id not in ROUTER_FACTORY_NAMES:
            continue
        prefix = ""
        for kw in call.keywords or []:
            if kw.arg == "prefix":
                prefix = _get_str_const(kw.value, "") or ""
        prefixes[var_name] = prefix
    return prefixes


def _extract_routes_from_file(path: Path, repo_root: Path) -> list[RouteItem]:
    text = path.read_text(encoding="utf-8")
    module = ast.parse(text, filename=str(path))
    prefixes = _extract_router_prefixes(module)

    routes: list[RouteItem] = []

    for node in module.body:
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        handler_name = node.name
        # service calls (heuristic)
        collector = _ServiceCallCollector()
        # 只解析函数体，避免把 decorator 中的 router.get/post(...) 计入调用点
        for stmt in node.body:
            collector.visit(stmt)
        service_calls = []
        seen = set()
        for item in collector.calls:
            class_name = item.split(".", 1)[0]
            if not _is_relevant_class_name(class_name):
                continue
            if item not in seen:
                seen.add(item)
                service_calls.append(item)

        for deco in node.decorator_list:
            if not isinstance(deco, ast.Call):
                continue
            if not isinstance(deco.func, ast.Attribute):
                continue
            if not isinstance(deco.func.value, ast.Name):
                continue
            router_var = deco.func.value.id
            http_method = deco.func.attr
            if http_method not in HTTP_METHOD_ATTRS:
                continue
            # path: first positional arg string, else empty string
            route_path = ""
            if deco.args:
                route_path = _get_str_const(deco.args[0], "") or ""
            summary = None
            for kw in deco.keywords or []:
                if kw.arg == "summary" and _is_str_const(kw.value):
                    summary = _get_str_const(kw.value)
            prefix = prefixes.get(router_var, "")
            full_path = _join_paths(prefix, route_path)
            rel_controller = path.relative_to(repo_root).as_posix()

            routes.append(
                RouteItem(
                    http_method=http_method.upper(),
                    full_path=full_path,
                    summary=summary,
                    controller_file=rel_controller,
                    router_var=router_var,
                    handler_func=handler_name,
                    service_calls=tuple(service_calls),
                )
            )

    return routes


def _iter_controller_files(backend_root: Path) -> Iterable[Path]:
    # 标准目录：**/controller/*.py，排除模板与 __init__.py
    for p in backend_root.rglob("controller/*.py"):
        if p.name.startswith("__"):
            continue
        if "templates" in p.parts:
            continue
        yield p


def _to_md(routes: list[RouteItem], backend_root: Path, repo_root: Path) -> str:
    now = _dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S %Z").strip()
    route_count = len(routes)
    controller_files = sorted({r.controller_file for r in routes})

    lines: list[str] = []
    lines.append("# Handler Map（Endpoint → Controller → Service.method）")
    lines.append("")
    lines.append(f"generated: `{now}`")
    lines.append("")
    lines.append(
        "用途：把接口（endpoint）与其实现入口（controller + service 方法）稳定对齐，便于："
    )
    lines.append("- 从任意 endpoint 反查到 controller handler 与 service 入口；")
    lines.append("- 将字段级契约（`openapi.json`）与“内部等价复刻”方法规格连接起来；")
    lines.append("- 做审查抽样与回归定位。")
    lines.append("")
    lines.append("生成方式（可复跑）：")
    lines.append("")
    lines.append("```bash")
    lines.append("python tools/spec/gen_handler_map.py \\")
    lines.append("  --backend-root ruoyi-fastapi-backend \\")
    lines.append("  --out docs/codebase-spec/03_API/HANDLER_MAP.md")
    lines.append("```")
    lines.append("")
    lines.append("说明：")
    lines.append(
        "- 该映射通过 AST 静态解析 controller 文件生成，为启发式结果；当 `service_calls` 为空时，通常表示业务逻辑被封装在 helper/依赖注入中，需要人工补齐。"
    )
    lines.append(
        f"- 扫描 controller 文件数：`{len(controller_files)}`；提取路由数：`{route_count}`。"
    )
    lines.append("")
    lines.append("## Route Table")
    lines.append("")
    lines.append(
        "| HTTP | Path | Summary | Controller | Handler | Service calls (heuristic) |"
    )
    lines.append("| --- | --- | --- | --- | --- | --- |")
    for r in routes:
        summary = (r.summary or "").replace("|", "\\|")
        service_calls = "<br/>".join(r.service_calls) if r.service_calls else ""
        lines.append(
            f"| `{r.http_method}` | `{r.full_path}` | {summary} | `{r.controller_file}` | `{r.handler_func}` | {service_calls} |"
        )
    lines.append("")
    lines.append("## Source")
    lines.append("")
    lines.append(
        f"- Controllers root: `{backend_root.relative_to(repo_root).as_posix()}`"
    )
    lines.append(
        "- Router auto-registration: `ruoyi-fastapi-backend/common/router.py`（`auto_register_routers`）"
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Handler Map markdown")
    parser.add_argument("--repo-root", default=".", help="Repo root (default: .)")
    parser.add_argument(
        "--backend-root", default="ruoyi-fastapi-backend", help="Backend root dir"
    )
    parser.add_argument("--out", default="", help="Output markdown file path")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    backend_root = (repo_root / args.backend_root).resolve()
    if not backend_root.exists():
        raise SystemExit(f"backend_root not found: {backend_root}")

    all_routes: list[RouteItem] = []
    for controller_file in _iter_controller_files(backend_root):
        all_routes.extend(_extract_routes_from_file(controller_file, repo_root))

    all_routes.sort(
        key=lambda r: (r.full_path, r.http_method, r.controller_file, r.handler_func)
    )
    md = _to_md(all_routes, backend_root, repo_root)

    if args.out:
        out_path = (
            (repo_root / args.out).resolve()
            if not Path(args.out).is_absolute()
            else Path(args.out).resolve()
        )
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(md, encoding="utf-8")
    else:
        print(md, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
