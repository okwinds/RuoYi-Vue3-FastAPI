# post_dao.py（DAO）

## Source
- Source: `ruoyi-fastapi-backend/module_admin/dao/post_dao.py`

## Imports（依赖概览）

```python
from typing import Any
from sqlalchemy import delete, func, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from common.vo import PageModel
from module_admin.entity.do.post_do import SysPost
from module_admin.entity.do.user_do import SysUserPost
from module_admin.entity.vo.post_vo import PostModel, PostPageQueryModel
from utils.page_util import PageUtil
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `get_post_by_id` | Y | `AsyncSession db, int post_id` | `SysPost \| None` | 根据岗位id获取在用岗位详细信息 |  |  |
| `get_post_detail_by_id` | Y | `AsyncSession db, int post_id` | `SysPost \| None` | 根据岗位id获取岗位详细信息 |  |  |
| `get_post_detail_by_info` | Y | `AsyncSession db, PostModel post` | `SysPost \| None` | 根据岗位参数获取岗位信息 |  |  |
| `get_post_list` | Y | `AsyncSession db, PostPageQueryModel query_object, bool is_page` | `PageModel \| list[dict[str, Any]]` | 根据查询参数获取岗位列表信息 |  |  |
| `add_post_dao` | Y | `AsyncSession db, PostModel post` | `SysPost` | 新增岗位数据库操作 |  |  |
| `edit_post_dao` | Y | `AsyncSession db, dict post` | `None` | 编辑岗位数据库操作 |  |  |
| `delete_post_dao` | Y | `AsyncSession db, PostModel post` | `None` | 删除岗位数据库操作 |  |  |
| `count_user_post_dao` | Y | `AsyncSession db, int post_id` | `int \| None` | 根据岗位id查询岗位关联的用户数量 |  |  |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
