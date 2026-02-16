# menu_dao.py（DAO）

## Source
- Source: `ruoyi-fastapi-backend/module_admin/dao/menu_dao.py`

## Imports（依赖概览）

```python
from collections.abc import Sequence
from sqlalchemy import and_, delete, func, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from module_admin.entity.do.menu_do import SysMenu
from module_admin.entity.do.role_do import SysRole, SysRoleMenu
from module_admin.entity.do.user_do import SysUser, SysUserRole
from module_admin.entity.vo.menu_vo import MenuModel, MenuQueryModel
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `get_menu_detail_by_id` | Y | `AsyncSession db, int menu_id` | `SysMenu \| None` | 根据菜单id获取菜单详细信息 |  |  |
| `get_menu_detail_by_info` | Y | `AsyncSession db, MenuModel menu` | `SysMenu \| None` | 根据菜单参数获取菜单信息 |  |  |
| `get_menu_list_for_tree` | Y | `AsyncSession db, int user_id, list role` | `Sequence[SysMenu]` | 根据角色信息获取所有在用菜单列表信息 |  |  |
| `get_menu_list` | Y | `AsyncSession db, MenuQueryModel page_object, int user_id, list role` | `Sequence[SysMenu]` | 根据查询参数获取菜单列表信息 |  |  |
| `add_menu_dao` | Y | `AsyncSession db, MenuModel menu` | `SysMenu` | 新增菜单数据库操作 |  |  |
| `edit_menu_dao` | Y | `AsyncSession db, dict menu` | `None` | 编辑菜单数据库操作 |  |  |
| `delete_menu_dao` | Y | `AsyncSession db, MenuModel menu` | `None` | 删除菜单数据库操作 |  |  |
| `has_child_by_menu_id_dao` | Y | `AsyncSession db, int menu_id` | `int \| None` | 根据菜单id查询菜单关联子菜单的数量 |  |  |
| `check_menu_exist_role_dao` | Y | `AsyncSession db, int menu_id` | `int \| None` | 根据菜单id查询菜单关联角色数量 |  |  |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
