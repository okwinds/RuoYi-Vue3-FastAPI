# AI Providers 集成规格（可复刻级）

本文件描述本仓库 AI 能力的“可替换实现”契约：**模型工厂、provider 命名、API key 加密、SSE 流式协议、会话存储引擎**。

> 复刻目标：允许替换为其它 LLM SDK/中间件（OpenAI/Anthropic/自建网关等），但必须保持接口与行为语义一致。

---

## 1) Provider 命名与模型工厂（Model Factory）

模型实例由 `AiUtil.get_model_from_factory()` 统一创建，输入字段（来自 AI 模型配置）：
- `provider`：提供商字符串（见 `provider_model_map`）
- `model_code`：模型编码（用作 `id`）
- `model_name`：模型名称（用作 `name`，可空）
- `api_key`：密钥（运行时解密得到）
- `base_url`：可空（部分 provider 有默认）
- `temperature/max_tokens`：可空

特殊规则（复刻必须项）：
- `provider == 'ollama'` 时：将 `base_url` 映射为参数 `host`
- `provider == 'DashScope'` 且未传 base_url：使用默认 `https://dashscope.aliyuncs.com/compatible-mode/v1`
- provider 未命中映射时：默认使用 `OpenAIChat`

Source：
- Source: `ruoyi-fastapi-backend/utils/ai_util.py`

### 1.1 provider_model_map（当前仓库内置）

`provider_model_map` keys 是“配置可选项”的真源（字段级以 DB 与 OpenAPI 为准）：
- `OpenAI` / `OpenAIResponses` / `Anthropic` / `Google` / `DeepSeek` / `Groq` / `Ollama` / `OpenRouter` ……

复刻约束：
- provider 字符串必须与存量数据一致（否则配置不可迁移）。
- 若要扩展 provider，应保持“向后兼容”：旧 provider 值必须仍可解析。

Source：
- Source: `ruoyi-fastapi-backend/utils/ai_util.py`

---

## 2) API Key 加密策略（对存量数据兼容）

AI 模型配置中 `api_key` 在 DB 中以密文存储：
- 写入（新增/编辑）时加密：`CryptoUtil.encrypt(api_key)`
- 运行时使用前解密：`CryptoUtil.decrypt(model_config.api_key)`

关键约束：
- 加解密 Fernet key **由 JWT secret 派生**（见 `05_Integrations/CRYPTO.md`）
- 旋转 `JWT_SECRET_KEY` 会导致历史密文无法解密（等价于“全部 API key 失效”）

Source：
- Source: `ruoyi-fastapi-backend/module_ai/service/ai_model_service.py`
- Source: `ruoyi-fastapi-backend/module_ai/service/ai_chat_service.py`
- Source: `ruoyi-fastapi-backend/utils/crypto_util.py`

---

## 3) 会话/记忆存储引擎（Agno DB）

本仓库使用 `agno` 的 DB 抽象保存 session/memory/metrics 等，并依据 `DB_TYPE` 选择引擎：
- `mysql` → `AsyncMySQLDb`
- `postgresql` → `AsyncPostgresDb`

固定表名（复刻必须项；对应业务查询与管理能力）：
- `ai_sessions`, `ai_memories`, `ai_metrics`, `ai_eval_runs`, `ai_knowledge`, `ai_culture`
- `ai_traces`, `ai_spans`, `ai_schema_versions`

Source：
- Source: `ruoyi-fastapi-backend/utils/ai_util.py`

复刻建议：
- 即便不用 agno，也应提供等价的数据抽象（按 user_id + session_id 分组，支持 runs/messages/metrics 查询）。

---

## 4) 流式对话协议（SSE-like JSON Lines）

后端对话接口返回的是“逐行 JSON”流（每行以 `\\n` 结尾），前端按行解析。

### 4.1 输出行格式

每一行是一段 JSON 对象，至少包含 `type` 字段：

- Meta（会话信息）：
  - `{"session_id":"<uuid>","type":"meta"}\\n`
- Run info（run_id）：
  - `{"run_id":"<id>","type":"run_info"}\\n`
- Content（增量内容）：
  - `{"content":"...","type":"content"}\\n`
- Reasoning（推理内容，可选）：
  - `{"content":"...","type":"reasoning"}\\n`
- Metrics（运行指标，可选）：
  - `{"metrics":{...},"type":"metrics"}\\n`
- Error（异常文本，可选）：
  - `{"error":"...","type":"error"}\\n`

复刻约束：
- `type` 值集合必须一致，否则前端渲染/状态机会失配。
- 该协议不是标准 EventSource（SSE），更接近 JSON Lines；但“逐行”这一点必须保持。

Source：
- Source: `ruoyi-fastapi-backend/module_ai/service/ai_chat_service.py`

### 4.2 Reasoning 开关语义

- 若 `model_config.support_reasoning != 'Y'`：无论请求如何，强制关闭
- 否则：取请求参数 `chat_req.is_reasoning` 的布尔值

Source：
- Source: `ruoyi-fastapi-backend/module_ai/service/ai_chat_service.py`

---

## 5) Vision 图片路径转换（Upload prefix ↔ 本地路径）

输入（前端 → 后端）：
- `chat_req.images` 中的每一项若以 `UploadConfig.UPLOAD_PREFIX` 开头（默认 `/profile`）：
  - 会被视为“上传目录中的资源”
  - 后端把它映射到 `UploadConfig.UPLOAD_PATH/<relative_path>`，存在才会加入 `images`

输出（后端 → 前端）：
- 从 agno Message 中拿到 `Image` 对象列表：
  - 若 `img.filepath` 位于 `UPLOAD_PATH` 目录下 → 转换为 `/profile/<relpath>` URL
  - 否则原样返回 filepath
  - 若 `img.url` 存在 → 直接返回 URL

Source：
- Source: `ruoyi-fastapi-backend/module_ai/service/ai_chat_service.py`
- Source: `ruoyi-fastapi-backend/config/env.py`

---

## 6) 验收与测试计划

- [ ] `AI 模型管理`：新增模型时 `api_key` 入库为密文；查询详情返回 `****************` 形态
- [ ] `AI 对话`：在相同输入下，返回的 JSON lines `type` 序列符合上述协议
- [ ] `Vision`：上传目录中的图片路径能被解析成可用的本地文件路径并参与请求

