# Page Spec: 缓存监控（monitor-cache）

PageId：`monitor-cache`  
Route：`/monitor/cache`

Source：
- `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue`
- `ruoyi-fastapi-frontend/src/views/monitor/cache/list.vue`
- E2E：`ruoyi-fastapi-test/monitor/test_cache_monitor.py`、`ruoyi-fastapi-test/monitor/test_cache_list.py`

视觉基线（截图 ID）：
- `light_1_monitor-cache.png`
- `dark_1_monitor-cache.png`

---

## 1) 目的（Purpose）

展示 Redis 缓存的运行信息与统计信息，并提供缓存 key 列表（子页或切换页）。

---

## 2) 像素级结构（Structure）

缓存监控页（`/monitor/cache`）要求至少包含可见模块：
- 基本信息（包含“Redis版本”“运行模式”等字段）
- 命令统计
- 内存信息

缓存列表页（实现中存在 `/monitor/cache/list`）：
- 列表展示 key、类型、TTL、大小等（以实现为准）

---

## 3) 稳定 Selector（用于截图/自动化等待）

缓存监控页（E2E 使用）：
- `text=基本信息`
- `text=Redis版本`
- `text=运行模式`
- `text=命令统计`
- `text=内存信息`

---

## 4) 关键交互（Interactions）

复刻要求（最小可观察行为）：
- 页面加载后上述模块必须可见；
- 端口行应包含 `6379`（测试环境默认）。

---

## 5) 视觉基线稳定性说明（Visual Baseline Notes）

本页包含运行时指标与图表（ECharts），即使同机也可能出现像素级抖动。为保证视觉基线可复跑：
- 视觉基线测试会隐藏“动态值”与图表（保留标签与结构骨架），避免 Redis 指标变化造成截图差异；
- 详见 `docs/ui-ux-spec/08_Visual_Baseline/README.md` 的“特殊处理”与测试实现。
