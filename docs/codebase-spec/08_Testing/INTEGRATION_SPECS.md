# 集成测试规格（Integration Specs）

本仓库的“集成测试”主要面向：**后端（FastAPI） ↔ DB/Redis ↔ 前端（Vue3）** 的联动验证。

现实约束：
- 上游更偏向提供 E2E 套件（`ruoyi-fastapi-test/`），集成验证多以 Docker Compose + pytest 的方式落地。
- 因此本文档以“**集成验证清单 + 推荐落地方式**”为主，优先复用 E2E 工程能力。

---

## 1) 集成验证目标（What to verify）

### 1.1 启动链路（Backend Lifespan）

验证点（至少）：
- 后端能在指定 env 下成功启动（`python app.py --env=dev|dockermy|dockerpg`）。
- DB 连接成功，并完成必要的初始化（SQL 初始化脚本已导入；或启动时 create_all 不报错）。
- Redis 连接池可用（用于在线 token、缓存等）。
- 字典/参数缓存预热（若实现存在预热步骤，应验证启动后接口读取正常）。
- 调度器（APScheduler）初始化不阻塞启动（jobs 加载正常）。

推荐验证方式：
- Docker Compose 拉起后，通过 HTTP 探针验证：`GET /captchaImage`（CI 里也使用该探针判断服务就绪）。

### 1.2 鉴权链路（Token ↔ Redis）

验证点（至少）：
- 登录成功后返回 token（见 `ruoyi-fastapi-test/common/login_helper.py` 的判定逻辑）。
- token 能被前端识别并作为 cookie `Admin-Token` 使用（E2E 覆盖）。
- “同账号多端登录策略”生效：
  - `APP_SAME_TIME_LOGIN=true/false` 两种模式下，旧 token 的失效/踢出策略正确。

### 1.3 Swagger/接口文档开关

验证点：
- 生产环境禁用 Swagger（`APP_ENABLE_ACCESS_DOC=false`）时，相关路由不可访问或被拒绝。
- 开发环境启用时，Swagger UI 可访问且能调试接口。

推荐验证方式：
- 复用 `ruoyi-fastapi-test/tool/test_swagger.py`（见 E2E 规格）。

### 1.4 代码生成器（Generator）

验证点：
- “导入表 → 预览/生成” 关键路径可用（至少验证生成接口可达、返回结构正常）。
- 生成后的文件内容/zip 下载行为正确。

推荐验证方式：
- 复用 `ruoyi-fastapi-test/tool/test_code_gen.py`（见 E2E 规格）。

---

## 2) 推荐落地方式（How to run）

### 2.1 本地手动启动（开发态）

1) 启动后端：`ruoyi-fastapi-backend/` 下 `python app.py --env=dev`  
2) 启动前端：`ruoyi-fastapi-frontend/` 下 `npm run dev`  
3) 运行测试：`ruoyi-fastapi-test/` 下执行 `pytest -v`

### 2.2 Docker Compose（更接近 CI / 更一致）

在 `ruoyi-fastapi-test/` 下：

- MySQL：`docker compose -f docker-compose.test.my.yml up -d --build`
- PostgreSQL：`docker compose -f docker-compose.test.pg.yml up -d --build`
- 运行：`pytest -v`
- 清理：`docker compose -f <compose> down`

> 注意：E2E compose 默认占用端口 `80`（前端）与 `9099`（后端）。
