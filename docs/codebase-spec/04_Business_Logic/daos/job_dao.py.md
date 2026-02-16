# job_dao.py（DAO）

## Source
- Source: `ruoyi-fastapi-backend/module_admin/dao/job_dao.py`

## Imports（依赖概览）

```python
from collections.abc import Sequence
from typing import Any
from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from common.vo import PageModel
from module_admin.entity.do.job_do import SysJob
from module_admin.entity.vo.job_vo import JobModel, JobPageQueryModel
from utils.page_util import PageUtil
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `get_job_detail_by_id` | Y | `AsyncSession db, int job_id` | `SysJob \| None` | 根据定时任务id获取定时任务详细信息 |  |  |
| `get_job_detail_by_info` | Y | `AsyncSession db, JobModel job` | `SysJob \| None` | 根据定时任务参数获取定时任务信息 |  |  |
| `get_job_list` | Y | `AsyncSession db, JobPageQueryModel query_object, bool is_page` | `PageModel \| list[dict[str, Any]]` | 根据查询参数获取定时任务列表信息 |  |  |
| `get_job_list_for_scheduler` | Y | `AsyncSession db` | `Sequence[SysJob]` | 获取定时任务列表信息 |  |  |
| `add_job_dao` | Y | `AsyncSession db, JobModel job` | `SysJob` | 新增定时任务数据库操作 |  |  |
| `edit_job_dao` | Y | `AsyncSession db, dict job, JobModel old_job` | `None` | 编辑定时任务数据库操作 |  |  |
| `delete_job_dao` | Y | `AsyncSession db, JobModel job` | `None` | 删除定时任务数据库操作 |  |  |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
