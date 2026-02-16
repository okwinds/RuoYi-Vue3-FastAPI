# Task Summary：规格文档复刻审查 + 像素级视觉基线稳定

## 1) Goal / Scope

- Goal：Review 并补齐本仓库规格文档，使其具备“像素级复刻（UI）+ 代码级复刻（内部等价）”的可落地能力，并用可复跑的视觉基线作为验收真源。
- In Scope：
  - 视觉基线（Playwright）稳定性修复与规则固化
  - UI Foundation 补齐“布局量化表”（可审查的 px/断点/z-index/阴影等）
  - 文档可移植性清理（去除本机绝对路径痕迹）
  - 文档索引更新
- Out of Scope：
  - 业务功能新增/重构
  - 依赖升级与漏洞治理（`npm audit` 等）
- Constraints：
  - 中文文档；不修改 `AGENTS.md`
  - 优先最小变更 + 可复跑验证

---

## 2) Context（背景与触发）

- 背景：用户要求规格文档达到“看文档即可实现完整系统复刻”的粒度，并要求 UI 具备像素级验收能力。
- 触发问题（Symptoms）：
  - 视觉基线生成可成功，但紧接着对比会出现像素差（同机同环境也可能波动），导致 flaky。
  - UI 布局常量（sidebar/navbar/tags/breakpoints/z-index 等）散落在源码中，缺少“量化表”。
  - 规格报告中存在本机绝对路径，影响外部复现。
- 影响范围（Impact）：
  - 视觉基线不稳定会导致“像素级复刻”验收无法作为门禁。
  - 布局常量缺失会导致复刻实现偏差难以被发现/定位。

---

## 3) Spec / Contract（文档契约）

- Contract：
  - 视觉基线：`docs/ui-ux-spec/08_Visual_Baseline/README.md`
  - 布局量化表：`docs/ui-ux-spec/01_Foundation/LAYOUT_METRICS.md`
- Acceptance Criteria：
  - `pytest -q ruoyi-fastapi-test/visual/test_visual_baseline.py` 可连续复跑通过
  - `docs/` 中不包含本机绝对路径痕迹（可用 `rg` 扫描）
- Test Plan：
  - Docker 启动测试环境（frontend/backend/mysql/redis）
  - 运行视觉基线用例（更新基线 + 对比基线）
- 风险与降级：
  - 若未来需要“严格 0 像素差”，可将容忍阈值置 0，并对图表/监控页做更强的 mask（维护成本更高）

---

## 4) Implementation（实现说明）

### 4.1 Key Decisions（关键决策与 trade-offs）

- Decision：视觉基线对比使用“像素级 hash + 极小容忍阈值”，而不是 PNG 字节严格一致。
  - Why：PNG 元数据与抗锯齿/阴影边缘可能导致少量像素抖动；严格字节一致容易 flaky。
  - Trade-off：极小阈值可能容忍极少量边缘像素变化，但阈值默认仅 10 像素，仍能对真实 UI 变更保持高敏感。
  - Alternatives：完全字节一致（不稳定）；对大量区域做 mask（维护成本高）。

### 4.2 Code Changes（按文件列）

- `ruoyi-fastapi-test/visual/test_visual_baseline.py`：增强确定性（冻结时间/禁动效/等待 loading mask/固定滚动），并支持极小像素容忍；对监控页隐藏动态值与图表以避免运行时指标造成 diff。
- `docs/ui-ux-spec/08_Visual_Baseline/README.md`：更新对比策略说明（像素对比 + env 可调阈值），并说明监控页的特殊处理。
- `docs/ui-ux-spec/01_Foundation/LAYOUT_METRICS.md`：新增布局常量量化表（sidebar/navbar/tags/breakpoints/z-index/shadow）。
- `docs/ui-ux-spec/04_Pages/pages/dashboard.md`：修正 dashboard 的结构与稳定 selector（以 `.pageHeaderContent` 为锚点）。
- `docs/ui-ux-spec/04_Pages/pages/monitor-cache.md`、`docs/ui-ux-spec/04_Pages/pages/monitor-server.md`：补充视觉基线稳定性说明。
- `docs/codebase-spec/09_Verification/ELEMENT_INVENTORY.md`：移除本机绝对路径，改为 `<repo_root>`。
- `docs/codebase-spec/09_Verification/SPEC_GAP_LIST.md`：将相关缺口标记为 Closed，并固化验收方式。
- `DOCS_INDEX.md`：补充新增文档入口。

---

## 5) Verification（验证与测试结果）

### Offline Regression（必须）

- 命令：
  - `cd ruoyi-fastapi-test && UPDATE_BASELINE=1 pytest -q visual/test_visual_baseline.py`
  - `cd ruoyi-fastapi-test && pytest -q visual/test_visual_baseline.py`
  - `rg -n "/Users/" docs`
- 结果：
  - 视觉基线更新与对比：PASS（可连续复跑）
  - 文档绝对路径扫描：0 命中

### Integration / E2E（可选但强烈建议）

- 环境：Docker compose（MySQL）启动测试环境，端口固定 `80/9099`
- 命令：
  - `cd ruoyi-fastapi-test && docker compose -f docker-compose.test.my.yml up -d --build`
- 结果：环境可启动（用于视觉基线/E2E）

---

## 6) Results（交付结果）

- 交付物列表：
  - 像素级视觉基线（截图 + 可复跑对比）
  - 布局量化表（可审查的 px/z-index/breakpoints/shadow）
  - 缺口清单状态更新 + 可移植性修复
- 如何使用/如何验收：
  - 启动环境后运行：`cd ruoyi-fastapi-test && pytest -q visual/test_visual_baseline.py`
  - 需要严格模式：设置 `VISUAL_MAX_TOLERATED_PIXELS=0` 与 `VISUAL_MAX_TOLERATED_DIFF_SUM_RGBA=0`

---

## 7) Known Issues / Follow-ups

- 已知问题：
  - Dashboard 含第三方图表库，跨机器/渲染后端仍可能出现极小抗锯齿像素差（已用极小阈值控制）。
- 后续建议：
  - 若要把视觉基线作为 CI 强门禁，建议在 CI 环境固定 Playwright 浏览器版本与渲染参数，并保持 docker 镜像/字体一致。

---

## 8) Doc Index Update

- 已在 `DOCS_INDEX.md` 登记：是

---

## 9) Follow-up（规格一致性回扫与证据自洽，2026-02-14）

本任务在初版交付后做了一次“规格 ↔ 代码 ↔ 验证证据”的回扫，确保新增的视觉基线/工具脚本被纳入一一对应映射，且报告统计数字不自相矛盾。

### 9.1 追加/修正的规格点

- UI 来源索引补齐（工程骨架）：`docs/ui-ux-spec/00_UI_SOURCE_SCAN.md` 增补 `router/store/plugins/directives` 等关键入口位置。
- 工程约束补齐：`docs/ui-ux-spec/07_Engineering_Constraints/ENGINEERING.md` 增补 `localStorage` keys（`layout-setting` schema、`vueuse-color-scheme`）。
- 复刻验收加入视觉基线：`docs/codebase-spec/09_Verification/REPLICATION_GUIDE.md` 明确“E2E + 视觉基线”作为最小验收线。
- 测试规格纳入视觉基线：`docs/codebase-spec/08_Testing/E2E_SPECS.md` 增加 `visual/test_visual_baseline.py` 的运行/更新/严格模式说明。
- 质量门禁文档补齐：`docs/testing-strategy.md` 增加“UI 变更建议跑视觉基线”。

### 9.2 对照表与验证证据同步

- Code→Spec 对照表更新：`docs/codebase-spec/09_Verification/CODE_TO_SPEC_MAP.md`
  - 纳入新增文件（`ruoyi-fastapi-test/visual/*`、`ruoyi-fastapi-test/conftest.py`、`tools/spec/*`、`ruoyi-fastapi-frontend/.dockerignore`）
  - 最新统计：Files scanned=`523`，Unmapped=`0`
- 对照表指针校验报告更新：`docs/codebase-spec/09_Verification/SPEC_POINTERS_VALIDATION_REPORT.md`
- 覆盖检查报告同步：`docs/codebase-spec/09_Verification/SPEC_COVERAGE_TOOL_REPORT.md`（E2E test_*.py=19）
- Source anchor 统计修正并与审计报告对齐：
  - `docs/codebase-spec/09_Verification/SOURCE_ANCHOR_REPORT.md`（anchors_total=`167`）
  - `docs/codebase-spec/09_Verification/SPEC_AUDIT_REPORT.md`（同步 anchors 统计）

### 9.3 复跑结果（本轮新增）

- OpenAPI 快照校验：`shasum -a 256 docs/codebase-spec/03_API/openapi.json` 与 `openapi.sha256` 一致
- Handler Map 生成一致性：
  - `python tools/spec/gen_handler_map.py --backend-root ruoyi-fastapi-backend --out /tmp/handler_map.md`
  - 与 `docs/codebase-spec/03_API/HANDLER_MAP.md`（忽略 generated 时间）一致
- Ruff（针对新增测试与工具脚本）：
  - `ruff check ruoyi-fastapi-test tools`：PASS
  - `ruff format ruoyi-fastapi-test tools --check`：PASS
