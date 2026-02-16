# Page Spec: 服务监控（monitor-server）

PageId：`monitor-server`  
Route：`/monitor/server`

Source：
- `ruoyi-fastapi-frontend/src/views/monitor/server/index.vue`
- E2E：`ruoyi-fastapi-test/monitor/test_server_monitor.py`

视觉基线（截图 ID）：
- `light_1_monitor-server.png`
- `dark_1_monitor-server.png`

---

## 1) 目的（Purpose）

展示服务器运行状态（CPU/内存/磁盘等）与运行环境信息（Python 解释器信息等）。

---

## 2) 稳定 Selector（用于截图/自动化等待）

E2E 依赖的最小可观察模块（页面加载完成应可见）：
- `text=CPU`
- `text=内存`
- `text=服务器信息`
- `text=Python解释器信息`
- `text=磁盘状态`

---

## 3) 关键断言（环境一致性）

在 Docker 测试环境中：
- 项目路径行应包含 `/app`

---

## 4) 视觉基线稳定性说明（Visual Baseline Notes）

本页包含运行时指标（CPU/内存/磁盘/路径等），会随环境与运行时变化。为保证视觉基线可复跑：
- 视觉基线测试会隐藏“动态值”（保留标签与结构骨架），避免运行时指标变化造成截图差异；
- 详见 `docs/ui-ux-spec/08_Visual_Baseline/README.md` 的“特殊处理”与测试实现。
