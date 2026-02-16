# Excel 导入/导出集成规格（可复刻级）

本文件描述本仓库 Excel 的生成策略与格式约束，目标是让复刻者在不依赖当前实现库（pandas/openpyxl）的情况下，也能生成“用户可接受且字段语义一致”的 Excel 文件。

---

## 1) 依赖与实现入口

当前实现使用：
- `pandas.DataFrame.to_excel(engine='openpyxl')` 输出二进制
- `openpyxl` 用于生成模板（表头样式、列宽、下拉选择器）

Source：
- Source: `ruoyi-fastapi-backend/utils/excel_util.py`

---

## 2) 列表导出（export_list2excel）

输入：
- `list_data`：list[dict]（通常为 service 查询出的字典列表）
- `mapping_dict`：dict[str, str]，将“英文 key”映射为“中文列名”

输出：
- bytes：xlsx 文件二进制

关键规则（复刻必须项）：
1) 先做字段映射：
   - 对 `list_data` 中每一项，按 mapping_dict 的 key 顺序取值
   - 输出的列名使用 mapping_dict 的 value（中文）
2) 用 DataFrame 输出：
   - `index=False`
   - `engine='openpyxl'`

Source：
- Source: `ruoyi-fastapi-backend/utils/excel_util.py`

复刻提示：
- 导出字段的“中文列名”是前端/用户侧可见契约，建议视为稳定接口的一部分（尤其是后台导出回归）。

---

## 3) Excel 模板生成（get_excel_template）

输入：
- `header_list`：表头（按列顺序）
- `selector_header_list`：需要变成“下拉选择器”的表头列名列表
- `option_list`：list[dict]，每个 dict 的 key 是表头列名，value 是选项数组

输出：
- bytes：xlsx 模板二进制

关键规则（复刻必须项）：
1) 表头写入第 1 行
2) 表头样式：
   - 填充色：`ababab`（灰）
   - 水平居中
3) 列宽：
   - 固定 `12`
4) 下拉选择器：
   - 对每个 selector header，创建 `DataValidation(type='list', formula1="\"a,b,c\"")`
   - 覆盖行范围：`2..1048576`（Excel 最大行）

Source：
- Source: `ruoyi-fastapi-backend/utils/excel_util.py`

---

## 4) 使用点（典型 service）

本仓库多个模块有“导出”能力，常见模式为：
- service 先把状态枚举映射为中文（例如 `Y/N` → `是/否`）
- 构造 mapping_dict（字段名 → 中文列名）
- 调用 `ExcelUtil.export_list2excel(...)` 返回 bytes

Source（示例）：
- Source: `ruoyi-fastapi-backend/module_admin/service/config_service.py`
- Source: `ruoyi-fastapi-backend/module_admin/service/dict_service.py`

---

## 5) 验收与测试计划

- [ ] 导出文件能被 Excel/WPS 正常打开
- [ ] 表头中文列名与 mapping_dict 对齐
- [ ] 模板下拉选择器在第 2 行开始生效，且覆盖到最大行（便于批量导入）

