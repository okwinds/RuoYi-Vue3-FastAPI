# log_service.py（Service）

## Source
- Source: `ruoyi-fastapi-backend/module_admin/service/log_service.py`

## Imports（依赖概览）

```python
from typing import Any
from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession
from common.vo import CrudResponseModel, PageModel
from exceptions.exception import ServiceException
from module_admin.dao.log_dao import LoginLogDao, OperationLogDao
from module_admin.entity.vo.log_vo import (
from module_admin.service.dict_service import DictDataService
from utils.excel_util import ExcelUtil
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `get_operation_log_list_services` | Y | `AsyncSession query_db, OperLogPageQueryModel query_object, bool is_page` | `PageModel \| list[dict[str, Any]]` | 获取操作日志列表信息service | OperationLogDao.get_operation_log_list |  |
| `add_operation_log_services` | Y | `AsyncSession query_db, OperLogModel page_object` | `CrudResponseModel` | 新增操作日志service | OperationLogDao.add_operation_log_dao |  |
| `delete_operation_log_services` | Y | `AsyncSession query_db, DeleteOperLogModel page_object` | `CrudResponseModel` | 删除操作日志信息service | OperationLogDao.delete_operation_log_dao | '传入操作日志id为空' |
| `clear_operation_log_services` | Y | `AsyncSession query_db` | `CrudResponseModel` | 清除操作日志信息service | OperationLogDao.clear_operation_log_dao |  |
| `export_operation_log_list_services` | Y | `Request request, list operation_log_list` | `bytes` | 导出操作日志信息service |  |  |
| `get_login_log_list_services` | Y | `AsyncSession query_db, LoginLogPageQueryModel query_object, bool is_page` | `PageModel \| list[dict[str, Any]]` | 获取登录日志列表信息service | LoginLogDao.get_login_log_list |  |
| `add_login_log_services` | Y | `AsyncSession query_db, LogininforModel page_object` | `CrudResponseModel` | 新增登录日志service | LoginLogDao.add_login_log_dao |  |
| `delete_login_log_services` | Y | `AsyncSession query_db, DeleteLoginLogModel page_object` | `CrudResponseModel` | 删除操作日志信息service | LoginLogDao.delete_login_log_dao | '传入登录日志id为空' |
| `clear_login_log_services` | Y | `AsyncSession query_db` | `CrudResponseModel` | 清除操作日志信息service | LoginLogDao.clear_login_log_dao |  |
| `unlock_user_services` | Y | `Request request, UnlockUser unlock_user` | `CrudResponseModel` |  |  | '该用户未锁定' |
| `export_login_log_list_services` | Y | `list login_log_list` | `bytes` | 导出登录日志信息service |  |  |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
