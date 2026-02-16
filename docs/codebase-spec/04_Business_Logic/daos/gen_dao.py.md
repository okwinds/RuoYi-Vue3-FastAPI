# gen_dao.py（DAO）

## Source
- Source: `ruoyi-fastapi-backend/module_generator/dao/gen_dao.py`

## Imports（依赖概览）

```python
from collections.abc import Sequence
from datetime import datetime, time
from typing import Any
from sqlalchemy import Row, delete, func, select, text, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlglot.expressions import Expression
from common.vo import PageModel
from config.env import DataBaseConfig
from module_generator.entity.do.gen_do import GenTable, GenTableColumn
from module_generator.entity.vo.gen_vo import (
from utils.page_util import PageUtil
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `get_gen_table_by_id` | Y | `AsyncSession db, int table_id` | `GenTable \| None` | 根据业务表id获取需要生成的业务表信息 |  |  |
| `get_gen_table_by_name` | Y | `AsyncSession db, str table_name` | `GenTable \| None` | 根据业务表名称获取需要生成的业务表信息 |  |  |
| `get_gen_table_all` | Y | `AsyncSession db` | `Sequence[GenTable]` | 获取所有业务表信息 |  |  |
| `create_table_by_sql_dao` | Y | `AsyncSession db, list[Expression] sql_statements` | `None` | 根据sql语句创建表结构 |  |  |
| `get_gen_table_list` | Y | `AsyncSession db, GenTablePageQueryModel query_object, bool is_page` | `PageModel \| list[dict[str, Any]]` | 根据查询参数获取代码生成业务表列表信息 |  |  |
| `get_gen_db_table_list` | Y | `AsyncSession db, GenTablePageQueryModel query_object, bool is_page` | `PageModel \| list[dict[str, Any]]` | 根据查询参数获取数据库列表信息 |  |  |
| `get_gen_db_table_list_by_names` | Y | `AsyncSession db, list[str] table_names` | `Sequence[Row]` | 根据业务表名称组获取数据库列表信息 |  |  |
| `add_gen_table_dao` | Y | `AsyncSession db, GenTableModel gen_table` | `GenTable` | 新增业务表数据库操作 |  |  |
| `edit_gen_table_dao` | Y | `AsyncSession db, dict gen_table` | `None` | 编辑业务表数据库操作 |  |  |
| `delete_gen_table_dao` | Y | `AsyncSession db, GenTableModel gen_table` | `None` | 删除业务表数据库操作 |  |  |
| `get_gen_table_column_list_by_table_id` | Y | `AsyncSession db, int table_id` | `GenTableColumn` | 根据业务表id获取需要生成的业务表字段列表信息 |  |  |
| `get_gen_db_table_columns_by_name` | Y | `AsyncSession db, str table_name` | `Sequence[Row]` | 根据业务表名称获取业务表字段列表信息 |  |  |
| `add_gen_table_column_dao` | Y | `AsyncSession db, GenTableColumnModel gen_table_column` | `GenTableColumn` | 新增业务表字段数据库操作 |  |  |
| `edit_gen_table_column_dao` | Y | `AsyncSession db, dict gen_table_column` | `None` | 编辑业务表字段数据库操作 |  |  |
| `delete_gen_table_column_by_table_id_dao` | Y | `AsyncSession db, GenTableColumnModel gen_table_column` | `None` | 通过业务表id删除业务表字段数据库操作 |  |  |
| `delete_gen_table_column_by_column_id_dao` | Y | `AsyncSession db, GenTableColumnModel gen_table_column` | `None` | 通过业务字段id删除业务表字段数据库操作 |  |  |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
