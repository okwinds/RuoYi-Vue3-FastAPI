# job_log_service.py（Service）

## Source
- Source: `ruoyi-fastapi-backend/module_admin/service/job_log_service.py`

## Imports（依赖概览）

```python
from typing import Any
from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from common.vo import CrudResponseModel, PageModel
from module_admin.dao.job_log_dao import JobLogDao
from module_admin.entity.vo.job_vo import DeleteJobLogModel, JobLogModel, JobLogPageQueryModel
from module_admin.service.dict_service import DictDataService
from utils.excel_util import ExcelUtil
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `get_job_log_list_services` | Y | `AsyncSession query_db, JobLogPageQueryModel query_object, bool is_page` | `PageModel \| list[dict[str, Any]]` | 获取定时任务日志列表信息service | JobLogDao.get_job_log_list |  |
| `add_job_log_services` | N | `Session query_db, JobLogModel page_object` | `CrudResponseModel` | 新增定时任务日志信息service | JobLogDao.add_job_log_dao |  |
| `delete_job_log_services` | Y | `AsyncSession query_db, DeleteJobLogModel page_object` | `CrudResponseModel` | 删除定时任务日志信息service | JobLogDao.delete_job_log_dao |  |
| `clear_job_log_services` | Y | `AsyncSession query_db` | `CrudResponseModel` | 清除定时任务日志信息service | JobLogDao.clear_job_log_dao |  |
| `export_job_log_list_services` | Y | `Request request, list job_log_list` | `bytes` | 导出定时任务日志信息service |  |  |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
