# Page Spec: 定时任务（monitor-job）

PageId：`monitor-job`  
Route：`/monitor/job`

Source：
- `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue`
- `ruoyi-fastapi-frontend/src/views/monitor/job/log.vue`
- E2E：`ruoyi-fastapi-test/monitor/test_job_management.py`

视觉基线（截图 ID）：
- `light_1_monitor-job.png`
- `dark_1_monitor-job.png`

---

## 1) 目的（Purpose）

管理 APScheduler 定时任务（新增/修改/启停/执行一次/查看日志/删除）。

---

## 2) 稳定 Selector（用于截图/自动化等待）

页面加载完成的最小判定：
- `text=任务名称`
- `.app-container`

---

## 3) 关键交互（Interactions）

E2E 覆盖的最小交互：
- 新增任务（任务名称/分组/执行器/调用方法/cron）
- 修改调用方法
- 启停状态（switch + 确认）
- 执行一次（确认后出现“执行成功”）
- 查看调度日志（跳转到 `/monitor/job-log`，出现“调度日志”，再关闭返回）
- 删除任务（“删除成功”）
