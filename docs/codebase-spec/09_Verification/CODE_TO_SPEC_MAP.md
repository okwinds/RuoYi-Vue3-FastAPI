# Code → Spec Map（全仓库文件级对照表）

generated: `2026-02-14 19:47:34 CST`

用途：对全仓库文件做“代码 → 规格文档”映射，确保每个文件都能被某份规格文档解释或被契约快照覆盖。

说明：
- 本表是“复刻交付”的索引层：它不替代字段级/流程级规格，但保证任何文件都有归属与定位入口。
- 规格主入口：`docs/codebase-spec/SPEC_INDEX.md`；UI-only 规格：`docs/ui-ux-spec/`。

## Summary
- Files scanned: 523
- Mapped: 523
- Unmapped: 0

| Category | Count |
| --- | ---: |
| Frontend Assets | 102 |
| Frontend UI | 87 |
| Frontend Other | 46 |
| Mobile Other | 44 |
| E2E Tests | 27 |
| Frontend API Client | 21 |
| Backend Service | 20 |
| Backend Controller | 19 |
| Backend Utils | 18 |
| Backend VO (API Models) | 18 |
| Mobile Pages | 16 |
| Backend DAO | 15 |
| Backend DO (DB/Domain Models) | 13 |
| Backend Common | 11 |
| Backend Middlewares | 8 |
| Backend Other | 6 |
| Backend Config | 5 |
| Docker/Compose | 4 |
| Mobile Store | 4 |
| Dockerfile | 3 |
| Backend Entrypoint | 2 |
| Backend Exceptions | 2 |
| Backend SubApps | 2 |
| CI/CD | 2 |
| DB Init SQL | 2 |
| E2E Other | 3 |
| Frontend Entrypoint | 2 |
| Mobile Request/Auth | 2 |
| Mobile Routing | 2 |
| Alembic | 1 |
| Backend Assets | 1 |
| Changelog | 1 |
| DocsIndex | 1 |
| E2E Test SQL | 1 |
| Frontend Dynamic Routes | 1 |
| Frontend Request | 1 |
| Frontend Router Guard | 1 |
| Frontend User Store | 1 |
| Governance | 1 |
| License | 1 |
| Mobile Config | 1 |
| README | 1 |
| Repo Metadata | 1 |
| RepoHygiene | 1 |
| Tooling | 1 |
| UpstreamREADME | 1 |

## Mapping（按路径）

| File | Category | Spec Pointers | Rationale |
| --- | --- | --- | --- |
| `.github/FUNDING.yml` | Repo Metadata | `docs/compliance/fork-upstream.md` | 上游/社区元数据（不影响运行时） |
| `.github/workflows/playwright.yml` | CI/CD | `docs/codebase-spec/07_Infrastructure/CI_CD.md` | CI 流水线说明 |
| `.github/workflows/ruff.yml` | CI/CD | `docs/codebase-spec/07_Infrastructure/CI_CD.md` | CI 流水线说明 |
| `.gitignore` | RepoHygiene | `docs/compliance/README.md` | 仓库卫生/忽略规则（高层） |
| `AGENTS.md` | Governance | `AGENTS.md` | 协作宪法/流程约束 |
| `CHANGELOG.md` | Changelog | `CHANGELOG.md` | 上游变更记录 |
| `DOCS_INDEX.md` | DocsIndex | `DOCS_INDEX.md` | 文档索引入口 |
| `LICENSE` | License | `LICENSE` | 许可证 |
| `README.md` | README | `README.md` | 面向人类入口 |
| `README.md.bak` | UpstreamREADME | `README.md.bak` | 上游 README 备份 |
| `docker-compose.my.yml` | Docker/Compose | `docs/codebase-spec/07_Infrastructure/DOCKER.md`<br/>`docs/codebase-spec/08_Testing/E2E_SPECS.md` | 环境与测试编排 |
| `docker-compose.pg.yml` | Docker/Compose | `docs/codebase-spec/07_Infrastructure/DOCKER.md`<br/>`docs/codebase-spec/08_Testing/E2E_SPECS.md` | 环境与测试编排 |
| `ruoyi-fastapi-app/README.md` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/netlify.toml` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/package.json` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/platform.ts` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/pnpm-lock.yaml` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/postcss.config.ts` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/App.vue` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/api/login.js` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/api/system/dict/data.js` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/api/system/dict/type.js` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/api/system/user.js` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/auto-imports.d.ts` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/config.js` | Mobile Config | `docs/codebase-spec/05_Mobile_App/APP.md`<br/>`docs/codebase-spec/01_Configuration/ENVIRONMENT.md` | baseUrl 等配置 |
| `ruoyi-fastapi-app/src/env.d.ts` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/main.ts` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/manifest.json` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/pages.json` | Mobile Routing | `docs/codebase-spec/05_Mobile_App/ROUTING.md` | 路由/守卫 |
| `ruoyi-fastapi-app/src/pages/common/agreement/index.vue` | Mobile Pages | `docs/codebase-spec/05_Mobile_App/PAGES.md` | 页面模板 |
| `ruoyi-fastapi-app/src/pages/common/privacy/index.vue` | Mobile Pages | `docs/codebase-spec/05_Mobile_App/PAGES.md` | 页面模板 |
| `ruoyi-fastapi-app/src/pages/common/textview/index.vue` | Mobile Pages | `docs/codebase-spec/05_Mobile_App/PAGES.md` | 页面模板 |
| `ruoyi-fastapi-app/src/pages/common/webview/index.vue` | Mobile Pages | `docs/codebase-spec/05_Mobile_App/PAGES.md` | 页面模板 |
| `ruoyi-fastapi-app/src/pages/index.vue` | Mobile Pages | `docs/codebase-spec/05_Mobile_App/PAGES.md` | 页面模板 |
| `ruoyi-fastapi-app/src/pages/login.vue` | Mobile Pages | `docs/codebase-spec/05_Mobile_App/PAGES.md` | 页面模板 |
| `ruoyi-fastapi-app/src/pages/mine/about/index.vue` | Mobile Pages | `docs/codebase-spec/05_Mobile_App/PAGES.md` | 页面模板 |
| `ruoyi-fastapi-app/src/pages/mine/avatar/index.vue` | Mobile Pages | `docs/codebase-spec/05_Mobile_App/PAGES.md` | 页面模板 |
| `ruoyi-fastapi-app/src/pages/mine/help/index.vue` | Mobile Pages | `docs/codebase-spec/05_Mobile_App/PAGES.md` | 页面模板 |
| `ruoyi-fastapi-app/src/pages/mine/index.vue` | Mobile Pages | `docs/codebase-spec/05_Mobile_App/PAGES.md` | 页面模板 |
| `ruoyi-fastapi-app/src/pages/mine/info/edit.vue` | Mobile Pages | `docs/codebase-spec/05_Mobile_App/PAGES.md` | 页面模板 |
| `ruoyi-fastapi-app/src/pages/mine/info/index.vue` | Mobile Pages | `docs/codebase-spec/05_Mobile_App/PAGES.md` | 页面模板 |
| `ruoyi-fastapi-app/src/pages/mine/pwd/index.vue` | Mobile Pages | `docs/codebase-spec/05_Mobile_App/PAGES.md` | 页面模板 |
| `ruoyi-fastapi-app/src/pages/mine/setting/index.vue` | Mobile Pages | `docs/codebase-spec/05_Mobile_App/PAGES.md` | 页面模板 |
| `ruoyi-fastapi-app/src/pages/register.vue` | Mobile Pages | `docs/codebase-spec/05_Mobile_App/PAGES.md` | 页面模板 |
| `ruoyi-fastapi-app/src/pages/work/index.vue` | Mobile Pages | `docs/codebase-spec/05_Mobile_App/PAGES.md` | 页面模板 |
| `ruoyi-fastapi-app/src/permission.js` | Mobile Routing | `docs/codebase-spec/05_Mobile_App/ROUTING.md` | 路由/守卫 |
| `ruoyi-fastapi-app/src/plugins/auth.js` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/plugins/index.js` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/plugins/modal.js` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/plugins/tab.js` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/static/favicon.ico` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/static/images/banner/banner01.jpg` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/static/images/banner/banner02.jpg` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/static/images/banner/banner03.jpg` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/static/images/profile.jpg` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/static/images/tabbar/home.png` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/static/images/tabbar/home_.png` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/static/images/tabbar/mine.png` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/static/images/tabbar/mine_.png` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/static/images/tabbar/work.png` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/static/images/tabbar/work_.png` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/static/logo.png` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/static/logo200.png` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/store/index.js` | Mobile Store | `docs/codebase-spec/05_Mobile_App/STORE.md` | 用户态/配置 |
| `ruoyi-fastapi-app/src/store/modules/config.js` | Mobile Store | `docs/codebase-spec/05_Mobile_App/STORE.md` | 用户态/配置 |
| `ruoyi-fastapi-app/src/store/modules/dict.js` | Mobile Store | `docs/codebase-spec/05_Mobile_App/STORE.md` | 用户态/配置 |
| `ruoyi-fastapi-app/src/store/modules/user.js` | Mobile Store | `docs/codebase-spec/05_Mobile_App/STORE.md` | 用户态/配置 |
| `ruoyi-fastapi-app/src/theme.json` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/utils/auth.js` | Mobile Request/Auth | `docs/codebase-spec/05_Mobile_App/AUTH_AND_REQUEST.md` | Bearer token 与请求封装 |
| `ruoyi-fastapi-app/src/utils/common.js` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/utils/constant.js` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/utils/dict.js` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/utils/errorCode.js` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/utils/permission.js` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/utils/request.js` | Mobile Request/Auth | `docs/codebase-spec/05_Mobile_App/AUTH_AND_REQUEST.md` | Bearer token 与请求封装 |
| `ruoyi-fastapi-app/src/utils/storage.js` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/utils/upload.js` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/src/utils/validate.js` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/tailwind.config.ts` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/tsconfig.json` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-app/vite.config.ts` | Mobile Other | `docs/codebase-spec/05_Mobile_App/APP.md` | 移动端工程说明 |
| `ruoyi-fastapi-backend/Dockerfile.my` | Dockerfile | `docs/codebase-spec/07_Infrastructure/DOCKER.md` | 镜像构建说明 |
| `ruoyi-fastapi-backend/Dockerfile.pg` | Dockerfile | `docs/codebase-spec/07_Infrastructure/DOCKER.md` | 镜像构建说明 |
| `ruoyi-fastapi-backend/alembic.ini` | Backend Other | `docs/codebase-spec/00_Overview/ARCHITECTURE.md` | 后端其余实现细节归入架构说明 |
| `ruoyi-fastapi-backend/alembic/env.py` | Alembic | `docs/codebase-spec/02_Data/MIGRATIONS.md` | 迁移工具 |
| `ruoyi-fastapi-backend/app.py` | Backend Entrypoint | `docs/codebase-spec/00_Overview/ARCHITECTURE.md`<br/>`docs/codebase-spec/00_Overview/PROJECT.md` | 后端启动/生命周期/路由注册 |
| `ruoyi-fastapi-backend/assets/font/Arial.ttf` | Backend Assets | `docs/codebase-spec/00_Overview/PROJECT.md` | 后端静态资源（文档静态/Logo 等） |
| `ruoyi-fastapi-backend/common/annotation/log_annotation.py` | Backend Common | `docs/codebase-spec/00_Overview/ARCHITECTURE.md`<br/>`docs/codebase-spec/03_API/ERRORS.md`<br/>`docs/codebase-spec/03_API/ENDPOINTS.md` | 路由、响应模型、常量与装饰器 |
| `ruoyi-fastapi-backend/common/annotation/pydantic_annotation.py` | Backend Common | `docs/codebase-spec/00_Overview/ARCHITECTURE.md`<br/>`docs/codebase-spec/03_API/ERRORS.md`<br/>`docs/codebase-spec/03_API/ENDPOINTS.md` | 路由、响应模型、常量与装饰器 |
| `ruoyi-fastapi-backend/common/aspect/data_scope.py` | Backend Common | `docs/codebase-spec/00_Overview/ARCHITECTURE.md`<br/>`docs/codebase-spec/03_API/ERRORS.md`<br/>`docs/codebase-spec/03_API/ENDPOINTS.md` | 路由、响应模型、常量与装饰器 |
| `ruoyi-fastapi-backend/common/aspect/db_seesion.py` | Backend Common | `docs/codebase-spec/00_Overview/ARCHITECTURE.md`<br/>`docs/codebase-spec/03_API/ERRORS.md`<br/>`docs/codebase-spec/03_API/ENDPOINTS.md` | 路由、响应模型、常量与装饰器 |
| `ruoyi-fastapi-backend/common/aspect/interface_auth.py` | Backend Common | `docs/codebase-spec/00_Overview/ARCHITECTURE.md`<br/>`docs/codebase-spec/03_API/ERRORS.md`<br/>`docs/codebase-spec/03_API/ENDPOINTS.md` | 路由、响应模型、常量与装饰器 |
| `ruoyi-fastapi-backend/common/aspect/pre_auth.py` | Backend Common | `docs/codebase-spec/00_Overview/ARCHITECTURE.md`<br/>`docs/codebase-spec/03_API/ERRORS.md`<br/>`docs/codebase-spec/03_API/ENDPOINTS.md` | 路由、响应模型、常量与装饰器 |
| `ruoyi-fastapi-backend/common/constant.py` | Backend Common | `docs/codebase-spec/00_Overview/ARCHITECTURE.md`<br/>`docs/codebase-spec/03_API/ERRORS.md`<br/>`docs/codebase-spec/03_API/ENDPOINTS.md` | 路由、响应模型、常量与装饰器 |
| `ruoyi-fastapi-backend/common/context.py` | Backend Common | `docs/codebase-spec/00_Overview/ARCHITECTURE.md`<br/>`docs/codebase-spec/03_API/ERRORS.md`<br/>`docs/codebase-spec/03_API/ENDPOINTS.md` | 路由、响应模型、常量与装饰器 |
| `ruoyi-fastapi-backend/common/enums.py` | Backend Common | `docs/codebase-spec/00_Overview/ARCHITECTURE.md`<br/>`docs/codebase-spec/03_API/ERRORS.md`<br/>`docs/codebase-spec/03_API/ENDPOINTS.md` | 路由、响应模型、常量与装饰器 |
| `ruoyi-fastapi-backend/common/router.py` | Backend Common | `docs/codebase-spec/00_Overview/ARCHITECTURE.md`<br/>`docs/codebase-spec/03_API/ERRORS.md`<br/>`docs/codebase-spec/03_API/ENDPOINTS.md` | 路由、响应模型、常量与装饰器 |
| `ruoyi-fastapi-backend/common/vo.py` | Backend Common | `docs/codebase-spec/00_Overview/ARCHITECTURE.md`<br/>`docs/codebase-spec/03_API/ERRORS.md`<br/>`docs/codebase-spec/03_API/ENDPOINTS.md` | 路由、响应模型、常量与装饰器 |
| `ruoyi-fastapi-backend/config/database.py` | Backend Config | `docs/codebase-spec/01_Configuration/ENVIRONMENT.md`<br/>`docs/codebase-spec/02_Data/MIGRATIONS.md`<br/>`docs/codebase-spec/04_Business_Logic/RULES.md` | 环境变量与 DB/Redis/Scheduler 配置 |
| `ruoyi-fastapi-backend/config/env.py` | Backend Config | `docs/codebase-spec/01_Configuration/ENVIRONMENT.md`<br/>`docs/codebase-spec/02_Data/MIGRATIONS.md`<br/>`docs/codebase-spec/04_Business_Logic/RULES.md` | 环境变量与 DB/Redis/Scheduler 配置 |
| `ruoyi-fastapi-backend/config/get_db.py` | Backend Config | `docs/codebase-spec/01_Configuration/ENVIRONMENT.md`<br/>`docs/codebase-spec/02_Data/MIGRATIONS.md`<br/>`docs/codebase-spec/04_Business_Logic/RULES.md` | 环境变量与 DB/Redis/Scheduler 配置 |
| `ruoyi-fastapi-backend/config/get_redis.py` | Backend Config | `docs/codebase-spec/01_Configuration/ENVIRONMENT.md`<br/>`docs/codebase-spec/02_Data/MIGRATIONS.md`<br/>`docs/codebase-spec/04_Business_Logic/RULES.md` | 环境变量与 DB/Redis/Scheduler 配置 |
| `ruoyi-fastapi-backend/config/get_scheduler.py` | Backend Config | `docs/codebase-spec/01_Configuration/ENVIRONMENT.md`<br/>`docs/codebase-spec/02_Data/MIGRATIONS.md`<br/>`docs/codebase-spec/04_Business_Logic/RULES.md` | 环境变量与 DB/Redis/Scheduler 配置 |
| `ruoyi-fastapi-backend/exceptions/exception.py` | Backend Exceptions | `docs/codebase-spec/03_API/ERRORS.md` | 异常映射与响应策略 |
| `ruoyi-fastapi-backend/exceptions/handle.py` | Backend Exceptions | `docs/codebase-spec/03_API/ERRORS.md` | 异常映射与响应策略 |
| `ruoyi-fastapi-backend/middlewares/context_middleware.py` | Backend Middlewares | `docs/codebase-spec/00_Overview/ARCHITECTURE.md` | 中间件链 |
| `ruoyi-fastapi-backend/middlewares/cors_middleware.py` | Backend Middlewares | `docs/codebase-spec/00_Overview/ARCHITECTURE.md` | 中间件链 |
| `ruoyi-fastapi-backend/middlewares/gzip_middleware.py` | Backend Middlewares | `docs/codebase-spec/00_Overview/ARCHITECTURE.md` | 中间件链 |
| `ruoyi-fastapi-backend/middlewares/handle.py` | Backend Middlewares | `docs/codebase-spec/00_Overview/ARCHITECTURE.md` | 中间件链 |
| `ruoyi-fastapi-backend/middlewares/trace_middleware/__init__.py` | Backend Middlewares | `docs/codebase-spec/00_Overview/ARCHITECTURE.md` | 中间件链 |
| `ruoyi-fastapi-backend/middlewares/trace_middleware/ctx.py` | Backend Middlewares | `docs/codebase-spec/00_Overview/ARCHITECTURE.md` | 中间件链 |
| `ruoyi-fastapi-backend/middlewares/trace_middleware/middle.py` | Backend Middlewares | `docs/codebase-spec/00_Overview/ARCHITECTURE.md` | 中间件链 |
| `ruoyi-fastapi-backend/middlewares/trace_middleware/span.py` | Backend Middlewares | `docs/codebase-spec/00_Overview/ARCHITECTURE.md` | 中间件链 |
| `ruoyi-fastapi-backend/module_admin/controller/cache_controller.py` | Backend Controller | `docs/codebase-spec/03_API/ENDPOINTS.md`<br/>`docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 端点清单 + 字段级契约 |
| `ruoyi-fastapi-backend/module_admin/controller/captcha_controller.py` | Backend Controller | `docs/codebase-spec/03_API/ENDPOINTS.md`<br/>`docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 端点清单 + 字段级契约 |
| `ruoyi-fastapi-backend/module_admin/controller/common_controller.py` | Backend Controller | `docs/codebase-spec/03_API/ENDPOINTS.md`<br/>`docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 端点清单 + 字段级契约 |
| `ruoyi-fastapi-backend/module_admin/controller/config_controller.py` | Backend Controller | `docs/codebase-spec/03_API/ENDPOINTS.md`<br/>`docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 端点清单 + 字段级契约 |
| `ruoyi-fastapi-backend/module_admin/controller/dept_controller.py` | Backend Controller | `docs/codebase-spec/03_API/ENDPOINTS.md`<br/>`docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 端点清单 + 字段级契约 |
| `ruoyi-fastapi-backend/module_admin/controller/dict_controller.py` | Backend Controller | `docs/codebase-spec/03_API/ENDPOINTS.md`<br/>`docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 端点清单 + 字段级契约 |
| `ruoyi-fastapi-backend/module_admin/controller/job_controller.py` | Backend Controller | `docs/codebase-spec/03_API/ENDPOINTS.md`<br/>`docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 端点清单 + 字段级契约 |
| `ruoyi-fastapi-backend/module_admin/controller/log_controller.py` | Backend Controller | `docs/codebase-spec/03_API/ENDPOINTS.md`<br/>`docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 端点清单 + 字段级契约 |
| `ruoyi-fastapi-backend/module_admin/controller/login_controller.py` | Backend Controller | `docs/codebase-spec/03_API/ENDPOINTS.md`<br/>`docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 端点清单 + 字段级契约 |
| `ruoyi-fastapi-backend/module_admin/controller/menu_controller.py` | Backend Controller | `docs/codebase-spec/03_API/ENDPOINTS.md`<br/>`docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 端点清单 + 字段级契约 |
| `ruoyi-fastapi-backend/module_admin/controller/notice_controller.py` | Backend Controller | `docs/codebase-spec/03_API/ENDPOINTS.md`<br/>`docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 端点清单 + 字段级契约 |
| `ruoyi-fastapi-backend/module_admin/controller/online_controller.py` | Backend Controller | `docs/codebase-spec/03_API/ENDPOINTS.md`<br/>`docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 端点清单 + 字段级契约 |
| `ruoyi-fastapi-backend/module_admin/controller/post_controller.py` | Backend Controller | `docs/codebase-spec/03_API/ENDPOINTS.md`<br/>`docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 端点清单 + 字段级契约 |
| `ruoyi-fastapi-backend/module_admin/controller/role_controller.py` | Backend Controller | `docs/codebase-spec/03_API/ENDPOINTS.md`<br/>`docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 端点清单 + 字段级契约 |
| `ruoyi-fastapi-backend/module_admin/controller/server_controller.py` | Backend Controller | `docs/codebase-spec/03_API/ENDPOINTS.md`<br/>`docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 端点清单 + 字段级契约 |
| `ruoyi-fastapi-backend/module_admin/controller/user_controller.py` | Backend Controller | `docs/codebase-spec/03_API/ENDPOINTS.md`<br/>`docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 端点清单 + 字段级契约 |
| `ruoyi-fastapi-backend/module_admin/dao/config_dao.py` | Backend DAO | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/daos/config_dao.py.md` | 方法级索引（数据访问边界） |
| `ruoyi-fastapi-backend/module_admin/dao/dept_dao.py` | Backend DAO | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/daos/dept_dao.py.md` | 方法级索引（数据访问边界） |
| `ruoyi-fastapi-backend/module_admin/dao/dict_dao.py` | Backend DAO | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/daos/dict_dao.py.md` | 方法级索引（数据访问边界） |
| `ruoyi-fastapi-backend/module_admin/dao/job_dao.py` | Backend DAO | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/daos/job_dao.py.md` | 方法级索引（数据访问边界） |
| `ruoyi-fastapi-backend/module_admin/dao/job_log_dao.py` | Backend DAO | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/daos/job_log_dao.py.md` | 方法级索引（数据访问边界） |
| `ruoyi-fastapi-backend/module_admin/dao/log_dao.py` | Backend DAO | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/daos/log_dao.py.md` | 方法级索引（数据访问边界） |
| `ruoyi-fastapi-backend/module_admin/dao/login_dao.py` | Backend DAO | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/daos/login_dao.py.md` | 方法级索引（数据访问边界） |
| `ruoyi-fastapi-backend/module_admin/dao/menu_dao.py` | Backend DAO | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/daos/menu_dao.py.md` | 方法级索引（数据访问边界） |
| `ruoyi-fastapi-backend/module_admin/dao/notice_dao.py` | Backend DAO | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/daos/notice_dao.py.md` | 方法级索引（数据访问边界） |
| `ruoyi-fastapi-backend/module_admin/dao/post_dao.py` | Backend DAO | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/daos/post_dao.py.md` | 方法级索引（数据访问边界） |
| `ruoyi-fastapi-backend/module_admin/dao/role_dao.py` | Backend DAO | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/daos/role_dao.py.md` | 方法级索引（数据访问边界） |
| `ruoyi-fastapi-backend/module_admin/dao/user_dao.py` | Backend DAO | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/daos/user_dao.py.md` | 方法级索引（数据访问边界） |
| `ruoyi-fastapi-backend/module_admin/entity/do/config_do.py` | Backend DO (DB/Domain Models) | `docs/codebase-spec/02_Data/ENTITIES.md`<br/>`docs/codebase-spec/02_Data/RELATIONSHIPS.md` | 与 DB 表结构/关系对应 |
| `ruoyi-fastapi-backend/module_admin/entity/do/dept_do.py` | Backend DO (DB/Domain Models) | `docs/codebase-spec/02_Data/ENTITIES.md`<br/>`docs/codebase-spec/02_Data/RELATIONSHIPS.md` | 与 DB 表结构/关系对应 |
| `ruoyi-fastapi-backend/module_admin/entity/do/dict_do.py` | Backend DO (DB/Domain Models) | `docs/codebase-spec/02_Data/ENTITIES.md`<br/>`docs/codebase-spec/02_Data/RELATIONSHIPS.md` | 与 DB 表结构/关系对应 |
| `ruoyi-fastapi-backend/module_admin/entity/do/job_do.py` | Backend DO (DB/Domain Models) | `docs/codebase-spec/02_Data/ENTITIES.md`<br/>`docs/codebase-spec/02_Data/RELATIONSHIPS.md` | 与 DB 表结构/关系对应 |
| `ruoyi-fastapi-backend/module_admin/entity/do/log_do.py` | Backend DO (DB/Domain Models) | `docs/codebase-spec/02_Data/ENTITIES.md`<br/>`docs/codebase-spec/02_Data/RELATIONSHIPS.md` | 与 DB 表结构/关系对应 |
| `ruoyi-fastapi-backend/module_admin/entity/do/menu_do.py` | Backend DO (DB/Domain Models) | `docs/codebase-spec/02_Data/ENTITIES.md`<br/>`docs/codebase-spec/02_Data/RELATIONSHIPS.md` | 与 DB 表结构/关系对应 |
| `ruoyi-fastapi-backend/module_admin/entity/do/notice_do.py` | Backend DO (DB/Domain Models) | `docs/codebase-spec/02_Data/ENTITIES.md`<br/>`docs/codebase-spec/02_Data/RELATIONSHIPS.md` | 与 DB 表结构/关系对应 |
| `ruoyi-fastapi-backend/module_admin/entity/do/post_do.py` | Backend DO (DB/Domain Models) | `docs/codebase-spec/02_Data/ENTITIES.md`<br/>`docs/codebase-spec/02_Data/RELATIONSHIPS.md` | 与 DB 表结构/关系对应 |
| `ruoyi-fastapi-backend/module_admin/entity/do/role_do.py` | Backend DO (DB/Domain Models) | `docs/codebase-spec/02_Data/ENTITIES.md`<br/>`docs/codebase-spec/02_Data/RELATIONSHIPS.md` | 与 DB 表结构/关系对应 |
| `ruoyi-fastapi-backend/module_admin/entity/do/user_do.py` | Backend DO (DB/Domain Models) | `docs/codebase-spec/02_Data/ENTITIES.md`<br/>`docs/codebase-spec/02_Data/RELATIONSHIPS.md` | 与 DB 表结构/关系对应 |
| `ruoyi-fastapi-backend/module_admin/entity/vo/cache_vo.py` | Backend VO (API Models) | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/SCHEMA_CATALOG.md` | 字段级 schema 在 OpenAPI |
| `ruoyi-fastapi-backend/module_admin/entity/vo/common_vo.py` | Backend VO (API Models) | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/SCHEMA_CATALOG.md` | 字段级 schema 在 OpenAPI |
| `ruoyi-fastapi-backend/module_admin/entity/vo/config_vo.py` | Backend VO (API Models) | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/SCHEMA_CATALOG.md` | 字段级 schema 在 OpenAPI |
| `ruoyi-fastapi-backend/module_admin/entity/vo/dept_vo.py` | Backend VO (API Models) | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/SCHEMA_CATALOG.md` | 字段级 schema 在 OpenAPI |
| `ruoyi-fastapi-backend/module_admin/entity/vo/dict_vo.py` | Backend VO (API Models) | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/SCHEMA_CATALOG.md` | 字段级 schema 在 OpenAPI |
| `ruoyi-fastapi-backend/module_admin/entity/vo/job_vo.py` | Backend VO (API Models) | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/SCHEMA_CATALOG.md` | 字段级 schema 在 OpenAPI |
| `ruoyi-fastapi-backend/module_admin/entity/vo/log_vo.py` | Backend VO (API Models) | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/SCHEMA_CATALOG.md` | 字段级 schema 在 OpenAPI |
| `ruoyi-fastapi-backend/module_admin/entity/vo/login_vo.py` | Backend VO (API Models) | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/SCHEMA_CATALOG.md` | 字段级 schema 在 OpenAPI |
| `ruoyi-fastapi-backend/module_admin/entity/vo/menu_vo.py` | Backend VO (API Models) | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/SCHEMA_CATALOG.md` | 字段级 schema 在 OpenAPI |
| `ruoyi-fastapi-backend/module_admin/entity/vo/notice_vo.py` | Backend VO (API Models) | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/SCHEMA_CATALOG.md` | 字段级 schema 在 OpenAPI |
| `ruoyi-fastapi-backend/module_admin/entity/vo/online_vo.py` | Backend VO (API Models) | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/SCHEMA_CATALOG.md` | 字段级 schema 在 OpenAPI |
| `ruoyi-fastapi-backend/module_admin/entity/vo/post_vo.py` | Backend VO (API Models) | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/SCHEMA_CATALOG.md` | 字段级 schema 在 OpenAPI |
| `ruoyi-fastapi-backend/module_admin/entity/vo/role_vo.py` | Backend VO (API Models) | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/SCHEMA_CATALOG.md` | 字段级 schema 在 OpenAPI |
| `ruoyi-fastapi-backend/module_admin/entity/vo/server_vo.py` | Backend VO (API Models) | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/SCHEMA_CATALOG.md` | 字段级 schema 在 OpenAPI |
| `ruoyi-fastapi-backend/module_admin/entity/vo/user_vo.py` | Backend VO (API Models) | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/SCHEMA_CATALOG.md` | 字段级 schema 在 OpenAPI |
| `ruoyi-fastapi-backend/module_admin/service/cache_service.py` | Backend Service | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/services/cache_service.py.md` | 方法级索引（DAO 调用点/异常文案） |
| `ruoyi-fastapi-backend/module_admin/service/captcha_service.py` | Backend Service | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/services/captcha_service.py.md` | 方法级索引（DAO 调用点/异常文案） |
| `ruoyi-fastapi-backend/module_admin/service/common_service.py` | Backend Service | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/services/common_service.py.md` | 方法级索引（DAO 调用点/异常文案） |
| `ruoyi-fastapi-backend/module_admin/service/config_service.py` | Backend Service | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/services/config_service.py.md` | 方法级索引（DAO 调用点/异常文案） |
| `ruoyi-fastapi-backend/module_admin/service/dept_service.py` | Backend Service | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/services/dept_service.py.md` | 方法级索引（DAO 调用点/异常文案） |
| `ruoyi-fastapi-backend/module_admin/service/dict_service.py` | Backend Service | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/services/dict_service.py.md` | 方法级索引（DAO 调用点/异常文案） |
| `ruoyi-fastapi-backend/module_admin/service/job_log_service.py` | Backend Service | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/services/job_log_service.py.md` | 方法级索引（DAO 调用点/异常文案） |
| `ruoyi-fastapi-backend/module_admin/service/job_service.py` | Backend Service | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/services/job_service.py.md` | 方法级索引（DAO 调用点/异常文案） |
| `ruoyi-fastapi-backend/module_admin/service/log_service.py` | Backend Service | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/services/log_service.py.md` | 方法级索引（DAO 调用点/异常文案） |
| `ruoyi-fastapi-backend/module_admin/service/login_service.py` | Backend Service | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/services/login_service.py.md` | 方法级索引（DAO 调用点/异常文案） |
| `ruoyi-fastapi-backend/module_admin/service/menu_service.py` | Backend Service | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/services/menu_service.py.md` | 方法级索引（DAO 调用点/异常文案） |
| `ruoyi-fastapi-backend/module_admin/service/notice_service.py` | Backend Service | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/services/notice_service.py.md` | 方法级索引（DAO 调用点/异常文案） |
| `ruoyi-fastapi-backend/module_admin/service/online_service.py` | Backend Service | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/services/online_service.py.md` | 方法级索引（DAO 调用点/异常文案） |
| `ruoyi-fastapi-backend/module_admin/service/post_service.py` | Backend Service | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/services/post_service.py.md` | 方法级索引（DAO 调用点/异常文案） |
| `ruoyi-fastapi-backend/module_admin/service/role_service.py` | Backend Service | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/services/role_service.py.md` | 方法级索引（DAO 调用点/异常文案） |
| `ruoyi-fastapi-backend/module_admin/service/server_service.py` | Backend Service | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/services/server_service.py.md` | 方法级索引（DAO 调用点/异常文案） |
| `ruoyi-fastapi-backend/module_admin/service/user_service.py` | Backend Service | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/services/user_service.py.md` | 方法级索引（DAO 调用点/异常文案） |
| `ruoyi-fastapi-backend/module_ai/controller/ai_chat_controller.py` | Backend Controller | `docs/codebase-spec/03_API/ENDPOINTS.md`<br/>`docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 端点清单 + 字段级契约 |
| `ruoyi-fastapi-backend/module_ai/controller/ai_model_controller.py` | Backend Controller | `docs/codebase-spec/03_API/ENDPOINTS.md`<br/>`docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 端点清单 + 字段级契约 |
| `ruoyi-fastapi-backend/module_ai/dao/ai_chat_dao.py` | Backend DAO | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/daos/ai_chat_dao.py.md` | 方法级索引（数据访问边界） |
| `ruoyi-fastapi-backend/module_ai/dao/ai_model_dao.py` | Backend DAO | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/daos/ai_model_dao.py.md` | 方法级索引（数据访问边界） |
| `ruoyi-fastapi-backend/module_ai/entity/do/ai_chat_do.py` | Backend DO (DB/Domain Models) | `docs/codebase-spec/02_Data/ENTITIES.md`<br/>`docs/codebase-spec/02_Data/RELATIONSHIPS.md` | 与 DB 表结构/关系对应 |
| `ruoyi-fastapi-backend/module_ai/entity/do/ai_model_do.py` | Backend DO (DB/Domain Models) | `docs/codebase-spec/02_Data/ENTITIES.md`<br/>`docs/codebase-spec/02_Data/RELATIONSHIPS.md` | 与 DB 表结构/关系对应 |
| `ruoyi-fastapi-backend/module_ai/entity/vo/ai_chat_vo.py` | Backend VO (API Models) | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/SCHEMA_CATALOG.md` | 字段级 schema 在 OpenAPI |
| `ruoyi-fastapi-backend/module_ai/entity/vo/ai_model_vo.py` | Backend VO (API Models) | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/SCHEMA_CATALOG.md` | 字段级 schema 在 OpenAPI |
| `ruoyi-fastapi-backend/module_ai/service/ai_chat_service.py` | Backend Service | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/services/ai_chat_service.py.md` | 方法级索引（DAO 调用点/异常文案） |
| `ruoyi-fastapi-backend/module_ai/service/ai_model_service.py` | Backend Service | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/services/ai_model_service.py.md` | 方法级索引（DAO 调用点/异常文案） |
| `ruoyi-fastapi-backend/module_generator/controller/gen_controller.py` | Backend Controller | `docs/codebase-spec/03_API/ENDPOINTS.md`<br/>`docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 端点清单 + 字段级契约 |
| `ruoyi-fastapi-backend/module_generator/dao/gen_dao.py` | Backend DAO | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/daos/gen_dao.py.md` | 方法级索引（数据访问边界） |
| `ruoyi-fastapi-backend/module_generator/entity/do/gen_do.py` | Backend DO (DB/Domain Models) | `docs/codebase-spec/02_Data/ENTITIES.md`<br/>`docs/codebase-spec/02_Data/RELATIONSHIPS.md` | 与 DB 表结构/关系对应 |
| `ruoyi-fastapi-backend/module_generator/entity/vo/gen_vo.py` | Backend VO (API Models) | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/SCHEMA_CATALOG.md` | 字段级 schema 在 OpenAPI |
| `ruoyi-fastapi-backend/module_generator/service/gen_service.py` | Backend Service | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md`<br/>`docs/codebase-spec/04_Business_Logic/services/gen_service.py.md` | 方法级索引（DAO 调用点/异常文案） |
| `ruoyi-fastapi-backend/module_task/__init__.py` | Backend Other | `docs/codebase-spec/00_Overview/ARCHITECTURE.md` | 后端其余实现细节归入架构说明 |
| `ruoyi-fastapi-backend/module_task/scheduler_test.py` | Backend Other | `docs/codebase-spec/00_Overview/ARCHITECTURE.md` | 后端其余实现细节归入架构说明 |
| `ruoyi-fastapi-backend/requirements-pg.txt` | Backend Other | `docs/codebase-spec/00_Overview/ARCHITECTURE.md` | 后端其余实现细节归入架构说明 |
| `ruoyi-fastapi-backend/requirements.txt` | Backend Other | `docs/codebase-spec/00_Overview/ARCHITECTURE.md` | 后端其余实现细节归入架构说明 |
| `ruoyi-fastapi-backend/ruff.toml` | Backend Other | `docs/codebase-spec/00_Overview/ARCHITECTURE.md` | 后端其余实现细节归入架构说明 |
| `ruoyi-fastapi-backend/server.py` | Backend Entrypoint | `docs/codebase-spec/00_Overview/ARCHITECTURE.md`<br/>`docs/codebase-spec/00_Overview/PROJECT.md` | 后端启动/生命周期/路由注册 |
| `ruoyi-fastapi-backend/sql/ruoyi-fastapi-pg.sql` | DB Init SQL | `docs/codebase-spec/02_Data/ENTITIES.md`<br/>`docs/codebase-spec/02_Data/MIGRATIONS.md` | 全量 schema + 初始数据 |
| `ruoyi-fastapi-backend/sql/ruoyi-fastapi.sql` | DB Init SQL | `docs/codebase-spec/02_Data/ENTITIES.md`<br/>`docs/codebase-spec/02_Data/MIGRATIONS.md` | 全量 schema + 初始数据 |
| `ruoyi-fastapi-backend/sub_applications/handle.py` | Backend SubApps | `docs/codebase-spec/00_Overview/ARCHITECTURE.md` | 子应用挂载 |
| `ruoyi-fastapi-backend/sub_applications/staticfiles.py` | Backend SubApps | `docs/codebase-spec/00_Overview/ARCHITECTURE.md` | 子应用挂载 |
| `ruoyi-fastapi-backend/utils/ai_util.py` | Backend Utils | `docs/codebase-spec/00_Overview/ARCHITECTURE.md`<br/>`docs/codebase-spec/03_API/ERRORS.md`<br/>`docs/codebase-spec/03_API/OPENAPI_SNAPSHOT.md` | 通用工具（日志/响应/导入/安全/文档代理等） |
| `ruoyi-fastapi-backend/utils/common_util.py` | Backend Utils | `docs/codebase-spec/00_Overview/ARCHITECTURE.md`<br/>`docs/codebase-spec/03_API/ERRORS.md`<br/>`docs/codebase-spec/03_API/OPENAPI_SNAPSHOT.md` | 通用工具（日志/响应/导入/安全/文档代理等） |
| `ruoyi-fastapi-backend/utils/cron_util.py` | Backend Utils | `docs/codebase-spec/00_Overview/ARCHITECTURE.md`<br/>`docs/codebase-spec/03_API/ERRORS.md`<br/>`docs/codebase-spec/03_API/OPENAPI_SNAPSHOT.md` | 通用工具（日志/响应/导入/安全/文档代理等） |
| `ruoyi-fastapi-backend/utils/crypto_util.py` | Backend Utils | `docs/codebase-spec/00_Overview/ARCHITECTURE.md`<br/>`docs/codebase-spec/03_API/ERRORS.md`<br/>`docs/codebase-spec/03_API/OPENAPI_SNAPSHOT.md` | 通用工具（日志/响应/导入/安全/文档代理等） |
| `ruoyi-fastapi-backend/utils/dependency_util.py` | Backend Utils | `docs/codebase-spec/00_Overview/ARCHITECTURE.md`<br/>`docs/codebase-spec/03_API/ERRORS.md`<br/>`docs/codebase-spec/03_API/OPENAPI_SNAPSHOT.md` | 通用工具（日志/响应/导入/安全/文档代理等） |
| `ruoyi-fastapi-backend/utils/excel_util.py` | Backend Utils | `docs/codebase-spec/00_Overview/ARCHITECTURE.md`<br/>`docs/codebase-spec/03_API/ERRORS.md`<br/>`docs/codebase-spec/03_API/OPENAPI_SNAPSHOT.md` | 通用工具（日志/响应/导入/安全/文档代理等） |
| `ruoyi-fastapi-backend/utils/gen_util.py` | Backend Utils | `docs/codebase-spec/00_Overview/ARCHITECTURE.md`<br/>`docs/codebase-spec/03_API/ERRORS.md`<br/>`docs/codebase-spec/03_API/OPENAPI_SNAPSHOT.md` | 通用工具（日志/响应/导入/安全/文档代理等） |
| `ruoyi-fastapi-backend/utils/import_util.py` | Backend Utils | `docs/codebase-spec/00_Overview/ARCHITECTURE.md`<br/>`docs/codebase-spec/03_API/ERRORS.md`<br/>`docs/codebase-spec/03_API/OPENAPI_SNAPSHOT.md` | 通用工具（日志/响应/导入/安全/文档代理等） |
| `ruoyi-fastapi-backend/utils/log_util.py` | Backend Utils | `docs/codebase-spec/00_Overview/ARCHITECTURE.md`<br/>`docs/codebase-spec/03_API/ERRORS.md`<br/>`docs/codebase-spec/03_API/OPENAPI_SNAPSHOT.md` | 通用工具（日志/响应/导入/安全/文档代理等） |
| `ruoyi-fastapi-backend/utils/message_util.py` | Backend Utils | `docs/codebase-spec/00_Overview/ARCHITECTURE.md`<br/>`docs/codebase-spec/03_API/ERRORS.md`<br/>`docs/codebase-spec/03_API/OPENAPI_SNAPSHOT.md` | 通用工具（日志/响应/导入/安全/文档代理等） |
| `ruoyi-fastapi-backend/utils/page_util.py` | Backend Utils | `docs/codebase-spec/00_Overview/ARCHITECTURE.md`<br/>`docs/codebase-spec/03_API/ERRORS.md`<br/>`docs/codebase-spec/03_API/OPENAPI_SNAPSHOT.md` | 通用工具（日志/响应/导入/安全/文档代理等） |
| `ruoyi-fastapi-backend/utils/pwd_util.py` | Backend Utils | `docs/codebase-spec/00_Overview/ARCHITECTURE.md`<br/>`docs/codebase-spec/03_API/ERRORS.md`<br/>`docs/codebase-spec/03_API/OPENAPI_SNAPSHOT.md` | 通用工具（日志/响应/导入/安全/文档代理等） |
| `ruoyi-fastapi-backend/utils/response_util.py` | Backend Utils | `docs/codebase-spec/00_Overview/ARCHITECTURE.md`<br/>`docs/codebase-spec/03_API/ERRORS.md`<br/>`docs/codebase-spec/03_API/OPENAPI_SNAPSHOT.md` | 通用工具（日志/响应/导入/安全/文档代理等） |
| `ruoyi-fastapi-backend/utils/server_util.py` | Backend Utils | `docs/codebase-spec/00_Overview/ARCHITECTURE.md`<br/>`docs/codebase-spec/03_API/ERRORS.md`<br/>`docs/codebase-spec/03_API/OPENAPI_SNAPSHOT.md` | 通用工具（日志/响应/导入/安全/文档代理等） |
| `ruoyi-fastapi-backend/utils/string_util.py` | Backend Utils | `docs/codebase-spec/00_Overview/ARCHITECTURE.md`<br/>`docs/codebase-spec/03_API/ERRORS.md`<br/>`docs/codebase-spec/03_API/OPENAPI_SNAPSHOT.md` | 通用工具（日志/响应/导入/安全/文档代理等） |
| `ruoyi-fastapi-backend/utils/template_util.py` | Backend Utils | `docs/codebase-spec/00_Overview/ARCHITECTURE.md`<br/>`docs/codebase-spec/03_API/ERRORS.md`<br/>`docs/codebase-spec/03_API/OPENAPI_SNAPSHOT.md` | 通用工具（日志/响应/导入/安全/文档代理等） |
| `ruoyi-fastapi-backend/utils/time_format_util.py` | Backend Utils | `docs/codebase-spec/00_Overview/ARCHITECTURE.md`<br/>`docs/codebase-spec/03_API/ERRORS.md`<br/>`docs/codebase-spec/03_API/OPENAPI_SNAPSHOT.md` | 通用工具（日志/响应/导入/安全/文档代理等） |
| `ruoyi-fastapi-backend/utils/upload_util.py` | Backend Utils | `docs/codebase-spec/00_Overview/ARCHITECTURE.md`<br/>`docs/codebase-spec/03_API/ERRORS.md`<br/>`docs/codebase-spec/03_API/OPENAPI_SNAPSHOT.md` | 通用工具（日志/响应/导入/安全/文档代理等） |
| `ruoyi-fastapi-frontend/.dockerignore` | Frontend Other | `docs/codebase-spec/07_Infrastructure/DOCKER.md`<br/>`docs/codebase-spec/06_Frontend/OVERVIEW.md` | Docker 构建上下文裁剪（影响镜像产物） |
| `ruoyi-fastapi-frontend/Dockerfile` | Dockerfile | `docs/codebase-spec/07_Infrastructure/DOCKER.md` | 镜像构建说明 |
| `ruoyi-fastapi-frontend/bin/nginx.dockermy.conf` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/bin/nginx.dockerpg.conf` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/package-lock.json` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/package.json` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/public/favicon.ico` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/App.vue` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/api/ai/chat.js` | Frontend API Client | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 前端 API 调用契约由 OpenAPI 驱动 |
| `ruoyi-fastapi-frontend/src/api/ai/model.js` | Frontend API Client | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 前端 API 调用契约由 OpenAPI 驱动 |
| `ruoyi-fastapi-frontend/src/api/login.js` | Frontend API Client | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 前端 API 调用契约由 OpenAPI 驱动 |
| `ruoyi-fastapi-frontend/src/api/menu.js` | Frontend API Client | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 前端 API 调用契约由 OpenAPI 驱动 |
| `ruoyi-fastapi-frontend/src/api/monitor/cache.js` | Frontend API Client | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 前端 API 调用契约由 OpenAPI 驱动 |
| `ruoyi-fastapi-frontend/src/api/monitor/job.js` | Frontend API Client | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 前端 API 调用契约由 OpenAPI 驱动 |
| `ruoyi-fastapi-frontend/src/api/monitor/jobLog.js` | Frontend API Client | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 前端 API 调用契约由 OpenAPI 驱动 |
| `ruoyi-fastapi-frontend/src/api/monitor/logininfor.js` | Frontend API Client | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 前端 API 调用契约由 OpenAPI 驱动 |
| `ruoyi-fastapi-frontend/src/api/monitor/online.js` | Frontend API Client | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 前端 API 调用契约由 OpenAPI 驱动 |
| `ruoyi-fastapi-frontend/src/api/monitor/operlog.js` | Frontend API Client | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 前端 API 调用契约由 OpenAPI 驱动 |
| `ruoyi-fastapi-frontend/src/api/monitor/server.js` | Frontend API Client | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 前端 API 调用契约由 OpenAPI 驱动 |
| `ruoyi-fastapi-frontend/src/api/system/config.js` | Frontend API Client | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 前端 API 调用契约由 OpenAPI 驱动 |
| `ruoyi-fastapi-frontend/src/api/system/dept.js` | Frontend API Client | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 前端 API 调用契约由 OpenAPI 驱动 |
| `ruoyi-fastapi-frontend/src/api/system/dict/data.js` | Frontend API Client | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 前端 API 调用契约由 OpenAPI 驱动 |
| `ruoyi-fastapi-frontend/src/api/system/dict/type.js` | Frontend API Client | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 前端 API 调用契约由 OpenAPI 驱动 |
| `ruoyi-fastapi-frontend/src/api/system/menu.js` | Frontend API Client | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 前端 API 调用契约由 OpenAPI 驱动 |
| `ruoyi-fastapi-frontend/src/api/system/notice.js` | Frontend API Client | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 前端 API 调用契约由 OpenAPI 驱动 |
| `ruoyi-fastapi-frontend/src/api/system/post.js` | Frontend API Client | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 前端 API 调用契约由 OpenAPI 驱动 |
| `ruoyi-fastapi-frontend/src/api/system/role.js` | Frontend API Client | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 前端 API 调用契约由 OpenAPI 驱动 |
| `ruoyi-fastapi-frontend/src/api/system/user.js` | Frontend API Client | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 前端 API 调用契约由 OpenAPI 驱动 |
| `ruoyi-fastapi-frontend/src/api/tool/gen.js` | Frontend API Client | `docs/codebase-spec/03_API/openapi.json`<br/>`docs/codebase-spec/03_API/OPERATION_MAP.md` | 前端 API 调用契约由 OpenAPI 驱动 |
| `ruoyi-fastapi-frontend/src/assets/401_images/401.gif` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/404_images/404.png` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/404_images/404_cloud.png` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/404.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/ai-chat.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/ai-manage.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/ai-model.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/bug.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/build.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/button.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/cascader.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/chart.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/checkbox.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/clipboard.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/code.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/color.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/component.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/dashboard.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/date-range.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/date.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/deepthink.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/dict.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/documentation.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/download.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/drag.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/druid.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/edit.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/education.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/email.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/enter.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/example.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/excel.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/exit-fullscreen.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/eye-open.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/eye.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/form.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/fullscreen.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/github.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/guide.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/icon.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/input.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/international.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/job.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/language.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/link.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/list.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/lock.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/log.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/logininfor.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/message.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/money.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/monitor.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/moon.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/more-up.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/nested.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/number.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/online.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/password.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/pdf.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/people.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/peoples.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/phone.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/post.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/qq.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/question.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/radio.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/rate.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/redis-list.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/redis.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/row.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/search.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/select.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/server.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/shopping.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/size.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/skill.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/slider.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/star.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/sunny.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/swagger.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/switch.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/system.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/tab.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/table.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/textarea.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/theme.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/time-range.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/time.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/tool.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/tree-table.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/tree.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/upload.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/user.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/validCode.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/wechat.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/icons/svg/zip.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/images/dark.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/images/light.svg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/images/login-background.jpg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/images/profile.jpg` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/assets/logo/logo.png` | Frontend Assets | `docs/ui-ux-spec/06_Assets/ASSETS.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI 资产（图标/图片/字体等） |
| `ruoyi-fastapi-frontend/src/components/Breadcrumb/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/components/Crontab/day.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/components/Crontab/hour.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/components/Crontab/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/components/Crontab/min.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/components/Crontab/result.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/components/Crontab/week.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/components/DictTag/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/components/Editor/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/components/FileUpload/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/components/Hamburger/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/components/HeaderSearch/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/components/IconSelect/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/components/IconSelect/requireIcons.js` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/components/ImagePreview/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/components/Pagination/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/components/ParentView/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/components/RuoYi/Doc/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/components/RuoYi/Git/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/components/Screenfull/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/components/SizeSelect/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/components/SvgIcon/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/components/SvgIcon/svgicon.js` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/components/TopNav/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/components/iFrame/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/directive/common/copyText.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/directive/index.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/directive/permission/hasPermi.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/directive/permission/hasRole.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/layout/components/AppMain.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/layout/components/Copyright/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/layout/components/IframeToggle/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/layout/components/InnerLink/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/layout/components/Navbar.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/layout/components/Settings/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Link.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Logo.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/layout/components/TagsView/ScrollPane.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/layout/components/index.js` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/layout/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/main.js` | Frontend Entrypoint | `docs/codebase-spec/06_Frontend/OVERVIEW.md` | 工程入口与构建 |
| `ruoyi-fastapi-frontend/src/permission.js` | Frontend Router Guard | `docs/codebase-spec/06_Frontend/PERMISSION_AND_ROUTING.md` | 路由守卫 |
| `ruoyi-fastapi-frontend/src/plugins/auth.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/plugins/cache.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/plugins/download.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/plugins/index.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/plugins/modal.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/plugins/tab.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/router/index.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/settings.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/store/index.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/store/modules/app.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/store/modules/dict.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/store/modules/permission.js` | Frontend Dynamic Routes | `docs/codebase-spec/06_Frontend/PERMISSION_AND_ROUTING.md` | 动态路由生成 |
| `ruoyi-fastapi-frontend/src/store/modules/settings.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/store/modules/tagsView.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/store/modules/user.js` | Frontend User Store | `docs/codebase-spec/06_Frontend/AUTH_AND_REQUEST.md` | 登录态/用户信息 |
| `ruoyi-fastapi-frontend/src/utils/auth.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/utils/dict.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/utils/dynamicTitle.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/utils/errorCode.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/utils/generator/config.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/utils/generator/css.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/utils/generator/drawingDefault.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/utils/generator/html.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/utils/generator/icon.json` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/utils/generator/js.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/utils/generator/render.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/utils/index.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/utils/jsencrypt.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/utils/permission.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/utils/request.js` | Frontend Request | `docs/codebase-spec/06_Frontend/AUTH_AND_REQUEST.md` | axios 拦截器/业务 code |
| `ruoyi-fastapi-frontend/src/utils/ruoyi.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/utils/scroll-to.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/utils/theme.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/utils/validate.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/src/views/ai/chat/components/AiMessage.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/ai/chat/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/ai/model/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/dashboard/editable-link-group.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/dashboard/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/error/401.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/error/404.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/login.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/monitor/cache/list.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/monitor/druid/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/monitor/job/log.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/monitor/logininfor/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/monitor/operlog/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/monitor/server/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/redirect/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/register.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/system/config/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/system/dept/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/system/dict/data.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/system/dict/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/system/menu/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/system/notice/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/system/post/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/system/role/authUser.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/system/role/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/system/user/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/system/user/profile/resetPwd.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/system/user/profile/userAvatar.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/system/user/profile/userInfo.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/tool/gen/basicInfoForm.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/tool/gen/createTable.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/tool/gen/editTable.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/tool/gen/genInfoForm.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/tool/gen/importTable.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/tool/gen/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/src/views/tool/swagger/index.vue` | Frontend UI | `docs/ui-ux-spec/02_Components/COMPONENTS.md`<br/>`docs/ui-ux-spec/04_Pages/PAGES.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | UI-only 规格覆盖 |
| `ruoyi-fastapi-frontend/vite.config.js` | Frontend Entrypoint | `docs/codebase-spec/06_Frontend/OVERVIEW.md` | 工程入口与构建 |
| `ruoyi-fastapi-frontend/vite/plugins/auto-import.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/vite/plugins/compression.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/vite/plugins/index.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/vite/plugins/setup-extend.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-frontend/vite/plugins/svg-icon.js` | Frontend Other | `docs/codebase-spec/06_Frontend/OVERVIEW.md`<br/>`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` | 其余前端实现归入工程概览/扫描 |
| `ruoyi-fastapi-test/README.md` | E2E Other | `docs/codebase-spec/08_Testing/E2E_SPECS.md` | 测试套件 |
| `ruoyi-fastapi-test/conftest.py` | E2E Other | `docs/codebase-spec/08_Testing/E2E_SPECS.md` | pytest 全局夹具/配置（E2E/视觉基线共用） |
| `ruoyi-fastapi-test/common/__init__.py` | E2E Tests | `docs/codebase-spec/08_Testing/E2E_SPECS.md` | pytest + Playwright E2E |
| `ruoyi-fastapi-test/common/base_page_test.py` | E2E Tests | `docs/codebase-spec/08_Testing/E2E_SPECS.md` | pytest + Playwright E2E |
| `ruoyi-fastapi-test/common/config.py` | E2E Tests | `docs/codebase-spec/08_Testing/E2E_SPECS.md` | pytest + Playwright E2E |
| `ruoyi-fastapi-test/common/login_helper.py` | E2E Tests | `docs/codebase-spec/08_Testing/E2E_SPECS.md` | pytest + Playwright E2E |
| `ruoyi-fastapi-test/disable_captcha.sql` | E2E Test SQL | `docs/codebase-spec/08_Testing/E2E_SPECS.md` | E2E 预置 SQL |
| `ruoyi-fastapi-test/docker-compose.test.my.yml` | Docker/Compose | `docs/codebase-spec/07_Infrastructure/DOCKER.md`<br/>`docs/codebase-spec/08_Testing/E2E_SPECS.md` | 环境与测试编排 |
| `ruoyi-fastapi-test/docker-compose.test.pg.yml` | Docker/Compose | `docs/codebase-spec/07_Infrastructure/DOCKER.md`<br/>`docs/codebase-spec/08_Testing/E2E_SPECS.md` | 环境与测试编排 |
| `ruoyi-fastapi-test/monitor/__init__.py` | E2E Tests | `docs/codebase-spec/08_Testing/E2E_SPECS.md` | pytest + Playwright E2E |
| `ruoyi-fastapi-test/monitor/test_cache_list.py` | E2E Tests | `docs/codebase-spec/08_Testing/E2E_SPECS.md` | pytest + Playwright E2E |
| `ruoyi-fastapi-test/monitor/test_cache_monitor.py` | E2E Tests | `docs/codebase-spec/08_Testing/E2E_SPECS.md` | pytest + Playwright E2E |
| `ruoyi-fastapi-test/monitor/test_job_management.py` | E2E Tests | `docs/codebase-spec/08_Testing/E2E_SPECS.md` | pytest + Playwright E2E |
| `ruoyi-fastapi-test/monitor/test_online_user.py` | E2E Tests | `docs/codebase-spec/08_Testing/E2E_SPECS.md` | pytest + Playwright E2E |
| `ruoyi-fastapi-test/monitor/test_server_monitor.py` | E2E Tests | `docs/codebase-spec/08_Testing/E2E_SPECS.md` | pytest + Playwright E2E |
| `ruoyi-fastapi-test/requirements.txt` | E2E Other | `docs/codebase-spec/08_Testing/E2E_SPECS.md` | 测试套件 |
| `ruoyi-fastapi-test/ruff.toml` | E2E Tests | `docs/codebase-spec/08_Testing/E2E_SPECS.md` | pytest + Playwright E2E |
| `ruoyi-fastapi-test/system/__init__.py` | E2E Tests | `docs/codebase-spec/08_Testing/E2E_SPECS.md` | pytest + Playwright E2E |
| `ruoyi-fastapi-test/system/test_config_management.py` | E2E Tests | `docs/codebase-spec/08_Testing/E2E_SPECS.md` | pytest + Playwright E2E |
| `ruoyi-fastapi-test/system/test_dept_management.py` | E2E Tests | `docs/codebase-spec/08_Testing/E2E_SPECS.md` | pytest + Playwright E2E |
| `ruoyi-fastapi-test/system/test_dict_management.py` | E2E Tests | `docs/codebase-spec/08_Testing/E2E_SPECS.md` | pytest + Playwright E2E |
| `ruoyi-fastapi-test/system/test_log_management.py` | E2E Tests | `docs/codebase-spec/08_Testing/E2E_SPECS.md` | pytest + Playwright E2E |
| `ruoyi-fastapi-test/system/test_menu_management.py` | E2E Tests | `docs/codebase-spec/08_Testing/E2E_SPECS.md` | pytest + Playwright E2E |
| `ruoyi-fastapi-test/system/test_notice_management.py` | E2E Tests | `docs/codebase-spec/08_Testing/E2E_SPECS.md` | pytest + Playwright E2E |
| `ruoyi-fastapi-test/system/test_post_management.py` | E2E Tests | `docs/codebase-spec/08_Testing/E2E_SPECS.md` | pytest + Playwright E2E |
| `ruoyi-fastapi-test/system/test_role_management.py` | E2E Tests | `docs/codebase-spec/08_Testing/E2E_SPECS.md` | pytest + Playwright E2E |
| `ruoyi-fastapi-test/system/test_user_management.py` | E2E Tests | `docs/codebase-spec/08_Testing/E2E_SPECS.md` | pytest + Playwright E2E |
| `ruoyi-fastapi-test/test_login.py` | E2E Tests | `docs/codebase-spec/08_Testing/E2E_SPECS.md` | pytest + Playwright E2E |
| `ruoyi-fastapi-test/test_pages.py` | E2E Tests | `docs/codebase-spec/08_Testing/E2E_SPECS.md` | pytest + Playwright E2E |
| `ruoyi-fastapi-test/tool/__init__.py` | E2E Tests | `docs/codebase-spec/08_Testing/E2E_SPECS.md` | pytest + Playwright E2E |
| `ruoyi-fastapi-test/tool/test_code_gen.py` | E2E Tests | `docs/codebase-spec/08_Testing/E2E_SPECS.md` | pytest + Playwright E2E |
| `ruoyi-fastapi-test/tool/test_swagger.py` | E2E Tests | `docs/codebase-spec/08_Testing/E2E_SPECS.md` | pytest + Playwright E2E |
| `ruoyi-fastapi-test/visual/test_visual_baseline.py` | E2E Tests | `docs/codebase-spec/08_Testing/E2E_SPECS.md`<br/>`docs/ui-ux-spec/08_Visual_Baseline/README.md` | 像素级视觉基线（可复跑 diff） |
| `tools/spec/gen_handler_map.py` | Tooling | `docs/codebase-spec/03_API/HANDLER_MAP.md` | 规格生成工具：静态生成 endpoint → controller → service 映射 |
