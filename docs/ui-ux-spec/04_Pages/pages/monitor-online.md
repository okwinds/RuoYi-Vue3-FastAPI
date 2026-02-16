# Page Spec: 在线用户（monitor-online）

PageId：`monitor-online`  
Route：`/monitor/online`

Source：
- `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue`
- E2E：`ruoyi-fastapi-test/monitor/test_online_user.py`

视觉基线（截图 ID）：
- `light_1_monitor-online.png`
- `dark_1_monitor-online.png`

---

## 1) 目的（Purpose）

展示当前在线用户会话列表，并支持“强退”操作。

---

## 2) 像素级结构（Structure）

模板：
- Search Form（用户名称等）
- Table（在线会话列表）
- 操作列：强退按钮

---

## 3) 稳定 Selector（用于截图/自动化等待）

- `.app-container`
- `div:has-text("在线用户")`（若页面标题文本存在）
- `button:has-text("搜索")`

---

## 4) 关键交互（Interactions）

E2E 覆盖：
- 搜索用户名（输入 + 搜索按钮）
- 表格存在行时：点击“强退” → 确认 → 出现“删除成功”

复刻要求：
- “强退”按钮文案必须为“强退”，确认按钮文案为“确定”。
