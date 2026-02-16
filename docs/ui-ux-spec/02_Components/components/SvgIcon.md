# SvgIcon（SVG Sprite 图标组件）

Source：
- `ruoyi-fastapi-frontend/src/components/SvgIcon/index.vue`
- `ruoyi-fastapi-frontend/src/assets/icons/svg/*.svg`

---

## 1) Purpose（目的）

SvgIcon 用于渲染 `src/assets/icons/svg/` 下的 svg sprite 图标，统一菜单/按钮图标的展示方式。

---

## 2) Props 契约

Props：
- `iconClass`（required）：svg 名称（不带扩展名）
- `className`（optional）：额外 class
- `color`（optional）：覆盖 `use` 的 fill；默认空字符串，继承 `currentColor`

---

## 3) Sprite ID 规则（必须保持稳定）

渲染规则：
- `iconName = '#icon-' + iconClass`
- `<use :xlink:href="iconName" />`

复刻要求：
- 必须保持“svg 文件名 → `#icon-<name>`”的稳定映射，否则路由 meta.icon 与按钮图标会丢失。
- 资产清单见：`docs/ui-ux-spec/06_Assets/ASSETS.md`

---

## 4) A11y 现状与复刻要求

现状：
- `<svg aria-hidden="true">`（图标不被读屏读取）

复刻要求：
- 装饰性图标可保持 aria-hidden
- 若图标承载语义（例如仅图标按钮），必须由外层补充可读文本（按钮文字或 `aria-label`）
