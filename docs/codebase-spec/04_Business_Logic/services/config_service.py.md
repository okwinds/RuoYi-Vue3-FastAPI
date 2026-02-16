# config_service.py（Service）

## Source
- Source: `ruoyi-fastapi-backend/module_admin/service/config_service.py`

## Imports（依赖概览）

```python
from typing import Any
from fastapi import Request
from redis import asyncio as aioredis
from sqlalchemy.ext.asyncio import AsyncSession
from common.constant import CommonConstant
from common.enums import RedisInitKeyConfig
from common.vo import CrudResponseModel, PageModel
from exceptions.exception import ServiceException
from module_admin.dao.config_dao import ConfigDao
from module_admin.entity.vo.config_vo import ConfigModel, ConfigPageQueryModel, DeleteConfigModel
from utils.common_util import CamelCaseUtil
from utils.excel_util import ExcelUtil
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `get_config_list_services` | Y | `AsyncSession query_db, ConfigPageQueryModel query_object, bool is_page` | `PageModel \| list[dict[str, Any]]` | 获取参数配置列表信息service | ConfigDao.get_config_list |  |
| `init_cache_sys_config_services` | Y | `AsyncSession query_db, aioredis.Redis redis` | `None` | 应用初始化：获取所有参数配置对应的键值对信息并缓存service | ConfigDao.get_config_list |  |
| `query_config_list_from_cache_services` | Y | `aioredis.Redis redis, str config_key` | `Any` | 从缓存获取参数键名对应值service |  |  |
| `check_config_key_unique_services` | Y | `AsyncSession query_db, ConfigModel page_object` | `bool` | 校验参数键名是否唯一service | ConfigDao.get_config_detail_by_info |  |
| `add_config_services` | Y | `Request request, AsyncSession query_db, ConfigModel page_object` | `CrudResponseModel` | 新增参数配置信息service | ConfigDao.add_config_dao | f'新增参数{page_object.config_name}失败，参数键名已存在' |
| `edit_config_services` | Y | `Request request, AsyncSession query_db, ConfigModel page_object` | `CrudResponseModel` | 编辑参数配置信息service | ConfigDao.edit_config_dao | f'修改参数{page_object.config_name}失败，参数键名已存在'; '参数配置不存在' |
| `delete_config_services` | Y | `Request request, AsyncSession query_db, DeleteConfigModel page_object` | `CrudResponseModel` | 删除参数配置信息service | ConfigDao.delete_config_dao | f'内置参数{config_info.config_key}不能删除'; '传入参数配置id为空' |
| `config_detail_services` | Y | `AsyncSession query_db, int config_id` | `ConfigModel` | 获取参数配置详细信息service | ConfigDao.get_config_detail_by_id |  |
| `export_config_list_services` | Y | `list config_list` | `bytes` | 导出参数配置信息service |  |  |
| `refresh_sys_config_services` | Y | `Request request, AsyncSession query_db` | `CrudResponseModel` | 刷新字典缓存信息service |  |  |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
