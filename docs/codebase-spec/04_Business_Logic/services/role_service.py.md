# role_service.py（Service）

## Source
- Source: `ruoyi-fastapi-backend/module_admin/service/role_service.py`

## Imports（依赖概览）

```python
from typing import Any
from sqlalchemy import ColumnElement
from sqlalchemy.ext.asyncio import AsyncSession
from common.constant import CommonConstant
from common.vo import CrudResponseModel, PageModel
from exceptions.exception import ServiceException
from module_admin.dao.role_dao import RoleDao
from module_admin.dao.user_dao import UserDao
from module_admin.entity.vo.role_vo import (
from module_admin.entity.vo.user_vo import UserInfoModel, UserRolePageQueryModel
from utils.common_util import CamelCaseUtil
from utils.excel_util import ExcelUtil
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `get_role_select_option_services` | Y | `AsyncSession query_db` | `list[dict[str, Any]]` | 获取角色列表不分页信息service | RoleDao.get_role_select_option_dao |  |
| `get_role_dept_tree_services` | Y | `AsyncSession query_db, int role_id` | `RoleDeptQueryModel` | 根据角色id获取部门树信息service | RoleDao.get_role_dept_dao |  |
| `get_role_list_services` | Y | `AsyncSession query_db, RolePageQueryModel query_object, ColumnElement data_scope_sql, bool is_page` | `PageModel \| list[dict[str, Any]]` | 获取角色列表信息service | RoleDao.get_role_list |  |
| `check_role_allowed_services` | Y | `RoleModel check_role` | `CrudResponseModel` | 校验角色是否允许操作service |  | '不允许操作超级管理员角色' |
| `check_role_data_scope_services` | Y | `AsyncSession query_db, str role_ids, ColumnElement data_scope_sql` | `None` | 校验角色是否有数据权限service | RoleDao.get_role_list | '没有权限访问角色数据' |
| `check_role_name_unique_services` | Y | `AsyncSession query_db, RoleModel page_object` | `bool` | 校验角色名称是否唯一service | RoleDao.get_role_by_info |  |
| `check_role_key_unique_services` | Y | `AsyncSession query_db, RoleModel page_object` | `bool` | 校验角色权限字符是否唯一service | RoleDao.get_role_by_info |  |
| `add_role_services` | Y | `AsyncSession query_db, AddRoleModel page_object` | `CrudResponseModel` | 新增角色信息service | RoleDao.add_role_dao, RoleDao.add_role_menu_dao | f'新增角色{page_object.role_name}失败，角色名称已存在'; f'新增角色{page_object.role_name}失败，角色权限已存在' |
| `edit_role_services` | Y | `AsyncSession query_db, AddRoleModel page_object` | `CrudResponseModel` | 编辑角色信息service | RoleDao.add_role_menu_dao, RoleDao.delete_role_menu_dao, RoleDao.edit_role_dao | f'修改角色{page_object.role_name}失败，角色名称已存在'; f'修改角色{page_object.role_name}失败，角色权限已存在'; '角色不存在' |
| `role_datascope_services` | Y | `AsyncSession query_db, AddRoleModel page_object` | `CrudResponseModel` | 分配角色数据权限service | RoleDao.add_role_dept_dao, RoleDao.delete_role_dept_dao, RoleDao.edit_role_dao | '角色不存在' |
| `delete_role_services` | Y | `AsyncSession query_db, DeleteRoleModel page_object` | `CrudResponseModel` | 删除角色信息service | RoleDao.count_user_role_dao, RoleDao.delete_role_dao, RoleDao.delete_role_dept_dao, RoleDao.delete_role_menu_dao | f'角色{role.role_name}已分配; '传入角色id为空' |
| `role_detail_services` | Y | `AsyncSession query_db, int role_id` | `RoleModel` | 获取角色详细信息service | RoleDao.get_role_detail_by_id |  |
| `export_role_list_services` | Y | `list role_list` | `bytes` | 导出角色列表信息service |  |  |
| `get_role_user_allocated_list_services` | Y | `AsyncSession query_db, UserRolePageQueryModel page_object, ColumnElement data_scope_sql, bool is_page` | `PageModel` | 根据角色id获取已分配用户列表 | UserDao.get_user_role_allocated_list_by_role_id |  |
| `get_role_user_unallocated_list_services` | Y | `AsyncSession query_db, UserRolePageQueryModel page_object, ColumnElement data_scope_sql, bool is_page` | `PageModel` | 根据角色id获取未分配用户列表 | UserDao.get_user_role_unallocated_list_by_role_id |  |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
