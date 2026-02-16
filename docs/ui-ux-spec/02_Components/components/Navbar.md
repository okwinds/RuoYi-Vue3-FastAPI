# Navbar（顶部导航）

Source：
- `ruoyi-fastapi-frontend/src/layout/components/Navbar.vue`
- `ruoyi-fastapi-frontend/src/components/Breadcrumb/index.vue`
- `ruoyi-fastapi-frontend/src/components/TopNav/index.vue`
- `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue`
- `ruoyi-fastapi-frontend/src/assets/styles/variables.module.scss`

---

## 1) Purpose（目的）

Navbar 提供：
- 三种导航布局（NavType=1/2/3）的顶部区域承载；
- 快捷入口（源码/文档、全屏、主题切换、布局大小等）；
- 用户头像下拉菜单（个人中心、布局设置、退出）。

---

## 2) 结构（Structure）

### 2.1 顶部区域分支（NavType）

容器 class：
- `.navbar.nav1` / `.navbar.nav2` / `.navbar.nav3`

分支渲染：
- NavType=1：显示 `Hamburger` + `Breadcrumb`
- NavType=2：显示 `Hamburger` + `TopNav`
- NavType=3：隐藏 hamburger；显示 `Logo` + `TopBar`

### 2.2 右侧菜单（Right menu）

桌面态（`appStore.device !== 'mobile'`）显示：
- `HeaderSearch`
- `RuoYiGit`（tooltip: 源码地址）
- `RuoYiDoc`（tooltip: 文档地址）
- `Screenfull`
- Theme switch（tooltip: 主题模式；icon sunny/moon）
- `SizeSelect`

始终显示：
- 用户头像下拉（`el-dropdown`，hover trigger）

---

## 3) 像素级常量（Metrics）

详表见：`docs/ui-ux-spec/01_Foundation/LAYOUT_METRICS.md`

摘要：
- Navbar 高度：50px
- shadow：`0 1px 4px rgba(0, 21, 41, 0.08)`

---

## 4) Theme / Dark Mode（颜色钩子）

Navbar 背景使用 CSS 变量：
- `background: var(--navbar-bg)`

暗黑模式下：
- `variables.module.scss` 设置 `--navbar-bg/#text/#hover`

注意：
- `.right-menu-item` 默认文字色在实现里写死 `#5a5e66`；暗黑模式下主要依赖 Element Plus 变量与继承关系，复刻时应保持最终视觉一致。

---

## 5) 交互（Interactions）

### 5.1 主题切换（Theme switch）

触发：
- 点击 `.theme-switch-wrapper` 调用 `settingsStore.toggleTheme()`（内部使用 `useToggle(useDark())`，表现为 `html.dark` class 切换）

Hover：
- 图标 `transform: scale(1.15)`，transition 0.3s

### 5.2 退出登录（Logout）

交互：
- 弹窗确认（`ElMessageBox.confirm`）
- 确认后 `userStore.logOut()`，成功后 `location.href='/index'`

---

## 6) A11y（可访问性要求）

复刻要求：
- 主题切换按钮应具备可读标签（当前 tooltip 提供可见提示，但 icon 本身无 aria-label；见 `docs/ui-ux-spec/05_A11y/A11Y.md` 的建议项）
- 下拉菜单项可用键盘操作（Element Plus 默认行为需保持）
