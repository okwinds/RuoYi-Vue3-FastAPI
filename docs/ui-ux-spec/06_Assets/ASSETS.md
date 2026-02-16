# 资产规范（Assets）

---

## 1) 图标（SVG Icons）

目录：`src/assets/icons/svg/`

- 图标以 `*.svg` 文件存放，通过 `SvgIcon` 组件以 sprite 方式渲染（`#icon-<name>`）。
- 路由 meta 的 `icon` 字段与 svg 文件名对应（例如 `dashboard.svg`）。

复刻要求：
- 必须保留“svg 名称 → icon id”的稳定映射，否则菜单与按钮图标会丢失。

---

## 2) 图片（Images）

常用图片资源：
- 登录背景：`src/assets/images/login-background.jpg`
- 登录页明暗模式辅助图：`src/assets/images/dark.svg` / `light.svg`
- 错误页：
  - `src/assets/401_images/401.gif`
  - `src/assets/404_images/404.png`
  - `src/assets/404_images/404_cloud.png`
- Logo：`src/assets/logo/logo.png`
- 默认头像：`src/assets/images/profile.jpg`

---

## 3) Public 资源

- `public/favicon.ico`
