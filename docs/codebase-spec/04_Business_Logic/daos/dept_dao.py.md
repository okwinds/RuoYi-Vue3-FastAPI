# dept_dao.py（DAO）

## Source
- Source: `ruoyi-fastapi-backend/module_admin/dao/dept_dao.py`

## Imports（依赖概览）

```python
from collections.abc import Sequence
from sqlalchemy import ColumnElement, bindparam, func, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.util import immutabledict
from module_admin.entity.do.dept_do import SysDept
from module_admin.entity.do.user_do import SysUser
from module_admin.entity.vo.dept_vo import DeptModel
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `get_dept_by_id` | Y | `AsyncSession db, int dept_id` | `SysDept \| None` | 根据部门id获取在用部门信息 |  |  |
| `get_dept_detail_by_id` | Y | `AsyncSession db, int dept_id` | `SysDept \| None` | 根据部门id获取部门详细信息 |  |  |
| `get_dept_detail_by_info` | Y | `AsyncSession db, DeptModel dept` | `SysDept \| None` | 根据部门参数获取部门信息 |  |  |
| `get_dept_info_for_edit_option` | Y | `AsyncSession db, DeptModel dept_info, ColumnElement data_scope_sql` | `Sequence[SysDept]` | 获取部门编辑对应的在用部门列表信息 |  |  |
| `get_children_dept_dao` | Y | `AsyncSession db, int dept_id` | `Sequence[SysDept]` | 根据部门id查询当前部门的子部门列表信息 |  |  |
| `get_dept_list_for_tree` | Y | `AsyncSession db, DeptModel dept_info, ColumnElement data_scope_sql` | `Sequence[SysDept]` | 获取所有在用部门列表信息 |  |  |
| `get_dept_list` | Y | `AsyncSession db, DeptModel page_object, ColumnElement data_scope_sql` | `Sequence[SysDept]` | 根据查询参数获取部门列表信息 |  |  |
| `add_dept_dao` | Y | `AsyncSession db, DeptModel dept` | `SysDept` | 新增部门数据库操作 |  |  |
| `edit_dept_dao` | Y | `AsyncSession db, dict dept` | `None` | 编辑部门数据库操作 |  |  |
| `update_dept_children_dao` | Y | `AsyncSession db, list update_dept` | `None` | 更新子部门信息 |  |  |
| `update_dept_status_normal_dao` | Y | `AsyncSession db, list dept_id_list` | `None` | 批量更新部门状态为正常 |  |  |
| `delete_dept_dao` | Y | `AsyncSession db, DeptModel dept` | `None` | 删除部门数据库操作 |  |  |
| `count_normal_children_dept_dao` | Y | `AsyncSession db, int dept_id` | `int \| None` | 根据部门id查询查询所有子部门（正常状态）的数量 |  |  |
| `count_children_dept_dao` | Y | `AsyncSession db, int dept_id` | `int \| None` | 根据部门id查询查询所有子部门（所有状态）的数量 |  |  |
| `count_dept_user_dao` | Y | `AsyncSession db, int dept_id` | `int \| None` | 根据部门id查询查询部门下的用户数量 |  |  |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
