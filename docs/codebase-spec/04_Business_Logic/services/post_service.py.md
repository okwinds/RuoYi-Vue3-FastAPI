# post_service.py（Service）

## Source
- Source: `ruoyi-fastapi-backend/module_admin/service/post_service.py`

## Imports（依赖概览）

```python
from typing import Any
from sqlalchemy.ext.asyncio import AsyncSession
from common.constant import CommonConstant
from common.vo import CrudResponseModel, PageModel
from exceptions.exception import ServiceException
from module_admin.dao.post_dao import PostDao
from module_admin.entity.vo.post_vo import DeletePostModel, PostModel, PostPageQueryModel
from utils.common_util import CamelCaseUtil
from utils.excel_util import ExcelUtil
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `get_post_list_services` | Y | `AsyncSession query_db, PostPageQueryModel query_object, bool is_page` | `PageModel \| list[dict[str, Any]]` | 获取岗位列表信息service | PostDao.get_post_list |  |
| `check_post_name_unique_services` | Y | `AsyncSession query_db, PostModel page_object` | `bool` | 检查岗位名称是否唯一service | PostDao.get_post_detail_by_info |  |
| `check_post_code_unique_services` | Y | `AsyncSession query_db, PostModel page_object` | `bool` | 检查岗位编码是否唯一service | PostDao.get_post_detail_by_info |  |
| `add_post_services` | Y | `AsyncSession query_db, PostModel page_object` | `CrudResponseModel` | 新增岗位信息service | PostDao.add_post_dao | f'新增岗位{page_object.post_name}失败，岗位名称已存在'; f'新增岗位{page_object.post_name}失败，岗位编码已存在' |
| `edit_post_services` | Y | `AsyncSession query_db, PostModel page_object` | `CrudResponseModel` | 编辑岗位信息service | PostDao.edit_post_dao | f'修改岗位{page_object.post_name}失败，岗位名称已存在'; f'修改岗位{page_object.post_name}失败，岗位编码已存在'; '岗位不存在' |
| `delete_post_services` | Y | `AsyncSession query_db, DeletePostModel page_object` | `CrudResponseModel` | 删除岗位信息service | PostDao.count_user_post_dao, PostDao.delete_post_dao | f'{post.post_name}已分配，不能删除'; '传入岗位id为空' |
| `post_detail_services` | Y | `AsyncSession query_db, int post_id` | `PostModel` | 获取岗位详细信息service | PostDao.get_post_detail_by_id |  |
| `export_post_list_services` | Y | `list post_list` | `bytes` | 导出岗位信息service |  |  |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
