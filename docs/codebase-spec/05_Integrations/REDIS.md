# Redis 集成规格（可复刻级）

本文件描述本仓库 Redis 的**连接方式、Key 约定、生命周期与错误策略**，目标是让复刻者可以用任意 Redis SDK/中间件实现“内部等价”行为。

---

## 1) 连接与客户端约束

连接由后端在启动生命周期中初始化，并挂载到 `app.state.redis`（全局复用）。

- 连接库：`redis`（asyncio client）
- 编码：`encoding='utf-8'` 且 `decode_responses=True`
  - 约束：**get/set 的值在 Python 侧表现为字符串**；对象缓存需要手工 JSON 序列化。

配置项（环境变量语义见 `01_Configuration/ENVIRONMENT.md`）：
- `REDIS_HOST/REDIS_PORT/REDIS_USERNAME/REDIS_PASSWORD/REDIS_DATABASE`

Source（实现位置）：
- Source: `ruoyi-fastapi-backend/config/get_redis.py`
- Source: `ruoyi-fastapi-backend/config/env.py`
- Source: `ruoyi-fastapi-backend/server.py`

---

## 2) 生命周期（启动预热 / 关闭）

### 2.1 启动时做什么

后端启动（lifespan）顺序中与 Redis 相关的动作：
1) 创建连接池 `RedisUtil.create_redis_pool()` → `app.state.redis`
2) 预热字典缓存 `RedisUtil.init_sys_dict(app.state.redis)`
3) 预热参数缓存 `RedisUtil.init_sys_config(app.state.redis)`

Source：
- Source: `ruoyi-fastapi-backend/server.py`
- Source: `ruoyi-fastapi-backend/config/get_redis.py`
- Source: `ruoyi-fastapi-backend/module_admin/service/dict_service.py`
- Source: `ruoyi-fastapi-backend/module_admin/service/config_service.py`

### 2.2 关闭时做什么

- `RedisUtil.close_redis_pool(app)` 关闭 `app.state.redis`。

Source：
- Source: `ruoyi-fastapi-backend/server.py`

---

## 3) Key 命名规范（必须一致）

Key 的前缀由 `RedisInitKeyConfig` 定义，核心前缀如下：

- `access_token`：登录在线态 token
- `sys_dict`：数据字典缓存
- `sys_config`：参数配置缓存
- `captcha_codes`：图片验证码
- `account_lock`：账号锁定
- `password_error_count`：密码错误次数
- `sms_code`：短信验证码

Source：
- Source: `ruoyi-fastapi-backend/common/enums.py`

### 3.1 `sys_config`（参数配置缓存）

- Key：`sys_config:<configKey>`
- Value：`configValue`（string）
- 写入来源：
  - 启动预热：全量读取 DB，先删除 `sys_config:*` 再 set
  - 管理端增改删：同步更新/删除对应 key
- 读出来源：
  - 登录/验证码/注册等会从 Redis 读取开关（如 `sys.account.captchaEnabled`）

Source：
- Source: `ruoyi-fastapi-backend/module_admin/service/config_service.py`
- Source: `ruoyi-fastapi-backend/module_admin/service/login_service.py`
- Source: `ruoyi-fastapi-backend/module_admin/controller/login_controller.py`
- Source: `ruoyi-fastapi-backend/module_admin/controller/captcha_controller.py`

### 3.2 `sys_dict`（字典缓存）

- Key：`sys_dict:<dictType>`
- Value：JSON 字符串（`ensure_ascii=False`），内容为字典数据行列表
- 写入来源：
  - 启动预热：全量字典类型（仅 `status=='0'`）逐个写入；先删除 `sys_dict:*`
  - 字典数据增改删：重新查询该 dictType 的列表并覆盖写回
- 读出来源：
  - 提供“从缓存查询字典数据”能力（业务与接口见 OpenAPI）

Source：
- Source: `ruoyi-fastapi-backend/module_admin/service/dict_service.py`

### 3.3 `access_token`（在线态 Token）

该仓库的鉴权不仅依赖 JWT 本身，还依赖 Redis 的“在线态”校验与滑动过期刷新。

Key 选择由 `APP_SAME_TIME_LOGIN` 决定：
- `APP_SAME_TIME_LOGIN=true`（默认）：同账号可多端同时在线
  - Key：`access_token:<session_id>`
- `APP_SAME_TIME_LOGIN=false`：同账号同一时间只能登录一次
  - Key：`access_token:<user_id>`

Value：`<jwt_token_string>`

TTL：`JWT_REDIS_EXPIRE_MINUTES`（分钟），并在每次 `get_current_user` 通过后刷新 TTL（滑动过期）。

Source：
- Source: `ruoyi-fastapi-backend/module_admin/controller/login_controller.py`
- Source: `ruoyi-fastapi-backend/module_admin/service/login_service.py`

### 3.4 `captcha_codes`（验证码）

- Key：`captcha_codes:<uuid>`
- Value：验证码计算结果（string）
- TTL：2 分钟（由 controller set）

Source：
- Source: `ruoyi-fastapi-backend/module_admin/controller/captcha_controller.py`

### 3.5 `account_lock` / `password_error_count`（登录风控）

用于“密码错误次数累计 + 10 分钟锁定”：

- `password_error_count:<username>`：密码错误次数（int 字符串），TTL 10 分钟
- `account_lock:<username>`：锁定标记（存 username），TTL 10 分钟

阈值：`CommonConstant.PASSWORD_ERROR_COUNT`（超过后触发锁定）

Source：
- Source: `ruoyi-fastapi-backend/module_admin/service/login_service.py`
- Source: `ruoyi-fastapi-backend/common/constant.py`

### 3.6 `sms_code`（短信验证码）

- Key：`sms_code:<session_id>`
- Value：6 位验证码（string）
- TTL：2 分钟

Source：
- Source: `ruoyi-fastapi-backend/module_admin/service/login_service.py`

---

## 4) 错误与恢复策略（复刻必须项）

### 4.1 Redis 不可用时的策略

`RedisUtil.create_redis_pool()` 会对 ping 的异常做日志记录，但**仍返回 redis client**：
- 用户名/密码错误、连接超时、连接错误 → logger.error
- 复刻约束：启动时 Redis 不可用会导致：
  - 无法预热 `sys_dict/sys_config`
  - 登录/鉴权、验证码、在线用户等功能失效或抛错

Source：
- Source: `ruoyi-fastapi-backend/config/get_redis.py`

### 4.2 缓存一致性策略

本仓库的策略是“写 DB 成功后再写 Redis”，并在异常时回滚 DB：
- add/edit/delete config/dict_data：`commit` 成功后 set/delete 对应 key
- refresh：全量覆盖（先清再写）

复刻建议：
- 采用同样的顺序（DB commit → Redis set/delete），保持业务读一致性。

Source：
- Source: `ruoyi-fastapi-backend/module_admin/service/config_service.py`
- Source: `ruoyi-fastapi-backend/module_admin/service/dict_service.py`

---

## 5) 验收与测试计划（离线/集成）

### 5.1 最小集成验证（推荐）

在 Docker 测试环境启动后（见 `ruoyi-fastapi-test/docker-compose.test.*.yml`）：
- 登录成功后，Redis 中存在 `access_token:*` key
- 调用 `/getInfo` 能刷新 token TTL（滑动过期）
- 调用验证码接口能在 Redis 写入 `captcha_codes:*` 并在过期后失效

### 5.2 复刻者自测清单

- [ ] `sys_config:*` 与 DB 中配置键值一致（抽样 20 个 key）
- [ ] `sys_dict:*` 的 value 是 JSON 字符串，且字段命名与 API 返回一致
- [ ] `APP_SAME_TIME_LOGIN` 两种策略都可正确工作（session_id vs user_id）

