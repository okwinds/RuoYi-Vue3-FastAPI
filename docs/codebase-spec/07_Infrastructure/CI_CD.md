# CI/CD（GitHub Actions）

本仓库目前的 CI 主要包含两条流水线：ruff 静态检查与 Playwright E2E。

---

## 1) Ruff（Lint + Format Check）

文件：`.github/workflows/ruff.yml`

- 触发：push / PR（分支 `master`）
- Python 版本：3.10
- 步骤：
  - 安装 `ruff`
  - `ruff check ruoyi-fastapi-backend` 与 `ruff check ruoyi-fastapi-test`
  - `ruff format ... --check`

结论：
- “离线回归最小集”应与此一致（见 `docs/testing-strategy.md`）。

---

## 2) Playwright（E2E）

文件：`.github/workflows/playwright.yml`

- 触发：push / PR（分支 `master`）
- Python 版本矩阵：3.10 / 3.11 / 3.12 / 3.13
- 数据库矩阵：
  - `mysql-test`：`ruoyi-fastapi-test/docker-compose.test.my.yml`
  - `pg-test`：`ruoyi-fastapi-test/docker-compose.test.pg.yml`

关键实现要点：
- CI 会临时改写 `ruoyi-fastapi-backend/Dockerfile.my` 的 base image Python 版本，以覆盖不同 Python runtime；结束后恢复原文件。
- 服务就绪探针：CI 通过 `GET http://localhost:9099/captchaImage` 判断后端是否可用（并在失败时输出容器日志）。
- 测试执行：在 `ruoyi-fastapi-test/` 下 `pip install -r requirements.txt`、`playwright install`、`pytest -v`。

