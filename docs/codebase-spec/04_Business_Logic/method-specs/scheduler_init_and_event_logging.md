# Method Spec：SchedulerUtil.init_system_scheduler / add_scheduler_job（可复刻级）

目标：复刻“启动加载任务 + Cron 扩展 + 事件监听落库”的关键行为。

Source：
- Source: `ruoyi-fastapi-backend/config/get_scheduler.py`
- Source: `ruoyi-fastapi-backend/server.py`

---

## 1) init_system_scheduler（启动加载）

输入：无（从全局配置与 DB 读取）

关键步骤（必须一致）：
1) `scheduler.start()`
2) 查询 job_list（DB）
3) 对每个 job：
   - `remove_scheduler_job(job_id)`
   - `add_scheduler_job(job)`
4) `scheduler.add_listener(scheduler_event_listener, EVENT_ALL)`

失败策略：
- 若 DB 不可用或 job 数据不合法，启动期会抛异常导致服务启动失败（复刻建议同样把它视为强依赖）。

---

## 2) add_scheduler_job（按字段转成调度任务）

输入：`job_info: JobModel`

决策树：
1) 解析 `invoke_target` → `job_func`
2) 选择 executor：
   - 若 `job_func` 为 coroutine：强制 `executor='default'`
   - 否则使用 `job_info.job_executor`
3) trigger：
   - `MyCronTrigger.from_crontab(job_info.cron_expression)`
4) args/kwargs：
   - args：`job_info.job_args.split(',') if job_info.job_args else None`
   - kwargs：`json.loads(job_info.job_kwargs) if job_info.job_kwargs else None`
5) misfire：
   - `misfire_policy=='3'` → `misfire_grace_time=1000000000000`
   - `misfire_policy=='2'` → `coalesce=True`
6) 并发：
   - `concurrent=='0'` → `max_instances=3`
   - else `max_instances=1`
7) jobstore：
   - `jobstore=job_info.job_group`

---

## 3) scheduler_event_listener（事件日志落库）

规则（简化）：
- `status='0'` 默认成功
- `JobExecutionEvent` 且 `event.exception` 存在：
  - `status='1'`
  - `exceptionInfo=str(event.exception)`
- 读取 job state，生成 JobLogModel 并写入 DB

验收：
- 错误任务必须产生 status=1 且 exceptionInfo 非空的日志记录

