# RuoYi-Vue3-FastAPI 后台能力可抽取复用评估报告（面向 AIGC OS / DAG 业务流）

日期：2026-02-18  
状态：Draft（分析报告 / 可落地）  

## 0) Goal

基于：
- 你提供的业务文档：
  - `/home/gavin/workspaces/codes/befun.studio/docs/original/aigc_dag_perfect.html`（DAG 业务流）
  - `/home/gavin/workspaces/codes/befun.studio/docs/original/AI Agent meta-task brief.xlsx`（元任务概要）
  - `/home/gavin/workspaces/codes/aigc-os-v5`（前端 UI/UX 规格 v5）
- 本仓库的“可复刻级规格文档”（`docs/codebase-spec/`、`docs/ui-ux-spec/`、`docs/codebase-spec/03_API/openapi.json`）

回答问题：如果你想复用当前仓库后台能力（权限管理、模块管理等），从规格文档出发，哪些能力可以**抽取/复用**、如何复用、边界与风险是什么。

本报告聚焦“平台型后台能力”（IAM/RBAC/配置/审计/调度/文件/AI 管理等），不尝试替你直接实现 AIGC 业务域（TP0-TP6/PP1-PP3 的具体数据模型与工作台逻辑）。

---

## 1) 背景对齐（从业务文档提炼“平台能力需求”）

### 1.1 DAG 业务流（TP0-TP6 / PP1-PP3）对平台层的隐含需求

从 `aigc_dag_perfect.html` 与 meta-task brief 可见，你的生产流包含：
- 文本链路：市场洞察 → 创作源头（三选一）→ 故事大纲（含子结构）→ 完整故事 → 分集概要 → 分集剧本 → 分镜剧本
- 制片链路：视觉设定（人设/场景/首尾帧抽卡）→ AI 视频片段 → 后期制作（配音/字幕/BGM/特效）→ 成品短剧

这类链路在“后台平台层”通常需要：
- **用户/团队/角色权限**：谁能创建项目、谁能执行某阶段、谁能导出/审计。
- **模块/菜单治理**：对不同岗位（编剧/导演/评审/管理员）呈现不同模块与操作。
- **任务调度与可观测性**：批处理/重试/定时触发、任务日志落库、失败追踪。
- **配置/字典**：模型参数、开关、枚举、人机协作策略等在不发版情况下可调。
- **文件与资产管理**：上传图片、下载导出（DOCX/XLSX/ZIP）、静态资源访问。
- **审计与合规**：操作日志、登录日志、在线会话管理、敏感操作二次确认（step-up）。

### 1.2 AIGC OS v5 前端规格对“系统管理”模块的要求

`aigc-os-v5/04_Pages/Settings/SETTINGS_V5_PAGE.md` 的管理项列表为：
`['团队成员', '角色权限', '组织设置', 'API配额', '操作日志']`

这基本与本仓库 `module_admin` 的系统管理/监控能力高度重合（用户/角色/部门/日志/参数/字典等），因此**优先建议复用 `module_admin`** 作为你系统的“后台平台层”。

---

## 2) 本仓库可抽取/复用的后台能力（按优先级）

> 说明：下面每项都给出“复用方式”和“关键契约来源”，尽量以本仓库规格文档为真源，不凭空补接口。

### P0-1：认证与会话在线态（OAuth2 Password Flow + JWT + Redis 在线态）

你可以复用：
- 登录/退出/当前用户接口与行为（验证码开关、黑名单、密码错误锁定、多端/单端策略）
- JWT payload 语义（`user_id/session_id/login_info/exp` 等）
- Redis 在线 token 的“滑动过期”与在线用户管理配套能力

典型用途：
- 为 AIGC OS 的前端（无论 Vue/React）提供统一登录态与权限基座。

关键契约来源：
- 认证机制与流程：`docs/codebase-spec/03_API/AUTHENTICATION.md`
- 体系结构与启动：`docs/codebase-spec/00_Overview/ARCHITECTURE.md`
- OpenAPI 真源：`docs/codebase-spec/03_API/openapi.json`（`/login`、`/logout`、`/getInfo`）

复用方式建议：
- **优先：整体复用后端服务**（把它当作 IAM 服务/后台管理域），不要“剪代码”。
- 若需对接你现有网关：保持 `Authorization: Bearer <token>` 语义不变，前端只需适配存储 token 的位置与刷新策略。

主要风险/注意：
- `APP_SAME_TIME_LOGIN` 会改变 token_id 的 Redis key 策略（`session_id` vs `user_id`），复用时必须按同一语义实现。

---

### P0-2：RBAC 权限模型（用户-角色-菜单/按钮权限 perms）

你可以复用：
- 以 `sys_menu.perms` 作为“权限标识”的权限集合计算方式（管理员通配 `*:*:*`）
- 角色分配、用户授权、角色-菜单、角色-部门等常见治理能力
- 以“菜单树 + perms”驱动“模块可见性 + 操作可用性”的通用范式

典型用途（对应 v5 Settings）：
- 团队成员 → `sys_user`
- 角色权限 → `sys_role` + `sys_role_menu` + `sys_menu.perms`
- 组织设置 → `sys_dept` + `sys_role_dept`
- 操作日志 → `sys_oper_log`（以及监控域的日志接口）
- API 配额 → 可以先用 `sys_config`（参数）表达“配额策略”，后续再扩展为独立表

关键契约来源：
- 权限模型说明：`docs/codebase-spec/03_API/AUTHENTICATION.md`（RBAC + perms）
- 数据表字段级契约：`docs/codebase-spec/02_Data/ENTITIES.md`（`sys_user/sys_role/sys_menu/...`）
- OpenAPI 真源：`docs/codebase-spec/03_API/openapi.json`（`/system/user/*`、`/system/role/*`、`/system/menu/*`、`/system/dept/*`）

复用方式建议：
- **整体复用 module_admin**，并在你的业务域中沿用 `perms` 作为动作级权限字符串。
- 对 AIGC OS 的模块（insight/dashboard/review_center/text_workbench/...），建议按“资源/动作”建 perms（示例形态即可，不要写死业务术语）：
  - `resource:module:view`
  - `resource:asset:export`
  - `resource:job:run`

主要风险/注意：
- “模块管理能力”如果依赖 `sys_menu.component` 去动态映射前端页面，需要适配前端工程（见下一节）。

---

### P0-3：模块管理（菜单树 + 动态路由树 getRouters）

你可以复用：
- “菜单/目录/按钮”三类（`sys_menu.menu_type` 为 M/C/F）表达模块与操作
- `GET /getRouters` 下发“可访问路由树”，让前端做动态路由注册与侧栏渲染

典型用途：
- 在同一套后台里，为不同角色呈现不同模块集合（例如：运营只看看板，评审只看评估中心，管理员能进系统管理）。

关键契约来源：
- 前端动态路由/权限复刻规范：`docs/codebase-spec/06_Frontend/PERMISSION_AND_ROUTING.md`
- 数据表：`docs/codebase-spec/02_Data/ENTITIES.md`（`sys_menu` 的 `path/component/route_name/perms/...`）
- OpenAPI：`docs/codebase-spec/03_API/openapi.json`（`/getRouters`）

复用方式建议（按你前端技术栈选择）：
- 方案 A（最省事）：继续使用本仓库自带管理后台前端（Vue3），只把它作为“系统管理/运维后台”，AIGC OS 前端另做。
- 方案 B（你使用 React 的 AIGC OS）：**仅复用路由树的数据模型**，前端实现自己的 `route.component` 映射（不要硬套 Vue 的 `Layout/ParentView/InnerLink` 约定）。
- 方案 C（抽取服务）：保留 `/getRouters` 作为“模块树 API”，但把 `component` 字段语义从“Vue 组件路径”改为“前端路由 key”，由前端自行映射（需要你接受字段语义变化/迁移成本）。

主要风险/注意：
- `PERMISSION_AND_ROUTING.md` 明确了 Vue 侧的组件映射规则；如果你换前端框架，就必然需要“适配层”，否则路由无法渲染。

---

### P0-4：系统配置与字典（sys_config / sys_dict）

你可以复用：
- 系统参数（如验证码开关、黑名单等）以 `sys_config` 配置并在启动时预热到 Redis
- 字典（枚举/选项集）以 `sys_dict` 维护，并作为前端下拉/标签/状态映射的数据源

典型用途：
- 把“阶段策略/模型参数/开关”从代码里抽出来，让运营/管理员能调整。

关键契约来源：
- 启动预热：`docs/codebase-spec/00_Overview/ARCHITECTURE.md`（Redis 预热 dict/config）
- 数据表：`docs/codebase-spec/02_Data/ENTITIES.md`（`sys_config`、`sys_dict_*`）
- OpenAPI：`docs/codebase-spec/03_API/openapi.json`（`/system/config/*`、`/system/dict/*`）

---

### P0-5：审计与监控（操作日志/登录日志/在线用户/缓存/服务监控）

你可以复用：
- 登录日志（谁在什么 IP、何时登录/失败/解锁等）
- 操作日志（后台写操作可追溯）
- 在线用户（强退会话等）
- 缓存监控/清理、服务监控（基础运维能力）

典型用途：
- 你的系统中“评估/导出/执行任务”等都属于高价值行为，后台审计能显著降低排障成本与合规风险。

关键契约来源：
- OpenAPI：`docs/codebase-spec/03_API/openapi.json`（`/monitor/*`）
- 数据表：`docs/codebase-spec/02_Data/ENTITIES.md`（`sys_oper_log` 等）
- Feature Flags：`docs/codebase-spec/01_Configuration/FEATURE_FLAGS.md`（演示模式对写操作的拦截范围说明）

---

### P0-6：定时任务系统（APScheduler + Job/JobLog + invoke_target 动态调用）

你可以复用：
- Job 管理（新增/启停/立即执行/导出/日志）
- Cron 扩展解析（支持 6/7 段、`L/?/#/W` 等）
- 事件监听落库（失败异常信息入库）
- `invoke_target` 以字符串定位任务函数（可替换为白名单注册表，但语义需等价）

典型用途：
- 对 TP/PP 阶段任务做：定时补跑、失败重试、夜间批量产出、异步队列/调度入口。
- 对 “Deep Research / 数据分析指令” 做：按计划生成日报/周报，或定时刷新洞察缓存。

关键契约来源：
- 调度器集成：`docs/codebase-spec/05_Integrations/SCHEDULER_APSCHEDULER.md`
- OpenAPI：`docs/codebase-spec/03_API/openapi.json`（`/monitor/job*`、`/monitor/jobLog*`）

主要风险/注意：
- `APP_WORKERS > 1` 会改变调度器行为与任务状态一致性（需要按仓库既定语义评估，见 `FEATURE_FLAGS.md`）。

---

### P1：文件上传/下载/静态资源（profile 挂载）与 Excel 导出能力

你可以复用：
- 文件上传（分片写入、后缀白名单、统一命名）
- 静态资源挂载（`/profile/...` 可直接访问）
- 资源下载校验（防路径穿越、文件名格式校验）
- Excel 导出/模板生成策略（适用于后台导出/批量导入模板）

典型用途：
- PP1/PP2 的图片/视频中间件产物的落盘与回显（注意：大文件/分片上传可能需要进一步增强）。
- Review Center 导出（XLSX）或报表下载。

关键契约来源：
- 上传与静态资源：`docs/codebase-spec/05_Integrations/UPLOAD_AND_STORAGE.md`
- Excel：`docs/codebase-spec/05_Integrations/EXCEL_IMPORT_EXPORT.md`
- OpenAPI：`docs/codebase-spec/03_API/openapi.json`（`/common/upload`、`/common/download*`）

---

### P1：AI 管理能力（模型配置 + 对话 JSON Lines 流式协议）

你可以复用：
- AI 模型配置管理（provider、base_url、temperature/max_tokens、api_key 加密入库）
- AI 对话接口（JSON Lines 逐行输出，包含 meta/run_info/content/metrics/error）
- provider 工厂与可替换实现契约（OpenAI/Anthropic/Google/Ollama/OpenRouter...）

典型用途：
- 作为你 AIGC OS 的“统一模型配置中心”（在后台维护 key 与路由），前端/业务服务只引用 model_id。
- 用统一的流式协议对接 Console（与 v5 的“过程可见性”理念一致）。

关键契约来源：
- AI Providers：`docs/codebase-spec/05_Integrations/AI_PROVIDERS.md`
- OpenAPI：`docs/codebase-spec/03_API/openapi.json`（`/ai/model*`、`/ai/chat*`）

主要风险/注意：
- API key 加密的 Fernet key 由 JWT secret 派生（见 `AI_PROVIDERS.md` 提及的 crypto 约束），旋转密钥会导致历史密文不可解。

---

### P2：代码生成器（tool/gen）

你可以复用：
- 对新业务表做 CRUD 脚手架的生成能力（适合快速起步）

关键契约来源：
- OpenAPI：`docs/codebase-spec/03_API/openapi.json`（`/tool/gen*`）
- API 清单：`docs/codebase-spec/03_API/ENDPOINTS.md`（生成器路由组）

复用建议：
- 更适合“内部快速迭代”，对外产品化需谨慎（生成代码的可维护性与规范一致性要再评估）。

---

## 3) “模块管理能力”如何落到你的 AIGC OS（对齐建议）

结合 AIGC OS v5 的模块结构（insight/dashboard/review_center/text_workbench/settings/video...），建议把“模块”在后台表达为：
- `sys_menu` 的目录/菜单项（M/C）
- 每个模块内关键动作表达为按钮权限（F）并填 `perms`

然后你可以有两条路线：

1) **后台模块树只用于“后台管理域”**（推荐起步）
   - 本仓库的 Vue3 管理后台继续做：用户/角色/组织/配置/日志/任务/模型管理
   - AIGC OS 前端只使用 `/login`、`/getInfo` 的权限集合做展示/禁用
   - 好处：不需要把 `getRouters`/component 映射适配到 React

2) **后台模块树也驱动 AIGC OS 的前端导航**（需要适配层）
   - 你需要定义“路由 key ↔ React 页面组件”的映射策略
   - 并决定 `sys_menu.component` 字段在你系统里的语义（不建议继续用 Vue 的路径约定）

---

## 4) 建议的“抽取方式”与边界（避免过度手工剪裁）

### 4.1 推荐：把本仓库后台作为平台层服务整体复用

最现实的复用是：**直接部署本仓库后端（FastAPI）**，并把它定位成：
- `IAM/RBAC + AdminOps + Scheduler + AI Config` 的平台服务

你的 AIGC 业务域（项目/资产/阶段任务/评估报告等）可以：
- 先独立开发为新模块（例如新增 `module_aigc_domain/`），复用已有鉴权依赖与审计能力；
- 或先跑在另一个服务里，只调用本服务的 IAM/配置/调度/文件/模型管理能力。

### 4.2 不建议：仅复制粘贴若干 controller/service 到新仓库

原因：
- 会引入大量隐式依赖（Redis 预热、异常/响应封装、路由 auto-register、DB 初始化、配置系统等）
- 最后更难回归与追溯

更好的方式是：
- 抽取“适配层/SDK”（调用 OpenAPI）而不是剪代码；
- 或保持单仓演进，用模块边界隔离业务域。

---

## 5) 最小可验证清单（建议你用来确认“复用成功”）

> 这些是“从规格出发”的黑盒验收点；具体命令与环境可参考 `docs/codebase-spec/00_Overview/PROJECT.md`、`docs/codebase-spec/07_Infrastructure/DOCKER.md`。

1) Auth
   - `POST /login` 成功拿到 token
   - `GET /getInfo` 返回 roles/permissions 且 Redis 在线态可校验
2) RBAC
   - 新建角色、分配菜单/按钮 perms
   - 用户绑定角色后，permissions 集合发生变化
3) Module Tree（可选）
   - `GET /getRouters` 下发路由树符合预期（菜单可见性变化）
4) Scheduler
   - 新建 job、立即执行、jobLog 产生落库记录
5) Upload
   - 上传文件返回 `/profile/...`，静态访问可用
6) AI（可选）
   - 新建模型（api_key 入库密文），对话接口按 JSON Lines 流式输出

---

## 6) Next Steps（需要你确认的决策点）

为把“可抽取能力”真正变成可用资产，建议你选定路线：

1) **只把 RuoYi 后台当平台层**（最推荐起步）：AIGC OS 业务域另起服务/模块，先复用 Auth/RBAC/Config/Scheduler/Upload/AI Config。
2) **把 RuoYi 的模块树也用于 AIGC OS 导航**：需要定义 `sys_menu.component` 的新语义并做前端映射适配。
3) **未来要做多租户/更强隔离**：需要在数据模型与权限上引入 tenant 维度（本报告未展开，建议另起 L2 spec）。

