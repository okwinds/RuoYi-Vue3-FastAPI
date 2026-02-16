# Docs Index

用途：作为 `RuoYi-Vue3-FastAPI` 仓库的“文档目录”，保证任何人/Agent 都能快速定位关键资料。

约定：
- 每条记录必须包含：**文件路径 + 一句话说明**
- 新增/删除/重命名文档时必须同步更新本索引

---

## Core

- `README.md`：项目介绍与开发启动说明（本 fork 的面向人类入口）。
- `CHANGELOG.md`：版本更新记录（上游文档）。
- `LICENSE`：开源许可证（上游文档）。
- `AGENTS.md`：协作宪法（Spec-Driven + 质量门禁 + 文档索引 + 工作记录 + 任务总结）。
- `DOCS_INDEX.md`：文档索引（本文件）。

---

## Specs / Plans

- `docs/specs/README.md`：规格/设计文档约定与写法说明（每个功能/模块一份 spec）。
- `docs/plans/README.md`：计划与草案归档说明（按日期/主题归档）。

---

## Worklog & Summaries

- `docs/worklog.md`：工作记录（按时间顺序追加，含命令与关键决策）。
- `docs/task-summaries/README.md`：任务总结目录说明（每次结项一份总结）。
- `docs/task-summaries/2026-02-07-codebase-spec-and-uiux-spec.md`：任务总结：可复刻规格文档 + 前端 UI/UX 规格（UI-only）。
- `docs/task-summaries/2026-02-14-spec-doc-review-and-visual-baseline.md`：任务总结：规格文档复刻审查 + 像素级视觉基线稳定（可复跑）。
- `docs/templates/task-summary-template.md`：任务总结模板（复制填空）。

---
- `docs/task-summaries/`：任务结束总结目录（每次结项一份）。


## Tests & Quality

- `docs/testing-strategy.md`：测试与质量门禁策略（离线回归最小集、集成/E2E 运行方式与约束）。

---

## Compliance

- `docs/compliance/README.md`：合规文档入口（为什么要这些文档、如何维护）。
- `docs/compliance/fork-upstream.md`：Fork/上游同步与改造边界约定（避免难以合并的漂移）。

---

## Codebase Spec（可复刻规格）

- `docs/codebase-spec/SPEC_INDEX.md`：可复刻规格文档索引（后端/数据/API/测试/复刻）。
- `docs/codebase-spec/00_Overview/PROJECT.md`：项目概览与快速运行。
- `docs/codebase-spec/03_API/ENDPOINTS.md`：端点清单（按 router 分组）。
- `docs/codebase-spec/03_API/OPENAPI_EXPORT.md`：OpenAPI 导出与 Swagger/ReDoc 路径约定（便于字段级契约沉淀）。
- `docs/codebase-spec/03_API/OPENAPI_SNAPSHOT.md`：OpenAPI 字段级快照说明（仓库固化）。
- `docs/codebase-spec/03_API/openapi.json`：OpenAPI JSON 快照（字段级接口契约真源）。
- `docs/codebase-spec/03_API/OPERATION_MAP.md`：端点 → schema/认证映射。
- `docs/codebase-spec/03_API/HANDLER_MAP.md`：Endpoint → Controller → Service.method 映射（实现入口快速定位）。
- `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`：Service/DAO 方法级索引入口。
- `docs/codebase-spec/04_Business_Logic/method-specs/INDEX.md`：关键方法“可重写级”规格索引（内部等价复刻）。
- `docs/codebase-spec/05_Integrations/`：外部依赖/集成专项规格（Redis/调度/AI/上传/Excel/Crypto）。
- `docs/codebase-spec/06_Frontend/OVERVIEW.md`：管理后台前端工程概览与环境变量联动。
- `docs/codebase-spec/06_Frontend/AUTH_AND_REQUEST.md`：鉴权与请求层契约（axios 拦截器、防重复提交、下载）。
- `docs/codebase-spec/06_Frontend/PERMISSION_AND_ROUTING.md`：动态路由/权限复刻规格。
- `docs/codebase-spec/05_Mobile_App/APP.md`：移动端规格入口与索引。
- `docs/codebase-spec/09_Verification/REPLICATION_GUIDE.md`：按规格复刻的落地指南。
- `docs/codebase-spec/09_Verification/SPEC_AUDIT_REPORT.md`：规格审查检查报告（代码 ↔ 规格，对外可交付的检查结论）。
- `docs/codebase-spec/09_Verification/CODE_TO_SPEC_MAP.md`：全仓库文件级对照表（代码 → 规格，一一对应审查入口）。
- `docs/codebase-spec/09_Verification/SPEC_POINTERS_VALIDATION_REPORT.md`：对照表指针有效性校验（确保映射指向的文档都存在）。

---

## UI/UX Spec（前端 UI-only 规格）

- `docs/ui-ux-spec/01_Foundation/FOUNDATION.md`：设计 tokens 与全局样式规范。
- `docs/ui-ux-spec/01_Foundation/LAYOUT_METRICS.md`：像素级布局量化表（宽高/层级/断点/阴影等真源）。
- `docs/ui-ux-spec/02_Components/COMPONENTS.md`：组件目录与关键组件规格。
- `docs/ui-ux-spec/03_Patterns/PATTERNS.md`：列表页/表单页等稳定模式。
- `docs/ui-ux-spec/04_Pages/PAGES.md`：页面模板与信息架构（含路由 meta 约定）。
- `docs/ui-ux-spec/08_Visual_Baseline/README.md`：像素级视觉基线（截图快照 + 可复跑 diff）。
