# Error Handling（统一响应与异常处理）

本仓库的后端接口采用“**HTTP 状态码 + 业务 code**”的组合策略：
- 大多数业务失败会返回 **HTTP 200**，但 `code/success/msg` 表达业务状态（`ResponseUtil.failure/unauthorized/forbidden/error`）。
- 对于 `HTTPException`，会保留 HTTP status code，并返回简化结构（见异常处理器）。

关键实现：
- 统一响应：`ruoyi-fastapi-backend/utils/response_util.py`
- 响应模型：`ruoyi-fastapi-backend/common/vo.py`
- 全局异常处理：`ruoyi-fastapi-backend/exceptions/handle.py`
- 状态码常量：`ruoyi-fastapi-backend/common/constant.py:HttpStatusConstant`

---

## 1) 成功/失败响应格式（ResponseUtil）

### 1.1 成功（success）

```json
{
  "code": 200,
  "msg": "操作成功",
  "success": true,
  "time": "2026-02-07T20:00:00",
  "data": {},
  "rows": [],
  "...": "（可能包含 controller 自定义字段）"
}
```

### 1.2 失败（failure / warn）

```json
{
  "code": 601,
  "msg": "操作失败",
  "success": false,
  "time": "2026-02-07T20:00:00",
  "data": {}
}
```

### 1.3 未认证（unauthorized）

```json
{
  "code": 401,
  "msg": "登录信息已过期，访问系统资源失败",
  "success": false,
  "time": "2026-02-07T20:00:00"
}
```

### 1.4 未授权（forbidden）

```json
{
  "code": 403,
  "msg": "该用户无此接口权限",
  "success": false,
  "time": "2026-02-07T20:00:00"
}
```

### 1.5 系统错误（error）

```json
{
  "code": 500,
  "msg": "接口异常",
  "success": false,
  "time": "2026-02-07T20:00:00"
}
```

> 注意：`time` 字段是服务端生成时间戳（datetime）。

---

## 2) 业务 code（HttpStatusConstant）

| code | 含义 | 常见来源 |
| --- | --- | --- |
| 200 | SUCCESS（操作成功） | `ResponseUtil.success` |
| 601 | WARN（系统警告/业务失败） | `ResponseUtil.failure` |
| 401 | UNAUTHORIZED（未认证） | `ResponseUtil.unauthorized` / `AuthException` |
| 403 | FORBIDDEN（未授权） | `ResponseUtil.forbidden` / `PermissionException` |
| 500 | ERROR（系统内部错误） | `ResponseUtil.error` / `ServiceException` / 未捕获异常 |

---

## 3) 全局异常映射（handle_exception）

异常处理器（见 `ruoyi-fastapi-backend/exceptions/handle.py`）核心映射：
- `AuthException` → `ResponseUtil.unauthorized(...)`
- `LoginException` → `ResponseUtil.failure(...)`
- `ModelValidatorException` / `FieldValidationError` → `ResponseUtil.failure(...)`
- `PermissionException` → `ResponseUtil.forbidden(...)`
- `ServiceException` → `ResponseUtil.error(...)`
- `ServiceWarning` → `ResponseUtil.failure(...)`
- `HTTPException` → `{"code": exc.status_code, "msg": exc.detail}`（HTTP status 仍为 exc.status_code）
- `Exception` → `ResponseUtil.error(msg=str(exc))`（并 `logger.exception` 记录堆栈）

---

## 4) 复刻要点（兼容性要求）

要“完美复刻”接口行为，必须保持：
- 统一响应字段：`code/msg/success/time` 的存在与语义
- 业务失败多为 HTTP 200 的策略（前端依赖此策略进行提示与重登录逻辑）
- `HTTPException` 的特殊返回格式（与业务失败结构不同）
- 未认证/未授权时的 code 与前端拦截逻辑一致（见 `ruoyi-fastapi-frontend/src/utils/request.js`、`src/permission.js`）
