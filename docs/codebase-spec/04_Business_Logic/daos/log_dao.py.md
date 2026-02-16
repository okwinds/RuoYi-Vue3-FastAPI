# log_dao.py（DAO）

## Source
- Source: `ruoyi-fastapi-backend/module_admin/dao/log_dao.py`

## Imports（依赖概览）

```python
from datetime import datetime, time
from typing import Any
from sqlalchemy import asc, delete, desc, select
from sqlalchemy.ext.asyncio import AsyncSession
from common.vo import PageModel
from module_admin.entity.do.log_do import SysLogininfor, SysOperLog
from module_admin.entity.vo.log_vo import LogininforModel, LoginLogPageQueryModel, OperLogModel, OperLogPageQueryModel
from utils.common_util import SnakeCaseUtil
from utils.page_util import PageUtil
from utils.time_format_util import TimeFormatUtil
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `get_operation_log_list` | Y | `AsyncSession db, OperLogPageQueryModel query_object, bool is_page` | `PageModel \| list[dict[str, Any]]` | 根据查询参数获取操作日志列表信息 |  |  |
| `add_operation_log_dao` | Y | `AsyncSession db, OperLogModel operation_log` | `SysOperLog` | 新增操作日志数据库操作 |  |  |
| `delete_operation_log_dao` | Y | `AsyncSession db, OperLogModel operation_log` | `None` | 删除操作日志数据库操作 |  |  |
| `clear_operation_log_dao` | Y | `AsyncSession db` | `None` | 清除操作日志数据库操作 |  |  |
| `get_login_log_list` | Y | `AsyncSession db, LoginLogPageQueryModel query_object, bool is_page` | `PageModel \| list[dict[str, Any]]` | 根据查询参数获取登录日志列表信息 |  |  |
| `add_login_log_dao` | Y | `AsyncSession db, LogininforModel login_log` | `SysLogininfor` | 新增登录日志数据库操作 |  |  |
| `delete_login_log_dao` | Y | `AsyncSession db, LogininforModel login_log` | `None` | 删除登录日志数据库操作 |  |  |
| `clear_login_log_dao` | Y | `AsyncSession db` | `None` | 清除登录日志数据库操作 |  |  |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
