# Frontend Overview（管理后台前端工程规格）

范围：仅覆盖 `ruoyi-fastapi-frontend/` 的“工程与行为契约”（路由、权限、鉴权、请求/响应约定、构建与环境）。  
UI 结构/样式/组件规格见 `docs/ui-ux-spec/`（UI-only）。

---

## 1) 工程形态与入口

- Source：
  - `ruoyi-fastapi-frontend/src/main.js`
  - `ruoyi-fastapi-frontend/vite.config.js`
- Framework：Vue 3（Vite 构建）
- UI：Element Plus
- Router：Vue Router（动态 addRoute）
- Store：Pinia（`defineStore`）

---

## 2) 环境变量与联动

环境文件：
- `ruoyi-fastapi-frontend/.env.development`
- `ruoyi-fastapi-frontend/.env.production`
- `ruoyi-fastapi-frontend/.env.staging`
- `ruoyi-fastapi-frontend/.env.docker`

关键变量（复刻必须保持语义一致）：
- `VITE_APP_BASE_API`：前端 API baseURL（例如 `/dev-api` 或反向代理前缀）
  - axios 将其作为 `baseURL`（见 `src/utils/request.js`）
  - 后端 `APP_ROOT_PATH`（`/dev-api`）与此变量需要协同，否则会出现路由/代理不一致

---

## 3) 对后端的外部契约依赖

- 登录：`POST /login`（获取 token）
- 获取用户信息：`GET /getInfo`（roles/permissions/user）
- 获取路由树：`GET /getRouters`（动态菜单/路由）
- 统一响应结构：`code/msg/success/time`（详见 `docs/codebase-spec/03_API/ERRORS.md`）

前端对后端状态码的假设：
- 业务成功/失败主要依赖 JSON 内的 `code`，而不是 HTTP status（axios response interceptor 以 `res.data.code` 判定，见 `src/utils/request.js`）。

---

## 4) 构建与运行（最小复刻）

```bash
cd ruoyi-fastapi-frontend
npm install
npm run dev
```

离线门禁（至少可构建）：

```bash
cd ruoyi-fastapi-frontend
npm run build:prod
```

