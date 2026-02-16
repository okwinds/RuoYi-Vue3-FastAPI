# dept_service.py（Service）

## Source
- Source: `ruoyi-fastapi-backend/module_admin/service/dept_service.py`

## Imports（依赖概览）

```python
from collections.abc import Sequence
from typing import Any
from sqlalchemy import ColumnElement
from sqlalchemy.ext.asyncio import AsyncSession
from common.constant import CommonConstant
from common.vo import CrudResponseModel
from exceptions.exception import ServiceException, ServiceWarning
from module_admin.dao.dept_dao import DeptDao
from module_admin.entity.do.dept_do import SysDept
from module_admin.entity.vo.dept_vo import DeleteDeptModel, DeptModel, DeptTreeModel
from utils.common_util import CamelCaseUtil
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `get_dept_tree_services` | Y | `AsyncSession query_db, DeptModel page_object, ColumnElement data_scope_sql` | `list[dict[str, Any]]` | 获取部门树信息service | DeptDao.get_dept_list_for_tree |  |
| `get_dept_for_edit_option_services` | Y | `AsyncSession query_db, DeptModel page_object, ColumnElement data_scope_sql` | `list[dict[str, Any]]` | 获取部门编辑部门树信息service | DeptDao.get_dept_info_for_edit_option |  |
| `get_dept_list_services` | Y | `AsyncSession query_db, DeptModel page_object, ColumnElement data_scope_sql` | `list[dict[str, Any]]` | 获取部门列表信息service | DeptDao.get_dept_list |  |
| `check_dept_data_scope_services` | Y | `AsyncSession query_db, int dept_id, ColumnElement data_scope_sql` | `CrudResponseModel` | 校验部门是否有数据权限service | DeptDao.get_dept_list | '没有权限访问部门数据' |
| `check_dept_name_unique_services` | Y | `AsyncSession query_db, DeptModel page_object` | `bool` | 校验部门名称是否唯一service | DeptDao.get_dept_detail_by_info |  |
| `add_dept_services` | Y | `AsyncSession query_db, DeptModel page_object` | `CrudResponseModel` | 新增部门信息service | DeptDao.add_dept_dao, DeptDao.get_dept_by_id | f'新增部门{page_object.dept_name}失败，部门名称已存在'; f'部门{parent_info.dept_name}停用，不允许新增' |
| `edit_dept_services` | Y | `AsyncSession query_db, DeptModel page_object` | `CrudResponseModel` | 编辑部门信息service | DeptDao.count_normal_children_dept_dao, DeptDao.edit_dept_dao, DeptDao.get_dept_by_id | f'修改部门{page_object.dept_name}失败，部门名称已存在'; f'修改部门{page_object.dept_name}失败，上级部门不能是自己'; f'修改部门{page_object.dept_name}失败，该部门包含未停用的子部门' |
| `delete_dept_services` | Y | `AsyncSession query_db, DeleteDeptModel page_object` | `CrudResponseModel` | 删除部门信息service | DeptDao.count_children_dept_dao, DeptDao.count_dept_user_dao, DeptDao.delete_dept_dao | '传入部门id为空' |
| `dept_detail_services` | Y | `AsyncSession query_db, int dept_id` | `DeptModel` | 获取部门详细信息service | DeptDao.get_dept_detail_by_id |  |
| `list_to_tree` | N | `Sequence[SysDept] permission_list` | `list[DeptTreeModel]` | 工具方法：根据部门列表信息生成树形嵌套数据 |  |  |
| `replace_first` | Y | `str original_str, str old_str, str new_str` | `str` | 工具方法：替换字符串 |  |  |
| `update_parent_dept_status_normal` | Y | `AsyncSession query_db, DeptModel dept` | `None` | 更新父部门状态为正常 | DeptDao.update_dept_status_normal_dao |  |
| `update_dept_children` | Y | `AsyncSession query_db, int dept_id, str new_ancestors, str old_ancestors` | `None` | 更新子部门信息 | DeptDao.get_children_dept_dao, DeptDao.update_dept_children_dao |  |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
