# Mobile Auth & Request（Token/请求封装契约）

Source：
- `ruoyi-fastapi-app/src/utils/auth.js`
- `ruoyi-fastapi-app/src/utils/request.js`
- `ruoyi-fastapi-app/src/api/login.js`

---

## 1) Token 存储

契约：
- token 通过 `uni.setStorageSync` 存储在本地
- 读取通过 `uni.getStorageSync`

复刻要求：
- token key 必须一致（否则路由守卫与请求封装会失效）。

---

## 2) 请求封装（request.js）

基础 URL：
- 默认来自 `src/config.js` 的 `baseUrl`（默认 `http://localhost:9099`）

Authorization 注入：
- 若请求未显式关闭 token，则在 header 写入：
  - `Authorization: Bearer <token>`

错误处理契约：
- 401/登录失效：统一跳回登录页（`uni.reLaunch({ url: '/pages/login' })`）
- 其它错误：使用 toast/modal 提示（具体文案与策略见 `utils/errorCode.js` 与封装实现）

---

## 3) 登录接口契约（api/login.js）

登录请求：
- `POST /login`，body 包含：
  - `username/password`
  - `code/uuid`（当后端启用验证码时）

登录响应：
- 期望返回 `token` 字段（与后台前端一致）

