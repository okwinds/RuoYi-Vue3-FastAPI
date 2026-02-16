# Method Specs Index（方法级可复刻规格索引）

本目录用于补齐“内部等价复刻”所需的**方法级决策树**：仅靠 `services/*.py.md` 的方法名目录不足以重写逻辑，这里把关键链路展开成可直接写伪代码的规格。

> 约定：每份方法规格都必须包含：输入/输出、依赖、决策树、边界条件、错误策略、Source anchors、验收与测试计划。

---

## 登录 / 鉴权 / 动态路由

- `login_authenticate_user.md`：登录校验（IP 黑名单、验证码、密码错误次数与锁定）。
- `auth_get_current_user.md`：JWT decode + Redis 在线态校验 + 权限/角色组装 + TTL 刷新。
- `routing_get_current_user_routers.md`：菜单树 → Router 树（目录/菜单/内链规则）。

## AI

- `ai_chat_stream_protocol.md`：AI 对话流式协议（JSON Lines）、Reasoning、Vision 图片路径转换。
- `ai_model_api_key_handling.md`：AI 模型 API key 加密入库、掩码回显、编辑时“保持原值”规则。

## 任务调度

- `scheduler_init_and_event_logging.md`：启动加载任务、Cron 扩展、事件监听日志落库。

## 上传/静态资源

- `upload_and_download_paths.md`：上传命名、resource 下载文件名校验与路径转换。

