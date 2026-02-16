# Mobile Store（Pinia/Vuex：用户态与配置）

Source：
- `ruoyi-fastapi-app/src/store/index.js`
- `ruoyi-fastapi-app/src/store/modules/user.js`
- `ruoyi-fastapi-app/src/store/modules/config.js`

---

## 1) 用户态（user）

核心 state：
- `token`：通过 `getToken()` 初始化
- `name/nickName/avatar/roles/permissions`（与后端 `/getInfo` 联动）

核心 actions（复刻必须保持语义一致）：
- `loginAction(userInfo)`：调用 `api/login.js::login`，成功后 `setToken(res.token)`
- `getInfoAction()`：调用 `api/login.js::getInfo`，并组装头像 URL（相对路径会拼 `baseUrl`）
- `logoutAction()`：调用 `api/login.js::logout`，并清理 token + 重置 state

---

## 2) 全局配置（config）

配置来源：
- `src/config.js`（baseUrl、AppInfo、协议地址等）

复刻要求：
- baseUrl 与后端端口/根路径前缀（`APP_ROOT_PATH`）协同一致。

