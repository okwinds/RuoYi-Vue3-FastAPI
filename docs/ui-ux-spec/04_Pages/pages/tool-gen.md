# Page Spec: 代码生成（tool-gen）

PageId：`tool-gen`  
Route：`/tool/gen`

Source：
- `ruoyi-fastapi-frontend/src/views/tool/gen/index.vue`
- E2E：`ruoyi-fastapi-test/tool/test_code_gen.py`

视觉基线（截图 ID）：
- `light_1_tool-gen.png`
- `dark_1_tool-gen.png`

---

## 1) 目的（Purpose）

提供代码生成器的表管理能力，包含“导入表 → 编辑 → 预览 → 删除”的闭环。

---

## 2) 像素级结构（Structure）

页面模板（CRUD List）：
1) Search Form（表名称）
2) Toolbar（导入/编辑/删除/同步/生成等）
3) Table（表清单）
4) Dialog：导入表（aria-label='导入表'）
5) Dialog：编辑表/预览代码（实现决定）

---

## 3) 稳定 Selector（用于截图/自动化等待）

建议等待：
- `.app-container`
- `button:has-text("导入")`

导入弹窗（E2E 依赖）：
- `div[role='dialog'][aria-label='导入表']`
- `input[placeholder*='请输入表名称']`

---

## 4) 关键交互（Interactions）

E2E 覆盖的最小交互：
- 导入表（以 `sys_post` 为例）
- 编辑表备注
- 预览代码
- 删除表清理

复刻要求：
- 导入弹窗标题必须为“导入表”（aria-label），否则测试与视觉基线会漂移。
