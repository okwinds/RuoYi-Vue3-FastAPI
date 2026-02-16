# dict_dao.py（DAO）

## Source
- Source: `ruoyi-fastapi-backend/module_admin/dao/dict_dao.py`

## Imports（依赖概览）

```python
from collections.abc import Sequence
from datetime import datetime, time
from typing import Any
from sqlalchemy import and_, delete, func, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from common.vo import PageModel
from module_admin.entity.do.dict_do import SysDictData, SysDictType
from module_admin.entity.vo.dict_vo import DictDataModel, DictDataPageQueryModel, DictTypeModel, DictTypePageQueryModel
from utils.page_util import PageUtil
from utils.time_format_util import list_format_datetime
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `get_dict_type_detail_by_id` | Y | `AsyncSession db, int dict_id` | `SysDictType \| None` | 根据字典类型id获取字典类型详细信息 |  |  |
| `get_dict_type_detail_by_info` | Y | `AsyncSession db, DictTypeModel dict_type` | `SysDictType \| None` | 根据字典类型参数获取字典类型信息 |  |  |
| `get_all_dict_type` | Y | `AsyncSession db` | `list[Any]` | 获取所有的字典类型信息 |  |  |
| `get_dict_type_list` | Y | `AsyncSession db, DictTypePageQueryModel query_object, bool is_page` | `PageModel \| list[dict[str, Any]]` | 根据查询参数获取字典类型列表信息 |  |  |
| `add_dict_type_dao` | Y | `AsyncSession db, DictTypeModel dict_type` | `SysDictType` | 新增字典类型数据库操作 |  |  |
| `edit_dict_type_dao` | Y | `AsyncSession db, dict dict_type` | `None` | 编辑字典类型数据库操作 |  |  |
| `delete_dict_type_dao` | Y | `AsyncSession db, DictTypeModel dict_type` | `None` | 删除字典类型数据库操作 |  |  |
| `get_dict_data_detail_by_id` | Y | `AsyncSession db, int dict_code` | `SysDictData \| None` | 根据字典数据id获取字典数据详细信息 |  |  |
| `get_dict_data_detail_by_info` | Y | `AsyncSession db, DictDataModel dict_data` | `SysDictData \| None` | 根据字典数据参数获取字典数据信息 |  |  |
| `get_dict_data_list` | Y | `AsyncSession db, DictDataPageQueryModel query_object, bool is_page` | `PageModel \| list[dict[str, Any]]` | 根据查询参数获取字典数据列表信息 |  |  |
| `query_dict_data_list` | Y | `AsyncSession db, str dict_type` | `Sequence[SysDictData]` | 根据查询参数获取字典数据列表信息 |  |  |
| `add_dict_data_dao` | Y | `AsyncSession db, DictDataModel dict_data` | `SysDictData` | 新增字典数据数据库操作 |  |  |
| `edit_dict_data_dao` | Y | `AsyncSession db, dict dict_data` | `None` | 编辑字典数据数据库操作 |  |  |
| `delete_dict_data_dao` | Y | `AsyncSession db, DictDataModel dict_data` | `None` | 删除字典数据数据库操作 |  |  |
| `count_dict_data_dao` | Y | `AsyncSession db, str dict_type` | `int \| None` | 根据字典类型查询字典类型关联的字典数据数量 |  |  |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
