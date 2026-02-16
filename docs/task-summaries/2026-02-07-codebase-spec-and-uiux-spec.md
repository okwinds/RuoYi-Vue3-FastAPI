# 任务总结：可复刻规格文档 + 前端 UI/UX 规格（2026-02-07 ~ 2026-02-08）

状态更新（完成补齐）：`2026-02-08`
- 已补齐字段级 API 契约快照（OpenAPI）
- 已补齐 Service/DAO 方法级索引（用于“完美复刻”与一致性校验）
- 已补齐管理后台前端与移动端的工程行为契约文档

## 1) Goal / Scope

- Goal：为 `RuoYi-Vue3-FastAPI` 生成“可复刻级别”的规格文档（codebase spec），并为管理后台前端生成 UI/UX（UI-only）规格包。
- In Scope：
  - `docs/codebase-spec/`：项目/配置/数据/API/业务骨架/测试/复刻
  - `docs/ui-ux-spec/`：tokens/组件/页面/模式/a11y/工程约束
  - 文档索引更新：`DOCS_INDEX.md`
- Out of Scope：
  - 不对业务代码做功能改造
  - 不补实际的后端单元测试代码（只输出“单测规格与建议”）
- Constraints：中文优先；尊重上游目录结构；UI/UX spec 不描述业务逻辑/接口契约。

---

## 2) Context（背景与触发）

- 背景：该仓库为 fork 的开源项目，拟作为自研系统的管理后台与集成前端底座。
- 触发问题：需要“可追溯、可复现、可回归”的合规文档环境，并产出足以支持重写/迁移的规格文档。
- 影响范围：文档与流程规范；不影响运行时代码行为。

---

## 3) Spec / Contract（文档契约）

- Contract：
  - 后端/数据/API/测试/复刻：`docs/codebase-spec/`
  - 前端 UI-only：`docs/ui-ux-spec/`
- Acceptance Criteria（验收标准）：
  - `docs/codebase-spec/SPEC_INDEX.md` 能作为总入口，覆盖项目的关键可复刻信息
  - `docs/ui-ux-spec/` 能说明布局、主题/暗黑模式、关键组件与页面模板
  - `DOCS_INDEX.md` 可定位到上述两套规格
- Test Plan：
  - 文档完整性：目录与索引可浏览、无 placeholder
  - 可回归策略入口：`docs/testing-strategy.md` 与 `docs/codebase-spec/08_Testing/*`
- 风险与降级：
  - 字段级契约已通过 `docs/codebase-spec/03_API/openapi.json` 固化；通过 sha256 与映射表降低 drift 风险（见 `OPENAPI_SNAPSHOT.md`）。

---

## 4) Implementation（实现说明）

### 4.1 Key Decisions（关键决策与 trade-offs）

- Decision：将前端规格拆为 UI-only（`docs/ui-ux-spec/`），把业务契约留在 `docs/codebase-spec/`。
  - Why：降低耦合；便于业务二次开发时只替换 API/规则，不必重写 UI Foundation 与布局规范。
  - Trade-off：页面文档不会包含“按钮背后的接口语义”；需在 codebase spec 的 API/业务骨架中查找。

### 4.2 Code Changes（按文件列）

- `docs/codebase-spec/08_Testing/UNIT_SPECS.md`：离线回归门禁与单测补齐建议。
- `docs/codebase-spec/08_Testing/INTEGRATION_SPECS.md`：集成验证清单与推荐运行方式。
- `docs/codebase-spec/08_Testing/E2E_SPECS.md`：E2E 套件覆盖范围与运行 runbook。
- `docs/codebase-spec/07_Infrastructure/DOCKER.md`：Dockerfile/Compose 与端口映射说明。
- `docs/codebase-spec/07_Infrastructure/CI_CD.md`：ruff + Playwright CI 行为说明。
- `docs/codebase-spec/09_Verification/*`：复刻指南、覆盖率报告、缺口清单。
- `docs/codebase-spec/03_API/openapi.json`：OpenAPI 字段级契约快照（含 sha256）。
- `docs/codebase-spec/03_API/OPERATION_MAP.md`：端点 → schema/认证映射。
- `docs/codebase-spec/04_Business_Logic/services/`：Service 方法级索引（自动抽取）。
- `docs/codebase-spec/04_Business_Logic/daos/`：DAO 方法级索引（自动抽取）。
- `docs/codebase-spec/06_Frontend/*`：管理后台前端工程契约（鉴权/请求/动态路由/文案现状）。
- `docs/codebase-spec/05_Mobile_App/*`：移动端路由/鉴权/请求封装/页面模板文档。
- `docs/ui-ux-spec/*`：Foundation/Components/Patterns/Pages/A11y/Assets/Engineering 规格补齐。
- `DOCS_INDEX.md`：新增 spec 入口索引。

---

## 5) Verification（验证与测试结果）

### Offline Regression（必须）

- 命令：见 `docs/testing-strategy.md`
- 结果（`2026-02-08`）：
  - `ruff check` / `ruff format --check`：PASS（后端 + 测试套件）
  - `ruoyi-fastapi-frontend`：`npm run build:prod` PASS（首次运行需要 `npm install`）
  - 详细命令与结论已写入：`docs/worklog.md`

### Integration / E2E（可选但强烈建议）

- 环境：Docker Compose（`ruoyi-fastapi-test/docker-compose.test.*.yml`）
- 命令：见 `docs/codebase-spec/08_Testing/E2E_SPECS.md`
- 结果：本次变更以“文档补齐”为主，未在本机跑 E2E（建议在首次落库/首次联调时跑通一次，并作为后续关键变更门禁）。

---

## 6) Results（交付结果）

- 交付物列表：
  - `docs/codebase-spec/`（可复刻规格）
  - `docs/ui-ux-spec/`（UI-only 规格）
  - `docs/codebase-spec/09_Verification/SPEC_AUDIT_REPORT.md`（交付级规格审查检查报告）
  - `DOCS_INDEX.md` 更新
- 如何验收：
  - 从 `DOCS_INDEX.md` 进入，逐级阅读 `docs/codebase-spec/SPEC_INDEX.md` 与 `docs/ui-ux-spec/*`
  - 按 `docs/codebase-spec/09_Verification/REPLICATION_GUIDE.md` 的 checklist 自查

---

## 7) Known Issues / Follow-ups

- 已知问题：无（本任务目标的“字段级契约 + 方法级索引 + UI/UX spec + 工程行为契约”已补齐）。
- 后续建议（面向二次开发）：
  - 业务级功能新增/改造请在 `docs/specs/` 按模块建立 spec（与 UI/UX spec、OpenAPI 契约解耦维护）

---

## 8) Doc Index Update

- 已在 `DOCS_INDEX.md` 登记：是
