# 规格覆盖率报告（Coverage Report）

Generated: 2026-02-14

本报告用于追踪“可复刻规格文档”对源码实现的覆盖情况。它不是自动生成的准确指标，而是便于持续迭代的**人工维护清单**。

数据参考：
- Controller 文件清单、Docker/CI 清单：`09_Verification/ELEMENT_INVENTORY.md`
- API 端点统计（routers/endpoints）：`03_API/ENDPOINTS.md`
- UI 源码扫描：`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md`

---

## 1) Summary（摘要）

- Backend routers：19（`03_API/ENDPOINTS.md`）
- Backend endpoints：143（`03_API/ENDPOINTS.md`）
- DB tables：21（`02_Data/ENTITIES.md`）
- Frontend components：约 28（不含 layout）（`09_Verification/ELEMENT_INVENTORY.md`）
- Layout components：约 13（`09_Verification/ELEMENT_INVENTORY.md`）
- E2E tests：19 个文件（含像素级视觉基线）（`09_Verification/ELEMENT_INVENTORY.md`）

---

## 2) 已覆盖（Documented）

### 2.1 项目与架构

- `00_Overview/PROJECT.md`
- `00_Overview/ARCHITECTURE.md`
- `00_Overview/GLOSSARY.md`

### 2.2 配置与开关

- `01_Configuration/ENVIRONMENT.md`
- `01_Configuration/FEATURE_FLAGS.md`

### 2.3 数据模型

- `02_Data/ENTITIES.md`
- `02_Data/RELATIONSHIPS.md`
- `02_Data/MIGRATIONS.md`

### 2.4 API（清单级）

- `03_API/ENDPOINTS.md`（清单：按 router 分组）
- `03_API/AUTHENTICATION.md`
- `03_API/ERRORS.md`
- `03_API/openapi.json` + `03_API/OPENAPI_SNAPSHOT.md`（字段级契约快照）
- `03_API/OPERATION_MAP.md`（端点 → schema 映射）
- `03_API/SCHEMA_CATALOG.md`（schema 索引）

### 2.5 系统级业务骨架

- `04_Business_Logic/RULES.md`
- `04_Business_Logic/STATE_MACHINES.md`
- `04_Business_Logic/WORKFLOWS.md`
- `04_Business_Logic/IMPLEMENTATION_INDEX.md`
- `04_Business_Logic/services/`（Service 方法级索引）
- `04_Business_Logic/daos/`（DAO 方法级索引）

### 2.6 测试与复刻

- `08_Testing/UNIT_SPECS.md`（门禁 + 单测建议）
- `08_Testing/INTEGRATION_SPECS.md`
- `08_Testing/E2E_SPECS.md`
- `09_Verification/REPLICATION_GUIDE.md`

### 2.7 UI/UX（前端 UI-only 规格）

- `docs/ui-ux-spec/`（Foundation/Components/Patterns/Pages/A11y/Assets/Engineering）

### 2.8 前端工程行为（非 UI-only）

- `06_Frontend/`（鉴权、请求、动态路由、文案现状）
- `05_Mobile_App/`（uni-app 路由/鉴权/请求/页面模板）

---

## 3) 未完全覆盖（Gaps / Partial Coverage）

> 这些缺口并不影响“先验复刻骨架”，但会影响“完美等价复刻”的细粒度一致性。

- **前端页面级交互边界（业务语义）**：UI/UX spec 是 UI-only；若要达到“业务等价复刻”，需要在 `docs/specs/` 为每个业务模块补齐业务级交互与字段语义（本仓库将其作为后续二次开发的工作项）。
