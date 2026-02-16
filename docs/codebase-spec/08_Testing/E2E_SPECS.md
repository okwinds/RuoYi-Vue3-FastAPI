# E2E 测试规格（pytest + Playwright）

E2E 套件位于：`ruoyi-fastapi-test/`。它是当前仓库最重要的“可回归护栏”，覆盖：
- 登录/鉴权（包含“未登录访问受保护页面”的重定向行为）
- 管理后台关键页面可访问性
- 监控类页面（缓存/在线用户/定时任务/服务监控）
- 工具页（代码生成、Swagger 接口页）

---

## 1) 测试环境与前置条件

### 1.1 端口与 URL 约定

默认配置写在：`ruoyi-fastapi-test/common/config.py`：
- Frontend：`http://localhost:80`
- Backend：`http://localhost:9099`

### 1.2 测试账户

测试默认使用管理员账号（上游初始化 SQL 自带）：
- 用户名：`admin`
- 密码：`admin123`

### 1.3 验证码禁用（测试环境）

E2E Docker Compose 会额外执行：`ruoyi-fastapi-test/disable_captcha.sql`。  
其目的是让登录流程可在 CI 中稳定跑通（无需人工识别验证码）。

---

## 2) 如何运行（Runbook）

权威入口：`ruoyi-fastapi-test/README.md`。

### 2.1 手动启动前后端 + 本地跑 pytest

```bash
cd ruoyi-fastapi-frontend
npm install
npm run dev

cd ../ruoyi-fastapi-backend
pip install -r requirements.txt
python app.py --env=dev

cd ../ruoyi-fastapi-test
pip install -r requirements.txt
playwright install
pytest -v
```

### 2.2 Docker Compose 一键环境（推荐复现 CI）

```bash
cd ruoyi-fastapi-test

# MySQL
docker compose -f docker-compose.test.my.yml up -d --build
pytest -v
docker compose -f docker-compose.test.my.yml down

# PostgreSQL
docker compose -f docker-compose.test.pg.yml up -d --build
pytest -v
docker compose -f docker-compose.test.pg.yml down
```

---

## 3) 覆盖范围（Test Inventory）

> 以下清单用于“规格级追踪”，不要求逐行对齐源码；但需要保证：每个关键旅程都存在可回归护栏。

### 3.1 登录/鉴权

- `ruoyi-fastapi-test/test_login.py`
  - 登录页可加载（存在账号/密码输入框）
  - 禁用验证码条件下可登录（API + Playwright UI 两种路径）
  - 未登录访问受保护路由会被重定向到登录页
  - 已登录（写入 `Admin-Token` cookie）可访问受保护页面

### 3.2 关键页面可达

- `ruoyi-fastapi-test/test_pages.py`
  - 仪表盘 `/index`
  - 数据监控 `/monitor/druid`
  - 表单构建 `/tool/build`

### 3.3 系统管理模块（system/）

目录：`ruoyi-fastapi-test/system/`
- 用户/角色/菜单/部门/岗位/字典/参数/公告/日志等页面的访问与核心交互（以具体 test 文件为准）。

### 3.4 监控模块（monitor/）

目录：`ruoyi-fastapi-test/monitor/`
- 缓存监控/缓存列表
- 在线用户
- 定时任务
- 服务监控

### 3.5 工具模块（tool/）

目录：`ruoyi-fastapi-test/tool/`
- `test_code_gen.py`：代码生成关键链路
- `test_swagger.py`：Swagger/接口文档页面可访问性

### 3.6 像素级视觉基线（visual/）

目录：`ruoyi-fastapi-test/visual/`
- `test_visual_baseline.py`：Playwright 截图基线对比（像素级 diff）

权威说明：
- `docs/ui-ux-spec/08_Visual_Baseline/README.md`

运行方式（在前后端已启动的前提下）：

```bash
cd ruoyi-fastapi-test
pytest -q visual/test_visual_baseline.py
```

更新基线（预期 UI 变更时）：

```bash
cd ruoyi-fastapi-test
UPDATE_BASELINE=1 pytest -q visual/test_visual_baseline.py
```

严格模式（完全像素一致）：

```bash
cd ruoyi-fastapi-test
VISUAL_MAX_TOLERATED_PIXELS=0 VISUAL_MAX_TOLERATED_DIFF_SUM_RGBA=0 \\
pytest -q visual/test_visual_baseline.py
```

---

## 4) 失败排查（Debug Checklist）

常见失败点：
- 端口被占用（E2E compose 默认占用 `80`/`9099`）。
- DB 未初始化或初始化脚本未被挂载（检查 compose volumes）。
- 后端未就绪：CI 使用 `GET http://localhost:9099/captchaImage` 做就绪探针。
- Playwright 浏览器依赖未安装：本地需 `playwright install`。
