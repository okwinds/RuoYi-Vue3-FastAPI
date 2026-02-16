# Page Spec: 仪表盘（dashboard）

PageId：`dashboard`  
Route：`/index`

Source：
- `ruoyi-fastapi-frontend/src/views/dashboard/index.vue`

视觉基线（截图 ID）：
- `light_1_dashboard.png`
- `dark_1_dashboard.png`
- `light_2_dashboard.png`
- `dark_2_dashboard.png`
- `light_3_dashboard.png`
- `dark_3_dashboard.png`
- `light_1_dashboard_collapsed.png`
- `dark_1_dashboard_collapsed.png`

---

## 1) 目的（Purpose）

作为登录后的默认首页，展示系统概览模块。具体卡片内容可能随上游变化，但布局壳与页面容器约定必须稳定。

---

## 2) 前置条件（Preconditions）

- 已登录（cookie `Admin-Token` 存在且有效）
- 动态路由已加载（路由守卫链路见 `docs/codebase-spec/06_Frontend/PERMISSION_AND_ROUTING.md`）

---

## 3) 像素级结构（Structure）

页面骨架（必须保持）：
- 顶部用户信息区：`.pageHeaderContent`
  - 左侧：avatar
  - 中间：问候语（`早安，{name}，祝你开心每一天！`）
  - 右侧：统计数字（项目数/排名/访问）
- 内容区：外层 `div[style*="padding: 10px"]`
  - 左列（`a-col :xl="16"`）：项目卡片（`进行中的项目`）+ 动态列表（`动态`）
  - 右列（`a-col :xl="8"`）：快捷开始、雷达图（`XX 指数`）、团队列表

布局壳：
- Sidebar + Navbar +（可选）TagsView + AppMain
- 具体结构见 `docs/ui-ux-spec/02_Components/components/LayoutShell.md`

---

## 4) 稳定 Selector（用于截图/自动化等待）

建议等待：
- `.pageHeaderContent`（Dashboard 页面加载完成的稳定锚点）
- `#hamburger-container`（NavType=1/2）
- `#topbar-container`（NavType=3）

说明：
- Dashboard 使用 Ant Design Vue + 图表库（G2Plot Radar），在不同机器/不同渲染后端上可能出现极少量抗锯齿像素抖动；
- 视觉基线测试默认开启“极小像素容忍”，见 `docs/ui-ux-spec/01_Foundation/LAYOUT_METRICS.md` 的稳定性章节。

---

## 5) 主题/暗黑模式（Theme）

Dashboard 内容区域应随 Element Plus 与全局 CSS 变量适配暗黑模式；视觉基线覆盖 dark/light。
