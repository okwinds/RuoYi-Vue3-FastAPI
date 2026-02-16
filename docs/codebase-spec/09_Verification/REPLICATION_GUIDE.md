# 复刻指南（Replication Guide）

本指南描述如何仅依赖 `docs/codebase-spec/` 与 `docs/ui-ux-spec/` 的规格文档，从零复刻出一个“能力等价”的系统。

注意：
- **复刻 ≠ 拷贝源码**：你可以替换技术栈，但必须复刻“外部契约（API/行为/UI 结构）”与关键系统性约束。
- 本项目存在若干“框架型约定”（例如：路由自动注册、HTTP 200 + 业务 code 的响应策略、JWT + Redis 在线 token），复刻时必须显式实现。

---

## 1) 前置条件（Prerequisites）

### 1.1 需要掌握的知识

- Web 管理后台常见信息架构（登录/权限/菜单/CRUD/审计日志）
- FastAPI 或同类 Web 框架的路由/中间件/依赖注入模型（可替换）
- JWT/OAuth2 基础与“在线 token”策略（token 存储与失效）
- 关系型数据库建模（RBAC、多表关联、数据权限）
- 前端路由与动态菜单渲染（Vue/React 均可替换）

### 1.2 工具与环境（复现上游同栈）

- Python：3.10+（CI 覆盖 3.10~3.13）
- Node.js：18+（前端构建）
- MySQL 8 / PostgreSQL 14（两套脚本二选一）
- Redis
- Docker & Docker Compose（用于一键环境与 E2E）

---

## 2) 推荐复刻顺序（Recommended Order）

### Step A：搭建“契约骨架”

1) 阅读 `00_Overview/PROJECT.md` 与 `00_Overview/ARCHITECTURE.md`  
2) 明确三大对外契约：
   - DB：`02_Data/ENTITIES.md` + `02_Data/RELATIONSHIPS.md`
   - API（字段级）：`03_API/openapi.json` + `03_API/OPENAPI_SNAPSHOT.md`（配合 `OPERATION_MAP.md` 快速索引）
   - UI：`docs/ui-ux-spec/`（仅 UI 结构/样式/组件，不含业务规则）

### Step B：先实现数据层（Data Layer）

1) 依据 `02_Data/ENTITIES.md` 创建所有表（MySQL 或 PostgreSQL）  
2) 依据 `02_Data/RELATIONSHIPS.md` 实现外键/关联/约束（如需可用逻辑外键）  
3) 导入初始化数据（至少包含管理员账号、基础菜单、基础字典/参数）

> 复刻判定：能用初始化账号登录，并获得系统菜单与权限集合。

### Step C：实现认证鉴权（AuthN/AuthZ）

1) 登录接口的输入输出与 token 策略：`03_API/AUTHENTICATION.md`  
2) 权限判定（角色/菜单/按钮权限）与数据权限（DataScope）  
3) token 的在线存储（Redis）与失效策略（单端/多端）

> 复刻判定：未登录访问受保护接口/页面被拒绝；登录后能访问对应权限范围的功能。

### Step D：实现路由与模块化（Backend + Frontend）

后端必须实现：
- controller/routers 的自动发现与挂载（见 `00_Overview/ARCHITECTURE.md` 的“路由自动注册”）
- 统一响应格式与全局异常处理（`03_API/ERRORS.md`）

前端必须实现：
- 动态路由/菜单渲染与路由守卫（token 有无、角色/权限加载、动态 addRoute）
- 三种导航形态（左侧/混合/顶部）（见 UI/UX spec 的 Layout 章节）

### Step E：用 E2E 反向验收（Verification）

1) 跑离线回归：`docs/testing-strategy.md`  
2) 跑 E2E：`08_Testing/E2E_SPECS.md`  
3) 如涉及 UI 变更：跑像素级视觉基线（`docs/ui-ux-spec/08_Visual_Baseline/README.md`）  
4) 以 E2E + 视觉基线通过作为“复刻最小验收线”

---

## 3) 复刻验收清单（Checklist）

- [ ] 数据库表结构与关键初始数据齐备（管理员可登录）
- [ ] 认证鉴权正确（未登录保护、登录态保持、权限控制可用）
- [ ] 统一响应结构一致（成功/失败字段、业务 code 语义、异常映射）
- [ ] 动态路由/菜单渲染一致（含隐藏路由、activeMenu 高亮、keep-alive 缓存规则）
- [ ] 暗黑模式与主题色切换一致（Element Plus CSS 变量联动）
- [ ] E2E 套件通过（或提供等价替代测试并说明）
- [ ] UI 像素级视觉基线通过（或提供等价的视觉回归证据并说明）
