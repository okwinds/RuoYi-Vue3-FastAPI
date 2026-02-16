# 已知缺口（Known Gaps）

本文件用于显式记录“当前规格文档尚未覆盖/不准备覆盖”的部分，并给出优先级，避免后续复刻或重构时踩坑。

---

## 1) 有意不覆盖（Intentionally Omitted）

| Area | Gap | Priority | Notes |
|------|-----|----------|-------|
| UI 业务规则 | 不在 `docs/ui-ux-spec/` 中描述具体业务流程/接口含义 | H | UI/UX spec 仅覆盖 UI 结构/样式/组件模式，业务契约在 codebase spec 中维护 |

---

## 2) 已补齐（Resolved）

| Area | Status | Evidence |
|------|--------|----------|
| API Schema（字段级） | Done | `docs/codebase-spec/03_API/openapi.json` + `OPENAPI_SNAPSHOT.md` + `OPERATION_MAP.md` |
| Service/DAO（方法级目录/耦合点） | Done | `docs/codebase-spec/04_Business_Logic/IMPLEMENTATION_INDEX.md` + `04_Business_Logic/services/` + `04_Business_Logic/daos/` |
| Mobile App（路由/鉴权/请求/页面） | Done | `docs/codebase-spec/05_Mobile_App/ROUTING.md`、`AUTH_AND_REQUEST.md`、`STORE.md`、`PAGES.md` |
| 前端 i18n/文案现状 | Done | `docs/codebase-spec/06_Frontend/I18N_AND_COPY.md` |

---

## 3) 已确认结论（Clarified）

| Area | Conclusion | Evidence |
|------|------------|----------|
| HTTP status vs 业务 `code` | 业务成功/失败主要使用 JSON `code`；统一响应工具（ResponseUtil）返回 HTTP 200；少量 `HTTPException` 会保留 HTTP status | `ruoyi-fastapi-backend/utils/response_util.py`、`ruoyi-fastapi-backend/exceptions/handle.py`、`ruoyi-fastapi-frontend/src/utils/request.js` |
| 迁移策略（SQL init / create_all / Alembic） | SQL init 负责全量 schema+初始数据；`create_all` 保底；Alembic 为可选正式迁移工具 | `docs/codebase-spec/02_Data/MIGRATIONS.md`、`ruoyi-fastapi-backend/alembic/env.py` |

---

## 4) 技术债/历史包袱（Technical Debt）

- E2E 端口默认占用 `80`，在本地开发环境可能与其它服务冲突；建议提供可配置端口（或在文档中给出替代方案）。
- Playwright CI 中会临时替换 `ruoyi-fastapi-backend/Dockerfile.my` 的 Python 版本（并在最后恢复）；此行为在本地复现时需注意（见 `.github/workflows/playwright.yml`）。
