# Layout Metrics（像素级布局量化表）

目标：把“像素级可观察常量”从源码中抽取出来，形成可复刻、可审查的量化表。  
说明：此文档只覆盖管理后台前端（`ruoyi-fastapi-frontend/`）的 UI 布局与视觉常量，不包含业务规则。

---

## 0) 像素级验收基线（Viewport / Rendering）

视觉基线测试（`ruoyi-fastapi-test/visual/test_visual_baseline.py`）固定：
- viewport：`1440 x 900`
- device scale factor：`1`
- locale：`zh-CN`
- timezone：`UTC`
- reduced motion：`reduce`

用途：
- 将“像素级复刻”从描述性文字变为可执行的截图基线；
- 复刻/改动时，以截图差异作为最终裁决。

Source：
- `ruoyi-fastapi-test/visual/test_visual_baseline.py`（`_new_context()`）

---

## 1) 侧边栏（Sidebar）

### 1.1 宽度（宽度必须精确复刻）

| 项 | 值 |
| --- | --- |
| 展开宽度 | `200px` |
| 折叠宽度 | `54px` |

Source：
- `ruoyi-fastapi-frontend/src/assets/styles/variables.module.scss`（`$base-sidebar-width: 200px`）
- `ruoyi-fastapi-frontend/src/assets/styles/sidebar.scss`（`.hideSidebar .sidebar-container { width: 54px }`）

### 1.2 定位与层级

| 项 | 值 |
| --- | --- |
| 位置 | `position: fixed; top: 0; left: 0; bottom: 0;` |
| z-index | `1001` |

Source：
- `ruoyi-fastapi-frontend/src/assets/styles/sidebar.scss`（`.sidebar-container`）

### 1.3 阴影（必须精确复刻）

| 项 | 值 |
| --- | --- |
| box-shadow | `0px 0px 8px 0px rgba(0, 0, 0, 0.1)` |
| webkit 备用 | `2px 0 6px rgba(0, 21, 41, .35)` |

Source：
- `ruoyi-fastapi-frontend/src/assets/styles/sidebar.scss`

---

## 2) 顶部导航（Navbar / Fixed Header）

### 2.1 高度

| 项 | 值 |
| --- | --- |
| navbar 高度 | `50px` |

Source：
- `ruoyi-fastapi-frontend/src/layout/components/Navbar.vue`（`.navbar { height: 50px }`）
- `ruoyi-fastapi-frontend/src/layout/components/AppMain.vue`（`min-height/height calc(100vh - 50px)`）

### 2.2 Fixed header 宽度计算

| 场景 | 值 |
| --- | --- |
| 默认（sidebar 展开） | `calc(100% - 200px)` |
| sidebar 折叠（hideSidebar） | `calc(100% - 54px)` |
| sidebarHide（隐藏侧边栏） | `100%` |

Source：
- `ruoyi-fastapi-frontend/src/layout/index.vue`（`.fixed-header` / `.hideSidebar .fixed-header` / `.sidebarHide .fixed-header`）

### 2.3 阴影

| 项 | 值 |
| --- | --- |
| navbar box-shadow | `0 1px 4px rgba(0, 21, 41, 0.08)` |

Source：
- `ruoyi-fastapi-frontend/src/layout/components/Navbar.vue`

---

## 3) 标签栏（TagsView）

| 项 | 值 |
| --- | --- |
| tags-view 容器高度 | `34px` |
| tags item 高度/行高 | `26px` |
| tags item padding | `0 8px` |
| tags item 左边距 | `5px`（首个 `15px`） |
| tags 阴影 | `0 1px 3px 0 rgba(0, 0, 0, .12), 0 0 3px 0 rgba(0, 0, 0, .04)` |
| contextmenu z-index | `3000` |

Source：
- `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue`

---

## 4) 内容容器（AppMain / app-container）

### 4.1 主滚动容器

说明：
- `.fixed-header + .app-main` 会成为滚动容器（`overflow-y: auto`），不是所有页面都会用 `window` 滚动。

Source：
- `ruoyi-fastapi-frontend/src/layout/components/AppMain.vue`

### 4.2 页面根容器 padding

| 项 | 值 |
| --- | --- |
| `.app-container` padding | `20px` |

Source：
- `ruoyi-fastapi-frontend/src/assets/styles/index.scss`（`.app-container { padding: 20px; }`）

---

## 5) 响应式断点（Breakpoints）

| 项 | 值 | 含义 |
| --- | --- | --- |
| WIDTH | `992` | `width - 1 < 992` 认为是 mobile（布局切换） |
| media query | `max-width: 991px` | fixed-header/mobile 高度与 padding 适配 |
| media query | `max-width: 768px` | ruoyi.scss 的移动端样式分支 |

Source：
- `ruoyi-fastapi-frontend/src/layout/index.vue`（`const WIDTH = 992`）
- `ruoyi-fastapi-frontend/src/layout/components/AppMain.vue`（`@media screen and (max-width: 991px)`）
- `ruoyi-fastapi-frontend/src/assets/styles/ruoyi.scss`（`@media (max-width: 768px)`）

---

## 6) Z-index（层级总表）

| 模块 | 值 |
| --- | --- |
| Sidebar（`.sidebar-container`） | `1001` |
| Mobile drawer mask（`.drawer-bg`） | `999` |
| Copyright（`.copyright`） | `999` |
| Fixed header（`.fixed-header`） | `9` |
| TagsView context menu（`.contextmenu`） | `3000` |

Source：
- `ruoyi-fastapi-frontend/src/assets/styles/sidebar.scss`
- `ruoyi-fastapi-frontend/src/layout/index.vue`
- `ruoyi-fastapi-frontend/src/layout/components/Copyright/index.vue`
- `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue`

---

## 7) 像素级基线的“稳定性约束”

### 7.1 为什么需要“极小像素容忍”

即使同机同环境，浏览器在抗锯齿/字体栅格化/阴影边缘渲染上也可能出现 **极少量像素抖动**（通常是圆角/阴影边缘的 1~数个像素）。

视觉基线测试默认允许极小容忍（避免 flaky）：
- `VISUAL_MAX_TOLERATED_PIXELS`：默认 `10`
- `VISUAL_MAX_TOLERATED_DIFF_SUM_RGBA`：默认 `120`

若需要“严格像素一致”，将两个 env 都设置为 `0`。

Source：
- `ruoyi-fastapi-test/visual/test_visual_baseline.py`（`test_visual_baseline()` env 读取）

