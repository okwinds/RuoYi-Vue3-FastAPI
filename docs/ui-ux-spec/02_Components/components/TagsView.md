# TagsView（页签视图）

Source：
- `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue`
- `ruoyi-fastapi-frontend/src/layout/components/TagsView/ScrollPane.vue`
- `ruoyi-fastapi-frontend/src/store/modules/tagsView.js`
- `ruoyi-fastapi-frontend/src/assets/styles/variables.module.scss`

---

## 1) Purpose（目的）

TagsView 提供：
- 已访问页面的标签（visited views）展示；
- 标签关闭、关闭其它/左侧/右侧/全部；
- 标签右键菜单（contextmenu）；
- 与 keep-alive 的缓存列表联动（由 tagsView store 提供 cachedViews）。

---

## 2) 像素级常量（Metrics）

详表见：`docs/ui-ux-spec/01_Foundation/LAYOUT_METRICS.md`

摘要（来自样式实现）：
- 容器高：34px
- tag 高：26px，margin-top 4px，左侧首个 margin-left 15px
- active tag：背景 `#42b983`，边框同色；左侧圆点 8px（当 `has-icon` 时不显示圆点）
- 右键菜单 z-index：3000

---

## 3) 结构（Structure）

骨架（简化）：

```
.tags-view-container
  ScrollPane.tags-view-wrapper
    router-link.tags-view-item*
      (可选) SvgIcon
      title text
      (可选) close icon
  ul.contextmenu (右键菜单)
```

关键 class（用于视觉基线等待）：
- `#tags-view-container.tags-view-container`
- `.tags-view-item.active`

---

## 4) 交互（Interactions）

### 4.1 激活样式（Active）

`activeStyle(tag)`：
- 当 tag 对应当前 route：
  - `background-color = settingsStore.theme`
  - `border-color = settingsStore.theme`

同时，CSS 中 `.tags-view-item.active` 也定义了绿色默认样式；最终视觉以“inline style 覆盖 + CSS”叠加为准，复刻时需要保证：
- active tag 的最终背景与边框跟随主题色（来自 settingsStore.theme）。

### 4.2 右键菜单定位

`openMenu(tag, e)`：
- `menuMinWidth = 105`
- `left` 计算：`e.clientX - containerLeft + 15`，并限制不超过 `maxLeft`
- `top = e.clientY`

### 4.3 刷新/关闭行为

通过 `proxy.$tab.*` 调用统一的 tab 管理插件完成：
- refresh page
- close current/others/left/right/all

---

## 5) Theme / Dark Mode（颜色钩子）

TagsView 的基础色尽量使用 CSS 变量（暗黑模式在 `variables.module.scss` 覆盖）：
- 容器背景：`--tags-bg`
- item 背景/边框/文字：`--tags-item-bg` / `--tags-item-border` / `--tags-item-text`
- hover：`--tags-item-hover`
- close hover：`--tags-close-hover`
