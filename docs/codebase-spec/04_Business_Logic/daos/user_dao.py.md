# user_dao.py（DAO）

## Source
- Source: `ruoyi-fastapi-backend/module_admin/dao/user_dao.py`

## Imports（依赖概览）

```python
from collections.abc import Sequence
from datetime import datetime, time
from typing import Any
from sqlalchemy import ColumnElement, and_, delete, desc, func, or_, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from common.vo import PageModel
from module_admin.entity.do.dept_do import SysDept
from module_admin.entity.do.menu_do import SysMenu
from module_admin.entity.do.post_do import SysPost
from module_admin.entity.do.role_do import SysRole, SysRoleMenu
from module_admin.entity.do.user_do import SysUser, SysUserPost, SysUserRole
from module_admin.entity.vo.user_vo import (
from utils.page_util import PageUtil
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `get_user_by_name` | Y | `AsyncSession db, str user_name` | `SysUser \| None` | 根据用户名获取用户信息 |  |  |
| `get_user_by_info` | Y | `AsyncSession db, UserModel user` | `SysUser \| None` | 根据用户参数获取用户信息 |  |  |
| `get_user_by_id` | Y | `AsyncSession db, int user_id` | `dict[str, Any]` | 根据user_id获取用户信息 |  |  |
| `get_user_detail_by_id` | Y | `AsyncSession db, int user_id` | `dict[str, Any]` | 根据user_id获取用户详细信息 |  |  |
| `get_user_list` | Y | `AsyncSession db, UserPageQueryModel query_object, ColumnElement data_scope_sql, bool is_page` | `PageModel \| list[list[dict[str, Any]]]` | 根据查询参数获取用户列表信息 |  |  |
| `add_user_dao` | Y | `AsyncSession db, UserModel user` | `SysUser` | 新增用户数据库操作 |  |  |
| `edit_user_dao` | Y | `AsyncSession db, dict user` | `None` | 编辑用户数据库操作 |  |  |
| `delete_user_dao` | Y | `AsyncSession db, UserModel user` | `None` | 删除用户数据库操作 |  |  |
| `get_user_role_allocated_list_by_user_id` | Y | `AsyncSession db, UserRoleQueryModel query_object` | `Sequence[SysRole]` | 根据用户id获取用户已分配的角色列表信息数据库操作 |  |  |
| `get_user_role_allocated_list_by_role_id` | Y | `AsyncSession db, UserRolePageQueryModel query_object, ColumnElement data_scope_sql, bool is_page` | `PageModel \| list[dict[str, Any]]` | 根据角色id获取已分配的用户列表信息 |  |  |
| `get_user_role_unallocated_list_by_role_id` | Y | `AsyncSession db, UserRolePageQueryModel query_object, ColumnElement data_scope_sql, bool is_page` | `PageModel \| list[dict[str, Any]]` | 根据角色id获取未分配的用户列表信息 |  |  |
| `add_user_role_dao` | Y | `AsyncSession db, UserRoleModel user_role` | `None` | 新增用户角色关联信息数据库操作 |  |  |
| `delete_user_role_dao` | Y | `AsyncSession db, UserRoleModel user_role` | `None` | 删除用户角色关联信息数据库操作 |  |  |
| `delete_user_role_by_user_and_role_dao` | Y | `AsyncSession db, UserRoleModel user_role` | `None` | 根据用户id及角色id删除用户角色关联信息数据库操作 |  |  |
| `get_user_role_detail` | Y | `AsyncSession db, UserRoleModel user_role` | `SysUserRole \| None` | 根据用户角色关联获取用户角色关联详细信息 |  |  |
| `add_user_post_dao` | Y | `AsyncSession db, UserPostModel user_post` | `None` | 新增用户岗位关联信息数据库操作 |  |  |
| `delete_user_post_dao` | Y | `AsyncSession db, UserPostModel user_post` | `None` | 删除用户岗位关联信息数据库操作 |  |  |
| `get_user_dept_info` | Y | `AsyncSession db, int dept_id` | `SysDept \| None` |  |  |  |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
