# Sidebar（侧边栏菜单）

Source：
- `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue`
- `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Logo.vue`
- `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue`
- `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Link.vue`
- `ruoyi-fastapi-frontend/src/assets/styles/sidebar.scss`
- `ruoyi-fastapi-frontend/src/assets/styles/variables.module.scss`

---

## 1) Purpose（目的）

Sidebar 承担：
- 动态路由生成后的菜单渲染（由 `permissionStore.sidebarRouters` 提供）；
- 展开/折叠与移动端抽屉交互；
- 主题/暗黑模式下菜单背景与文字颜色的适配。

---

## 2) 结构（Structure）

`Sidebar/index.vue` 的骨架：

```
.sidebar-container (div)
  Logo (可选：settingsStore.sidebarLogo)
  el-scrollbar.scrollbar-wrapper
    el-menu (mode=vertical, unique-opened=true, collapse-transition=false)
      SidebarItem* (按 sidebarRouters 渲染)
```

`el-menu` 关键 props（复刻必须保持等价语义）：
- `default-active = activeMenu`（优先使用 `route.meta.activeMenu`）
- `collapse = !appStore.sidebar.opened`
- `active-text-color = settingsStore.theme`（跟随主题色）
- `background-color/text-color`：由 `getMenuBackground/getMenuTextColor` 计算（见第 4 节）

---

## 3) 像素级常量（Metrics）

详表见：`docs/ui-ux-spec/01_Foundation/LAYOUT_METRICS.md`

摘要：
- 展开宽：200px
- 折叠宽：54px
- Sidebar 固定定位，z-index=1001
- 盒阴影：`0px 0px 8px 0px rgba(0, 0, 0, 0.1)`

---

## 4) Theme / Dark Mode（颜色钩子）

菜单背景色（`getMenuBackground`）：
- 若 `settingsStore.isDark=true`：`var(--sidebar-bg)`（由 `variables.module.scss` 在 `html.dark` 下定义）
- 否则：
  - `sideTheme==='theme-dark'`：`variables.menuBg`（`#304156`）
  - `sideTheme==='theme-light'`：`variables.menuLightBg`（`#ffffff`）

菜单文字色（`getMenuTextColor`）：
- 若 `isDark=true`：`var(--sidebar-text)`
- 否则：
  - `theme-dark`：`variables.menuText`（`#bfcbd9`）
  - `theme-light`：`variables.menuLightText`（`#303133`）

hover/active：
- hover 背景：`var(--menu-hover, rgba(0, 0, 0, 0.06))`
- active 背景：同 hover
- active 文字：
  - 代码里写 `var(--menu-active-text, #409eff)`；
  - 暗黑模式下 `variables.module.scss` 会设置 `--menu-active-text: $menuActiveText`（`#409eff`）。

---

## 5) 折叠态（Collapsed）

折叠触发：
- `appStore.sidebar.opened=false`

可观察变化（`sidebar.scss`）：
- `.hideSidebar .sidebar-container { width: 54px }`
- `.hideSidebar .main-container { margin-left: 54px }`
- 折叠菜单项文本隐藏（通过 `el-menu--collapse` 下的 `span/i` 尺寸与可见性控制）

---

## 6) A11y（可访问性要求）

现状依赖 Element Plus 的 menu 组件键盘与 aria 支持。

复刻要求（保持等价体验）：
- 菜单可用键盘上下移动与回车激活（或提供等价替代）
- 折叠态仍能访问子菜单（通过 tooltip 或弹出菜单）

---

## 7) 视觉基线绑定（Visual Baseline）

Sidebar 相关截图基线：
- navType=1 + dashboard：展开态与折叠态（dark/light）
- 见 `docs/ui-ux-spec/08_Visual_Baseline/README.md`
