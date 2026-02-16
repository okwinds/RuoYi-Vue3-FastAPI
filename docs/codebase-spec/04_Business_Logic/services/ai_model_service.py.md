# ai_model_service.py（Service）

## Source
- Source: `ruoyi-fastapi-backend/module_ai/service/ai_model_service.py`

## Imports（依赖概览）

```python
from typing import Any
from sqlalchemy import ColumnElement
from sqlalchemy.ext.asyncio import AsyncSession
from common.vo import CrudResponseModel, PageModel
from exceptions.exception import ServiceException
from module_ai.dao.ai_model_dao import AiModelDao
from module_ai.entity.vo.ai_model_vo import AiModelModel, AiModelPageQueryModel, DeleteAiModelModel
from utils.common_util import CamelCaseUtil
from utils.crypto_util import CryptoUtil
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `get_ai_model_list_services` | Y | `AsyncSession query_db, AiModelPageQueryModel query_object, ColumnElement data_scope_sql, bool is_page` | `PageModel \| list[dict[str, Any]]` | 获取AI模型列表信息service | AiModelDao.get_ai_model_list |  |
| `check_ai_model_data_scope_services` | Y | `AsyncSession query_db, int model_id, ColumnElement data_scope_sql` | `CrudResponseModel` | 校验用户是否有AI模型数据权限service | AiModelDao.get_ai_model_list | '没有权限访问AI模型数据' |
| `add_ai_model_services` | Y | `AsyncSession query_db, AiModelModel page_object` | `CrudResponseModel` | 新增AI模型信息service | AiModelDao.add_ai_model_dao |  |
| `edit_ai_model_services` | Y | `AsyncSession query_db, AiModelModel page_object` | `CrudResponseModel` | 编辑AI模型信息service | AiModelDao.edit_ai_model_dao | 'AI模型不存在' |
| `delete_ai_model_services` | Y | `AsyncSession query_db, DeleteAiModelModel page_object` | `CrudResponseModel` | 删除AI模型信息service | AiModelDao.delete_ai_model_dao | '传入AI模型id为空' |
| `ai_model_detail_services` | Y | `AsyncSession query_db, int model_id` | `AiModelModel` | 获取AI模型详细信息service | AiModelDao.get_ai_model_detail_by_id |  |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
