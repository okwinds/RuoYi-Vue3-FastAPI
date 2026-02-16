# menu_service.py（Service）

## Source
- Source: `ruoyi-fastapi-backend/module_admin/service/menu_service.py`

## Imports（依赖概览）

```python
from collections.abc import Sequence
from typing import Any
from sqlalchemy.ext.asyncio import AsyncSession
from common.constant import CommonConstant, MenuConstant
from common.vo import CrudResponseModel
from exceptions.exception import ServiceException, ServiceWarning
from module_admin.dao.menu_dao import MenuDao
from module_admin.dao.role_dao import RoleDao
from module_admin.entity.do.menu_do import SysMenu
from module_admin.entity.vo.menu_vo import DeleteMenuModel, MenuModel, MenuQueryModel, MenuTreeModel
from module_admin.entity.vo.role_vo import RoleMenuQueryModel
from module_admin.entity.vo.user_vo import CurrentUserModel
from utils.common_util import CamelCaseUtil
from utils.string_util import StringUtil
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `get_menu_tree_services` | Y | `AsyncSession query_db, CurrentUserModel \| None current_user` | `list[dict[str, Any]]` | 获取菜单树信息service | MenuDao.get_menu_list_for_tree |  |
| `get_role_menu_tree_services` | Y | `AsyncSession query_db, int role_id, CurrentUserModel \| None current_user` | `RoleMenuQueryModel` | 根据角色id获取菜单树信息service | MenuDao.get_menu_list_for_tree, RoleDao.get_role_detail_by_id, RoleDao.get_role_menu_dao |  |
| `get_menu_list_services` | Y | `AsyncSession query_db, MenuQueryModel page_object, CurrentUserModel \| None current_user` | `list[dict[str, Any]]` | 获取菜单列表信息service | MenuDao.get_menu_list |  |
| `check_menu_name_unique_services` | Y | `AsyncSession query_db, MenuModel page_object` | `bool` | 校验菜单名称是否唯一service | MenuDao.get_menu_detail_by_info |  |
| `add_menu_services` | Y | `AsyncSession query_db, MenuModel page_object` | `CrudResponseModel` | 新增菜单信息service | MenuDao.add_menu_dao | f'新增菜单{page_object.menu_name}失败，菜单名称已存在'; f'新增菜单{page_object.menu_name}失败，地址必须以http(s |
| `edit_menu_services` | Y | `AsyncSession query_db, MenuModel page_object` | `CrudResponseModel` | 编辑菜单信息service | MenuDao.edit_menu_dao | f'修改菜单{page_object.menu_name}失败，菜单名称已存在'; f'修改菜单{page_object.menu_name}失败，地址必须以http(s; f'修改菜单{page_object.menu_name}失败，上级菜单不能选择自己'; '菜单不存在' |
| `delete_menu_services` | Y | `AsyncSession query_db, DeleteMenuModel page_object` | `CrudResponseModel` | 删除菜单信息service | MenuDao.check_menu_exist_role_dao, MenuDao.delete_menu_dao, MenuDao.has_child_by_menu_id_dao | '传入菜单id为空' |
| `menu_detail_services` | Y | `AsyncSession query_db, int menu_id` | `MenuModel` | 获取菜单详细信息service | MenuDao.get_menu_detail_by_id |  |
| `list_to_tree` | N | `Sequence[SysMenu] permission_list` | `list[MenuTreeModel]` | 工具方法：根据菜单列表信息生成树形嵌套数据 |  |  |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
