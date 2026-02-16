# OpenAPI Snapshot（字段级接口契约快照）

目的：为“可复刻级”交付提供**字段级**的 API 契约来源，补齐仅靠 `ENDPOINTS.md`（清单级）无法覆盖的请求/响应 schema 细节。

本仓库已将一次导出的 OpenAPI 快照固化在代码库中：
- `docs/codebase-spec/03_API/openapi.json`：OpenAPI 3.x JSON（建议作为复刻的“契约真源”）
- `docs/codebase-spec/03_API/openapi.sha256`：快照校验值（用于防止误改/漂移）
- `docs/codebase-spec/03_API/OPERATION_MAP.md`：端点 → schema/认证映射（从快照生成）
- `docs/codebase-spec/03_API/SCHEMA_CATALOG.md`：schema 名称索引（从快照生成）

> 复刻目标：即便不阅读源码，也能通过 `openapi.json` 复刻出所有 endpoint 的字段、校验、响应结构，并用它驱动 SDK/Mock/Contract Test。

---

## 1) 如何使用该快照（复刻建议）

推荐把 `openapi.json` 作为契约源，执行以下动作：
- 生成 API SDK（前端/测试/第三方集成）
- 生成 Mock Server（用于 UI 开发、E2E 预跑）
- 做契约测试（CI 中比对 schema drift）

注意事项（与本仓库实现一致）：
- 统一响应结构：后端几乎所有响应均为 HTTP 200，并在 JSON 体中返回业务 `code`（见 `docs/codebase-spec/03_API/ERRORS.md` 与 `ruoyi-fastapi-backend/utils/response_util.py`）。
- 认证标记：在 OpenAPI 中，`security` 存在时表示需要 Bearer Token（前端 axios 会在默认情况下加 `Authorization: Bearer <token>`）。

---

## 2) 如何重新导出（在同栈复现/升级时）

推荐导出方式：**通过导入 FastAPI app 并调用 `app.openapi()`**（无需真正启动服务/连接 DB 生命周期）。

示例（在 `ruoyi-fastapi-backend/` 目录执行）：

```bash
# 建议保证 UTF-8 locale（某些 macOS/终端环境可能会出现 ascii 解码错误）
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8

python - <<'PY'
import json
from app import app
o = app.openapi()
with open('../docs/codebase-spec/03_API/openapi.json', 'w', encoding='utf-8') as f:
    json.dump(o, f, ensure_ascii=False, indent=2, sort_keys=True)
print('paths', len(o.get('paths', {})))
PY

shasum -a 256 ../docs/codebase-spec/03_API/openapi.json | awk '{print $1}' > ../docs/codebase-spec/03_API/openapi.sha256
```

如果导入时出现“可选 AI SDK/客户端未安装”导致 `module_ai` 路由无法注册，需要补齐对应依赖后再导出（以保证 AI 端点也被纳入快照）。

