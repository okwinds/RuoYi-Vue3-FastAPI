# Authentication（认证与鉴权）

本仓库使用 **OAuth2 Password Flow + JWT** 作为认证机制，并在 Redis 中维护 token 的“在线态”（支持同账号多端/单端策略）。

关键实现：
- 配置：`ruoyi-fastapi-backend/config/env.py`（`JwtSettings`、`AppSettings`）
- 登录接口：`ruoyi-fastapi-backend/module_admin/controller/login_controller.py`
- 核心服务：`ruoyi-fastapi-backend/module_admin/service/login_service.py`

---

## 1) 支持的认证方式

- OAuth2 Password Flow（用户名/密码表单）：
  - 使用 FastAPI 的 `OAuth2PasswordRequestForm` 并扩展验证码与会话参数（`CustomOAuth2PasswordRequestForm`）
- JWT（Bearer Token）：
  - `Authorization: Bearer <token>`（服务端会兼容已带 `Bearer` 的 token 字符串）

---

## 2) 登录流程（Login Flow）

入口：`POST /login`

高层步骤（对应 `LoginService.authenticate_user` + controller）：
1) 读取“是否启用验证码”配置：
   - 从 Redis 读取 `sys.account.captchaEnabled`（配置预热见 `config/get_redis.py`）
2) 校验登录 IP 黑名单（Redis 配置 `sys.login.blackIPList`）
3) 若启用验证码：
   - 校验 `CAPTCHA_CODES:{uuid}` 中的验证码值
4) 校验账号/密码：
   - 用户不存在/密码错误/用户停用会抛出 `LoginException`
   - 密码错误次数会记录到 Redis（超过阈值会锁定账号 10 分钟）
5) 生成 JWT：
   - `create_access_token(data, expires_delta)` 会在 payload 写入 `exp`
6) 写入 Redis 作为“在线 token”：
   - `APP_SAME_TIME_LOGIN=true`：key 采用 `session_id`
   - `APP_SAME_TIME_LOGIN=false`：key 采用 `user_id`（实现同账号同一时间只能登录一次）
7) 返回响应：
   - 普通请求：统一响应结构（`ResponseUtil.success(..., dict_content={'token': access_token})`）
   - 从 Swagger/ReDoc 发起：返回 OAuth2 兼容结构 `{'access_token': ..., 'token_type': 'Bearer'}`（修复文档页面 token 显示问题）

---

## 3) 获取当前用户（Token → User）

入口：
- `GET /getInfo`：controller 层读取 `CurrentUserDependency()`（依赖注入）

核心逻辑：`LoginService.get_current_user()`：
1) JWT decode 并读取 payload（至少包含 `user_id`，并读取 `session_id` 用于多端策略）
2) DB 查询用户基本信息、角色信息、岗位信息、菜单权限信息
3) Redis 在线 token 校验：
   - 同账号多端：用 `session_id` 查 token
   - 单端：用 `user_id` 查 token
4) 校验通过后，会刷新 Redis 中 token 的过期时间（滑动过期）
5) 组装 `CurrentUserModel`（包含 roles/permissions 等），返回给 controller

---

## 4) 权限模型（RBAC + Permissions）

数据源：
- 用户/角色/菜单相关表：`sys_user`、`sys_role`、`sys_menu` 及关联表（见 `02_Data/RELATIONSHIPS.md`）

权限计算（简化）：
- 如果用户角色包含 `role_id == 1`：权限集合直接为 `['*:*:*']`
- 否则：权限集合来自菜单权限集合（`perms` 字段）

前端使用方式（高层）：
- 登录后调用 `GET /getRouters` 获取路由树
- 并基于权限动态生成可访问路由（见 `ruoyi-fastapi-frontend/src/store/modules/permission.js` 与 `src/permission.js`）

---

## 5) 退出（Logout）

入口：`POST /logout`

- 后端会 decode token，按多端/单端策略确定 token_id（`session_id` 或 `user_id`）
- 调用 `LoginService.logout_services()` 清理 Redis 在线 token

---

## 6) Token Payload（复刻约束）

本项目的 JWT payload 至少包含：
- `user_id`（字符串化的数字）
- `user_name`
- `dept_name`（可空）
- `session_id`（UUID 字符串，多端策略使用）
- `login_info`（客户端上报的登录信息，类型为 dict）
- `exp`（过期时间，UTC）

> 复刻时需要保持 payload 字段语义一致，否则会影响 Redis 在线态校验与权限计算。
