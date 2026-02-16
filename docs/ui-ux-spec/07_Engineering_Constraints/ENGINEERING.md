# 工程约束（Engineering Constraints）

本文件记录 UI 实现层面的约束：构建方式、目录结构、样式组织、主题机制与本地开发代理等。复刻时可替换框架，但需保持这些“可观察行为”一致。

---

## 1) 构建与运行（Vite）

配置文件：`ruoyi-fastapi-frontend/vite.config.js`

关键约束：
- Dev server 默认端口：`80`
- Dev proxy：
  - `/dev-api` → `http://127.0.0.1:9099`
  - 并 rewrite 去掉 `/dev-api` 前缀
- Path alias：
  - `@` → `./src`
  - `~` → `./`
- Build 输出：
  - `dist/`
  - chunk/asset 命名规则固定（`static/js/[name]-[hash].js` 等）

---

## 2) 样式组织（SCSS）

全局入口：`src/assets/styles/index.scss`

结构：
- 基础 mixin/transition
- Element Plus 覆写：`element-ui.scss`
- Sidebar/按钮/通用样式：`sidebar.scss` / `btn.scss` / `ruoyi.scss`
- Tokens 与 CSS vars：`variables.module.scss`（同时导出为 SCSS 变量与 CSS 变量）

实现约束：
- 组件内多使用 `scoped` 样式；需要穿透时使用 `:deep(...)`
- 暗黑模式统一以 `html.dark` 作为根开关（由 `@vueuse/core` 控制）

---

## 3) 主题机制（Theme）

- 用户主题色：`settingsStore.theme`（默认 `#409EFF`）
- 应用时机：主题设置变更时调用 `src/utils/theme.js:handleThemeStyle(theme)`，写入 `--el-color-primary` 及 light/dark 系列变量
- 暗黑模式：`settingsStore.toggleTheme()` 通过 `useToggle(useDark())` 切换，最终表现为 `html.dark` class 的存在与否

---

## 4) 三种导航布局（NavType）

配置源：`src/settings.js`（默认 `navType=1`），并持久化到 `localStorage['layout-setting']`。

- `navType=1`：Navbar + Breadcrumb
- `navType=2`：Navbar + TopNav（混合）
- `navType=3`：Logo + TopBar（顶部导航为主，隐藏 hamburger）

---

## 5) 本地持久化（localStorage keys）

### 5.1 `layout-setting`（布局设置）

来源：
- 默认值：`ruoyi-fastapi-frontend/src/settings.js`
- 读取与合并：`ruoyi-fastapi-frontend/src/store/modules/settings.js`
- 写入/清空：`ruoyi-fastapi-frontend/src/layout/components/Settings/index.vue`

数据形态：
- Key：`localStorage["layout-setting"]`
- Value：JSON 字符串（对象）

Schema（复刻必须保持字段语义一致）：

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

说明：
- `Settings` 抽屉保存时会把上述字段全量写回 localStorage；复刻实现若拆分存储，也必须保证最终 UI 表现一致（侧栏/顶部布局、页签、主题色、暗黑模式等）。

### 5.2 `vueuse-color-scheme`（暗黑模式）

来源：
- `@vueuse/core` 的 `useDark()` 默认会使用 `localStorage["vueuse-color-scheme"]` 存储主题模式（常见值：`"dark"` / `"light"`）。

约束：
- 暗黑模式的最终可观察开关为 `html.dark` class（见 `docs/ui-ux-spec/01_Foundation/FOUNDATION.md`）。
- 视觉基线测试（`ruoyi-fastapi-test/visual/test_visual_baseline.py`）会写入该 key 来固定 light/dark；因此复刻实现应尽量保持该 key 的兼容性（或在初始化时做向后兼容读取）。
