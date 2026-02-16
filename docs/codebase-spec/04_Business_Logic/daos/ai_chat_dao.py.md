# ai_chat_dao.py（DAO）

## Source
- Source: `ruoyi-fastapi-backend/module_ai/dao/ai_chat_dao.py`

## Imports（依赖概览）

```python
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from module_ai.entity.do.ai_chat_do import AiChatConfig
from module_ai.entity.vo.ai_chat_vo import AiChatConfigModel
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `get_chat_config_detail_by_user_id` | Y | `AsyncSession db, int user_id` | `AiChatConfig \| None` | 根据用户ID获取配置 |  |  |
| `add_chat_config_dao` | Y | `AsyncSession db, AiChatConfigModel chat_config` | `AiChatConfig` | 新增对话配置数据库操作 |  |  |
| `edit_chat_config_dao` | Y | `AsyncSession db, dict chat_config` | `None` | 编辑对话配置数据库操作 |  |  |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
