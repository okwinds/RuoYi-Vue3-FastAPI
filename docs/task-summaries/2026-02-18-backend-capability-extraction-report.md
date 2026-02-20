# Task Summary：后台能力可抽取复用评估（面向 AIGC OS / DAG）

日期：2026-02-18  
Owner：agent  
变更分级：L0（文档/分析交付）

## Goal / Scope

- 读取业务侧 DAG/元任务概要与前端规格（v5），结合本仓库 `codebase-spec`，整理“可抽取/复用”的后台能力与落地建议。

交付物：
- `docs/specs/2026-02-18-ruoyi-backend-capability-extraction-for-aigc-os.md`

## Key Decisions

- 优先建议“整体复用后端服务/模块边界扩展”，而不是复制粘贴若干 controller/service 到新仓库（降低隐式依赖与回归成本）。
- “模块管理/动态路由树”对前端框架强绑定：React 侧应做适配层，不建议硬套 Vue 的 `Layout/ParentView/InnerLink` 约定。

## Code Changes

- Docs added:
  - `docs/specs/2026-02-18-ruoyi-backend-capability-extraction-for-aigc-os.md`
  - `docs/task-summaries/2026-02-18-backend-capability-extraction-report.md`
- Docs updated:
  - `DOCS_INDEX.md`（登记新增文档）

## Test Plan & Results

- L0 文档交付：无需新增/运行仓库测试。
- 过程性验证（非仓库测试）：
  - 使用 `doc-processor` 安装依赖并读取 `AI Agent meta-task brief.xlsx`（用于提炼业务阶段与上下文长度约束）。

## Known Issues / Risks

- AIGC OS（React）若要复用 `/getRouters` 作为导航驱动，需要额外定义字段语义与映射规则；否则建议仅复用 Auth/RBAC 作为平台层。

## Next Steps

- 人类确认：选择“平台层整体复用”还是“模块树也驱动 AIGC OS 导航”路线（两者工程量差异很大）。

