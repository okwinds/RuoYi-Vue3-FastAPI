# Method Spec：AiChatService.chat_services / _stream_agent（可复刻级）

目标：仅凭本文档即可实现 AI 对话接口的关键行为：配置解析、Agent 构建、Vision 图片路径处理、流式协议（JSON Lines）。

Source：
- Source: `ruoyi-fastapi-backend/module_ai/service/ai_chat_service.py`
- Source: `ruoyi-fastapi-backend/utils/ai_util.py`
- Source: `ruoyi-fastapi-backend/utils/crypto_util.py`
- Source: `ruoyi-fastapi-backend/config/env.py`

---

## 1) 输入输出

入口方法：
- `chat_services(query_db, chat_req, user_id) -> AsyncGenerator[str]`

输入（关键字段）：
- `chat_req.model_id`：模型配置 id
- `chat_req.message`：用户输入
- `chat_req.session_id`：可空；空则生成 UUID
- `chat_req.images`：可空；当启用 vision 时用于附带图片
- `chat_req.is_reasoning`：是否输出推理内容（受模型配置支持限制）

输出：
- 流式字符串，每条为一行 JSON + `\\n`（见下文协议）

---

## 2) 配置解析规则（必须一致）

温度 temperature：
- `user_config.temperature or model_config.temperature`

Reasoning：
- 若 `model_config.support_reasoning != 'Y'` → False
- 否则 `bool(chat_req.is_reasoning)`

历史消息：
- `add_history = (user_config.add_history_to_context == '0')`
- `num_history = user_config.num_history_runs or 3`

Source：
- Source: `ruoyi-fastapi-backend/module_ai/service/ai_chat_service.py`

---

## 3) Agent 构建（_build_agent）

1) 解密 `api_key`：
- `real_api_key = CryptoUtil.decrypt(model_config.api_key)`
2) 用模型工厂创建 model：
- `AiUtil.get_model_from_factory(provider, model_code, model_name, api_key, base_url, temperature, max_tokens)`
3) 获取 storage engine：
- `AiUtil.get_storage_engine()`
4) 创建 `Agent(...)`：
- 固定 `id='chat-agent'`
- `description = system_prompt or 'You are a helpful AI assistant.'`
- `user_id` 使用字符串化
- `session_id` 使用请求/生成的 uuid
- `add_history_to_context/num_history_runs` 如上
- `markdown=True`

---

## 4) Vision 图片处理（_build_run_kwargs）

默认 run_kwargs：
- `{'stream': True, 'stream_events': True}`

当 `chat_req.images` 存在且 `user_config.vision_enabled` 为真：
- 遍历每个 img：
  - 只处理以 `UPLOAD_PREFIX`（默认 `/profile`）开头的路径
  - 转换为本地路径：`UPLOAD_PATH/<relative_path>`
  - `os.path.exists(abs_path)` 才加入 `processed_images`
- 最终：`run_kwargs['images'] = processed_images`

复刻约束：
- 必须保留“只接受上传目录内图片路径”的约束（避免任意文件读取风险）。

---

## 5) 流式协议（_stream_agent）

协议形态：JSON Lines（不是标准 SSE EventSource）。

严格输出顺序（复刻必须项）：
1) 首行 meta：
   - `{"session_id": session_id, "type": "meta"}\\n`
2) 消费 `agent.arun(chat_req.message, **run_kwargs)` 的 event stream：
   - `RunEvent.run_started` 且存在 `chunk.run_id`：
     - `{"run_id": chunk.run_id, "type": "run_info"}\\n`
   - `RunEvent.run_content`：
     - 若 `chunk.content` 存在：
       - `{"content": chunk.content, "type": "content"}\\n`
     - 若 `chunk.reasoning_content` 存在且 `is_reasoning=True`：
       - `{"content": reasoning, "type": "reasoning"}\\n`
   - `RunEvent.run_completed` 且存在 `chunk.metrics`：
     - `{"metrics": <camelCase metrics dict>, "type":"metrics"}\\n`
3) 异常：
   - 捕获异常并输出：`{"error": str(e), "type":"error"}\\n`

注意：
- 实现中会累积 `full_response/full_reasoning`，但不返回聚合结果；复刻时可以不保留该累积，只要流式输出一致。

---

## 6) 验收与测试计划

- [ ] 相同输入输出的 `type` 序列稳定：`meta` → `run_info` → (`content`/`reasoning`)* → `metrics`
- [ ] vision_enabled=false 或 images 为空时，run_kwargs 不包含 images
- [ ] images 含非 `/profile/...` 的路径时必须被忽略（不参与请求）

