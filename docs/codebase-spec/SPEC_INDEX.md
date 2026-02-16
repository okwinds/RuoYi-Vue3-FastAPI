# Codebase Spec Index（可复刻规格文档索引）

本目录（`docs/codebase-spec/`）是“可复刻级别”的工程规格文档：目标是让读者在**不阅读源码实现细节**的前提下，也能复刻出同等能力的系统（可替换技术栈）。

配套材料：
- 前端 UI/UX 规格（仅 UI，不含业务逻辑）：`docs/ui-ux-spec/`
- 自动扫描/清点产物（辅助发现，不代表完整性）：`09_Verification/PROJECT_DISCOVERY_REPORT.md`、`09_Verification/ELEMENT_INVENTORY.md`

---

## 00_Overview（项目概览）

- `00_Overview/PROJECT.md`：项目定位、目录结构、快速运行、依赖与版本约束。
- `00_Overview/ARCHITECTURE.md`：系统架构、模块边界、关键数据流与启动生命周期。
- `00_Overview/GLOSSARY.md`：术语表（域名/系统名/模块名/常用缩写）。

---

## 01_Configuration（配置）

- `01_Configuration/ENVIRONMENT.md`：环境变量总表（后端 + 前端，含联动关系）。
- `01_Configuration/FEATURE_FLAGS.md`：关键开关与行为差异（含生产禁用 Swagger 等）。

---

## 02_Data（数据模型）

- `02_Data/ENTITIES.md`：数据库实体/表结构（字段级，MySQL + PostgreSQL）。
- `02_Data/RELATIONSHIPS.md`：实体关系与关联表语义（RBAC、数据权限等）。
- `02_Data/MIGRATIONS.md`：迁移策略（SQL 初始化 + Alembic + 启动时 create_all 的角色）。

---

## 03_API（HTTP API）

- `03_API/ENDPOINTS.md`：接口清单（按 controller/router 分组）。
- `03_API/AUTHENTICATION.md`：认证鉴权（JWT/OAuth2 形态、Token 存储策略、多端登录策略）。
- `03_API/ERRORS.md`：统一响应结构与错误处理策略（异常映射、HTTP vs 业务 code）。
- `03_API/HANDLER_MAP.md`：Endpoint → Controller → Service.method 映射（可定位实现入口）。
- `03_API/OPENAPI_EXPORT.md`：OpenAPI 导出与 Swagger/ReDoc 路径约定。
- `03_API/OPENAPI_SNAPSHOT.md`：字段级 OpenAPI 快照说明（仓库固化）。
- `03_API/openapi.json`：字段级接口契约（OpenAPI JSON 快照）。
- `03_API/OPERATION_MAP.md`：端点 → schema/认证映射（从快照生成）。
- `03_API/SCHEMA_CATALOG.md`：schema 名称索引（从快照生成）。

---

## 04_Business_Logic（业务/规则骨架）

> 注意：这里仅抽象“系统级规则骨架”，不代替具体业务二次开发的领域建模。

- `04_Business_Logic/RULES.md`：核心规则目录（用户/角色/菜单/权限/数据范围/字典/参数/生成器等）。
- `04_Business_Logic/STATE_MACHINES.md`：状态机与状态约束（账号状态、任务状态等）。
- `04_Business_Logic/WORKFLOWS.md`：关键流程（登录、路由下发、代码生成、定时任务加载等）。
- `04_Business_Logic/IMPLEMENTATION_INDEX.md`：Service/DAO 复刻索引（方法级自动抽取）。
- `04_Business_Logic/method-specs/INDEX.md`：关键方法“可重写级”规格索引（内部等价复刻）。
- `04_Business_Logic/services/`：Service 方法级索引（按文件拆分）。
- `04_Business_Logic/daos/`：DAO 方法级索引（按文件拆分）。

---

## 05_Integrations（外部依赖/集成）

- `05_Integrations/REDIS.md`：Redis 连接、Key 约定、缓存一致性与错误策略。
- `05_Integrations/SCHEDULER_APSCHEDULER.md`：APScheduler 任务调度（Cron 扩展、misfire、事件日志落库）。
- `05_Integrations/AI_PROVIDERS.md`：AI provider 工厂、API key 加密、流式协议（JSON Lines）、会话存储。
- `05_Integrations/UPLOAD_AND_STORAGE.md`：上传/下载/静态资源挂载契约。
- `05_Integrations/EXCEL_IMPORT_EXPORT.md`：Excel 导入/导出与模板生成规格。
- `05_Integrations/CRYPTO.md`：加密/哈希策略（JWT secret 派生 Fernet key 等）。

---

## 05_Mobile_App（移动端 / uni-app）

- `05_Mobile_App/APP.md`：移动端规格入口（技术栈、运行构建、契约索引）。
- `05_Mobile_App/ROUTING.md`：路由与守卫（pages.json + permission）。
- `05_Mobile_App/AUTH_AND_REQUEST.md`：鉴权与请求封装（Bearer token + 失效跳转）。
- `05_Mobile_App/STORE.md`：用户态/配置 store 约定。
- `05_Mobile_App/PAGES.md`：页面模板与状态清单。

---

## 06_Frontend（管理后台前端工程规格）

- `06_Frontend/OVERVIEW.md`：前端工程概览与环境变量联动。
- `06_Frontend/AUTH_AND_REQUEST.md`：axios 拦截器、token 注入、防重复提交、下载契约。
- `06_Frontend/PERMISSION_AND_ROUTING.md`：路由守卫与动态路由生成规则。
- `06_Frontend/I18N_AND_COPY.md`：多语言/文案现状与约束。

---

## 07_Infrastructure（基础设施与交付）

- `07_Infrastructure/DOCKER.md`：Dockerfile/Compose 结构、端口映射与测试环境差异。
- `07_Infrastructure/CI_CD.md`：CI 流水线（ruff + Playwright）与关键行为说明。

---

## 08_Testing（测试规格）

- `08_Testing/UNIT_SPECS.md`：离线回归/单元级的最小门禁与建议补齐项。
- `08_Testing/INTEGRATION_SPECS.md`：集成验证建议（DB/Redis/Swagger/静态资源等）。
- `08_Testing/E2E_SPECS.md`：E2E 测试套件（pytest + Playwright）覆盖范围与运行方式。

---

## 09_Verification（验证与复刻）

- `09_Verification/PROJECT_DISCOVERY_REPORT.md`：自动发现报告（技术栈/目录/入口）。
- `09_Verification/ELEMENT_INVENTORY.md`：自动清单（controller/service/sql/ui 等候选点）。
- `09_Verification/COVERAGE_REPORT.md`：覆盖率/缺口追踪（人工维护）。
- `09_Verification/SPEC_COVERAGE_TOOL_REPORT.md`：规格覆盖检查报告（工具生成，复跑友好）。
- `09_Verification/SOURCE_ANCHOR_REPORT.md`：Source 锚点校验报告（spec → code 可验证性）。
- `09_Verification/PLACEHOLDER_SCAN_REPORT.md`：placeholder/TODO 扫描结果（完备性检查）。
- `09_Verification/SPEC_AUDIT_REPORT.md`：规格审查检查报告（交付级审查结论）。
- `09_Verification/CODE_TO_SPEC_MAP.md`：全仓库文件级对照表（代码 → 规格，确保无死角归属）。
- `09_Verification/SPEC_POINTERS_VALIDATION_REPORT.md`：对照表指针有效性校验（指向的规格文件均存在）。
- `09_Verification/REPLICATION_GUIDE.md`：复刻步骤（从零搭建到可用）。
- `09_Verification/KNOWN_GAPS.md`：已知缺口与后续计划。
