# ai_chat_service.py（Service）

## Source
- Source: `ruoyi-fastapi-backend/module_ai/service/ai_chat_service.py`

## Imports（依赖概览）

```python
import json
import os
import uuid
from collections.abc import AsyncGenerator, AsyncIterator
from datetime import datetime
from typing import TYPE_CHECKING, Any
from agno.agent import Agent
from agno.db.base import SessionType
from agno.media import Image
from agno.run.agent import RunEvent, RunOutput, RunOutputEvent
from agno.run.cancel import acancel_run
from sqlalchemy.ext.asyncio import AsyncSession
from common.vo import CrudResponseModel
from config.env import UploadConfig
from exceptions.exception import ServiceException
from module_ai.dao.ai_chat_dao import AiChatConfigDao
from module_ai.dao.ai_model_dao import AiModelDao
from module_ai.entity.do.ai_chat_do import AiChatConfig
from module_ai.entity.vo.ai_chat_vo import (
from module_ai.entity.vo.ai_model_vo import AiModelModel
from utils.ai_util import AiUtil
from utils.common_util import CamelCaseUtil
from utils.crypto_util import CryptoUtil
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `chat_services` | Y | `AsyncSession query_db, AiChatRequestModel chat_req, int user_id` | `AsyncGenerator[str, None]` | 流式对话 | AiModelDao.get_ai_model_detail_by_id | '模型不存在' |
| `ai_chat_config_detail_services` | Y | `AsyncSession query_db, int user_id` | `AiChatConfigModel` | 获取用户配置 | AiChatConfigDao.get_chat_config_detail_by_user_id |  |
| `save_ai_chat_config_services` | Y | `AsyncSession query_db, int user_id, AiChatConfigModel page_object` | `CrudResponseModel` | 保存用户配置 | AiChatConfigDao.add_chat_config_dao, AiChatConfigDao.edit_chat_config_dao, AiChatConfigDao.get_chat_config_detail_by_user_id | '只允许修改当前用户的配置' |
| `get_chat_session_list_services` | Y | `int user_id` | `list[AiChatSessionBaseModel]` | 获取用户会话列表 |  |  |
| `delete_chat_session_services` | Y | `str session_id` | `CrudResponseModel` | 删除会话 |  | '删除会话失败' |
| `get_chat_session_detail_services` | Y | `str session_id` | `AiChatSessionModel` | 获取会话消息详情 |  | '会话不存在' |
| `cancel_run_services` | Y | `str run_id` | `CrudResponseModel` | 取消运行 |  | '取消运行失败' |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
