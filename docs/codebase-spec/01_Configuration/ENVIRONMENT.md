# Environment Variables（环境变量）

本文件汇总 **后端（FastAPI）** 与 **前端（Vite/Vue3）** 的环境变量与其语义，目标是让项目可复现部署/运行。

说明：
- 后端通过 `ruoyi-fastapi-backend/config/env.py` 读取变量，并在启动时加载 `ruoyi-fastapi-backend/.env.<env>`（参见 `GetConfig.parse_cli_args()`）。
- 前端通过 Vite 的 `import.meta.env` 读取以 `VITE_` 开头的变量（配置文件位于 `ruoyi-fastapi-frontend/.env.*`）。
- **不要在仓库中提交真实密钥**；如需生产密钥，请通过部署平台注入。

---

## 1) 后端环境变量（ruoyi-fastapi-backend）

来源：`ruoyi-fastapi-backend/config/env.py` 与 `ruoyi-fastapi-backend/.env.*`。

### 应用（App）

| 变量 | 类型 | 默认值（env.py） | 说明（.env.dev 注释） | 配置文件 |
| --- | --- | --- | --- | --- |
| APP_DISABLE_REDOC | bool | false | 应用是否禁用ReDoc文档 | ruoyi-fastapi-backend/.env.* |
| APP_DISABLE_SWAGGER | bool | false | 应用是否禁用Swagger文档 | ruoyi-fastapi-backend/.env.* |
| APP_ENV | str | dev | 应用运行环境 | ruoyi-fastapi-backend/.env.* |
| APP_HOST | str | 0.0.0.0 | 应用主机 | ruoyi-fastapi-backend/.env.* |
| APP_IP_LOCATION_QUERY | bool | true | 应用是否开启IP归属区域查询 | ruoyi-fastapi-backend/.env.* |
| APP_NAME | str | RuoYi-FasAPI | 应用名称 | ruoyi-fastapi-backend/.env.* |
| APP_PORT | int | 9099 | 应用端口 | ruoyi-fastapi-backend/.env.* |
| APP_RELOAD | bool | true | 应用是否开启热重载 | ruoyi-fastapi-backend/.env.* |
| APP_ROOT_PATH | str | /dev-api | 应用代理路径 | ruoyi-fastapi-backend/.env.* |
| APP_SAME_TIME_LOGIN | bool | true | 应用是否允许账号同时登录 | ruoyi-fastapi-backend/.env.* |
| APP_VERSION | str | 1.0.0 | 应用版本 | ruoyi-fastapi-backend/.env.* |

### 鉴权（JWT）

| 变量 | 类型 | 默认值（env.py） | 说明（.env.dev 注释） | 配置文件 |
| --- | --- | --- | --- | --- |
| JWT_ALGORITHM | str | HS256 | Jwt算法 | ruoyi-fastapi-backend/.env.* |
| JWT_EXPIRE_MINUTES | int | 1440 | 令牌过期时间 | ruoyi-fastapi-backend/.env.* |
| JWT_REDIS_EXPIRE_MINUTES | int | 30 | redis中令牌过期时间 | ruoyi-fastapi-backend/.env.* |
| JWT_SECRET_KEY | str | b01c66dc2c58… | Jwt秘钥 | ruoyi-fastapi-backend/.env.* |

### 数据库（DB）

| 变量 | 类型 | 默认值（env.py） | 说明（.env.dev 注释） | 配置文件 |
| --- | --- | --- | --- | --- |
| DB_DATABASE | str | ruoyi-fastapi | 数据库名称 | ruoyi-fastapi-backend/.env.* |
| DB_ECHO | bool | true | 是否开启sqlalchemy日志 | ruoyi-fastapi-backend/.env.* |
| DB_HOST | str | 127.0.0.1 | 数据库主机 | ruoyi-fastapi-backend/.env.* |
| DB_MAX_OVERFLOW | int | 10 | 允许溢出连接池大小的最大连接数 | ruoyi-fastapi-backend/.env.* |
| DB_PASSWORD | str | mysqlroot | 数据库密码 | ruoyi-fastapi-backend/.env.* |
| DB_POOL_RECYCLE | int | 3600 | 连接回收时间（单位：秒） | ruoyi-fastapi-backend/.env.* |
| DB_POOL_SIZE | int | 50 | 连接池大小，0表示连接数无限制 | ruoyi-fastapi-backend/.env.* |
| DB_POOL_TIMEOUT | int | 30 | 连接池中没有线程可用时，最多等待的时间（单位：秒） | ruoyi-fastapi-backend/.env.* |
| DB_PORT | int | 3306 | 数据库端口 | ruoyi-fastapi-backend/.env.* |
| DB_TYPE | Literal['mysql', 'postgresql'] | mysql | 数据库类型，可选的有'mysql'、'postgresql'，默认为'mysql' | ruoyi-fastapi-backend/.env.* |
| DB_USERNAME | str | root | 数据库用户名 | ruoyi-fastapi-backend/.env.* |

### 缓存（Redis）

| 变量 | 类型 | 默认值（env.py） | 说明（.env.dev 注释） | 配置文件 |
| --- | --- | --- | --- | --- |
| REDIS_DATABASE | int | 2 | Redis数据库 | ruoyi-fastapi-backend/.env.* |
| REDIS_HOST | str | 127.0.0.1 | Redis主机 | ruoyi-fastapi-backend/.env.* |
| REDIS_PASSWORD | str |  | Redis密码 | ruoyi-fastapi-backend/.env.* |
| REDIS_PORT | int | 6379 | Redis端口 | ruoyi-fastapi-backend/.env.* |
| REDIS_USERNAME | str |  | Redis用户名 | ruoyi-fastapi-backend/.env.* |

---

## 2) 前端环境变量（ruoyi-fastapi-frontend）

来源：`ruoyi-fastapi-frontend/.env.*`。

| 变量 | 类型 | 说明 | 配置文件 |
| --- | --- | --- | --- |
| VITE_APP_BASE_API | string | vfadmin管理系统/开发环境 | ruoyi-fastapi-frontend/.env.development, .env.docker, .env.production, .env.staging |
| VITE_APP_ENV | string | 开发环境配置 | ruoyi-fastapi-frontend/.env.development, .env.docker, .env.production, .env.staging |
| VITE_APP_TITLE | string | 页面标题 | ruoyi-fastapi-frontend/.env.development, .env.docker, .env.production, .env.staging |
| VITE_BUILD_COMPRESS | string | 是否在打包时开启压缩，支持 gzip 和 brotli | ruoyi-fastapi-frontend/.env.docker, .env.production, .env.staging |

---

## 3) 关键联动关系（必须一致）

- **前端 `VITE_APP_BASE_API`** 与 **后端 `APP_ROOT_PATH`** 需要在同一环境中保持一致（例如开发：`/dev-api`，生产：`/prod-api`，Docker：`/docker-api`）。
- E2E 测试（`ruoyi-fastapi-test/`）默认通过 Docker Compose 拉起服务，并在容器内使用固定端口（见 `ruoyi-fastapi-test/README.md` 与 `.github/workflows/playwright.yml`）。

---

## 4) 移动端配置（ruoyi-fastapi-app）

移动端未使用 `.env.*` 作为主要配置来源，而是通过 `ruoyi-fastapi-app/src/config.js` 固化运行时配置：
- `baseUrl`：默认 `http://localhost:9099`（与后端 `APP_PORT` 对齐）

复刻注意：
- 若后端通过反向代理暴露并启用了根路径前缀（类似 `APP_ROOT_PATH=/dev-api`），移动端也需要同步拼接前缀；否则移动端会请求到错误路径。
