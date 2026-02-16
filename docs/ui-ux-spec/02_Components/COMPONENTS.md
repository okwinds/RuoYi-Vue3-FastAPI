# 组件目录（Component Catalog）

本目录记录“管理后台前端”的组件级 UI 规格：目的、结构/插槽、交互状态、主题/暗黑模式钩子、以及可复刻的实现要点。

> 约束：只描述 UI 层组件，不描述其背后的业务含义与接口契约。

---

## 1) 组件清单（Inventory）

来源：`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md`（扫描结果）。

### 1.1 通用组件（src/components）

包含但不限于：
- `Breadcrumb`：面包屑导航
- `Pagination`：列表分页（包装 Element Plus pagination）
- `SvgIcon`：SVG Sprite 图标渲染
- `RightToolbar`：表格右侧工具条（搜索显隐、刷新、列显隐）
- `IconSelect`：图标选择器
- `FileUpload` / `ImageUpload` / `ImagePreview`：上传与预览
- `Editor`：富文本编辑器封装
- `Crontab/*`：cron 表达式编辑/结果展示
- `TopNav`：混合布局下的顶部菜单
- `Screenfull`、`Hamburger`、`HeaderSearch`、`SizeSelect` 等

### 1.2 布局组件（src/layout/components）

布局由 `src/layout/index.vue` 组合：
- `Sidebar`（含 `Logo`, `SidebarItem`, `Link`）
- `Navbar`
- `TagsView`
- `AppMain`
- `Settings`（布局设置抽屉/弹窗）
- `TopBar`（纯顶部导航模式）
- `Copyright`

---

## 2) 关键组件规格（Key Components）

像素级复刻要求：
- 本仓库的 UI 主要由 Element Plus 组件构成，复刻时允许替换 UI 框架，但必须保持这些组件的**可观察结构、状态与交互**一致；
- 除了本文件的概览描述，关键组件的“可复刻级规格卡”统一放在：`docs/ui-ux-spec/02_Components/components/`。

### 2.0 规格卡索引（Spec Cards）

| Component | Spec |
| --- | --- |
| Layout Shell（Sidebar/Navbar/TagsView/AppMain） | `docs/ui-ux-spec/02_Components/components/LayoutShell.md` |
| Sidebar（含 Logo/SidebarItem） | `docs/ui-ux-spec/02_Components/components/Sidebar.md` |
| Navbar | `docs/ui-ux-spec/02_Components/components/Navbar.md` |
| TagsView | `docs/ui-ux-spec/02_Components/components/TagsView.md` |
| AppMain | `docs/ui-ux-spec/02_Components/components/AppMain.md` |
| Settings（布局设置抽屉） | `docs/ui-ux-spec/02_Components/components/Settings.md` |
| SvgIcon | `docs/ui-ux-spec/02_Components/components/SvgIcon.md` |
| Pagination | `docs/ui-ux-spec/02_Components/components/Pagination.md` |
| RightToolbar | `docs/ui-ux-spec/02_Components/components/RightToolbar.md` |

### 2.1 `SvgIcon`

文件：`src/components/SvgIcon/index.vue`

- Purpose：统一渲染 `src/assets/icons/svg/*.svg` 生成的 sprite 图标
- Props：
  - `iconClass`（required）：svg 名（对应 `#icon-<name>`）
  - `className`：额外 class
  - `color`：覆盖 fill（默认空字符串，继承 `currentColor`）
- A11y：`aria-hidden="true"`（默认不被读屏读取；若图标承载语义，应在外层补文本）

### 2.2 `Pagination`

文件：`src/components/Pagination/index.vue`

- Purpose：统一分页交互，封装 Element Plus `<el-pagination>`
- Props：
  - `total`（required）
  - `page`（default 1）+ `limit`（default 20），支持 `v-model:page` / `v-model:limit`
  - `pageSizes`（default `[10,20,30,50]`）
  - `pagerCount`：移动端默认 5（`document.body.clientWidth < 992`），桌面 7
  - `layout`：默认 `total, sizes, prev, pager, next, jumper`
  - `autoScroll`：分页切换后滚动到顶部（调用 `scrollTo(0, 800)`）
  - `hidden`：隐藏分页容器
- Responsive：
  - 768 以下隐藏 sizes/jumper（见 `src/assets/styles/ruoyi.scss` 的 media query）

### 2.3 `RightToolbar`

文件：`src/components/RightToolbar/index.vue`

- Purpose：表格页右侧工具条（常与搜索表单、列表刷新、列显隐联动）
- Props：
  - `showSearch`（v-model）：控制搜索表单显隐
  - `columns`（Array/Object）：列配置（需要包含 `visible` 与 `label`）
  - `search`：是否显示搜索按钮
  - `showColumnsType`：`checkbox`（默认）或 `transfer`
  - `gutter`：右外边距（默认 10）
- Emits：
  - `update:showSearch`
  - `queryTable`：触发父页面刷新列表
- 列显隐交互：
  - `checkbox`：下拉菜单中复选框勾选
  - `transfer`：弹窗穿梭框

---

## 3) 复刻注意事项（Implementation Notes）

- 本项目大量组件依赖 Element Plus 的默认交互与样式；复刻时应优先保持“Element Plus 语义组件 + 少量覆写”的策略。
- 暗黑模式通过 `html.dark` + CSS 变量覆盖实现；组件应尽量使用 CSS var（例如 `--el-*`、`--sidebar-*`）而不是写死颜色。
