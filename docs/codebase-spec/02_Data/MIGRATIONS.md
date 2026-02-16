# Schema Migrations（迁移与演进）

本仓库的“数据库结构演进”同时存在三类机制，复刻时需要明确它们各自的定位与优先级：

1) **初始化 SQL（强主线）**
   - MySQL：`ruoyi-fastapi-backend/sql/ruoyi-fastapi.sql`
   - PostgreSQL：`ruoyi-fastapi-backend/sql/ruoyi-fastapi-pg.sql`
   - 用途：从零初始化表结构 + 初始数据（组织/用户/角色/菜单/字典/参数等）

2) **启动时 create_all（保底机制）**
   - `ruoyi-fastapi-backend/config/get_db.py:init_create_table()`
   - 用途：应用启动时执行 `Base.metadata.create_all`，确保 ORM 模型所需表存在
   - 注意：该机制通常不用于生产环境的严谨迁移（无法表达复杂变更/回滚）

3) **Alembic（可选的正式迁移机制）**
   - 配置：`ruoyi-fastapi-backend/alembic.ini`
   - 环境脚本：`ruoyi-fastapi-backend/alembic/env.py`
   - 特点：
     - 异步 engine 运行迁移（`async_engine_from_config`）
     - 启动时会自动创建 `alembic/versions/` 目录（若不存在）
     - 通过扫描 `Base.metadata` 自动发现模型；若无变更不会生成迁移文件（`process_revision_directives` 会清空空操作）

---

## 推荐迁移策略（复刻/二开建议）

### A) 初始化（从零部署）

1) 选定 DB 类型（MySQL / PostgreSQL）
2) 执行对应 SQL 初始化脚本（建立 schema + 初始数据）
3) 启动后端服务（允许 `create_all` 做保底补齐）

### B) 演进（生产环境）

建议使用 Alembic 管理“增量变更”，并明确：
- 迁移文件归档策略（`alembic/versions/` 纳入版本管理）
- 每次迁移的回滚策略（降级脚本、备份、数据修复）
- 与上游同步时的冲突处理（见 `docs/compliance/fork-upstream.md`）

---

## 回滚（Rollback）建议

由于本项目包含“初始化 SQL + 运行时保底 create_all”，回滚建议按场景区分：
- **结构性变更**：优先通过 Alembic downgrade（或对等回滚脚本）处理
- **数据变更**：优先使用备份恢复或双写/补偿脚本；避免仅靠 ORM 代码回滚

---

## 已知事实（当前仓库状态）

- 当前仓库中 `ruoyi-fastapi-backend/alembic/versions/` 目录默认不存在（首次运行迁移时由 `alembic/env.py` 创建）。
- 初始化 SQL 是唯一明确记录“全量 schema + 初始数据”的材料（字段级见 `02_Data/ENTITIES.md`）。
