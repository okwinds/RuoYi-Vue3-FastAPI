# Settings（布局设置抽屉）

Source：
- `ruoyi-fastapi-frontend/src/layout/components/Settings/index.vue`
- `ruoyi-fastapi-frontend/src/store/modules/settings.js`
- `ruoyi-fastapi-frontend/src/settings.js`
- `ruoyi-fastapi-frontend/src/utils/theme.js`

---

## 1) Purpose（目的）

Settings 提供可视化的布局与主题配置入口，包含：
- NavType（三种导航布局）切换；
- Sidebar 主题（theme-dark/theme-light）切换；
- 主题色（Element Plus primary）调整；
- TagsView / tagsIcon / fixedHeader / sidebarLogo / dynamicTitle / footerVisible 等开关；
- 保存到本地（localStorage）与重置（清除 localStorage 并刷新）。

---

## 2) 数据持久化契约（localStorage）

key：
- `layout-setting`：JSON 字符串

写入字段（`saveSetting`）：
```json
{
  "navType": 1,
  "tagsView": true,
  "tagsIcon": false,
  "fixedHeader": true,
  "sidebarLogo": true,
  "dynamicTitle": false,
  "footerVisible": false,
  "sideTheme": "theme-dark",
  "theme": "#409EFF"
}
```

读取位置：
- `src/store/modules/settings.js`：启动时 `JSON.parse(localStorage.getItem('layout-setting')) || ''`

复刻要求：
- `layout-setting` 的字段名与语义必须保持一致，否则 UI 配置无法在刷新后保持。

---

## 3) NavType 切换可观察行为

触发：
- 点击三种布局图标（left/mix/top）调用 `handleNavType(1|2|3)`

副作用（watch navType）：
- navType=1：
  - `appStore.sidebar.opened = true`
  - `appStore.toggleSideBarHide(false)`（sidebar 可见）
- navType=2：
  - `appStore.sidebar.opened = true`（sidebar 可见）
- navType=3：
  - `appStore.sidebar.opened = false`
  - `appStore.toggleSideBarHide(true)`（sidebar 隐藏）
- 当 navType in [1,3]：`permissionStore.setSidebarRouters(permissionStore.defaultRoutes)`

---

## 4) 主题与主题色

Sidebar Theme（theme-dark/theme-light）：
- 更新 `settingsStore.sideTheme`

主题色（primary）：
- 更新 `settingsStore.theme`
- 调用 `handleThemeStyle(val)` 写入：
  - `--el-color-primary`
  - `--el-color-primary-light-1..9`
  - `--el-color-primary-dark-1..9`

暗黑模式：
- 不在 Settings 抽屉中切换（暗黑切换位于 Navbar 的主题按钮）

---

## 5) 视觉基线提示

视觉基线测试在生成截图前会写入 `layout-setting`，以确保截图稳定可复现：
- 见 `docs/ui-ux-spec/08_Visual_Baseline/README.md`
