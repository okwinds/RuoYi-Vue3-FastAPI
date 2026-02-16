# 规格缺口清单（Spec Gap List）

generated: `2026-02-14`

用途：把“影响复刻/像素级验收”的缺口显式登记，避免在多次迭代中被口头约定吞没。  
规则：每条缺口必须包含 **现状**、**缺什么**、**补到哪里**、**如何验收**。

---

## A) UI 像素级复刻（高优先级）

### A1. 缺：布局常量的量化表（像素/层级/断点）

Status：Closed（`2026-02-14`）

- 已补齐：
  - `docs/ui-ux-spec/01_Foundation/LAYOUT_METRICS.md`（量化表 + Source 指向）
- 验收方式：
  - 人工抽样核对至少 10 项常量与源码一致；
  - UI 视觉基线（截图）在这些常量变化时能稳定反映差异（见视觉基线章节）。

### A2. 缺：可复现的视觉基线（截图快照）

Status：Closed（`2026-02-14`）

- 已补齐：
  - `docs/ui-ux-spec/08_Visual_Baseline/README.md`
  - `ruoyi-fastapi-test/visual/test_visual_baseline.py`
  - `docs/ui-ux-spec/08_Visual_Baseline/screenshots/*.png`
- 验收方式：
  - 在干净环境启动 `docker compose -f ruoyi-fastapi-test/docker-compose.test.*.yml up -d --build` 后，
    运行 `pytest -q ruoyi-fastapi-test/visual/test_visual_baseline.py` 通过；
  - 如需严格像素一致：按视觉基线 README 设置 env（将容忍阈值置 0）。

---

## B) 后端“内部等价”复刻（高优先级）

### B1. 缺：Integrations（外部依赖）专项规格

Status：Closed（`2026-02-14`）

- 已补齐：`docs/codebase-spec/05_Integrations/` 下的专项规格（Redis/APScheduler/AI/上传/Excel/Crypto）。

### B2. 缺：Endpoint → Controller → Service.method 的完整映射

Status：Closed（`2026-02-14`）

- 已补齐：`docs/codebase-spec/03_API/HANDLER_MAP.md` + 生成工具 `tools/spec/gen_handler_map.py`。

### B3. 缺：关键工作流方法的“可重写级”方法规格（method-spec）

Status：Closed（`2026-02-14`）

- 已补齐：`docs/codebase-spec/04_Business_Logic/method-specs/` 的关键链路方法规格（登录/路由/AI/调度/上传等）。

---

## C) 可移植性/复跑性（中优先级）

### C1. 缺：报告中出现本机绝对路径（影响外部复现）

Status：Closed（`2026-02-14`）

- 已补齐：将发现到的绝对路径替换为 `<repo_root>` 形式，并确保 `docs/` 中不再包含本机 home 目录路径。
