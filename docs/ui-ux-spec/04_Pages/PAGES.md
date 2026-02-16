# 页面与信息架构（Pages & IA）

来源：`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md`（views 清单） + `src/router/index.js`（路由 meta 约定）+ `src/permission.js`（路由守卫）。

像素级复刻要求：
- 关键页面必须提供“页面规格卡”（结构/状态/关键交互/稳定 selector/视觉基线绑定），统一放在 `docs/ui-ux-spec/04_Pages/pages/`。
- 视觉基线（截图）是像素级验收真源：见 `docs/ui-ux-spec/08_Visual_Baseline/README.md`。

---

## 1) 全局路由约定（Router Meta）

`src/router/index.js` 在注释中约定了路由字段语义（复刻时必须保持）：
- `hidden`：不在侧边栏展示（401/404/login 等）
- `alwaysShow`：强制显示父级菜单
- `redirect`：`noRedirect` 表示面包屑不可点
- `roles` / `permissions`：路由访问权限（动态路由生成使用）
- `meta`：
  - `title`：菜单与面包屑显示名，同时用于动态标题
  - `icon`：SVG icon name（`src/assets/icons/svg`）
  - `noCache`：keep-alive 缓存开关
  - `breadcrumb`：是否在面包屑显示
  - `activeMenu`：用于“详情/编辑”页高亮父级菜单

---

## 2) 页面类型（Templates）

### 2.1 登录/注册（Auth）

- 登录：`src/views/login.vue`
  - 居中卡片（宽 400）
  - 背景：`login-background.jpg`
  - 支持验证码（由后端 `/captchaImage` 返回 `captchaEnabled` 控制）
  - 支持“记住密码”（cookie 存储加密后的密码）
- 注册：`src/views/register.vue`（同类结构）

### 2.2 错误页（Error）

- `src/views/error/401.vue`
- `src/views/error/404.vue`（含动画）

### 2.3 仪表盘（Dashboard）

- `src/views/dashboard/index.vue`
- 典型：卡片/图表区域（具体内容由上游实现决定）

### 2.4 系统管理（System）

目录：`src/views/system/*`

典型页面：
- 用户、角色、菜单、部门、岗位、字典、参数、公告等
- 以“搜索 + 工具条 + 表格 + 分页 + 弹窗表单”为主模板（见 Patterns）。

### 2.5 监控（Monitor）

目录：`src/views/monitor/*`

典型页面：
- 在线用户、定时任务、日志、服务监控、缓存监控、数据监控（druid iframe 或内嵌）。

### 2.6 工具（Tool）

目录：`src/views/tool/*`

典型页面：
- 代码生成（表导入、配置编辑、预览/下载）
- Swagger 接口页（对接后端接口文档开关）
- 表单构建（Form Generator）

### 2.7 AI 模块（AI）

目录：`src/views/ai/*`

典型页面：
- Chat：`src/views/ai/chat/index.vue` + `components/AiMessage.vue`
- Model：`src/views/ai/model/index.vue`

---

## 3) 三种导航布局（NavType）

配置来源：`src/settings.js` + `src/store/modules/settings.js`

- `navType=1`：纯左侧（Navbar 显示 Breadcrumb）
- `navType=2`：混合（Navbar 显示 TopNav）
- `navType=3`：纯顶部（Navbar 显示 Logo + TopBar，隐藏 hamburger）

---

## 4) 关键页面规格卡索引（Spec Cards）

说明：
- 下面列出“像素级验收必覆盖”的关键页面。
- 每页规格卡包含：路由、前置条件、骨架结构、关键交互、稳定 selector、视觉基线 ID。

| PageId | Route | Spec |
| --- | --- | --- |
| `login` | `/login` | `docs/ui-ux-spec/04_Pages/pages/login.md` |
| `dashboard` | `/index` | `docs/ui-ux-spec/04_Pages/pages/dashboard.md` |
| `system-user` | `/system/user` | `docs/ui-ux-spec/04_Pages/pages/system-user.md` |
| `system-role` | `/system/role` | `docs/ui-ux-spec/04_Pages/pages/system-role.md` |
| `system-menu` | `/system/menu` | `docs/ui-ux-spec/04_Pages/pages/system-menu.md` |
| `monitor-online` | `/monitor/online` | `docs/ui-ux-spec/04_Pages/pages/monitor-online.md` |
| `monitor-cache` | `/monitor/cache` | `docs/ui-ux-spec/04_Pages/pages/monitor-cache.md` |
| `monitor-server` | `/monitor/server` | `docs/ui-ux-spec/04_Pages/pages/monitor-server.md` |
| `monitor-job` | `/monitor/job` | `docs/ui-ux-spec/04_Pages/pages/monitor-job.md` |
| `tool-swagger` | `/tool/swagger` | `docs/ui-ux-spec/04_Pages/pages/tool-swagger.md` |
| `tool-gen` | `/tool/gen` | `docs/ui-ux-spec/04_Pages/pages/tool-gen.md` |
| `ai-chat` | `/ai/chat` | `docs/ui-ux-spec/04_Pages/pages/ai-chat.md` |
| `ai-model` | `/ai/model` | `docs/ui-ux-spec/04_Pages/pages/ai-model.md` |
