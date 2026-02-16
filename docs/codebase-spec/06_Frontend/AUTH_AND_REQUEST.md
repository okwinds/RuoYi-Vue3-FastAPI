# Auth & Request Contract（鉴权与请求层契约）

Source：
- `ruoyi-fastapi-frontend/src/utils/request.js`
- `ruoyi-fastapi-frontend/src/utils/auth.js`
- `ruoyi-fastapi-frontend/src/store/modules/user.js`

---

## 1) Token 存储与使用

- Token 存储：
  - `setToken(res.token)`：登录成功后写入本地存储（实现位于 `src/utils/auth.js`）
  - `removeToken()`：退出登录时清理
- Token 注入：
  - axios request interceptor：默认给每个请求加 `Authorization: Bearer <token>`
  - 若某请求不需要 token，需要显式设置：`config.headers.isToken = false`

复刻要求：
- **Bearer 前缀必须一致**（后端解析与 Swagger OAuth2 展示都有依赖）。

---

## 2) 统一响应判定（HTTP 200 + 业务 code）

axios response interceptor 的核心契约：
- `const code = res.data.code || 200`
- `code === 200`：Promise resolve（返回 `res.data`）
- `code === 401`：弹出“重新登录”确认框，调用 `useUserStore().logOut()` 并跳转 `/index`
- `code === 500`：`ElMessage.error`
- `code === 601`：`ElMessage.warning`
- 其它非 200：`ElNotification.error` 并 reject

复刻要求（与后端一致）：
- 后端主要通过 JSON 内的 `code` 表达业务状态（见 `ruoyi-fastapi-backend/utils/response_util.py`）。

---

## 3) 防重复提交（repeatSubmit）

契约：
- 默认开启“防重复提交”（仅对 `POST/PUT`）
- 如果要关闭，需要设置：`config.headers.repeatSubmit = false`

行为（复刻必须保持一致的用户体验）：
- 将 `{url, data, time}` 写入 sessionStorage（`cache.session`）
- 在 `interval=1000ms` 内相同 url + 相同 data 视为重复提交并 reject：`数据正在处理，请勿重复提交`
- 单次存储限制：5MB（超过则跳过校验，仅 warn）

---

## 4) 下载接口契约（blob/arraybuffer）

契约：
- 当 `responseType` 为 `blob/arraybuffer` 时，直接返回二进制数据
- `download()` 会：
  - 显示全屏 Loading
  - 以 `application/x-www-form-urlencoded` 提交（transformRequest：`tansParams`）
  - 校验 blob 是否为合法文件（`blobValidate`），否则尝试解析 JSON 并展示错误 msg

