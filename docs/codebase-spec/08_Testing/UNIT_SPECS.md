# 单元测试规格（Unit Specs）与离线回归门禁

本文件的定位不是“逐函数模板”，而是把本仓库目前最现实、最可落地的**单元级验证策略**写清楚：

1) **离线回归最小集（必须）**：任何改动都必须可在本地离线跑通；与 CI 对齐。  
2) **单测建议补齐项（建议逐步补齐）**：将可稳定测试的核心逻辑下沉为单测，降低 E2E 维护成本。

> 说明：上游仓库主要提供 `ruoyi-fastapi-test/` 的 E2E 套件；后端单测当前不完整。本文档把“应该如何补齐”以规格形式固定下来，便于后续迭代逐步落地。

---

## 1) 离线回归最小集（必须通过）

权威来源：`docs/testing-strategy.md`（以该文档为准）。

### 1.1 Python（后端 + 测试套件）

- `ruff check ruoyi-fastapi-backend`
- `ruff check ruoyi-fastapi-test`
- `ruff format ruoyi-fastapi-backend --check`
- `ruff format ruoyi-fastapi-test --check`

### 1.2 Web（管理后台前端）

在 `ruoyi-fastapi-frontend/` 目录执行：

- `npm run build:prod`

---

## 2) 后端单元测试（建议优先级）

### 2.1 优先补齐的单测目标（P0）

这些模块“纯函数/弱 IO/边界清晰”，适合优先单测化：

- **主题/颜色计算（前端亦同）**
  - `ruoyi-fastapi-frontend/src/utils/theme.js`：`hexToRgb` / `rgbToHex` / `getLightColor` / `getDarkColor` 的边界与逆运算一致性。
- **统一响应结构（后端）**
  - `ruoyi-fastapi-backend/utils/response_util.py`（或同类工具）：成功/失败的 JSON 结构、code/msg/data 组合规则。
- **异常映射（后端）**
  - `ruoyi-fastapi-backend/exceptions/handle.py`：典型异常到响应体的映射（注意：项目存在“HTTP 200 + 业务 code”的策略）。
- **路由自动注册（后端）**
  - `ruoyi-fastapi-backend/common/router.py`：目录扫描规则、忽略规则、加载顺序稳定性（至少保证“扫描到的 controller 都被挂载”）。

### 2.2 Service 逻辑单测（P1）

建议以“可 mock 的边界”分层：

- service 层把 DB/Redis/外部依赖通过依赖注入（或显式传参）抽离后，对**纯业务分支**做单测；
- 对于不可轻易 mock 的部分，用集成测试/E2E 覆盖（见 `08_Testing/INTEGRATION_SPECS.md`、`08_Testing/E2E_SPECS.md`）。

优先建议覆盖（示例）：
- 登录态规则：多端登录开关、token 写入/失效策略（与 `APP_SAME_TIME_LOGIN` 联动）。
- 菜单/路由下发：菜单树构建、路由 meta 规则（避免 UI 侧出现“空路由/错误重定向”）。

---

## 3) 单测落地约定（建议）

### 3.1 目录建议

- 后端单测建议新增（或逐步补齐）：`ruoyi-fastapi-backend/tests/`
- 命名建议：`test_<module>_<behavior>.py`

### 3.2 覆盖目标（阶段性）

- Phase 1：关键纯函数与工具类（P0），确保稳定可回归。
- Phase 2：关键 service 分支（P1），减少 E2E 依赖。
- Phase 3：复杂流程用集成/E2E（P2），并通过少量“契约单测”兜底（例如响应 schema、关键错误码）。
