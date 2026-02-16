# gen_service.py（Service）

## Source
- Source: `ruoyi-fastapi-backend/module_generator/service/gen_service.py`

## Imports（依赖概览）

```python
import io
import json
import os
import zipfile
from datetime import datetime
from typing import Any
import aiofiles
from sqlalchemy.ext.asyncio import AsyncSession
from sqlglot import parse as sqlglot_parse
from sqlglot.expressions import Add, Alter, Create, Delete, Drop, Expression, Insert, Table, TruncateTable, Update
from common.constant import GenConstant
from common.vo import CrudResponseModel, PageModel
from config.env import DataBaseConfig, GenConfig
from exceptions.exception import ServiceException
from module_admin.entity.vo.user_vo import CurrentUserModel
from module_generator.dao.gen_dao import GenTableColumnDao, GenTableDao
from module_generator.entity.vo.gen_vo import (
from utils.common_util import CamelCaseUtil
from utils.gen_util import GenUtils
from utils.template_util import TemplateInitializer, TemplateUtils
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `get_gen_table_list_services` | Y | `AsyncSession query_db, GenTablePageQueryModel query_object, bool is_page` | `PageModel \| list[dict[str, Any]]` | 获取代码生成业务表列表信息service | GenTableDao.get_gen_table_list |  |
| `get_gen_db_table_list_services` | Y | `AsyncSession query_db, GenTablePageQueryModel query_object, bool is_page` | `PageModel \| list[dict[str, Any]]` | 获取数据库列表信息service | GenTableDao.get_gen_db_table_list |  |
| `get_gen_db_table_list_by_name_services` | Y | `AsyncSession query_db, list[str] table_names` | `list[GenTableModel]` | 根据表名称组获取数据库列表信息service | GenTableDao.get_gen_db_table_list_by_names |  |
| `import_gen_table_services` | Y | `AsyncSession query_db, list[GenTableModel] gen_table_list, CurrentUserModel current_user` | `CrudResponseModel` | 导入表结构service | GenTableColumnDao.add_gen_table_column_dao, GenTableColumnDao.get_gen_db_table_columns_by_name, GenTableDao.add_gen_table_dao | f'导入失败 |
| `edit_gen_table_services` | Y | `AsyncSession query_db, EditGenTableModel page_object` | `CrudResponseModel` | 编辑业务表信息service | GenTableColumnDao.edit_gen_table_column_dao, GenTableDao.edit_gen_table_dao | '业务表不存在' |
| `delete_gen_table_services` | Y | `AsyncSession query_db, DeleteGenTableModel page_object` | `CrudResponseModel` | 删除业务表信息service | GenTableColumnDao.delete_gen_table_column_by_table_id_dao, GenTableDao.delete_gen_table_dao | '传入业务表id为空' |
| `get_gen_table_by_id_services` | Y | `AsyncSession query_db, int table_id` | `GenTableModel` | 获取需要生成的业务表详细信息service | GenTableDao.get_gen_table_by_id |  |
| `get_gen_table_all_services` | Y | `AsyncSession query_db` | `list[GenTableModel]` | 获取所有业务表信息service | GenTableDao.get_gen_table_all |  |
| `create_table_services` | Y | `AsyncSession query_db, str sql, CurrentUserModel current_user` | `CrudResponseModel` | 创建表结构service | GenTableDao.create_table_by_sql_dao | f'创建表结构异常，详细错误信息：{e}'; '建表语句不合法' |
| `preview_code_services` | Y | `AsyncSession query_db, int table_id` | `dict[str, str]` | 预览代码service | GenTableDao.get_gen_table_by_id |  |
| `generate_code_services` | Y | `AsyncSession query_db, str table_name` | `CrudResponseModel` | 生成代码至指定路径service |  | f'渲染模板失败，表名：{render_info[3].table_name}，详细错误信息：{e}' |
| `batch_gen_code_services` | Y | `AsyncSession query_db, list[str] table_names` | `bytes` | 批量生成代码service |  |  |
| `sync_db_services` | Y | `AsyncSession query_db, str table_name` | `CrudResponseModel` | 同步数据库service | GenTableColumnDao.add_gen_table_column_dao, GenTableColumnDao.delete_gen_table_column_by_column_id_dao, GenTableColumnDao.edit_gen_table_column_dao, GenTableColumnDao.get_gen_db_table_columns_by_name, GenTableDao.get_gen_table_by_name |  |
| `set_sub_table` | Y | `AsyncSession query_db, GenTableModel gen_table` | `None` | 设置主子表信息 | GenTableDao.get_gen_table_by_name |  |
| `set_pk_column` | Y | `GenTableModel gen_table` | `None` | 设置主键列信息 |  |  |
| `set_table_from_options` | Y | `GenTableModel gen_table` | `GenTableModel` | 设置代码生成其他选项值 |  |  |
| `validate_edit` | Y | `EditGenTableModel edit_gen_table` | `None` | 编辑保存参数校验 |  | '树编码字段不能为空'; '树父编码字段不能为空'; '树名称字段不能为空'; '关联子表的表名不能为空'; '子表关联的外键名不能为空' |
| `get_gen_table_column_list_by_table_id_services` | Y | `AsyncSession query_db, int table_id` | `list[GenTableColumnModel]` | 获取业务表字段列表信息service | GenTableColumnDao.get_gen_table_column_list_by_table_id |  |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
