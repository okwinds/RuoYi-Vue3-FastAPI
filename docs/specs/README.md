# Specs（规格/设计文档）

用途：把“要做什么、为什么这么做、怎么验收”写清楚，减少口头约定与返工。

约定：
- 每个功能/模块一份 spec（建议文件名包含主题与日期，例如：`2026-02-07-auth-refresh-token.md`）
- spec 至少包含：
  - Goal
  - Constraints
  - Contract（接口/数据结构/协议）
  - Acceptance Criteria
  - Test Plan（离线回归 + 可选集成/E2E）
  - Risk/Rollback（可选）

完成后：
- 在 `DOCS_INDEX.md` 登记该 spec（路径 + 一句话说明）
- 在 `docs/worklog.md` 记录关键决策与验证命令

