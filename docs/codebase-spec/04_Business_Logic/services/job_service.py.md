# job_service.py（Service）

## Source
- Source: `ruoyi-fastapi-backend/module_admin/service/job_service.py`

## Imports（依赖概览）

```python
from typing import Any
from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession
from common.constant import CommonConstant, JobConstant
from common.vo import CrudResponseModel, PageModel
from config.get_scheduler import SchedulerUtil
from exceptions.exception import ServiceException
from module_admin.dao.job_dao import JobDao
from module_admin.entity.vo.job_vo import DeleteJobModel, EditJobModel, JobModel, JobPageQueryModel
from module_admin.service.dict_service import DictDataService
from utils.common_util import CamelCaseUtil
from utils.cron_util import CronUtil
from utils.excel_util import ExcelUtil
from utils.string_util import StringUtil
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `get_job_list_services` | Y | `AsyncSession query_db, JobPageQueryModel query_object, bool is_page` | `PageModel \| list[dict[str, Any]]` | 获取定时任务列表信息service | JobDao.get_job_list |  |
| `check_job_unique_services` | Y | `AsyncSession query_db, JobModel page_object` | `bool` | 校验定时任务是否存在service | JobDao.get_job_detail_by_info |  |
| `add_job_services` | Y | `AsyncSession query_db, JobModel page_object` | `CrudResponseModel` | 新增定时任务信息service | JobDao.add_job_dao | f'新增定时任务{page_object.job_name}失败，Cron表达式不正确'; f'新增定时任务{page_object.job_name}失败，目标字符串不允许rmi调用'; f'新增定时任务{page_object.job_name}失败，目标字符串不允许ldap(s; f'新增定时任务{page_object.job_name}失败，目标字符串不允许http(s; f'新增定时任务{page_object.job_name}失败，目标字符串存在违规'; f'新增定时任务{page_object.job_name}失败，目标字符串不在白名单内'; f'新增定时任务{page_object.job_name}失败，定时任务已存在' |
| `edit_job_services` | Y | `AsyncSession query_db, EditJobModel page_object` | `CrudResponseModel` | 编辑定时任务信息service | JobDao.edit_job_dao | f'修改定时任务{page_object.job_name}失败，Cron表达式不正确'; f'修改定时任务{page_object.job_name}失败，目标字符串不允许rmi调用'; f'修改定时任务{page_object.job_name}失败，目标字符串存在违规'; f'修改定时任务{page_object.job_name}失败，目标字符串不在白名单内'; f'修改定时任务{page_object.job_name}失败，定时任务已存在'; '定时任务不存在' |
| `execute_job_once_services` | Y | `AsyncSession query_db, JobModel page_object` | `CrudResponseModel` | 执行一次定时任务service |  | '定时任务不存在' |
| `delete_job_services` | Y | `AsyncSession query_db, DeleteJobModel page_object` | `CrudResponseModel` | 删除定时任务信息service | JobDao.delete_job_dao | '传入定时任务id为空' |
| `job_detail_services` | Y | `AsyncSession query_db, int job_id` | `JobModel` | 获取定时任务详细信息service | JobDao.get_job_detail_by_id |  |
| `export_job_list_services` | Y | `Request request, list job_list` | `bytes` | 导出定时任务信息service |  |  |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
