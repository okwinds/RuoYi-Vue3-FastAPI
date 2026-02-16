# Page Spec: 菜单管理（system-menu）

PageId：`system-menu`  
Route：`/system/menu`

Source：
- `ruoyi-fastapi-frontend/src/views/system/menu/index.vue`
- E2E：`ruoyi-fastapi-test/system/test_menu_management.py`

视觉基线（截图 ID）：
- `light_1_system-menu.png`
- `dark_1_system-menu.png`

---

## 1) 目的（Purpose）

菜单管理页面以树表格（tree table）的形式管理目录/菜单/按钮等层级结构，支持：
- 新增目录
- 在目录下新增子菜单
- 修改菜单路由
- 删除菜单

---

## 2) 像素级结构（Structure）

页面骨架（模板）：
1) Search Form（菜单名称）
2) Toolbar（新增/展开/折叠等）
3) Tree Table（层级展示）
4) Dialog（新增/修改）

---

## 3) 稳定 Selector（用于截图/自动化等待）

- `div:has-text("菜单管理")`
- `.app-container`
- `tbody tr`（树表格行）

---

## 4) 关键交互（Interactions）

E2E 覆盖的最小交互：
- 新增目录：页面顶部“新增” → 弹窗 → 填写“显示排序/菜单名称/路由地址” → “确 定”
- 新增子菜单：在父级行内点“新增” → 弹窗 → 选择“菜单”类型 → 填写 → “确 定”
- 修改：行内“修改” → 修改路由地址 → “确 定”
- 删除：行内“删除” → 确认 → “删除成功”
