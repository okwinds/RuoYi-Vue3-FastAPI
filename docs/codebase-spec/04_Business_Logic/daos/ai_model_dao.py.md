# ai_model_dao.py（DAO）

## Source
- Source: `ruoyi-fastapi-backend/module_ai/dao/ai_model_dao.py`

## Imports（依赖概览）

```python
from typing import Any
from sqlalchemy import ColumnElement, delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from common.vo import PageModel
from module_ai.entity.do.ai_model_do import AiModels
from module_ai.entity.vo.ai_model_vo import AiModelModel, AiModelPageQueryModel
from utils.page_util import PageUtil
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `get_ai_model_detail_by_id` | Y | `AsyncSession db, int model_id` | `AiModels \| None` | 根据AI模型id获取AI模型详细信息 |  |  |
| `get_ai_model_list` | Y | `AsyncSession db, AiModelPageQueryModel query_object, ColumnElement data_scope_sql, bool is_page` | `PageModel \| list[dict[str, Any]]` | 根据查询参数获取AI模型列表信息 |  |  |
| `add_ai_model_dao` | Y | `AsyncSession db, AiModelModel ai_model` | `AiModels` | 新增AI模型数据库操作 |  |  |
| `edit_ai_model_dao` | Y | `AsyncSession db, dict ai_model` | `None` | 编辑AI模型数据库操作 |  |  |
| `delete_ai_model_dao` | Y | `AsyncSession db, AiModelModel ai_model` | `None` | 删除AI模型数据库操作 |  |  |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
