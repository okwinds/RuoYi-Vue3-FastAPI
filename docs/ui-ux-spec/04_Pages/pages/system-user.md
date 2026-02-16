# Page Spec: 用户管理（system-user）

PageId：`system-user`  
Route：`/system/user`

Source：
- `ruoyi-fastapi-frontend/src/views/system/user/index.vue`
- E2E：`ruoyi-fastapi-test/system/test_user_management.py`

视觉基线（截图 ID）：
- `light_1_system-user.png`
- `dark_1_system-user.png`

---

## 1) 目的（Purpose）

提供用户的 CRUD 管理界面，典型“搜索 + 工具条 + 表格 + 分页 + 弹窗表单”模板。

---

## 2) 前置条件（Preconditions）

- 已登录
- 具备进入“用户管理”的路由权限（权限语义见 `docs/codebase-spec/03_API/AUTHENTICATION.md` 与后端权限规则）

---

## 3) 像素级结构（Structure）

页面模板：
1) Search Form（可隐藏）
2) Toolbar（新增/修改/删除/导入/导出等）
3) Table（含操作列按钮）
4) Pagination（右对齐）
5) Dialog（新增/编辑用户弹窗）

可复用模式详述：
- `docs/ui-ux-spec/03_Patterns/PATTERNS.md`（CRUD List 模板）

关键布局常量：
- `.app-container { padding: 20px }`
- inline 表单控件默认宽度：200px
- pagination 在移动端隐藏 sizes/jumper（<768px）

---

## 4) 稳定 Selector（用于截图/自动化等待）

建议等待（与 E2E 一致）：
- `div:has-text("用户管理")`
- `.app-container`
- `span.el-pagination__total`（分页总条数存在）

---

## 5) 关键交互（Interactions）

E2E 覆盖的最小可观察交互：
- 新增用户：点击“新增” → 弹窗表单 → 填写字段 → “确 定” → 成功提示
- 搜索：在搜索表单输入“用户名称” → “搜索”
- 修改状态：表格行内 switch → 确认弹窗“确定”
- 编辑：表格行内“修改”按钮 → 弹窗 → “确 定”
- 删除：表格行内“删除”按钮 → 确认 → “删除成功”

复刻要求：
- 弹窗字段 label、按钮文案与交互顺序需保持（否则 E2E/视觉基线会漂移）。
