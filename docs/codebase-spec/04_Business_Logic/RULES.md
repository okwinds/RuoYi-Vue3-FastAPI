# Business Rules（系统级规则骨架）

> 本文件抽取“系统级”的稳定规则（权限、登录态、缓存预热、定时任务、代码生成等）。  
> 二次开发的业务规则请在 `docs/specs/` 下按功能单独建 spec。

---

## 1) 认证与登录态规则

### 规则：同账号多端/单端登录策略

- Source：
  - `ruoyi-fastapi-backend/config/env.py`（`APP_SAME_TIME_LOGIN`）
  - `ruoyi-fastapi-backend/module_admin/controller/login_controller.py`
  - `ruoyi-fastapi-backend/module_admin/service/login_service.py`
- 描述：
  - 当 `APP_SAME_TIME_LOGIN=true`：同账号可同时登录；token 以 `session_id` 作为 Redis key。
  - 当 `APP_SAME_TIME_LOGIN=false`：同账号同一时间只允许一个在线；token 以 `user_id` 作为 Redis key。
- 触发：
  - 登录成功写 token
  - 每次请求校验 token 并滑动刷新过期

### 规则：验证码校验开关

- 描述：
  - 验证码是否开启来自 Redis 配置项 `sys.account.captchaEnabled`
  - 启用时：登录必须校验 `CAPTCHA_CODES:{uuid}` 对应验证码值
- 例外：
  - 在 dev 环境且请求来自 Swagger/ReDoc 时，可跳过验证码校验（便于调试）

### 规则：账号锁定（防爆破）

- 描述：
  - 密码连续输错会递增计数（Redis），超过阈值（默认 5）锁定账号 10 分钟
- Source：
  - `ruoyi-fastapi-backend/common/constant.py:CommonConstant.PASSWORD_ERROR_COUNT`
  - `ruoyi-fastapi-backend/module_admin/service/login_service.py`

---

## 2) 权限与数据范围规则（RBAC + Data Scope）

### 规则：权限集合的来源

- 描述：
  - 角色 `role_id == 1` 视为超级管理员：权限集合为 `['*:*:*']`
  - 其他用户权限集合来源于菜单 `perms` 字段聚合
- 影响：
  - 前端动态路由生成与按钮级权限显示

### 规则：数据范围（Data Scope）

- 描述：
  - 角色字段 `sys_role.data_scope` 控制数据可见范围（全量/自定/本部门/本部门及以下）
  - 自定范围依赖 `sys_role_dept`
- 影响：
  - 列表查询接口的数据过滤（实现点通常位于依赖项/dao 层）

---

## 3) 缓存预热规则（Redis）

- 描述：
  - 服务启动后会预热：
    - 字典数据（`sys_dict_*`）
    - 参数配置（`sys_config`）
- Source：
  - `ruoyi-fastapi-backend/config/get_redis.py`
  - `ruoyi-fastapi-backend/server.py:lifespan`

---

## 4) 定时任务规则（Scheduler）

### 规则：任务定义与加载

- 描述：
  - `sys_job` 定义 cron、执行器、调用目标函数、参数等
  - 启动时从 DB 加载所有任务，并注册到 APScheduler
- 调用目标函数约束：
  - `invoke_target` 为字符串路径，如 `module_task.scheduler_test.job`
  - scheduler 会动态 import 并执行；必须在白名单规则内（禁止危险模块/语句，见 `JobConstant.JOB_ERROR_LIST`）
- Source：
  - `ruoyi-fastapi-backend/config/get_scheduler.py`
  - `ruoyi-fastapi-backend/common/constant.py:JobConstant`

---

## 5) 代码生成规则（Generator）

- 描述：
  - 生成器元数据保存在 `gen_table` 与 `gen_table_column`
  - 前端提供导入/编辑/预览/生成等 UI（E2E 覆盖了全流程）
- Source：
  - 后端：`ruoyi-fastapi-backend/module_generator/*`
  - 前端：`ruoyi-fastapi-frontend/src/views/tool/gen/*`
  - E2E：`ruoyi-fastapi-test/tool/test_code_gen.py`

---

## 6) UI/UX 规则（前端，UI-only）

UI/UX 可复刻规格请见：`docs/ui-ux-spec/`（本文件不重复描述）。
