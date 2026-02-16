# Implementation Index（Service/DAO 复刻索引）

本目录用于补齐“可复刻级规格文档”中最容易遗漏的一类信息：**Service 层分支/校验/事务边界** 与 **DAO 层数据访问边界**。

> 说明：为避免手写文档遗漏，本仓库将 Service/DAO 进行“方法级自动抽取”，生成可检索的索引文档；并通过 `Source:` 锚点与源码保持可验证的一致性（见 `09_Verification` 下的验证脚本输出）。

---

## 1) Service 文档（业务/规则落地层）

路径：`docs/codebase-spec/04_Business_Logic/services/`

命名约定：
- 以源码文件名为准：`<xxx>_service.py.md`
- 每份文档至少包含：
  - Source（源码锚点）
  - Public Methods 表格：方法名 / 入参 / 返回 / docstring 首行 / DAO 调用点 / ServiceException 文案

复刻建议：
- 将每个 `ServiceException(message=...)` 视为“可见错误提示契约”的一部分（前端会直接展示 message）。
- 将 `DAO calls` 视为“数据访问边界”，在替换存储实现时按同名语义复刻。

---

## 2) DAO 文档（数据访问层）

路径：`docs/codebase-spec/04_Business_Logic/daos/`

命名约定：
- 以源码文件名为准：`<xxx>_dao.py.md`

复刻建议：
- DAO 层通常是“可复刻的最小查询语义集合”（分页、条件过滤、关联查询、导出数据准备）。
- 结合 `02_Data/*` 与 `openapi.json`，即可复刻实体字段、查询条件与返回结构的对齐。

---

## 3) 与其它规格的联动点（必须一致）

- API 字段级契约：`docs/codebase-spec/03_API/openapi.json`
- 统一响应结构与错误策略：`docs/codebase-spec/03_API/ERRORS.md`
- 系统级规则骨架（登录/权限/缓存/任务/代码生成）：`docs/codebase-spec/04_Business_Logic/RULES.md`
- 关键流程：`docs/codebase-spec/04_Business_Logic/WORKFLOWS.md`

---

## 4) 方法级可复刻规格（内部等价复刻）

当目标是“代码级复刻/内部等价”，仅有 Service/DAO 方法名与索引仍不足以重写完整逻辑；需要把关键链路展开为决策树与边界条件（method-spec）。

- 方法规格索引：`docs/codebase-spec/04_Business_Logic/method-specs/INDEX.md`

