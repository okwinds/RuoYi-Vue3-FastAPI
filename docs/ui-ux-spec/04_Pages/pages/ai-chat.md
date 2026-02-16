# Page Spec: AI 对话（ai-chat）

PageId：`ai-chat`  
Route：`/ai/chat`

Source：
- `ruoyi-fastapi-frontend/src/views/ai/chat/index.vue`
- `ruoyi-fastapi-frontend/src/views/ai/chat/components/AiMessage.vue`
- Backend contract（stream）：`docs/codebase-spec/03_API/openapi.json`（AI 管理-AI 对话相关 endpoints）

视觉基线（截图 ID）：
- `light_1_ai-chat.png`
- `dark_1_ai-chat.png`

---

## 1) 目的（Purpose）

提供 AI 流式对话 UI，包括：
- 输入消息与发送
- 消息列表展示（用户/助手气泡）
- 流式响应的逐步追加显示（前端表现为文本逐渐增长）

---

## 2) 像素级结构（Structure）

页面根容器：
- `.app-container.chat-container`

左右布局（Element Plus container）：
- 左侧会话历史（Aside）：
  - `el-aside.session-sidebar`，`width="260px"`
  - header：新建对话按钮（`el-button.new-chat-btn`，icon Plus）
  - session list：`.session-list`（支持 loading；无数据时显示“暂无历史对话”）
- 右侧主聊天区（Main）：
  - `.chat-main`
  - header：
    - 标题：`AI 智能助手`
    - 全局参数配置按钮（icon Setting，circle）
    - 模型选择 `el-select`（`style="width: 210px"`，placeholder="选择模型"）
  - history：
    - `.chat-history`（滚动容器）
    - 空态 welcome：`你好！我是你的 AI 助手` + 引导文案
    - 消息行：`.message-row.message-user` / `.message-row.message-ai`
  - input area：
    - `.chat-input-area` 内 `el-input[type=textarea]`（placeholder：`请输入您的问题... (Enter 发送，Shift + Enter 换行)`）
    - 可选图片预览区域 `.selected-images`（vision enabled 且选中图片时）

消息渲染由 `AiMessage.vue` 负责（具体气泡样式与内容格式以实现为准，但复刻需保持最终视觉一致）。

---

## 3) 稳定 Selector（用于截图/自动化等待）

建议等待（用于视觉基线与自动化稳定性）：
- `.app-container.chat-container`
- `text=AI 智能助手`
- `textarea[placeholder^="请输入您的问题"]`

---

## 4) 关键交互（Interactions）

最小可观察行为（复刻必须满足）：
- 发送后进入 loading/streaming 状态（可通过禁用按钮/展示加载提示等体现）
- 服务端以流式返回时，页面能持续追加内容直到结束
- 允许取消运行（如实现提供“取消”入口，需保持等价行为）
