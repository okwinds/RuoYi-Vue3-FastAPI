# OpenAPI 导出与接口文档路径（Swagger/ReDoc）

本项目对 FastAPI 的文档路由做了自定义与“代理路径”封装（见 `ruoyi-fastapi-backend/utils/server_util.py`），用于解决“通过后端地址直接访问文档”的兼容问题，并支持在生产环境关闭文档。

---

## 1) 文档与 OpenAPI 的路径约定

> 以下路径均以后端运行地址为前缀：`http://<host>:<port>`  
> 若后端启用了 `APP_ROOT_PATH`（Uvicorn `root_path`），外部访问路径可能需要追加该前缀。

### 1.1 OpenAPI JSON

- 原始 OpenAPI：`/openapi.json`
- 代理 OpenAPI：`/proxy-openapi.json`（当 Swagger 与 ReDoc 都未被禁用时启用）

### 1.2 Swagger UI

- 原始：`/docs`
- 代理：`/proxy-docs`

### 1.3 ReDoc

- 原始：`/redoc`
- 代理：`/proxy-redoc`

---

## 2) 如何导出 OpenAPI（推荐）

> 如果你的目标是“复刻级”交付，建议优先使用仓库内固化的快照：`docs/codebase-spec/03_API/openapi.json`（见 `OPENAPI_SNAPSHOT.md`）。

### 2.1 方式一：HTTP 直接下载（推荐）

1) 启动后端（开发环境）  
2) 下载 OpenAPI JSON（示例）：

```bash
curl -fsSL "http://127.0.0.1:9099/openapi.json" -o openapi.json
```

如果启用了 `APP_ROOT_PATH`，示例：

```bash
curl -fsSL "http://127.0.0.1:9099<APP_ROOT_PATH>/openapi.json" -o openapi.json
```

### 2.2 方式二：通过代理路径下载

当需要与“代理 docs 页面”保持一致时，可用：

```bash
curl -fsSL "http://127.0.0.1:9099/proxy-openapi.json" -o openapi.json
```

### 2.3 方式三：从源码导出（不依赖启动 HTTP 服务）

适用：
- CI/离线环境
- 想导出“当前分支/当前代码”对应的 schema 快照

在 `ruoyi-fastapi-backend/` 目录执行：

```bash
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8

python - <<'PY'
import json
from app import app
with open('openapi.json', 'w', encoding='utf-8') as f:
    json.dump(app.openapi(), f, ensure_ascii=False, indent=2, sort_keys=True)
print('exported openapi.json')
PY
```

---

## 3) 关闭文档的行为（生产安全）

关闭策略由环境变量控制（见 `docs/codebase-spec/01_Configuration/FEATURE_FLAGS.md`），典型为：
- `APP_DISABLE_SWAGGER=true`：Swagger UI 关闭（代理路径返回禁用提示页）
- `APP_DISABLE_REDOC=true`：ReDoc 关闭

复刻要求：
- 在生产环境必须能关闭接口文档入口；
- 关闭后不应影响业务 API 的正常访问。
