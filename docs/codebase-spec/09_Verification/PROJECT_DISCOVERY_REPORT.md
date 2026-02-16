# Project Discovery Report（Monorepo 视角）

root: `RuoYi-Vue3-FastAPI/`

用途：说明本仓库是由多个可独立运行的工程组成的 monorepo，并给出每个工程的入口、技术栈与“复刻必须关注点”。

---

## 1) 子工程清单（Projects）

| Project | Path | Type | Entry | Notes |
| --- | --- | --- | --- | --- |
| Backend | `ruoyi-fastapi-backend/` | FastAPI API Server | `app.py` / `server.create_app()` | 自动注册 controller 路由；生命周期中预热 Redis/字典/参数并加载 Scheduler |
| Admin Frontend | `ruoyi-fastapi-frontend/` | Vue3 Admin SPA | `src/main.js` | 动态路由：`/getRouters` 下发；axios 以 `code` 判定业务状态 |
| Mobile App | `ruoyi-fastapi-app/` | uni-app（Vue3） | `src/main.ts` | `pages.json` + 路由守卫；请求封装注入 Bearer token |
| E2E Tests | `ruoyi-fastapi-test/` | pytest + Playwright | `pytest` | 覆盖登录/系统管理/监控/工具（生成器/Swagger）关键路径 |

---

## 2) 语言与生态（Languages & Tooling）

- Python：后端 + E2E（pytest/Playwright）
- JavaScript：PC 管理后台前端（Vue3）
- TypeScript：移动端工程（uni-app + TS 工具链）

---

## 3) 对外契约入口（Replication Entrypoints）

- DB：`docs/codebase-spec/02_Data/`
- API（字段级）：`docs/codebase-spec/03_API/openapi.json`
- 认证鉴权：`docs/codebase-spec/03_API/AUTHENTICATION.md`
- 前端工程/权限/请求：`docs/codebase-spec/06_Frontend/`
- UI 结构/样式/组件（UI-only）：`docs/ui-ux-spec/`
- E2E（反向验收）：`docs/codebase-spec/08_Testing/E2E_SPECS.md`
