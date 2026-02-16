# user_service.py（Service）

## Source
- Source: `ruoyi-fastapi-backend/module_admin/service/user_service.py`

## Imports（依赖概览）

```python
import io
from datetime import datetime
from typing import Any
import pandas as pd
from fastapi import Request, UploadFile
from sqlalchemy import ColumnElement
from sqlalchemy.ext.asyncio import AsyncSession
from common.constant import CommonConstant
from common.vo import CrudResponseModel, PageModel
from exceptions.exception import ServiceException
from module_admin.dao.user_dao import UserDao
from module_admin.entity.do.user_do import SysUserRole
from module_admin.entity.vo.post_vo import PostPageQueryModel
from module_admin.entity.vo.user_vo import (
from module_admin.service.config_service import ConfigService
from module_admin.service.dept_service import DeptService
from module_admin.service.post_service import PostService
from module_admin.service.role_service import RoleService
from utils.common_util import CamelCaseUtil
from utils.excel_util import ExcelUtil
from utils.pwd_util import PwdUtil
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `get_user_list_services` | Y | `AsyncSession query_db, UserPageQueryModel query_object, ColumnElement data_scope_sql, bool is_page` | `PageModel[UserRowModel] \| list[dict[str, Any]]` | 获取用户列表信息service | UserDao.get_user_list |  |
| `check_user_allowed_services` | Y | `UserModel check_user` | `CrudResponseModel` | 校验用户是否允许操作service |  | '不允许操作超级管理员用户' |
| `check_user_data_scope_services` | Y | `AsyncSession query_db, int user_id, ColumnElement data_scope_sql` | `CrudResponseModel` | 校验用户数据权限service | UserDao.get_user_list | '没有权限访问用户数据' |
| `check_user_name_unique_services` | Y | `AsyncSession query_db, UserModel page_object` | `bool` | 校验用户名是否唯一service | UserDao.get_user_by_info |  |
| `check_phonenumber_unique_services` | Y | `AsyncSession query_db, UserModel page_object` | `bool` | 校验用户手机号是否唯一service | UserDao.get_user_by_info |  |
| `check_email_unique_services` | Y | `AsyncSession query_db, UserModel page_object` | `bool` | 校验用户邮箱是否唯一service | UserDao.get_user_by_info |  |
| `add_user_services` | Y | `AsyncSession query_db, AddUserModel page_object` | `CrudResponseModel` | 新增用户信息service | UserDao.add_user_dao, UserDao.add_user_post_dao, UserDao.add_user_role_dao | f'新增用户{page_object.user_name}失败，登录账号已存在'; f'新增用户{page_object.user_name}失败，手机号码已存在'; f'新增用户{page_object.user_name}失败，邮箱账号已存在' |
| `edit_user_services` | Y | `AsyncSession query_db, EditUserModel page_object` | `CrudResponseModel` | 编辑用户信息service | UserDao.add_user_post_dao, UserDao.add_user_role_dao, UserDao.delete_user_post_dao, UserDao.delete_user_role_dao, UserDao.edit_user_dao | f'修改用户{page_object.user_name}失败，登录账号已存在'; f'修改用户{page_object.user_name}失败，手机号码已存在'; f'修改用户{page_object.user_name}失败，邮箱账号已存在'; '用户不存在' |
| `delete_user_services` | Y | `AsyncSession query_db, DeleteUserModel page_object` | `CrudResponseModel` | 删除用户信息service | UserDao.delete_user_dao, UserDao.delete_user_post_dao, UserDao.delete_user_role_dao | '传入用户id为空' |
| `user_detail_services` | Y | `AsyncSession query_db, int \| str user_id` | `UserDetailModel` | 获取用户详细信息service | UserDao.get_user_detail_by_id |  |
| `user_profile_services` | Y | `AsyncSession query_db, int user_id` | `UserProfileModel` | 获取用户个人详细信息service | UserDao.get_user_detail_by_id |  |
| `reset_user_services` | Y | `AsyncSession query_db, ResetUserModel page_object` | `CrudResponseModel` | 重置用户密码service | UserDao.edit_user_dao, UserDao.get_user_detail_by_id | '修改密码失败，旧密码错误'; '新密码不能与旧密码相同' |
| `batch_import_user_services` | Y | `Request request, AsyncSession query_db, UploadFile file, bool update_support, CurrentUserModel current_user, ColumnElement user_data_scope_sql, ColumnElement dept_data_scope_sql` | `CrudResponseModel` | 批量导入用户service | UserDao.add_user_dao, UserDao.edit_user_dao, UserDao.get_user_by_info |  |
| `get_user_import_template_services` | Y | `` | `bytes` | 获取用户导入模板service |  |  |
| `export_user_list_services` | Y | `list user_list` | `bytes` | 导出用户信息service |  |  |
| `get_user_role_allocated_list_services` | Y | `AsyncSession query_db, UserRoleQueryModel page_object` | `UserRoleResponseModel` | 根据用户id获取已分配角色列表 | UserDao.get_user_detail_by_id |  |
| `add_user_role_services` | Y | `AsyncSession query_db, CrudUserRoleModel page_object` | `CrudResponseModel` | 新增用户关联角色信息service | UserDao.add_user_role_dao, UserDao.delete_user_role_by_user_and_role_dao | '不满足新增条件' |
| `delete_user_role_services` | Y | `AsyncSession query_db, CrudUserRoleModel page_object` | `CrudResponseModel` | 删除用户关联角色信息service | UserDao.delete_user_role_by_user_and_role_dao | '不满足删除条件'; '传入用户角色关联信息为空' |
| `detail_user_role_services` | Y | `AsyncSession query_db, UserRoleModel page_object` | `SysUserRole \| None` | 获取用户关联角色详细信息service | UserDao.get_user_role_detail |  |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
