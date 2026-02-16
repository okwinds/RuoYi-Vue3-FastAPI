# Testing Strategy & Quality Gates

本文档描述本仓库的测试分层与“完成定义”的最小质量门禁（Quality Gates），避免出现“能跑但不可回归/不可复现”的交付。

---

## 1) 分层原则

我们将验证分为三层（从轻到重）：

1) **离线回归（必须）**
   - 目标：在不依赖外网、不依赖真实密钥的前提下，确保代码可被静态检查、可被格式化规则约束、可构建（前端）。
   - 适用：任何变更（包括小改动/bugfix）。

2) **集成 / E2E（强烈建议）**
   - 目标：覆盖关键路径（登录、权限、核心页面/接口），防止“功能看似没改但行为回归”。
   - 适用：影响用户可见行为、权限/鉴权、接口契约、页面交互、代码生成等。
   - 建议优先复用 `ruoyi-fastapi-test/`（pytest + Playwright）。

3) **后端单元测试（建议逐步补齐）**
   - 目标：将可测试的核心逻辑下沉为单元测试，减少对 E2E 的依赖与维护成本。
   - 备注：当前上游仓库主要提供 E2E 套件；我方改造过程中建议逐步补齐后端单测与可 mock 的 service 层测试。

---

## 2) 离线回归最小集（必须通过）

> 本节是本仓库对“完成”的最低门禁要求。命令应写入 `docs/worklog.md`。

### 2.1 Python（后端 + 测试套件）

前置：本地可用 `ruff`。

- `ruff check ruoyi-fastapi-backend`
- `ruff check ruoyi-fastapi-test`
- `ruff format ruoyi-fastapi-backend --check`
- `ruff format ruoyi-fastapi-test --check`

说明：
- 以上规则与仓库 CI（`.github/workflows/ruff.yml`）保持一致。
- 若需要自动修复，可在本地执行 `ruff check ... --fix` 与 `ruff format ...`，但提交前必须确保 `--check` 通过。

### 2.2 Web（管理后台前端）

前置：Node.js 与包管理器（npm/yarn）可用。

- 在 `ruoyi-fastapi-frontend/` 目录执行：`npm run build:prod`

说明：
- 上游前端未提供 lint/test 脚本时，至少保证可构建，以防止明显语法/依赖问题进入主分支。

---

## 3) 集成 / E2E（推荐路径）

上游提供了 E2E 测试套件：`ruoyi-fastapi-test/`（pytest + Playwright）。

### 3.1 手动启动前后端（本地开发常用）

1) 启动前端：`ruoyi-fastapi-frontend/`
2) 启动后端：`ruoyi-fastapi-backend/`
3) 运行测试：`ruoyi-fastapi-test/` 下执行 `pytest -v`

详细步骤可参考：`ruoyi-fastapi-test/README.md`。

### 3.2 使用 Docker Compose（CI/一致性更强）

在 `ruoyi-fastapi-test/` 下，按 MySQL 或 PostgreSQL 选择 compose 文件启动后执行 `pytest -v`。

说明：
- 端口占用与镜像构建耗时属于预期成本；如无法运行 E2E，必须在 Task Summary 中写清原因与替代验证方式。

### 3.3 像素级视觉基线（UI 变更强烈建议）

当变更涉及 UI 样式/布局/组件交互时，除常规 E2E 外建议额外跑“像素级视觉基线”：

- 规格入口：`docs/ui-ux-spec/08_Visual_Baseline/README.md`
- 测试入口：`ruoyi-fastapi-test/visual/test_visual_baseline.py`

```bash
cd ruoyi-fastapi-test
pytest -q visual/test_visual_baseline.py
```

说明：
- 该测试会对比当前截图与基线图片（`docs/ui-ux-spec/08_Visual_Baseline/screenshots/`）的像素差异；
- 若是预期 UI 变更：先更新页面/组件规格卡，再执行 `UPDATE_BASELINE=1 ...` 更新基线。

---

## 4) 什么时候必须补测试

以下变更类型必须补齐可回归护栏（优先 E2E，其次后端单测）：

- 鉴权/权限（OAuth2/JWT、数据权限、菜单/路由控制）
- 登录/用户态（登录、登出、强退、多端登录策略等）
- 核心业务页面或接口（用户/角色/菜单/部门/岗位/字典/参数/日志/任务/代码生成）
- 接口契约变更（请求/响应模型、字段语义、错误码等）
