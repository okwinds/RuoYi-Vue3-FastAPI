# config_dao.py（DAO）

## Source
- Source: `ruoyi-fastapi-backend/module_admin/dao/config_dao.py`

## Imports（依赖概览）

```python
from datetime import datetime, time
from typing import Any
from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from common.vo import PageModel
from module_admin.entity.do.config_do import SysConfig
from module_admin.entity.vo.config_vo import ConfigModel, ConfigPageQueryModel
from utils.page_util import PageUtil
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `get_config_detail_by_id` | Y | `AsyncSession db, int config_id` | `SysConfig \| None` | 根据参数配置id获取参数配置详细信息 |  |  |
| `get_config_detail_by_info` | Y | `AsyncSession db, ConfigModel config` | `SysConfig \| None` | 根据参数配置参数获取参数配置信息 |  |  |
| `get_config_list` | Y | `AsyncSession db, ConfigPageQueryModel query_object, bool is_page` | `PageModel \| list[dict[str, Any]]` | 根据查询参数获取参数配置列表信息 |  |  |
| `add_config_dao` | Y | `AsyncSession db, ConfigModel config` | `SysConfig` | 新增参数配置数据库操作 |  |  |
| `edit_config_dao` | Y | `AsyncSession db, dict config` | `None` | 编辑参数配置数据库操作 |  |  |
| `delete_config_dao` | Y | `AsyncSession db, ConfigModel config` | `None` | 删除参数配置数据库操作 |  |  |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
