# Docker 与容器化（Infrastructure / Docker）

本仓库提供两类 Docker Compose：

1) **运行环境 compose（顶层）**：用于快速拉起“可用的前后端 + DB + Redis”。  
2) **测试环境 compose（ruoyi-fastapi-test）**：用于 E2E（额外挂载 `disable_captcha.sql`）。

---

## 1) 顶层 Compose（运行环境）

### 1.1 MySQL 版本

文件：`docker-compose.my.yml`

- 前端 `ruoyi-frontend`
  - Nginx 容器，端口映射：`12580:80`
  - 挂载配置：`ruoyi-fastapi-frontend/bin/nginx.dockermy.conf` → `/etc/nginx/conf.d/default.conf`
- 后端 `ruoyi-backend-my`
  - 端口映射：`19099:9099`
  - 镜像来自 `ruoyi-fastapi-backend/Dockerfile.my`
  - 启动参数：`python app.py --env=dockermy`
- MySQL `ruoyi-mysql`
  - 端口映射：`13306:3306`
  - 初始化脚本挂载：`ruoyi-fastapi-backend/sql/ruoyi-fastapi.sql`
- Redis `ruoyi-redis`
  - 端口映射：`16379:6379`

### 1.2 PostgreSQL 版本

文件：`docker-compose.pg.yml`

差异点：
- 后端镜像来自 `ruoyi-fastapi-backend/Dockerfile.pg`，启动 `--env=dockerpg`
- DB 使用 `postgres:14`，端口映射：`15432:5432`
- 初始化脚本挂载：`ruoyi-fastapi-backend/sql/ruoyi-fastapi-pg.sql`

---

## 2) ruoyi-fastapi-frontend 的 Dockerfile（前端）

文件：`ruoyi-fastapi-frontend/Dockerfile`

- 构建阶段：
  - `node:18-slim`
  - `npm install` + `npm run build:docker`（产生 `dist/`）
- 运行阶段：
  - `nginx:latest`
  - 将 `dist/` 拷贝到 `/usr/share/nginx/html`

---

## 3) ruoyi-fastapi-backend 的 Dockerfile（后端）

- `ruoyi-fastapi-backend/Dockerfile.my`：安装 `requirements.txt`，启动 `--env=dockermy`
- `ruoyi-fastapi-backend/Dockerfile.pg`：安装 `requirements-pg.txt`，启动 `--env=dockerpg`

> 注意：CI 的 Playwright 流水线会临时替换 `Dockerfile.my` 的 `FROM python:3.10` 为矩阵版本（3.10~3.13），并在 job 结束时恢复（见 `.github/workflows/playwright.yml`）。

