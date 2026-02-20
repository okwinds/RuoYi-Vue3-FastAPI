# Task Summary: 规格一致性复核（Demo Mode + OpenAPI + Code→Spec）

## 1) Goal / Scope

- Goal：复核并补齐“可复刻规格文档”，保证 **Spec 与当前源码一致**，并满足“不读源码也可复刻”的交付要求。
- In Scope：
  - 后端配置/开关：补齐 `APP_WORKERS`、`APP_DEMO_MODE` 的规格说明与行为规则
  - OpenAPI 字段级契约：校验运行态导出是否与仓库快照一致，并在漂移时同步
  - `CODE_TO_SPEC_MAP.md`：修正为对当前仓库文件系统的全覆盖映射（无漏映射/无陈旧条目）
- Out of Scope：
  - 业务二次开发的领域规则扩展（应在 `docs/specs/` 另起模块 spec）
  - 改动业务代码实现
- Constraints：仅做“增量补齐与一致性修正”，避免大范围文档重排。

---

## 2) Context（背景与触发）

- 背景：用户要求以“当前源码”为事实依据，对规格文档做全仓库复核，发现缺失必须补齐。
- 触发问题（Symptoms）：
  - 环境变量规格未覆盖实现中已存在的 `APP_WORKERS` / `APP_DEMO_MODE`
  - `CODE_TO_SPEC_MAP.md` 对照表存在漏映射与陈旧条目
  - OpenAPI 快照与运行态导出存在漂移（版本与 schema 细节）
- 影响范围（Impact）：
  - 影响复刻者对“演示模式”的行为预期（写操作是否允许、哪些路径被拦截）
  - 影响 Code→Spec 的“无死角”交付证据可信度
  - 影响字段级 API 契约真源（OpenAPI）与代码一致性

---

## 3) Spec / Contract（文档契约）

- Contract（接口/事件协议/数据结构）：
  - `docs/codebase-spec/03_API/openapi.json` 为字段级 API 契约真源（配套 `openapi.sha256`）
  - `APP_DEMO_MODE` 的拦截规则固化在 `docs/codebase-spec/01_Configuration/FEATURE_FLAGS.md`
- Acceptance Criteria（验收标准）：
  - `ENVIRONMENT.md` 覆盖 `AppSettings` 的全部 `APP_*` 变量（含 `APP_WORKERS` / `APP_DEMO_MODE`）
  - `CODE_TO_SPEC_MAP.md` 在扫描口径内 `missing=0` 且 `stale=0`
  - OpenAPI：运行态导出 JSON 与 `openapi.json` 对齐（object_equal=true），且 `openapi.sha256` 校验一致
  - placeholder/TODO 扫描 hits=0（仅扫描 spec 目录，不含 worklog/task-summaries）；Source anchors missing_total=0；Spec pointers missing=0
- Test Plan（测试计划，至少含离线回归）：
  - placeholder 扫描：`rg -n "TODO|TBD|FIXME|待补充|PLACEHOLDER|未完成|WIP" docs/codebase-spec docs/ui-ux-spec ...`
  - Source anchors：按 `docs/codebase-spec/09_Verification/SOURCE_ANCHOR_REPORT.md` 的 one-liner 复跑
  - OpenAPI：`docker compose` 拉起后端并抓取 `/openapi.json`，canonicalize 后对比
  - Code→Spec coverage：对照表与文件系统集合差分检查（missing/stale）
- 风险与降级（Risk/Rollback）：
  - OpenAPI 快照更新会影响下游 SDK/Mock/契约测试的基线；通过 `openapi.sha256` 固化并可审计回滚。

---

## 4) Implementation（实现说明）

### 4.1 Key Decisions（关键决策与 trade-offs）

- Decision：以运行态导出的 OpenAPI 作为“当前代码”的对照基线，更新仓库快照（而不是忽略漂移）。
  - Why：用户要求“源码为真源”；OpenAPI 快照是字段级契约真源，必须随代码更新。
  - Trade-off：会引入一次性 diff（sha256 变化），但换来契约一致性与可验证性。
  - Alternatives：只记录漂移但不更新快照（会长期累积不一致，不符合复刻要求）。

### 4.2 Code Changes（按文件列）

- `docs/codebase-spec/01_Configuration/ENVIRONMENT.md`：补齐 `APP_WORKERS`、`APP_DEMO_MODE`。
- `docs/codebase-spec/01_Configuration/FEATURE_FLAGS.md`：补齐 `APP_WORKERS`、`APP_DEMO_MODE`，并写明 Demo Mode 的拦截路径、方法与返回语义。
- `docs/codebase-spec/03_API/openapi.json`、`docs/codebase-spec/03_API/openapi.sha256`：同步运行态导出差异（版本与 `ValidationError` schema）。
- `docs/codebase-spec/09_Verification/CODE_TO_SPEC_MAP.md`：修正为全覆盖（补齐缺失文件、移除已不存在条目），并刷新统计。
- `docs/codebase-spec/09_Verification/SPEC_POINTERS_VALIDATION_REPORT.md`：同步指针校验统计与时间戳。
- `docs/worklog.md`：追加本轮命令与结论。

---

## 5) Verification（验证与测试结果）

### Offline Regression（必须）

- 命令：
  - placeholder 扫描（hits=0）
  - Source anchors 校验（missing_total=0）
  - Code→Spec 对照：Files scanned=`563`，Missing=`0`，Stale=`0`
  - OpenAPI sha256：`openapi.sha256` 与 `openapi.json` 计算值一致（match=true）
- 结果：通过

### Integration / E2E（可选但强烈建议）

- 环境：Docker Compose（MySQL + Redis + Backend）
- 命令：
  - `docker compose -f docker-compose.my.yml up -d --build ruoyi-mysql ruoyi-redis ruoyi-backend-my`
  - `curl http://127.0.0.1:19099/openapi.json`
  - `docker compose -f docker-compose.my.yml down`
- 结果：运行态 OpenAPI 与仓库快照对齐（object_equal=true）

---

## 6) Results（交付结果）

- 交付物列表：
  - Demo Mode（演示模式）行为已在规格文档中可复刻、可验收
  - Code→Spec 对照表已恢复“全覆盖、无陈旧条目”的可交付证据
  - OpenAPI 字段级契约快照与运行态一致，并由 sha256 固化

---

## 7) Known Issues / Follow-ups

- 运行态 OpenAPI 校验依赖 docker 构建后端镜像（安装依赖较多）；如后续要提升速度，可考虑提供“最小依赖导出 OpenAPI”的专用镜像/目标。

---

## 8) Doc Index Update

- 已在 `DOCS_INDEX.md` 登记：是
