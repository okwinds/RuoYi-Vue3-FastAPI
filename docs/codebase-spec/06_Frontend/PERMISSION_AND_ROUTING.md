# Permission & Routing（动态路由/权限复刻规格）

Source：
- `ruoyi-fastapi-frontend/src/permission.js`（全局路由守卫）
- `ruoyi-fastapi-frontend/src/store/modules/permission.js`（动态路由生成）
- `ruoyi-fastapi-frontend/src/router/index.js`（路由 meta 语义）

---

## 1) 路由守卫（beforeEach/afterEach）

入口：`src/permission.js`

核心契约（复刻必须保持一致）：
- 白名单：`/login`、`/register`（通过 `isPathMatch` 判断）
- 有 token：
  - 访问 `/login`：重定向到 `/`
  - 非白名单且 `useUserStore().roles.length === 0`：
    1) `useUserStore().getInfo()` 拉用户信息
    2) `usePermissionStore().generateRoutes()` 拉路由树并生成可访问路由
    3) 对每个 route 执行 `router.addRoute(route)`（仅对非 http path）
    4) `next({ ...to, replace: true })` 确保动态路由注册完成
- 无 token：
  - 白名单放行
  - 其它：重定向 `/login?redirect=<fullPath>`

用户体验契约：
- 进度条：NProgress（开始于 beforeEach，结束于 afterEach）

---

## 2) 动态路由生成（后端路由树 → 前端组件）

入口：`src/store/modules/permission.js`

关键步骤：
1) 调用后端：`getRouters()`（`GET /getRouters`）
2) 深拷贝三份数据：`sdata/rdata/defaultData`
3) `filterAsyncRouter()`：
   - 将 `route.component` 的字符串映射为真实组件
   - 特殊值：
     - `Layout` → `@/layout/index`
     - `ParentView` → `@/components/ParentView`
     - `InnerLink` → `@/layout/components/InnerLink`
   - 其它：通过 `import.meta.glob('../../views/**/*.vue')` 做按需加载映射（`loadView`）
4) 合并 `dynamicRoutes`（前端预置的动态路由）并 `router.addRoute`
5) 将结果写入 store：
   - `routes`（constantRoutes + rewriteRoutes）
   - `sidebarRouters`（constantRoutes + sidebarRoutes）
   - `topbarRouters`（defaultRoutes）

复刻要求：
- 后端下发的 `component` 字符串必须与前端 views 路径映射规则一致，否则页面无法渲染。
- `ParentView` 的 children flatten 规则必须一致（`filterChildren` 会拼接父 path）。

---

## 3) 权限过滤（前端动态路由）

入口：`filterDynamicRoutes(dynamicRoutes)`

契约：
- route 配置 `permissions`：使用 `auth.hasPermiOr(route.permissions)` 判断
- route 配置 `roles`：使用 `auth.hasRoleOr(route.roles)` 判断

