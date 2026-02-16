# notice_dao.py（DAO）

## Source
- Source: `ruoyi-fastapi-backend/module_admin/dao/notice_dao.py`

## Imports（依赖概览）

```python
from datetime import datetime, time
from typing import Any
from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from common.vo import PageModel
from module_admin.entity.do.notice_do import SysNotice
from module_admin.entity.vo.notice_vo import NoticeModel, NoticePageQueryModel
from utils.page_util import PageUtil
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `get_notice_detail_by_id` | Y | `AsyncSession db, int notice_id` | `SysNotice \| None` | 根据通知公告id获取通知公告详细信息 |  |  |
| `get_notice_detail_by_info` | Y | `AsyncSession db, NoticeModel notice` | `SysNotice \| None` | 根据通知公告参数获取通知公告信息 |  |  |
| `get_notice_list` | Y | `AsyncSession db, NoticePageQueryModel query_object, bool is_page` | `PageModel \| list[dict[str, Any]]` | 根据查询参数获取通知公告列表信息 |  |  |
| `add_notice_dao` | Y | `AsyncSession db, NoticeModel notice` | `SysNotice` | 新增通知公告数据库操作 |  |  |
| `edit_notice_dao` | Y | `AsyncSession db, dict notice` | `None` | 编辑通知公告数据库操作 |  |  |
| `delete_notice_dao` | Y | `AsyncSession db, NoticeModel notice` | `None` | 删除通知公告数据库操作 |  |  |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
