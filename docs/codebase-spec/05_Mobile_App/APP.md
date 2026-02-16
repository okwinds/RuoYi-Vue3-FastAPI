# 移动端（uni-app）规格（Mobile App）

本仓库包含可选的移动端工程：`ruoyi-fastapi-app/`。该工程面向多端（小程序/H5/App 等）并采用 uni-app 生态。

本文档定位：为“完美复刻整个仓库”补齐移动端的工程/路由/鉴权/请求封装等关键契约。

---

## 1) 技术栈（Tech Stack）

来源：`ruoyi-fastapi-app/package.json`、`ruoyi-fastapi-app/README.md`。

- Framework：uni-app + Vue 3 + Vite
- State：
  - Pinia（`pinia@2.2.4`）
  - 同时依赖了 `vuex`（需要在项目内确认实际使用范围）
- Styling：TailwindCSS（含 weapp-tailwindcss patch）
- Language：TypeScript（项目级 tsconfig 与 ts 工具链）
- Tooling：Stylelint（见 `stylelint.config.mjs`）、PostCSS（`postcss.config.ts`）

---

## 2) 运行与构建（Build & Run）

脚本定义在：`ruoyi-fastapi-app/package.json`。

常用开发命令（示例）：
- 微信小程序：`pnpm dev:mp-weixin`（等价 `uni -p mp-weixin`）
- App：`pnpm dev:app`
- H5：`pnpm dev:h5`

构建命令（示例）：
- 微信小程序构建：`pnpm build:mp-weixin`
- App 构建：`pnpm build:app`

> 上游 README 建议 Node.js 版本：`^20.19.0 || >=22.12.0`（与后台前端 `ruoyi-fastapi-frontend` 的 Node 建议版本可能不同，复刻时需统一/隔离）。

---

## 3) 与后端联动（Backend Coupling）

全局配置：`ruoyi-fastapi-app/src/config.js`

- `baseUrl` 默认：`http://localhost:9099`（与后端默认端口一致）
- AppInfo：
  - name/version/logo/site_url
  - agreements（隐私政策/用户服务协议 URL）

复刻要求：
- 移动端请求封装应以 `baseUrl` 为根，保持与后端 `APP_PORT` 的端口约定一致；
- 若后端启用根路径前缀（例如 `APP_ROOT_PATH`），移动端也需要同步拼接（具体契约见 `docs/codebase-spec/01_Configuration/ENVIRONMENT.md`）。

---

## 4) 页面与信息架构（当前仓库快照级）

页面清单与路由配置见：
- `docs/codebase-spec/05_Mobile_App/ROUTING.md`（`pages.json` + 路由守卫）
- `docs/codebase-spec/05_Mobile_App/PAGES.md`（页面模板与状态）

常见页面类型：
- 登录/注册
- 工作台（work）
- 我的（mine）：个人信息、头像、设置、关于、帮助
- 通用页面：协议/隐私、webview、文本展示

---

## 5) 核心契约索引（复刻入口）

- 路由与拦截：`docs/codebase-spec/05_Mobile_App/ROUTING.md`
- 鉴权与请求封装：`docs/codebase-spec/05_Mobile_App/AUTH_AND_REQUEST.md`
- Store（用户态/配置）：`docs/codebase-spec/05_Mobile_App/STORE.md`
- 页面模板：`docs/codebase-spec/05_Mobile_App/PAGES.md`

