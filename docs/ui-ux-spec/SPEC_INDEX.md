# UI/UX Spec Index（像素级复刻规格索引）

本目录（`docs/ui-ux-spec/`）用于描述 **PC 管理后台前端（ruoyi-fastapi-frontend/）** 的 UI/UX 规格，目标是达到“像素级复刻”的可交付程度：
- 文字规格（tokens/结构/交互/状态）可复刻；
- 可执行视觉基线（Playwright screenshots）可验收；
- 规格与源码可互相定位（通过路径与关键 selector/约定）。

> 注意：本目录为 **UI-only**。业务含义、接口契约与权限语义不在此处解释，见 `docs/codebase-spec/` 与 `docs/specs/`。

---

## 01_Foundation（基础规范）

- `01_Foundation/FOUNDATION.md`：设计 tokens 与全局样式规范（颜色/暗黑模式/字体/通用样式）。
- `01_Foundation/LAYOUT_METRICS.md`：布局与像素级常量表（宽高/z-index/断点/阴影等，像素级复刻必须项）。

---

## 02_Components（组件规格）

- `02_Components/COMPONENTS.md`：组件目录与索引（从 inventory 到具体规格卡的导航入口）。
- `02_Components/components/`：组件规格卡（每个关键组件一份，可复刻级）。

---

## 03_Patterns（稳定模式）

- `03_Patterns/PATTERNS.md`：列表页/表单页/分栏等可复用页面模式与组合规则。

---

## 04_Pages（页面模板）

- `04_Pages/PAGES.md`：页面索引与信息架构（路由 meta、页面类型、导航布局）。
- `04_Pages/pages/`：关键页面的像素级模板（每页一份，含稳定 selector 与视觉基线绑定）。

---

## 05_A11y（可访问性）

- `05_A11y/A11Y.md`：可访问性现状、复刻要求与改进建议。

---

## 06_Assets（资产规范）

- `06_Assets/ASSETS.md`：图标与图片等 UI 资产清单与复刻要求。

---

## 07_Engineering_Constraints（工程约束）

- `07_Engineering_Constraints/ENGINEERING.md`：构建、样式组织、主题机制、NavType 等工程约束。

---

## 08_Visual_Baseline（视觉基线）

- `08_Visual_Baseline/README.md`：如何生成/校验截图基线（像素级验收真源）。
- `08_Visual_Baseline/screenshots/`：基线图片（PNG，命名规则固定）。
