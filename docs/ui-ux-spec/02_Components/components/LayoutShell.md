# Layout Shell（整体布局壳）

Scope：PC 管理后台前端（`ruoyi-fastapi-frontend/`）。

Source：
- `ruoyi-fastapi-frontend/src/layout/index.vue`
- `ruoyi-fastapi-frontend/src/assets/styles/sidebar.scss`
- `ruoyi-fastapi-frontend/src/layout/components/Navbar.vue`
- `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue`
- `ruoyi-fastapi-frontend/src/layout/components/AppMain.vue`

---

## 1) Purpose（目的）

Layout Shell 定义了整个后台的“可观察结构”：
- 左侧菜单（Sidebar）+ 顶部导航（Navbar）+ 页签（TagsView，可开关）+ 内容区（AppMain）+ 设置抽屉（Settings）。
- 三种导航布局（NavType=1/2/3）切换时，壳层结构与关键交互保持一致（见 `docs/ui-ux-spec/04_Pages/PAGES.md` 与 `07_Engineering_Constraints/ENGINEERING.md`）。

---

## 2) DOM 结构（可观察骨架）

骨架（伪结构树）：

```
.app-wrapper (div)
  .drawer-bg (div, mobile 且 sidebar.opened 时出现，点击关闭)
  .sidebar-container (Sidebar, 可隐藏)
  .main-container (div, 包含 fixed header 与内容区)
    .fixed-header (div, fixedHeader=true 时)
      Navbar
      TagsView (可选)
    AppMain (router-view + keep-alive)
    Settings (el-drawer)
```

关键 class 与行为（必须复刻）：
- `.app-wrapper.mobile.openSidebar`：移动端侧边栏打开时 `position: fixed`，防止页面滚动穿透。
- `.drawer-bg`：移动端侧边栏遮罩（透明黑 0.3），点击关闭侧边栏。
- `.main-container.sidebarHide`：当 sidebar 整体隐藏（NavType=3）时，fixed-header 宽度=100%。

---

## 3) 关键尺寸与层级（与像素级复刻绑定）

详表见：
- `docs/ui-ux-spec/01_Foundation/LAYOUT_METRICS.md`

必须保持的核心常量（摘要）：
- Sidebar 宽：200px；折叠宽：54px
- Navbar 高：50px
- TagsView 高：34px
- fixed-header z-index：9；sidebar z-index：1001；drawer-bg z-index：999

---

## 4) Mobile/Responsive（响应式规则）

阈值：
- `< 992px` 视为 mobile（`src/layout/index.vue`）

行为：
- 进入 mobile：
  - 强制关闭侧边栏（opened=false），并且 `withoutAnimation=true`（避免动画卡顿）。
- 从 mobile 回到 desktop：
  - device=desktop（不强制展开 sidebar，由 store 决定）。

---

## 5) 视觉基线绑定（Visual Baseline）

Layout Shell 的视觉验收基线：
- 见 `docs/ui-ux-spec/08_Visual_Baseline/README.md`（navType=1/2/3、dark/light、折叠态）。
