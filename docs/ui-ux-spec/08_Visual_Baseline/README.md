# Visual Baseline（像素级视觉基线）

本目录把“像素级复刻”的验收从纯文字提升为 **可执行** 的视觉基线（screenshots）。  
基线的目标不是替代 UI 规格文档，而是作为其“像素级验收真源”：任何 UI 变更都必须能解释其截图差异。

---

## 1) 基线覆盖范围（固定组合）

截图命名规则：
- `{theme}_{navType}_{pageId}.png`
- `{theme}_{navType}_{pageId}_collapsed.png`（仅用于 navType=1 的 dashboard 折叠态）

其中：
- `theme`：`light` / `dark`
- `navType`：`1` / `2` / `3`
- `pageId`：见 `docs/ui-ux-spec/04_Pages/PAGES.md`

本仓库当前固定覆盖（总计 32 张，对齐 `ruoyi-fastapi-test/visual/test_visual_baseline.py`）：
- 登录页：`light/dark`（2）
- NavType=1：关键页全部 `light+dark`（12×2=24）
  - dashboard、system-user、system-role、system-menu
  - monitor-online、monitor-cache、monitor-server、monitor-job
  - tool-swagger、tool-gen
  - ai-chat、ai-model
- NavType=2：只覆盖 dashboard 的 `light+dark`（2）
- NavType=3：只覆盖 dashboard 的 `light+dark`（2）
- Sidebar 折叠态：navType=1 的 dashboard `light+dark`（2）

> 说明：覆盖范围固定是为了让视觉基线可维护、可复跑；新增页面基线属于“规格变更”，必须登记到 `DOCS_INDEX.md` 与 task summary。

---

## 2) 前置条件（如何启动可截图环境）

方式 A：使用 Docker（推荐，保证数据与端口一致）

```bash
cd ruoyi-fastapi-test

# MySQL 版本
docker compose -f docker-compose.test.my.yml up -d --build

# 或 PostgreSQL 版本
docker compose -f docker-compose.test.pg.yml up -d --build
```

默认端口（必须保持，截图与 E2E 均依赖）：
- Frontend：`http://localhost:80`
- Backend：`http://localhost:9099`

方式 B：手动启动（用于本地调试）
- Frontend：`cd ruoyi-fastapi-frontend && npm run dev`
- Backend：`cd ruoyi-fastapi-backend && python app.py --env=dev`

---

## 3) 生成/更新基线（Update baseline）

首次生成或更新基线时，设置环境变量：

```bash
cd ruoyi-fastapi-test
pip install -r requirements.txt
playwright install

UPDATE_BASELINE=1 pytest -q visual/test_visual_baseline.py
```

输出目录：
- `docs/ui-ux-spec/08_Visual_Baseline/screenshots/`

---

## 4) 校验基线（Verify baseline）

不设置 `UPDATE_BASELINE` 时，测试将对比当前截图与基线 PNG 的 **像素一致性**（忽略 PNG 元数据差异）：

```bash
cd ruoyi-fastapi-test
pytest -q visual/test_visual_baseline.py
```

像素对比策略：
- 先计算两张图的 RGBA 像素 bytes 的 sha256（快速判断是否一致）；
- 若不一致：默认允许“极小像素抖动容忍”，用于抵抗抗锯齿/阴影边缘的少量像素差异（同机也可能发生）。

容忍阈值可通过 env 调整：
- `VISUAL_MAX_TOLERATED_PIXELS`：默认 `10`（允许最多 10 个像素不同）
- `VISUAL_MAX_TOLERATED_DIFF_SUM_RGBA`：默认 `120`（单个像素 RGBA 差值和的上限）

严格模式（完全像素一致）：

```bash
VISUAL_MAX_TOLERATED_PIXELS=0 VISUAL_MAX_TOLERATED_DIFF_SUM_RGBA=0 \
pytest -q visual/test_visual_baseline.py
```

若失败：
- 测试会在 `ruoyi-fastapi-test/.artifacts/visual/` 写出 `*.actual.png`，用于人工对比；
- 若是预期 UI 变更：先更新页面规格卡（`docs/ui-ux-spec/04_Pages/pages/*.md` / `02_Components/components/*.md`），再执行“生成/更新基线”。

---

## 5) 稳定性策略（避免 flaky）

视觉基线测试内置稳定性策略（见 `ruoyi-fastapi-test/visual/test_visual_baseline.py`）：
- 固定 viewport：`1440x900`
- reduced motion：`reduce`（降低动画影响）
- 初始化脚本：
  - 写入 `localStorage['layout-setting']` 固定 navType、tagsView 等
  - 写入 `localStorage['vueuse-color-scheme']` 固定 light/dark
  - 注入 CSS 禁用 transition/animation（并隐藏滚动条）
  - 冻结 `Date`（避免时间类文案波动）

如果某页仍有动态内容（例如实时监控、时间戳），应在对应页面规格卡中标注，并在视觉基线测试中对该区域做“稳定等待或隐藏”处理。

本仓库的特殊处理（为了可复跑）：
- `monitor-cache` / `monitor-server`：会在截图前隐藏动态值与图表（保留标签与结构骨架），避免运行时指标导致像素 diff。
