# dict_service.py（Service）

## Source
- Source: `ruoyi-fastapi-backend/module_admin/service/dict_service.py`

## Imports（依赖概览）

```python
import json
from collections.abc import Sequence
from typing import Any
from fastapi import Request
from redis import asyncio as aioredis
from sqlalchemy.ext.asyncio import AsyncSession
from common.constant import CommonConstant
from common.enums import RedisInitKeyConfig
from common.vo import CrudResponseModel, PageModel
from exceptions.exception import ServiceException
from module_admin.dao.dict_dao import DictDataDao, DictTypeDao
from module_admin.entity.do.dict_do import SysDictData
from module_admin.entity.vo.dict_vo import (
from utils.common_util import CamelCaseUtil
from utils.excel_util import ExcelUtil
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `get_dict_type_list_services` | Y | `AsyncSession query_db, DictTypePageQueryModel query_object, bool is_page` | `PageModel \| list[dict[str, Any]]` | 获取字典类型列表信息service | DictTypeDao.get_dict_type_list |  |
| `check_dict_type_unique_services` | Y | `AsyncSession query_db, DictTypeModel page_object` | `bool` | 校验字典类型称是否唯一service | DictTypeDao.get_dict_type_detail_by_info |  |
| `add_dict_type_services` | Y | `Request request, AsyncSession query_db, DictTypeModel page_object` | `CrudResponseModel` | 新增字典类型信息service | DictTypeDao.add_dict_type_dao | f'新增字典{page_object.dict_name}失败，字典类型已存在' |
| `edit_dict_type_services` | Y | `Request request, AsyncSession query_db, DictTypeModel page_object` | `CrudResponseModel` | 编辑字典类型信息service | DictDataDao.edit_dict_data_dao, DictDataDao.get_dict_data_list, DictTypeDao.edit_dict_type_dao | f'修改字典{page_object.dict_name}失败，字典类型已存在'; '字典类型不存在' |
| `delete_dict_type_services` | Y | `Request request, AsyncSession query_db, DeleteDictTypeModel page_object` | `CrudResponseModel` | 删除字典类型信息service | DictDataDao.count_dict_data_dao, DictTypeDao.delete_dict_type_dao | f'{dict_type_into.dict_name}已分配，不能删除'; '传入字典类型id为空' |
| `dict_type_detail_services` | Y | `AsyncSession query_db, int dict_id` | `DictTypeModel` | 获取字典类型详细信息service | DictTypeDao.get_dict_type_detail_by_id |  |
| `export_dict_type_list_services` | Y | `list dict_type_list` | `bytes` | 导出字典类型信息service |  |  |
| `refresh_sys_dict_services` | Y | `Request request, AsyncSession query_db` | `CrudResponseModel` | 刷新字典缓存信息service |  |  |
| `get_dict_data_list_services` | Y | `AsyncSession query_db, DictDataPageQueryModel query_object, bool is_page` | `PageModel \| list[dict[str, Any]]` | 获取字典数据列表信息service | DictDataDao.get_dict_data_list |  |
| `query_dict_data_list_services` | Y | `AsyncSession query_db, str dict_type` | `Sequence[SysDictData]` | 获取字典数据列表信息service | DictDataDao.query_dict_data_list |  |
| `init_cache_sys_dict_services` | Y | `AsyncSession query_db, aioredis.Redis redis` | `None` | 应用初始化：获取所有字典类型对应的字典数据信息并缓存service | DictDataDao.query_dict_data_list, DictTypeDao.get_all_dict_type |  |
| `query_dict_data_list_from_cache_services` | Y | `aioredis.Redis redis, str dict_type` | `list[dict[str, Any]]` | 从缓存获取字典数据列表信息service |  |  |
| `check_dict_data_unique_services` | Y | `AsyncSession query_db, DictDataModel page_object` | `bool` | 校验字典数据是否唯一service | DictDataDao.get_dict_data_detail_by_info |  |
| `add_dict_data_services` | Y | `Request request, AsyncSession query_db, DictDataModel page_object` | `CrudResponseModel` | 新增字典数据信息service | DictDataDao.add_dict_data_dao |  |
| `edit_dict_data_services` | Y | `Request request, AsyncSession query_db, DictDataModel page_object` | `CrudResponseModel` | 编辑字典数据信息service | DictDataDao.edit_dict_data_dao | '字典数据不存在' |
| `delete_dict_data_services` | Y | `Request request, AsyncSession query_db, DeleteDictDataModel page_object` | `CrudResponseModel` | 删除字典数据信息service | DictDataDao.delete_dict_data_dao | '传入字典数据id为空' |
| `dict_data_detail_services` | Y | `AsyncSession query_db, int dict_code` | `DictDataModel` | 获取字典数据详细信息service | DictDataDao.get_dict_data_detail_by_id |  |
| `export_dict_data_list_services` | Y | `list dict_data_list` | `bytes` | 导出字典数据信息service |  |  |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
