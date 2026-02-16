# Method Spec：LoginService.get_current_user（可复刻级）

目标：实现“JWT + Redis 在线态”的鉴权与用户态组装，保持与当前仓库内部等价（含滑动过期、权限计算）。

Source：
- Source: `ruoyi-fastapi-backend/module_admin/service/login_service.py`
- Source: `ruoyi-fastapi-backend/module_admin/dao/user_dao.py`
- Source: `ruoyi-fastapi-backend/config/env.py`

---

## 1) 签名与输入输出

签名（FastAPI dependency）：
- `get_current_user(request, token, query_db) -> CurrentUserModel`

输入：
- `token`：从 `Authorization` header 解析得到；兼容 `Bearer <token>` 或直接 token
- Redis：在线态 token、系统配置
- DB：用户基本信息/角色/岗位/菜单权限

输出：
- 成功：返回 `CurrentUserModel`（包含 roles/permissions/user 信息）
- 失败：抛 `AuthException("用户token已失效，请重新登录")` 或 `AuthException("用户token不合法")`

---

## 2) 决策树（伪代码级）

1) 规范化 token
   - 若 `token.startswith('Bearer')` → `token = token.split(' ')[1]`

2) JWT decode
   - `payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])`
   - 读取 `user_id`（必须存在）与 `session_id`（用于在线态 key）
   - 若 `user_id` 缺失 → `AuthException("用户token不合法")`
   - decode 失败（InvalidTokenError）→ `AuthException("用户token已失效，请重新登录")`

3) DB 查询用户
   - `query_user = UserDao.get_user_by_id(query_db, user_id)`
   - 若 `user_basic_info` 为空 → `AuthException("用户token不合法")`

4) Redis 在线态校验（核心）
   - 若 `APP_SAME_TIME_LOGIN == True`：
     - `redis_token = redis.get(f'access_token:{session_id}')`
   - 否则：
     - `redis_token = redis.get(f'access_token:{user_id}')`
   - 若 `token != redis_token` → `AuthException("用户token已失效，请重新登录")`

5) 刷新在线态 TTL（滑动过期）
   - 对上一步的同一个 key，再次 `set(key, redis_token, ex=JWT_REDIS_EXPIRE_MINUTES)`

6) 组装 permissions / roles
   - `role_id_list = [role.role_id ...]`
   - 若包含 `1`（管理员）→ `permissions=['*:*:*']`
   - 否则 → `permissions=[menu.perms for menu in user_menu_info]`
   - `roles=[role.role_key ...]`

7) 计算密码状态
   - `isDefaultModifyPwd = (sys.account.initPasswordModify == '1') and pwd_update_date is None`
   - `isPasswordExpired`：
     - 读取 `sys.account.passwordValidateDays`，若 >0：
       - `pwd_update_date is None` → True
       - `now > pwd_update_date + days` → True

8) 返回 `CurrentUserModel` 并写入 RequestContext

---

## 3) 复刻必须一致的字段语义

- `APP_SAME_TIME_LOGIN` 决定在线态 key 使用 `session_id` 还是 `user_id`
- 管理员识别：`role_id == 1` 特判
- `permissions` 的含义：用于接口权限校验与前端按钮权限控制

---

## 4) 验收与测试计划

- [ ] Redis 中删除对应在线态 key 后，任意受保护接口必须返回“token 已失效”
- [ ] 管理员返回 permissions 为 `*:*:*`
- [ ] 非管理员 permissions 由菜单 perms 字段集合构成
- [ ] 多端/单端策略切换后 key 选择行为一致

