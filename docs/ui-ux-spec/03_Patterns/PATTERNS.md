# UI Patterns（页面模式/组合规则）

本文件归纳前端在“列表页/表单页/弹窗/权限显隐”等方面的稳定模式，便于复刻或进行一致性重构。

---

## 1) 页面容器与布局

- 页面根容器：`<div class="app-container">`（全局 padding 20px）
- PC/移动端切换阈值：
  - Layout：宽度 `< 992` 视为 mobile（`src/layout/index.vue`）
  - Pagination：小屏隐藏 sizes/jumper（`max-width: 768px`）

---

## 2) 列表页（CRUD List）标准结构

典型页面：`src/views/system/user/index.vue`（其它 `system/*` 多为同型）

结构约定：
1) Search Form（可隐藏）
   - `el-form :inline="true"`，由 `RightToolbar v-model:showSearch` 控制显隐
2) Toolbar（主操作区）
   - 新增/修改/删除/导入/导出等按钮，配合权限指令 `v-hasPermi`
3) Table（数据表格）
   - `el-table v-loading`
   - 操作列常用 `el-tooltip + el-button link icon=Edit/Delete`
4) Pagination（分页）
   - 使用 `src/components/Pagination`，统一触发 `pagination` 事件

列显隐模式：
- `RightToolbar :columns="columns"`：页面维护一份列配置（key/label/visible），用于 `v-if="columns.xxx.visible"` 控制列展示。

---

## 3) Splitpanes（左右/上下分栏）

典型页面：用户管理页左侧部门树 + 右侧用户表格。

模式：
- 桌面：左右分栏
- 移动端：上下分栏（`:horizontal="device === 'mobile'"`）

主题变量：
- `variables.module.scss` 中提供 splitpanes 的 CSS 变量（暗黑模式下亦覆盖）。

---

## 4) 路由切换体验（Loading / Progress）

- 路由守卫：`src/permission.js`
- 交互：进入路由时 `NProgress.start()`，完成后 `NProgress.done()`。

---

## 5) 权限显隐（UI 层）

模式：
- 使用指令 `v-hasPermi` 控制按钮是否可见（例如新增/删除/导入/导出）。
- 路由级访问控制：动态路由 + 路由守卫（`usePermissionStore().generateRoutes()`）。

> 注意：此处仅记录“UI 层表现模式”；权限语义与数据权限规则属于后端规格范围（见 `docs/codebase-spec/`）。
