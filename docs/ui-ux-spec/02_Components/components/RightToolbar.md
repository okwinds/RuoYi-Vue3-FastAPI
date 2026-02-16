# RightToolbar（表格右侧工具条）

Source：
- `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue`

---

## 1) Purpose（目的）

RightToolbar 用于列表页（CRUD List）顶部右侧的“搜索显隐 + 刷新 + 列显隐”组合交互，典型搭配：
- 搜索表单（可隐藏）
- 表格列配置（可动态显隐）
- 列表刷新（重新 query）

---

## 2) Props / Emits 契约

Props：
- `showSearch`（bool，default=true）：是否显示搜索条件
- `columns`（Array/Object，default={}）：列配置
- `search`（bool，default=true）：是否显示“搜索显隐”按钮
- `showColumnsType`（string，default="checkbox"）：`checkbox` 或 `transfer`
- `gutter`（number，default=10）：右外边距（计算为 `marginRight = gutter/2`）

Emits：
- `update:showSearch`：切换搜索区域显隐
- `queryTable`：触发父页面刷新

---

## 3) 列显隐数据结构（Columns Shape）

支持两种输入形态：

### 3.1 Object 形态（推荐）

约束（每列）：
- `label`：显示名
- `visible`：是否展示

示例：
```js
const columns = {
  userName: { label: '用户名称', visible: true },
  nickName: { label: '用户昵称', visible: true }
}
```

### 3.2 Array 形态

约束：
- 每项必须包含 `key`（用于与 transfer/checkbox 对齐）与 `visible`

---

## 4) 两种列显隐模式

### 4.1 checkbox（默认）

UI：
- `el-dropdown` + `el-dropdown-menu`
- 顶部有“列展示”全选/半选 checkbox

逻辑：
- `isChecked`：全部 visible = true
- `isIndeterminate`：部分 visible = true
- `toggleCheckAll`：全选/反选（对 columns 全量写 visible）
- `checkboxChange(event, key)`：单项切换

### 4.2 transfer

UI：
- `el-dialog` + `el-transfer`
- `value` 存储“隐藏列”的 key/index

逻辑：
- `dataChange(data)`：根据 data 反推各列 visible

---

## 5) 与列表页模式的绑定点（Patterns）

RightToolbar 与页面的最小绑定契约：
- 页面使用 `v-model:showSearch` 控制搜索表单容器显隐
- 页面维护 `columns` 并在 `<el-table-column>` 上按 `columns.xxx.visible` 控制展示
- 页面监听 `queryTable` 来重新拉取列表数据

对应页面模式详述见：
- `docs/ui-ux-spec/03_Patterns/PATTERNS.md`
