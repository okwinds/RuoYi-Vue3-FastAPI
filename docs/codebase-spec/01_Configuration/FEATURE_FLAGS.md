# Feature Flags（功能开关 / 行为差异）

本文件描述对系统行为影响显著的开关（Feature Toggles / Flags），以便复刻时能还原同样的“运行策略”。

来源：
- 后端：`ruoyi-fastapi-backend/config/env.py` 与 `ruoyi-fastapi-backend/.env.*`
- 前端：`ruoyi-fastapi-frontend/.env.*` 与 `ruoyi-fastapi-frontend/src/settings.js`、`src/store/modules/settings.js`

---

## 1) Active Flags（当前生效开关）

> 完整变量表见：`docs/codebase-spec/01_Configuration/ENVIRONMENT.md`。

| Flag | Type | Default（dev） | Description | Affects |
| --- | --- | --- | --- | --- |
| `APP_RELOAD` | bool | `true` | 是否开启热重载（开发环境建议开启，生产关闭） | 后端启动方式（uvicorn reload） |
| `APP_IP_LOCATION_QUERY` | bool | `true` | 是否启用 IP 归属地查询 | 登录/日志等信息展示 |
| `APP_SAME_TIME_LOGIN` | bool | `true` | 是否允许同账号同时登录 | token 在 Redis 的 key 策略（session_id vs user_id） |
| `APP_DISABLE_SWAGGER` | bool | `false`（prod 为 `true`） | 是否禁用 Swagger 文档 | API 文档页面与 E2E 断言 |
| `APP_DISABLE_REDOC` | bool | `false`（prod 为 `true`） | 是否禁用 ReDoc 文档 | API 文档页面 |
| `DB_TYPE` | enum | `mysql` | 选择 MySQL / PostgreSQL | DB 连接串、方言、初始化脚本选择 |
| `DB_ECHO` | bool | `true` | 是否输出 SQLAlchemy 日志 | 日志噪音与性能 |
| `VITE_APP_BASE_API` | string | `/dev-api` | 前端 API 前缀 | 必须与后端 `APP_ROOT_PATH` 对齐 |
| `VITE_BUILD_COMPRESS` | string | （prod/staging/docker） | 打包压缩策略 | 前端构建产物 |

---

## 2) Flag Evaluation Logic（评估/生效机制）

### 2.1 后端（ENV → Settings）

- 加载入口：`ruoyi-fastapi-backend/config/env.py:GetConfig.parse_cli_args()`：
  - `python app.py --env=dev` → 加载 `.env.dev`
  - `python app.py --env=prod` → 加载 `.env.prod`
  - Dockerfile 内也会通过 `--env=dockermy` / `--env=dockerpg` 选择对应 `.env.*`
- `BaseSettings` 会把环境变量映射到 Settings 字段（例如 `APP_ROOT_PATH` → `app_root_path`）。

### 2.2 前端（Build-time ENV + Runtime Store）

- Vite：只暴露 `VITE_` 前缀变量到 `import.meta.env`（页面标题、API 前缀、构建压缩策略等）。
- 运行期布局开关来自 Pinia store：
  - 默认值：`ruoyi-fastapi-frontend/src/settings.js`
  - 用户覆盖：`localStorage['layout-setting']`（`src/store/modules/settings.js`）
- 暗黑模式：`@vueuse/core` 的 `useDark()` 会通过 `html.dark` class 驱动 CSS（见 `variables.module.scss`）。

---

## 3) Deprecated Flags（暂无）

当前未发现明确的废弃开关；如后续废弃，需在此登记并标注迁移路径。
