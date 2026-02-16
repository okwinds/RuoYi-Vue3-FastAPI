# UI/UX Foundation（基础规范）

范围说明：
- 本文档只描述 **PC 管理后台前端**（`ruoyi-fastapi-frontend/`）的 UI Foundation；
- 不描述业务规则、接口契约、权限规则的“业务含义”（这些属于 `docs/codebase-spec/`）。

Source（实现位置）：
- `ruoyi-fastapi-frontend/src/assets/styles/variables.module.scss`
- `ruoyi-fastapi-frontend/src/assets/styles/index.scss`
- `ruoyi-fastapi-frontend/src/assets/styles/sidebar.scss`
- `ruoyi-fastapi-frontend/src/assets/styles/ruoyi.scss`
- `ruoyi-fastapi-frontend/src/utils/theme.js`

像素级复刻提示：
- 所有“宽高/层级/断点/阴影”等**可观察常量**统一整理在：`docs/ui-ux-spec/01_Foundation/LAYOUT_METRICS.md`。

---

## 1) 设计 Tokens（Design Tokens）

### 1.1 颜色（Colors）

来源：`src/assets/styles/variables.module.scss` + Element Plus 默认主题 + `src/utils/theme.js` 的动态主题色覆盖。

#### 1.1.1 SCSS 变量（静态）

基础色（节选，保持与源码一致）：

| Token | Value |
| --- | --- |
| `$blue` | `#324157` |
| `$light-blue` | `#333c46` |
| `$red` | `#C03639` |
| `$pink` | `#E65D6E` |
| `$green` | `#30B08F` |
| `$tiffany` | `#4AB7BD` |
| `$yellow` | `#FEC171` |
| `$panGreen` | `#30B08F` |

- 主色（Primary）
  - 默认：`#409EFF`（`$--color-primary`）
  - 运行时可被用户设置覆盖：通过设置 `--el-color-primary` 以及 light/dark 系列变量（见 `src/utils/theme.js:handleThemeStyle`）。
- 语义色（Success/Warning/Danger/Info）
  - `#67C23A` / `#E6A23C` / `#F56C6C` / `#909399`
- 侧边栏（Sidebar / Menu）
  - 暗色：`$menuBg=#304156`、`$menuText=#bfcbd9`、hover=`#263445`
  - 浅色：`$menuLightBg=#ffffff`、hover=`#f0f1f5`、text=`#303133`

组件色（Element Plus 覆写变量）：

| Token | Value |
| --- | --- |
| `$--color-primary` | `#409EFF` |
| `$--color-success` | `#67C23A` |
| `$--color-warning` | `#E6A23C` |
| `$--color-danger` | `#F56C6C` |
| `$--color-info` | `#909399` |

暗黑模式（Dark Mode）：
- 触发方式：`html.dark`（由 `@vueuse/core` 的 `useDark()` 控制）
- 覆盖内容：
  - Element Plus：`--el-bg-color` / `--el-text-color-*` / `--el-border-color*`
  - Layout：`--sidebar-bg` / `--sidebar-text` / `--navbar-bg` / `--navbar-text`
  - TagsView、Splitpanes、blockquote、Cron 等组件的专用变量

#### 1.1.2 CSS 变量（运行时与暗黑模式）

亮色模式（`:root`）关键变量：

| CSS Var | Value | Notes |
| --- | --- | --- |
| `--sidebar-bg` | `#304156` | 侧边栏背景（与 `$menuBg` 同源） |
| `--sidebar-text` | `#bfcbd9` | 侧边栏文字（与 `$menuText` 同源） |
| `--menu-hover` | `#263445` | 侧边栏 hover |
| `--navbar-bg` | `#ffffff` | 顶部导航背景 |
| `--navbar-text` | `#303133` | 顶部导航文字 |
| `--splitpanes-default-bg` | `#ffffff` | splitpanes 默认主题背景 |

暗黑模式（`html.dark`）关键变量（节选，复刻时必须覆盖这些语义）：

| CSS Var | Value |
| --- | --- |
| `--el-bg-color` | `#141414` |
| `--el-bg-color-overlay` | `#1d1e1f` |
| `--el-text-color-primary` | `#ffffff` |
| `--el-text-color-regular` | `#d0d0d0` |
| `--el-border-color` | `#434343` |
| `--el-border-color-light` | `#434343` |
| `--sidebar-bg` | `#141414` |
| `--sidebar-text` | `#ffffff` |
| `--menu-hover` | `#2d2d2d` |
| `--navbar-bg` | `#141414` |
| `--navbar-text` | `#ffffff` |
| `--navbar-hover` | `#141414` |
| `--tags-bg` | `#141414` |
| `--tags-item-bg` | `#1d1e1f` |
| `--tags-item-border` | `#303030` |
| `--tags-item-text` | `#d0d0d0` |
| `--tags-item-hover` | `#2d2d2d` |
| `--tags-close-hover` | `#64666a` |
| `--splitpanes-bg` | `#141414` |
| `--splitpanes-border` | `#303030` |
| `--splitpanes-splitter-bg` | `#1d1e1f` |
| `--splitpanes-splitter-hover-bg` | `#2d2d2d` |
| `--blockquote-bg` | `#1d1e1f` |
| `--blockquote-border` | `#303030` |
| `--blockquote-text` | `#d0d0d0` |
| `--cron-border` | `#303030` |
| `--splitpanes-default-bg` | `#141414` |

#### 1.1.3 主题色动态覆盖（Primary 动态计算）

实现：`src/utils/theme.js:handleThemeStyle(theme)`

约束（复刻必须保持）：
- 写入 `document.documentElement.style`：
  - `--el-color-primary = <theme>`
  - `--el-color-primary-light-1..9`：按 `getLightColor(theme, i/10)` 计算
  - `--el-color-primary-dark-1..9`：按 `getDarkColor(theme, i/10)` 计算

### 1.2 字体（Typography）

来源：`src/assets/styles/index.scss`

- `body` 字体栈：`Helvetica Neue, Helvetica, PingFang SC, Hiragino Sans GB, Microsoft YaHei, Arial, sans-serif`
- 标题/正文主要依赖 Element Plus 默认样式；项目额外对 `label` 做加粗（700）。

### 1.3 间距与布局（Spacing）

来源：`src/assets/styles/index.scss` + `src/assets/styles/ruoyi.scss`

常用工具类（节选）：
- `mt5/mr5/mb5/ml5`、`mt10/...`、`mt20/...`（ruoyi.scss）
- `app-container`：页面内边距 `20px`（index.scss）
- 表格与工具条常见间距：`mb8`（ruoyi.scss）

### 1.4 圆角、阴影（Radius / Shadow）

- Login 卡片圆角：`6px`（`src/views/login.vue`）
- Navbar 阴影：`box-shadow: 0 1px 4px rgba(0, 21, 41, 0.08)`（`src/layout/components/Navbar.vue`）
- 其它组件主要继承 Element Plus 默认。

### 1.5 Z-index（层级）

显式层级（节选）：
- 移动端抽屉遮罩：`z-index: 999`（`src/layout/index.vue`）
- Fixed header：`z-index: 9`（`src/layout/index.vue`）

> 完整 z-index/阴影/断点/关键尺寸详表见：`docs/ui-ux-spec/01_Foundation/LAYOUT_METRICS.md`。

### 1.6 动效（Motion）

来源：
- NProgress：路由切换顶部加载条（`src/permission.js` + `nprogress.css`）
- 错误页 404：云朵动画与文字上滑（`src/views/error/404.vue`）
- 主题按钮 hover：图标缩放（`src/layout/components/Navbar.vue`）

---

## 2) 全局样式（Global Styles）

入口：`src/assets/styles/index.scss`，并按顺序引入：
- `mixin.scss` / `transition.scss` / `element-ui.scss` / `sidebar.scss` / `btn.scss` / `ruoyi.scss`

### 2.1 Reset/Normalize（轻量）

- 统一 `box-sizing: border-box`
- `html, body, #app` 高度 100%
- 清理 `body` 默认 margin

### 2.2 链接与可交互元素

- `a` 去除下划线，继承颜色；hover 只改变 cursor
- `div:focus` 强制 `outline: none`（注意：这会弱化键盘焦点可见性，见 A11y 章节的“缺口与建议”）

### 2.3 表单与表格基础样式

来源：`src/assets/styles/ruoyi.scss` 与 `element-ui.scss`

- Inline 表单：`el-input/el-select/...` 默认宽度 200px（ruoyi.scss）
- Table header：背景 `#f8f8f9`，文字 `#515a6e`，高度 40px，字号 13px（ruoyi.scss）
- Dialog：非全屏默认 margin-top 6vh（ruoyi.scss）
