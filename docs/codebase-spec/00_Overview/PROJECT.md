# Project Overview（项目概览）

## 1) 身份信息（Identity）

- Name：`RuoYi-Vue3-FastAPI`（Fork & 二次开发）
- Upstream：开源项目 RuoYi-Vue3-FastAPI（原始说明见 `README.md.bak`）
- 当前前端版本号（package.json）：`ruoyi-fastapi-frontend@1.8.1`
- 后端运行端口默认值：`9099`（见 `APP_PORT`）
- 协作约定：`AGENTS.md`

> 本仓库的目标：基于上游快速开发框架，构建我方系统的管理后台与集成前端，并保证可回归、可同步上游、可复现交付。

---

## 2) 技术栈（Tech Stack）

### 后端（FastAPI）

- Runtime：Python（CI 覆盖 3.10 ~ 3.13；本地建议 3.10+）
- Web：FastAPI + Uvicorn
- ORM：SQLAlchemy（Async）
- DB：MySQL / PostgreSQL（两套初始化脚本）
- Cache：Redis（async 客户端）
- Auth：OAuth2 Password Flow + JWT
- Scheduler：APScheduler（AsyncIOScheduler；jobstore 支持 memory/sqlalchemy/redis）
- Lint/Format：ruff（见 `.github/workflows/ruff.yml`）

### PC 管理后台前端（Vue3）

- Runtime：Node.js（建议 18+）
- Framework：Vue 3 + Vue Router + Pinia
- UI：Element Plus（并通过 CSS 变量做暗黑模式与主题色适配）
- Build：Vite

### E2E 测试

- pytest + pytest-asyncio + pytest-playwright（见 `ruoyi-fastapi-test/`）
- CI：GitHub Actions + Docker Compose 拉起前后端与数据库（见 `.github/workflows/playwright.yml`）

---

## 3) 仓库目录结构（Top-level）

```text
.
├── ruoyi-fastapi-backend/     # FastAPI 后端（含 SQL 初始化脚本与 Dockerfile）
├── ruoyi-fastapi-frontend/    # Vue3 管理后台（Vite）
├── ruoyi-fastapi-app/         # uni-app（可选；移动端）
├── ruoyi-fastapi-test/        # pytest + Playwright E2E 测试套件
├── docker-compose.my.yml      # MySQL 版本 Docker Compose
├── docker-compose.pg.yml      # PostgreSQL 版本 Docker Compose
└── docs/                      # 合规文档、worklog、spec、UI/UX spec 等
```

---

## 4) 启动与运行（Build & Run）

> 运行前请先阅读：`docs/codebase-spec/01_Configuration/ENVIRONMENT.md`（环境变量联动：`VITE_APP_BASE_API` ↔ `APP_ROOT_PATH`）。

### 4.1 后端（本地开发）

```bash
cd ruoyi-fastapi-backend

# MySQL
pip install -r requirements.txt

# 或 PostgreSQL
# pip install -r requirements-pg.txt

# 初始化数据库：执行 sql/ 目录脚本（MySQL / PostgreSQL 二选一）
# 运行后端（会加载 .env.dev）
python app.py --env=dev
```

### 4.2 前端（本地开发）

```bash
cd ruoyi-fastapi-frontend
npm install
npm run dev
```

### 4.3 Docker Compose（建议用于快速一致性验证）

```bash
# MySQL 版本
docker compose -f docker-compose.my.yml up -d --build

# PostgreSQL 版本
docker compose -f docker-compose.pg.yml up -d --build
```

---

## 5) 测试（Test）

### 5.1 离线回归（最小门禁）

```bash
ruff check ruoyi-fastapi-backend
ruff check ruoyi-fastapi-test
ruff format ruoyi-fastapi-backend --check
ruff format ruoyi-fastapi-test --check

cd ruoyi-fastapi-frontend
npm run build:prod
```

### 5.2 E2E（pytest + Playwright）

参考：`ruoyi-fastapi-test/README.md` 与 `.github/workflows/playwright.yml`。

---

## 6) 环境要求（Environment Requirements）

- Python：建议 3.10+（CI 覆盖 3.10 ~ 3.13）
- Node.js：建议 18+（上游文档要求 node ≥ 18）
- DB：MySQL 8.0 / PostgreSQL 14（docker-compose 默认）
- Redis：最新版镜像可用（docker-compose 默认）
- 关键环境变量：见 `docs/codebase-spec/01_Configuration/ENVIRONMENT.md`
