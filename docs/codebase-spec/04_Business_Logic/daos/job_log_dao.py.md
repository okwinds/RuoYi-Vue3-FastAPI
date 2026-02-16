# job_log_dao.py（DAO）

## Source
- Source: `ruoyi-fastapi-backend/module_admin/dao/job_log_dao.py`

## Imports（依赖概览）

```python
from datetime import datetime, time
from typing import Any
from sqlalchemy import delete, desc, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from common.vo import PageModel
from module_admin.entity.do.job_do import SysJobLog
from module_admin.entity.vo.job_vo import JobLogModel, JobLogPageQueryModel
from utils.page_util import PageUtil
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `get_job_log_list` | Y | `AsyncSession db, JobLogPageQueryModel query_object, bool is_page` | `PageModel \| list[dict[str, Any]]` | 根据查询参数获取定时任务日志列表信息 |  |  |
| `add_job_log_dao` | N | `Session db, JobLogModel job_log` | `SysJobLog` | 新增定时任务日志数据库操作 |  |  |
| `delete_job_log_dao` | Y | `AsyncSession db, JobLogModel job_log` | `None` | 删除定时任务日志数据库操作 |  |  |
| `clear_job_log_dao` | Y | `AsyncSession db` | `None` | 清除定时任务日志数据库操作 |  |  |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
