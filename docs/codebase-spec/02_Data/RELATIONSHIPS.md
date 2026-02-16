# Entity Relationships（实体关系）

本仓库的数据库结构属于典型的后台管理系统（RBAC + 数据权限 + 字典/参数/日志/任务/代码生成）。

说明：
- 初始化 SQL 中多数表**未显式声明外键约束**（常见于便于跨库兼容/减少迁移难度的设计），但业务语义上存在稳定的关联关系。
- 复刻时需要同时复刻：
  1) 表结构（见 `02_Data/ENTITIES.md`）
  2) 关联语义（本文件）
  3) 业务层校验/约束（见 `04_Business_Logic/` 与 `03_API/`）

---

## 1) ER 图（语义级）

```mermaid
erDiagram
  SYS_DEPT ||--o{ SYS_USER : \"dept_id\"

  SYS_USER ||--o{ SYS_USER_ROLE : \"user_id\"
  SYS_ROLE ||--o{ SYS_USER_ROLE : \"role_id\"

  SYS_ROLE ||--o{ SYS_ROLE_MENU : \"role_id\"
  SYS_MENU ||--o{ SYS_ROLE_MENU : \"menu_id\"

  SYS_ROLE ||--o{ SYS_ROLE_DEPT : \"role_id\"
  SYS_DEPT ||--o{ SYS_ROLE_DEPT : \"dept_id\"

  SYS_USER ||--o{ SYS_USER_POST : \"user_id\"
  SYS_POST ||--o{ SYS_USER_POST : \"post_id\"

  GEN_TABLE ||--o{ GEN_TABLE_COLUMN : \"table_id\"
```

---

## 2) 关系总览（关键 Join 表）

| 关系 | Join 表 | 说明 |
| --- | --- | --- |
| 用户 ↔ 角色 | `sys_user_role` | RBAC 的用户-角色多对多 |
| 角色 ↔ 菜单 | `sys_role_menu` | 角色拥有的菜单/权限点集合 |
| 角色 ↔ 部门（数据范围） | `sys_role_dept` | 当 `sys_role.data_scope=2`（自定）时生效 |
| 用户 ↔ 岗位 | `sys_user_post` | 用户所属岗位（可多岗位） |

---

## 3) 核心实体关系（业务语义）

### 3.1 组织结构

- `sys_dept`（部门树）：
  - `parent_id`：父部门
  - `ancestors`：祖先路径（字符串）
  - 典型关系：一棵树（树形结构）

- `sys_user.dept_id` → `sys_dept.dept_id`：
  - 用户归属部门（可为空）

### 3.2 RBAC（角色与权限）

- `sys_user` ↔ `sys_role`（多对多）：
  - 通过 `sys_user_role(user_id, role_id)` 关联

- `sys_role` ↔ `sys_menu`（多对多）：
  - 通过 `sys_role_menu(role_id, menu_id)` 关联
  - 菜单（`sys_menu`）通常承载：
    - 前端路由树结构（目录/菜单/按钮）
    - 权限标识（permissions）
    - 可见性与排序

### 3.3 数据范围（Data Scope）

- `sys_role.data_scope` 决定数据权限策略（见表字段注释）：
  - `1`：全部数据权限
  - `2`：自定数据权限（依赖 `sys_role_dept`）
  - `3`：本部门数据权限
  - `4`：本部门及以下数据权限

- 当 `data_scope=2` 时：
  - `sys_role` ↔ `sys_dept` 通过 `sys_role_dept(role_id, dept_id)` 形成授权部门集合

---

## 4) 业务支撑类关系

### 4.1 字典与参数

- 字典类型：`sys_dict_type`（类型定义）与 `sys_dict_data`（类型下的数据项）：
  - 关系键通常为 `dict_type`（字符串）
  - 后端启动时会将字典与参数表预热到 Redis（见 `config/get_redis.py`）

### 4.2 日志与审计

- `sys_oper_log`：操作日志（通常与用户关联，但通过用户名/账号字段间接关联）
- `sys_logininfor`：登录日志

### 4.3 定时任务

- `sys_job`：任务定义（包含 `invoke_target` 函数字符串路径、cron 表达式等）
- `sys_job_log`：任务执行日志
- 任务加载：启动时从 DB 读取任务列表并注册到 APScheduler（见 `config/get_scheduler.py`）。

### 4.4 代码生成

- `gen_table` 与 `gen_table_column` 为代码生成的元数据表：
  - `gen_table`：一张“业务表”的生成配置
  - `gen_table_column`：对应业务表的列配置（字段、校验、展示等）

### 4.5 AI 管理

- `ai_models`：模型配置
- `ai_chat_config`：对话相关配置

---

## 5) 约束与一致性（复刻要点）

- 即使 SQL 未声明外键，业务上仍需要保证关联字段的一致性：
  - 删除角色/菜单/部门时的级联处理策略（由 service/controller 实现）
  - RBAC 缓存/权限树生成的正确性（影响前端动态路由）
- 复刻实现时建议显式实现：
  - Unique 约束（如账号名、角色 key、菜单权限标识等）
  - 删除策略（软删除 `del_flag` vs 硬删除）
