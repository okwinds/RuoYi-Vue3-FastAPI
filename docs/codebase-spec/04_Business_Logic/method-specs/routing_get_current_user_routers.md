# Method Spec：LoginService.get_current_user_routers（可复刻级）

目标：把“菜单表/权限”转换为前端可用的 Router 树（动态路由下发），并保持路径/组件/meta 规则等价。

Source：
- Source: `ruoyi-fastapi-backend/module_admin/service/login_service.py`
- Source: `ruoyi-fastapi-backend/common/constant.py`
- Source: `ruoyi-fastapi-backend/module_admin/entity/vo/login_vo.py`

---

## 1) 输入输出

输入：
- `user_id`
- `query_db`

依赖数据：
- `UserDao.get_user_by_id(...)` 返回 `user_menu_info`（菜单列表，含 menu_type/order_num/path/component/visible/is_cache/is_frame 等）

输出：
- `list[dict]`：每个元素是 `RouterModel` 的 dict（`by_alias=True`），供前端动态注册路由。

---

## 2) 过滤与排序规则（必须一致）

只保留 menu_type 属于：
- `TYPE_DIR`（目录）
- `TYPE_MENU`（菜单）

并按 `order_num` 升序排序。

Source：
- Source: `ruoyi-fastapi-backend/module_admin/service/login_service.py`

---

## 3) 菜单树生成（__generate_menus）

输入：`pid`（初始 0）与扁平菜单列表

规则：
- 对每个 menu，若 `menu.parent_id == pid`：
  - 递归生成 children（pid=menu.menu_id）
  - 转成 `MenuTreeModel(**CamelCaseUtil.transform_result(menu))`
  - children 非空则挂载

输出：树形 `MenuTreeModel` 列表

---

## 4) Router 树生成（__generate_user_router_menu）

对每个 `permission: MenuTreeModel` 生成一个 `RouterModel`，核心字段：

- `hidden = (permission.visible == '1')`
- `name = RouterUtil.get_router_name(permission)`
- `path = RouterUtil.get_router_path(permission)`
- `component = RouterUtil.get_component(permission)`
- `query = permission.query`
- `meta`：
  - `title = permission.menu_name`
  - `icon = permission.icon`
  - `noCache = (permission.is_cache == 1)`
  - `link = permission.path if RouterUtil.is_http(permission.path) else None`

然后根据三类分支改写：

### 4.1 目录且有子菜单

条件：`c_menus` 存在且 `permission.menu_type == TYPE_DIR`
- `always_show = True`
- `redirect = 'noRedirect'`
- `children = recurse(c_menus)`

### 4.2 菜单内部跳转（is_menu_frame）

条件：`permission.parent_id == 0 and permission.menu_type == TYPE_MENU and permission.is_frame == NO_FRAME`
- `router.meta = None`
- router.children 仅包含 1 个子 route：
  - `path = permission.path`
  - `component = permission.component`
  - `name = RouterUtil.get_route_name(permission.route_name, permission.path)`
  - `meta` 同上

### 4.3 一级内链（parent_id==0 且 is_inner_link）

条件：`permission.parent_id==0 and permission.is_frame==NO_FRAME and is_http(permission.path)`
- `router.meta = {title, icon}`
- `router.path = '/'`
- children 仅包含 1 个子 route：
  - `path = RouterUtil.inner_link_replace_each(permission.path)`
  - `component = INNER_LINK`
  - `name = RouterUtil.get_route_name(permission.route_name, permission.path)`
  - `meta = {title, icon, link}`

Source：
- Source: `ruoyi-fastapi-backend/module_admin/service/login_service.py`

---

## 5) RouterUtil 关键规则（复刻必须项）

- `get_route_name(name, path)`：`name if name else path`，并 `capitalize()`
- `get_router_path(menu)`：
  - 若 `menu.parent_id != 0` 且 `is_inner_link(menu)`：path = `inner_link_replace_each(menu.path)`
  - 若一级目录（menu_type==DIR 且 NO_FRAME）：path = `/{menu.path}`
  - 若 `is_menu_frame(menu)`：path = `/`
- `get_component(menu)`：
  - 默认 `LAYOUT`
  - 若 `menu.component` 非空且非 menu_frame：取 menu.component
  - 若 component 为空且内链：`INNER_LINK`
  - 若 component 为空且 parent_view：`PARENT_VIEW`
- `inner_link_replace_each(path)`：依次替换：
  - `http://`, `https://`, `www`, `.`, `:` → `'', '', '', '/', '/'`

Source：
- Source: `ruoyi-fastapi-backend/module_admin/service/login_service.py`
- Source: `ruoyi-fastapi-backend/common/constant.py`

---

## 6) 验收与测试计划

- [ ] 给定同一套菜单数据，输出 Router 树的 path/component/meta 与现仓库一致
- [ ] 一级内链会生成 `path='/'` 的父 route + 单子 route（inner_link path 替换规则一致）
- [ ] menu_frame 产生 `path='/'` 且 meta=None 的父 route（子 route 指向真实页面 component）

