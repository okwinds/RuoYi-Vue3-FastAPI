# AppMain（内容区）

Source：
- `ruoyi-fastapi-frontend/src/layout/components/AppMain.vue`
- `ruoyi-fastapi-frontend/src/layout/components/IframeToggle/index.vue`
- `ruoyi-fastapi-frontend/src/layout/components/Copyright/index.vue`

---

## 1) Purpose（目的）

AppMain 承担：
- `router-view` 的渲染与转场；
- keep-alive 缓存（`include = tagsViewStore.cachedViews`）；
- iframe 类型路由（`route.meta.link`）的特殊处理；
- 底部版权区域的占位与 padding 处理。

---

## 2) 结构（Structure）

骨架（简化）：

```
section.app-main
  router-view (slot: { Component, route })
    transition.fade-transform
      keep-alive (include=cachedViews)
        component (当 !route.meta.link 时渲染)
  iframe-toggle
  copyright
```

---

## 3) 像素级常量（Metrics）

详表见：`docs/ui-ux-spec/01_Foundation/LAYOUT_METRICS.md`

关键行为（必须复刻）：
- 默认：`min-height = calc(100vh - 50px)`（navbar 高）
- 开启 tagsView：`min-height = calc(100vh - 84px)`（50 + 34）
- `.fixed-header + .app-main`：
  - `margin-top` 与 `height` 随 tagsView 开关变化
  - `overflow-y: auto` 形成“头部固定、内容滚动”的效果
- iOS/Safari（`@supports (-webkit-touch-callout: none)`）下使用 `100svh/100dvh` 适配地址栏高度变化

---

## 4) Iframe 路由（route.meta.link）

逻辑：
- 若 `route.meta.link` 为真：不渲染当前 `Component`，而是调用 `useTagsViewStore().addIframeView(route)`，由 `IframeToggle` 管理 iframe 展示。

复刻要求：
- iframe 的标签与关闭行为必须与 TagsView 联动（刷新/关闭时需同步清理 iframe view）。
