# Page Spec: 系统接口（Swagger）（tool-swagger）

PageId：`tool-swagger`  
Route：`/tool/swagger`

Source：
- `ruoyi-fastapi-frontend/src/views/tool/swagger/index.vue`
- E2E：`ruoyi-fastapi-test/tool/test_swagger.py`

视觉基线（截图 ID）：
- `light_1_tool-swagger.png`
- `dark_1_tool-swagger.png`

---

## 1) 目的（Purpose）

通过 iframe 承载后端 Swagger UI 或“Swagger 已禁用提示”，用于接口自查与调试入口。

---

## 2) 像素级结构（Structure）

页面结构要求：
- 页面中存在 `iframe` 元素
- iframe 内部显示内容：
  - 当后端禁用 Swagger：显示禁用提示（见 E2E 断言）
  - 当后端启用 Swagger：显示 Swagger UI（标题包含后端项目名）

---

## 3) 稳定 Selector（用于截图/自动化等待）

- `iframe` 可见
- `iframe` 内 `h1` 包含：
  - `Swagger UI has been disabled. Please enable it first.`（默认生产禁用情况下的期望）

---

## 4) 交互（Interactions）

该页面主要为“只读 iframe 内容”，不要求额外按钮交互。
