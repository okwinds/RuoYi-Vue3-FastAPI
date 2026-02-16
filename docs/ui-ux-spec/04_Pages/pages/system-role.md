# Page Spec: 角色管理（system-role）

PageId：`system-role`  
Route：`/system/role`

Source：
- `ruoyi-fastapi-frontend/src/views/system/role/index.vue`
- E2E：`ruoyi-fastapi-test/system/test_role_management.py`

视觉基线（截图 ID）：
- `light_1_system-role.png`
- `dark_1_system-role.png`

---

## 1) 目的（Purpose）

提供角色的 CRUD 管理界面，并包含“菜单权限树”的选择交互。

---

## 2) 像素级结构（Structure）

模板与用户管理相同（CRUD List），额外包含：
- 新增/编辑弹窗中存在 `el-tree` 权限树（复选框选择）。

---

## 3) 稳定 Selector（用于截图/自动化等待）

- `div:has-text("角色管理")`
- `.app-container`
- `.el-tree`（新增/编辑弹窗中出现）

---

## 4) 关键交互（Interactions）

E2E 覆盖的最小交互：
- 新增：填写“角色名称/权限字符/角色顺序” → 勾选权限树 → “确 定” → “新增成功”
- 搜索：按 placeholder 输入角色名称/权限字符 → “搜索”
- 修改：表格行内修改 → 填写备注 → “确 定” → “修改成功”
- 状态切换：switch → 确认
- 删除：删除 → 确认 → “删除成功”
