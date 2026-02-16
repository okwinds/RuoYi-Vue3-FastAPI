# role_dao.py（DAO）

## Source
- Source: `ruoyi-fastapi-backend/module_admin/dao/role_dao.py`

## Imports（依赖概览）

```python
from collections.abc import Sequence
from datetime import datetime, time
from typing import Any
from sqlalchemy import ColumnElement, and_, delete, desc, func, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from common.vo import PageModel
from module_admin.entity.do.dept_do import SysDept
from module_admin.entity.do.menu_do import SysMenu
from module_admin.entity.do.role_do import SysRole, SysRoleDept, SysRoleMenu
from module_admin.entity.do.user_do import SysUser, SysUserRole
from module_admin.entity.vo.role_vo import RoleDeptModel, RoleMenuModel, RoleModel, RolePageQueryModel
from utils.page_util import PageUtil
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `get_role_by_name` | Y | `AsyncSession db, str role_name` | `SysRole \| None` | 根据角色名获取在用角色信息 |  |  |
| `get_role_by_info` | Y | `AsyncSession db, RoleModel role` | `SysRole \| None` | 根据角色参数获取角色信息 |  |  |
| `get_role_by_id` | Y | `AsyncSession db, int role_id` | `SysRole \| None` | 根据角色id获取在用角色信息 |  |  |
| `get_role_detail_by_id` | Y | `AsyncSession db, int role_id` | `SysRole \| None` | 根据role_id获取角色详细信息 |  |  |
| `get_role_select_option_dao` | Y | `AsyncSession db` | `Sequence[SysRole]` | 获取编辑页面对应的在用角色列表信息 |  |  |
| `get_role_list` | Y | `AsyncSession db, RolePageQueryModel query_object, ColumnElement data_scope_sql, bool is_page` | `PageModel \| list[dict[str, Any]]` | 根据查询参数获取角色列表信息 |  |  |
| `add_role_dao` | Y | `AsyncSession db, RoleModel role` | `SysRole` | 新增角色数据库操作 |  |  |
| `edit_role_dao` | Y | `AsyncSession db, dict role` | `None` | 编辑角色数据库操作 |  |  |
| `delete_role_dao` | Y | `AsyncSession db, RoleModel role` | `None` | 删除角色数据库操作 |  |  |
| `get_role_menu_dao` | Y | `AsyncSession db, RoleModel role` | `Sequence[SysMenu]` | 根据角色id获取角色菜单关联列表信息 |  |  |
| `add_role_menu_dao` | Y | `AsyncSession db, RoleMenuModel role_menu` | `None` | 新增角色菜单关联信息数据库操作 |  |  |
| `delete_role_menu_dao` | Y | `AsyncSession db, RoleMenuModel role_menu` | `None` | 删除角色菜单关联信息数据库操作 |  |  |
| `get_role_dept_dao` | Y | `AsyncSession db, RoleModel role` | `Sequence[SysDept]` | 根据角色id获取角色部门关联列表信息 |  |  |
| `add_role_dept_dao` | Y | `AsyncSession db, RoleDeptModel role_dept` | `None` | 新增角色部门关联信息数据库操作 |  |  |
| `delete_role_dept_dao` | Y | `AsyncSession db, RoleDeptModel role_dept` | `None` | 删除角色部门关联信息数据库操作 |  |  |
| `count_user_role_dao` | Y | `AsyncSession db, int role_id` | `int \| None` | 根据角色id查询角色关联用户数量 |  |  |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
