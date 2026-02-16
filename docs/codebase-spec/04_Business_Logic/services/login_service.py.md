# login_service.py（Service）

## Source
- Source: `ruoyi-fastapi-backend/module_admin/service/login_service.py`

## Imports（依赖概览）

```python
import random
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any
import jwt
from fastapi import Depends, Form, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from sqlalchemy import Row
from sqlalchemy.ext.asyncio import AsyncSession
from common.constant import CommonConstant, MenuConstant
from common.context import RequestContext
from common.enums import RedisInitKeyConfig
from common.vo import CrudResponseModel
from config.env import AppConfig, JwtConfig
from config.get_db import get_db
from exceptions.exception import AuthException, LoginException, ServiceException
from module_admin.dao.login_dao import login_by_account
from module_admin.dao.user_dao import UserDao
from module_admin.entity.do.dept_do import SysDept
from module_admin.entity.do.menu_do import SysMenu
from module_admin.entity.do.user_do import SysUser
from module_admin.entity.vo.login_vo import MenuTreeModel, MetaModel, RouterModel, SmsCode, UserLogin, UserRegister
from module_admin.entity.vo.user_vo import AddUserModel, CurrentUserModel, ResetUserModel, TokenData, UserInfoModel
from module_admin.service.user_service import UserService
from utils.common_util import CamelCaseUtil
from utils.log_util import logger
from utils.message_util import message_service
from utils.pwd_util import PwdUtil
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `authenticate_user` | Y | `Request request, AsyncSession query_db, UserLogin login_user` | `Row[tuple[SysUser, SysDept]]` | 根据用户名密码校验用户登录 |  |  |
| `create_access_token` | Y | `dict data, timedelta \| None expires_delta` | `str` | 根据登录信息创建当前用户token |  |  |
| `get_current_user` | Y | `Request request, str token, AsyncSession query_db` | `CurrentUserModel` | 根据token获取当前用户信息 | UserDao.get_user_by_id |  |
| `get_current_user_routers` | Y | `int user_id, AsyncSession query_db` | `list[dict[str, Any]]` | 根据用户id获取当前用户路由信息 | UserDao.get_user_by_id |  |
| `register_user_services` | Y | `Request request, AsyncSession query_db, UserRegister user_register` | `CrudResponseModel` | 用户注册services |  | '验证码已失效'; '验证码错误'; '注册程序已关闭，禁止注册'; '两次输入的密码不一致' |
| `get_sms_code_services` | Y | `Request request, AsyncSession query_db, ResetUserModel user` | `SmsCode` | 获取短信验证码service | UserDao.get_user_by_name |  |
| `forget_user_services` | Y | `Request request, AsyncSession query_db, ResetUserModel forget_user` | `CrudResponseModel` | 用户忘记密码services | UserDao.get_user_by_name |  |
| `logout_services` | Y | `Request request, str token_id` | `bool` | 退出登录services |  |  |
| `get_router_name` | N | `MenuTreeModel menu` | `str` | 获取路由名称 |  |  |
| `get_route_name` | N | `str name, str path` | `str` | 获取路由名称，如没有配置路由名称则取路由地址 |  |  |
| `get_router_path` | N | `MenuTreeModel menu` | `str \| None` | 获取路由地址 |  |  |
| `get_component` | N | `MenuTreeModel menu` | `str` | 获取组件信息 |  |  |
| `is_menu_frame` | N | `MenuTreeModel menu` | `bool` | 判断是否为菜单内部跳转 |  |  |
| `is_inner_link` | N | `MenuTreeModel menu` | `bool` | 判断是否为内链组件 |  |  |
| `is_parent_view` | N | `MenuTreeModel menu` | `bool` | 判断是否为parent_view组件 |  |  |
| `is_http` | N | `str link` | `bool` | 判断是否为http(s)://开头 |  |  |
| `inner_link_replace_each` | N | `str path` | `str` | 内链域名特殊字符替换 |  |  |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
