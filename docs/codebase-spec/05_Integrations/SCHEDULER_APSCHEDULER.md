# APScheduler 集成规格（可复刻级）

本文件描述本仓库“定时任务系统”的实现约束：**启动加载、Cron 表达式解析、任务存储、并发/错过策略、事件日志落库**。

> 复刻目标：不要求使用 APScheduler，但要求外部行为与数据语义等价（例如 Cron 解析扩展、misfire 策略、日志字段）。

---

## 1) 生命周期：启动加载与关闭

### 1.1 启动时做什么

后端启动生命周期中会初始化 Scheduler：
1) `scheduler.start()`
2) 从 DB 查询任务列表 `JobDao.get_job_list_for_scheduler(session)`
3) 对每个任务：
   - 先 `remove_scheduler_job(job_id)`
   - 再 `add_scheduler_job(job_info)`
4) 注册事件监听 `scheduler.add_listener(cls.scheduler_event_listener, EVENT_ALL)`

Source：
- Source: `ruoyi-fastapi-backend/server.py`
- Source: `ruoyi-fastapi-backend/config/get_scheduler.py`
- Source: `ruoyi-fastapi-backend/module_admin/dao/job_dao.py`

### 1.2 关闭时做什么

- `scheduler.shutdown()`

Source：
- Source: `ruoyi-fastapi-backend/config/get_scheduler.py`

---

## 2) JobStore 与执行器（必须一致的行为）

本仓库配置了 3 种 job store，并在添加任务时通过 `job_info.job_group` 选择：

- `default`: `MemoryJobStore()`
- `sqlalchemy`: `SQLAlchemyJobStore(url=SQLALCHEMY_DATABASE_URL, engine=engine)`
- `redis`: `RedisJobStore(**redis_config)`

执行器（executors）：
- `default`: `AsyncIOExecutor()`
- `processpool`: `ProcessPoolExecutor(5)`

job_defaults：
- `coalesce=False`
- `max_instance=1`（注意：这里是 defaults；单个任务会被 `add_scheduler_job` 覆盖 `max_instances`）

Source：
- Source: `ruoyi-fastapi-backend/config/get_scheduler.py`

复刻注意：
- 即便不使用 APScheduler，也必须支持“任务存储后端”的概念（至少能表达 `memory/sqlalchemy/redis` 三类语义）。
- 本仓库允许 `job_group` 选择不同 store（见数据表/字典配置；字段级以 `openapi.json` 与 DB schema 为准）。

---

## 3) Cron 表达式：MyCronTrigger 扩展规则

本仓库重写 `CronTrigger.from_crontab` 为 `MyCronTrigger.from_crontab`，并支持 6 或 7 段表达式：
- 6 段：`second minute hour day month week`
- 7 段：`... year`

关键扩展（复刻必须项）：
- `day` 字段支持 `?`：当 `?` 存在时，day 视为 `None`
- `week` 字段支持：
  - `L`：last week day（会影响 `day` 与 `week` 的处理）
  - `?`：week 视为 `None`
  - `#`：第几个星期几（week=`N`，`day_of_week=int(before#)-1`）
- `day` 字段支持：
  - `L`：`last` 语义（替换为 `last...`）
  - `W`：最近工作日（内部用 `__find_recent_workday`，若落在周末会向前回退到最近工作日）

Source：
- Source: `ruoyi-fastapi-backend/config/get_scheduler.py`

---

## 4) invoke_target：动态导入与调用约束

任务的实际执行函数通过字符串路径导入，例如：
- `module_task.scheduler_test.job`
- `module_task.scheduler_test.async_job`

导入规则：
- `module_path, func_name = func_path.rsplit('.', 1)`
- `importlib.import_module(module_path)` 后 `getattr(module, func_name)`

Source：
- Source: `ruoyi-fastapi-backend/config/get_scheduler.py`
- Source: `ruoyi-fastapi-backend/module_task/scheduler_test.py`

复刻约束：
- 必须支持“以字符串定位可调用对象”的机制（可替换为注册表/白名单映射，但外部字段语义需一致）。

---

## 5) 并发与 misfire 策略（字段语义）

添加任务时的关键策略（来自 `job_info` 字段）：

- `misfire_policy == '3'`：`misfire_grace_time` 设置为一个极大值（近似“永不丢失”）
- `misfire_policy == '2'`：`coalesce=True`（合并错过的多次触发）
- 其他：保持默认（`None/False`）

并发（`concurrent`）：
- `concurrent == '0'` → `max_instances=3`
- 否则 → `max_instances=1`

执行器（`job_executor`）：
- 若目标函数为 coroutine：强制 `executor='default'`
- 否则：使用 `job_info.job_executor`

Source：
- Source: `ruoyi-fastapi-backend/config/get_scheduler.py`

---

## 6) 事件监听与日志落库（关键可复刻点）

监听范围：`EVENT_ALL`

事件处理要点（简化）：
- `event_type = event.__class__.__name__`
- 若为 `JobExecutionEvent` 且 `event.exception` 存在：
  - `status='1'`
  - `exceptionInfo=str(event.exception)`
- 读取 scheduler 中 job 的 state（`query_job.__getstate__()`），组装日志字段：
  - jobName, jobGroup, jobExecutor, invokeTarget, jobArgs, jobKwargs, jobTrigger, jobMessage, status, exceptionInfo, createTime
- 使用同步 SQLAlchemy session（`SessionLocal = sessionmaker(bind=engine)`）写入日志表

Source：
- Source: `ruoyi-fastapi-backend/config/get_scheduler.py`
- Source: `ruoyi-fastapi-backend/module_admin/service/job_log_service.py`
- Source: `ruoyi-fastapi-backend/module_admin/entity/vo/job_vo.py`

复刻约束：
- 必须保留“任务执行事件 → 落库日志”的能力与字段语义，便于前端监控页/日志页复刻。

---

## 7) 验收与测试计划

- [ ] DB 中存在启用的任务时，重启服务会自动加载到 scheduler
- [ ] `invoke_target` 写错时，事件监听能记录 exceptionInfo（且 status=1）
- [ ] `misfire_policy` 与 `concurrent` 的行为与上述规则一致

