# SPEC 覆盖检查报告（可复跑规则集）
generated: `2026-02-14`

用途：对齐“代码元素清单”与“规格文档输出”，用可重复的规则检查：
- OpenAPI 字段级契约是否存在且可校验
- controller/service/dao 是否有对应的文档/索引
- 关键前端/移动端工程入口是否已在 spec 中固化

复跑说明：
- 本报告为“规则与结果”的固化；统计数据来自对仓库目录的扫描与对 spec 文档的字符串匹配。
- 复跑方式可参考 `docs/codebase-spec/09_Verification/SOURCE_ANCHOR_REPORT.md` 中的 Python one-liner（同理可扩展校验维度）。

## 1) OpenAPI 快照
- [ x ] `03_API/openapi.json` 存在
- [ x ] `03_API/openapi.sha256` 存在
- [ x ] sha256 匹配
- Stats: paths=129, operations=143, schemas=130

## 2) Backend Controllers → ENDPOINTS.md
- Controllers found: 19
- Covered by `03_API/ENDPOINTS.md`: 19/19
- Missing: (none)

## 3) Service/DAO 方法级索引
- Services found: 20; documented: 20/20
- DAOs found: 15; documented: 15/15

## 4) Frontend 工程行为契约（关键文件引用）
- Key files: 4
- Mentioned in `06_Frontend/*`: 4/4
- Missing: (none)

## 5) Mobile 工程契约（关键文件引用）
- Key files: 3
- Mentioned in `05_Mobile_App/*`: 3/3
- Missing: (none)

## 6) E2E 测试资产
- pytest files: 19（含像素级视觉基线 `ruoyi-fastapi-test/visual/test_visual_baseline.py`）
- Spec entry: `08_Testing/E2E_SPECS.md`

## 7) Verdict
- Result: OK
