# Method Spec：LoginService.authenticate_user（可复刻级）

目标：仅凭本文档即可实现“登录校验”内部等价逻辑（包含风控缓存、验证码、禁用用户等分支）。

Source：
- Source: `ruoyi-fastapi-backend/module_admin/service/login_service.py`
- Source: `ruoyi-fastapi-backend/module_admin/controller/login_controller.py`
- Source: `ruoyi-fastapi-backend/module_admin/controller/captcha_controller.py`

---

## 1) 签名与输入输出

签名：
- `authenticate_user(request, query_db, login_user) -> Row[(SysUser, SysDept)]`

输入（关键字段）：
- `request.headers['X-Forwarded-For']`：用于 IP 黑名单校验（如果存在）
- `login_user.user_name/password`：用户名/密码
- `login_user.captcha_enabled`：是否启用验证码（由 controller 读取 `sys.account.captchaEnabled` 注入）
- `login_user.code/login_user.uuid`：验证码值与 uuid（当启用验证码时使用）

输出：
- 成功：返回 DB 查询到的 user + dept（Row tuple）
- 失败：抛 `LoginException`（业务错误）或 `AuthException/ServiceException`（少数分支）

---

## 2) 依赖与数据源

Redis key（见 `05_Integrations/REDIS.md`）：
- `sys_config:sys.login.blackIPList`：IP 黑名单（逗号分隔字符串）
- `account_lock:<username>`：账号锁定标记（10 分钟）
- `captcha_codes:<uuid>`：验证码（2 分钟）
- `password_error_count:<username>`：密码错误次数（10 分钟）

DB：
- `login_by_account(query_db, username)`：获取用户与部门信息

密码哈希：
- `PwdUtil.verify_password(plain, hashed)`（bcrypt）

阈值：
- `CommonConstant.PASSWORD_ERROR_COUNT`（超过后锁定 10 分钟）

---

## 3) 决策树（可直接写伪代码）

按严格顺序执行（复刻必须一致）：

1) `__check_login_ip(request)`
   - 从 Redis 读 `sys_config:sys.login.blackIPList`
   - 若 `X-Forwarded-For` 在黑名单内 → 抛 `LoginException("当前IP禁止登录")`

2) 账号锁定检查
   - 从 Redis 读 `account_lock:<username>`
   - 若命中且值等于 username → 抛 `LoginException("账号已锁定，请稍后再试")`

3) 判断“来自 API 文档的登录请求”
   - `referer.endswith('docs')` → swagger
   - `referer.endswith('redoc')` → redoc

4) 验证码检查（有条件）
   - 若 `login_user.captcha_enabled == False` → 跳过
   - 若（来自 swagger/redoc 且 `APP_ENV == 'dev'`）→ 跳过
   - 否则执行 `__check_login_captcha(request, login_user)`：
     - 从 Redis 读 `captcha_codes:<uuid>`
     - 缺失 → `LoginException("验证码已失效")`
     - 不等于 `login_user.code` → `LoginException("验证码错误")`

5) 查用户
   - `user = login_by_account(...)`
   - 不存在 → `LoginException("用户不存在")`

6) 校验密码（失败要累计次数并可能锁定）
   - 若密码不匹配：
     - 从 Redis 读 `password_error_count:<username>`（缺省视为 0）
     - `password_error_count = int(value)+1`
     - 写回该 key，TTL=10 分钟
     - 若 `password_error_count > PASSWORD_ERROR_COUNT`：
       - 删除 `password_error_count:<username>`
       - 写入 `account_lock:<username>` = username，TTL=10 分钟
       - 抛 `LoginException("10分钟内密码已输错超过5次，账号已锁定，请10分钟后再试")`
     - 否则抛 `LoginException("密码错误")`

7) 校验用户状态
   - 若 `user.status == '1'` → `LoginException("用户已停用")`

8) 登录成功后清理错误次数
   - 删除 `password_error_count:<username>`
   - 返回 `user`

---

## 4) 边界条件与错误策略

- Redis 不可用时：
  - 这些分支将抛异常（或返回 None），会导致登录失败或行为不确定；复刻时建议把 Redis 作为强依赖。
- referer 缺失时：
  - 视为非 swagger/redoc 请求，不走“dev 环境跳过验证码”特例。

---

## 5) 验收与测试计划（建议最小集）

- [ ] 黑名单 IP：设置 `sys.login.blackIPList` 后，携带对应 `X-Forwarded-For` 的请求必定失败
- [ ] 密码错误累计：连续输错 6 次触发锁定（锁定 10 分钟）
- [ ] 验证码：开启验证码后，uuid 不存在/错误都会失败

> 测试环境可通过 `ruoyi-fastapi-test/disable_captcha.sql` 关闭验证码开关（见 compose）。

