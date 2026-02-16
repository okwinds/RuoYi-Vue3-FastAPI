# Page Spec: AI 模型管理（ai-model）

PageId：`ai-model`  
Route：`/ai/model`

Source：
- `ruoyi-fastapi-frontend/src/views/ai/model/index.vue`
- Backend contract：`docs/codebase-spec/03_API/openapi.json`（AI 管理-AI 模型相关 endpoints）

视觉基线（截图 ID）：
- `light_1_ai-model.png`
- `dark_1_ai-model.png`

---

## 1) 目的（Purpose）

管理 AI 模型配置（列表、添加、编辑、删除），包括 provider、model name、base url、api key 等字段（字段级契约以 OpenAPI 为准）。

---

## 2) 像素级结构（Structure）

页面模板（CRUD List）：
1) Search Form（按实现提供）
2) Toolbar（新增/修改/删除）
3) Table（模型列表）
4) Dialog（新增/编辑）

实现约束（可观察）：
- 搜索表单字段：
  - 模型编码（`label="模型编码"`，input 宽度 200px）
  - 提供商（select 宽度 200px）
  - 状态（select 宽度 240px）
- 工具条按钮包含 v-hasPermi：
  - 新增：`ai:model:add`
  - 修改：`ai:model:edit`
  - 删除：`ai:model:remove`
- 表格列包含：
  - 模型ID、模型编码、提供商、支持推理、支持图片、状态、创建时间、操作（修改/删除）
- 弹窗：
  - 宽度 `700px`
  - 包含 API Key/Base URL 等字段（API Key 为 password input）

---

## 3) 稳定 Selector（用于截图/自动化等待）

建议等待：
- `.app-container`
- `text=模型编码`
- `button:has-text("新增")`

---

## 4) 关键交互（Interactions）

复刻必须满足：
- API key 在编辑时的显示策略与提交策略保持一致（后端会对 api_key 做加密存储与更新策略；见后端 method-spec 与 service 实现）。
