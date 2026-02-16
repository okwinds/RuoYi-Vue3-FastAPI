# notice_service.py（Service）

## Source
- Source: `ruoyi-fastapi-backend/module_admin/service/notice_service.py`

## Imports（依赖概览）

```python
from typing import Any
from sqlalchemy.ext.asyncio import AsyncSession
from common.constant import CommonConstant
from common.vo import CrudResponseModel, PageModel
from exceptions.exception import ServiceException
from module_admin.dao.notice_dao import NoticeDao
from module_admin.entity.vo.notice_vo import DeleteNoticeModel, NoticeModel, NoticePageQueryModel
from utils.common_util import CamelCaseUtil
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `get_notice_list_services` | Y | `AsyncSession query_db, NoticePageQueryModel query_object, bool is_page` | `PageModel \| list[dict[str, Any]]` | 获取通知公告列表信息service | NoticeDao.get_notice_list |  |
| `check_notice_unique_services` | Y | `AsyncSession query_db, NoticeModel page_object` | `bool` | 校验通知公告是否存在service | NoticeDao.get_notice_detail_by_info |  |
| `add_notice_services` | Y | `AsyncSession query_db, NoticeModel page_object` | `CrudResponseModel` | 新增通知公告信息service | NoticeDao.add_notice_dao | f'新增通知公告{page_object.notice_title}失败，通知公告已存在' |
| `edit_notice_services` | Y | `AsyncSession query_db, NoticeModel page_object` | `CrudResponseModel` | 编辑通知公告信息service | NoticeDao.edit_notice_dao | f'修改通知公告{page_object.notice_title}失败，通知公告已存在'; '通知公告不存在' |
| `delete_notice_services` | Y | `AsyncSession query_db, DeleteNoticeModel page_object` | `CrudResponseModel` | 删除通知公告信息service | NoticeDao.delete_notice_dao | '传入通知公告id为空' |
| `notice_detail_services` | Y | `AsyncSession query_db, int notice_id` | `NoticeModel` | 获取通知公告详细信息service | NoticeDao.get_notice_detail_by_id |  |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
