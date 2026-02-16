# System Architecture（系统架构）

本文件描述本仓库的“可复刻级”架构：模块边界、启动生命周期、关键数据流与依赖关系。

---

## 1) 高层架构图（Container）

```mermaid
flowchart LR
  U[Browser 用户] -->|HTTP| FE[Nginx / ruoyi-fastapi-frontend 静态站点]
  FE -->|/dev-api /prod-api /docker-api| BE[FastAPI / ruoyi-fastapi-backend]
  BE --> DB[(MySQL 或 PostgreSQL)]
  BE --> R[(Redis)]
  BE --> SCH[APScheduler]

  subgraph Backend
    BE --> MW[Middlewares]
    BE --> EX[Exception Handlers]
    BE --> RT[Auto Router Register]
    RT --> CTL[Controllers (module_*/controller)]
    CTL --> SVC[Services]
    SVC --> DAO[DAO]
    DAO --> ORM[SQLAlchemy AsyncSession]
  end
```

关键点：
- 前端通过 `VITE_APP_BASE_API` 指定 API 前缀（如 `/dev-api`），通常由 Nginx/反向代理转发到后端。
- 后端通过 `APP_ROOT_PATH` 配置 `FastAPI(root_path=...)`，用于与反向代理路径对齐（尤其影响文档与静态资源路径）。
- 后端在启动生命周期中初始化：DB 连接、Redis 连接与缓存预热、Scheduler 加载与监听。

---

## 2) 后端启动生命周期（lifespan）

入口：
- `ruoyi-fastapi-backend/app.py`：`create_app()` 并在 `__main__` 中 `uvicorn.run(...)`
- `ruoyi-fastapi-backend/server.py`：定义 `create_app()` 与 `lifespan`

启动顺序（见 `ruoyi-fastapi-backend/server.py:lifespan`）：
1) 初始化数据库连接并确保表存在：`config/get_db.py:init_create_table()`（`Base.metadata.create_all`）
2) 建立 Redis 连接池：`config/get_redis.py:RedisUtil.create_redis_pool()`
3) 预热缓存：
   - 字典：`RedisUtil.init_sys_dict()`
   - 参数：`RedisUtil.init_sys_config()`
4) 启动定时任务调度器并加载 DB 中的任务：`config/get_scheduler.py:SchedulerUtil.init_system_scheduler()`
5) 输出应用访问地址与 API 文档地址（Swagger/ReDoc 可禁用）
6) shutdown：关闭 Redis、关闭 Scheduler

---

## 3) 路由注册机制（Auto Register Routers）

路由注册由 `ruoyi-fastapi-backend/common/router.py:auto_register_routers()` 完成：
- 遍历项目根目录下所有 `controller/` 目录
- 动态 import 每个 controller 模块
- 收集模块内的 `APIRouter` 与 `APIRouterPro`
- 对 `APIRouterPro`：
  - `auto_register=True` 才会被注册
  - 按 `order_num` 排序，越小越优先注册
- 最终 `app.include_router(router=router)`

这意味着：
- controller 文件名不是路由前缀的来源，**router 变量的 `prefix` 才决定路径**；
- 任意新增 controller 只要声明 router 变量并暴露在模块顶层即可自动注册；
- 运行时 import 失败会导致对应 router 丢失（会打印错误）。

---

## 4) 模块划分（Backend Modules）

- `module_admin/`：系统管理与监控（用户/角色/菜单/部门/岗位/字典/参数/公告/日志/在线用户/定时任务/服务监控/缓存等）
- `module_generator/`：代码生成（`/tool/gen` 前缀）
- `module_ai/`：AI 管理（模型管理、AI 对话等）
- `module_task/`：定时任务函数入口（调度器通过字符串路径动态导入执行）

---

## 5) 横切关注点（Cross-cutting）

### 5.1 Middlewares

统一加载入口：`ruoyi-fastapi-backend/middlewares/handle.py:handle_middleware()`，包含：
- 上下文清理中间件
- CORS 中间件
- Gzip 中间件
- Trace 中间件（链路追踪/日志关联）

### 5.2 Exception Handling

统一加载入口：`ruoyi-fastapi-backend/exceptions/handle.py:handle_exception()`：
- 业务异常映射到统一响应结构（`ResponseUtil.*`）
- `HTTPException` 会返回 `{\"code\": status_code, \"msg\": detail}`（HTTP status 仍按 exception）
- 未捕获异常统一返回 `ResponseUtil.error(msg=str(exc))`

### 5.3 静态资源（上传文件访问）

`ruoyi-fastapi-backend/sub_applications/staticfiles.py`：
- 将上传目录挂载到 `UploadConfig.UPLOAD_PREFIX`（默认 `/profile`）
- 访问路径通常是：`{APP_ROOT_PATH}/profile/...`（取决于反向代理与 root_path）

---

## 6) 依赖关系（Module Dependencies）

| 模块 | 依赖 | 被依赖 |
| --- | --- | --- |
| `server.py` | config / common / middlewares / exceptions / sub_applications | `app.py` |
| `common/router.py` | importlib / FastAPI | `server.py` |
| `module_*/*/controller` | service / vo / dependencies | router auto register |
| `service` | dao / entity / utils / redis / scheduler | controllers |

---

## 7) 相关规格入口

- API 清单：`docs/codebase-spec/03_API/ENDPOINTS.md`
- 环境变量：`docs/codebase-spec/01_Configuration/ENVIRONMENT.md`
- 数据库表结构：`docs/codebase-spec/02_Data/ENTITIES.md`
- 前端 UI/UX 规格：`docs/ui-ux-spec/`
