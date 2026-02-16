# API Endpoints（接口清单）

本文件通过 **静态解析 controller 源码** 生成，用于列出后端 FastAPI 的路由与接口。

重要说明：
- 后端会在启动时通过 `common.router.auto_register_routers()` 自动注册所有 `*/controller/*.py` 中的 `APIRouter` / `APIRouterPro` 实例。
- 对外可访问路径通常会叠加反向代理前缀（`APP_ROOT_PATH`），例如开发环境默认 `/dev-api`。
- 本清单只覆盖 controller 层的 HTTP API；不包含 WebSocket（如有）。

来源：
- 路由注册：`ruoyi-fastapi-backend/common/router.py`
- Controllers：`ruoyi-fastapi-backend/*/controller/*.py`

---

## 1) 路由组（Router）概览

| Router 变量 | 类型 | prefix | tags | order_num | auto_register | Source |
| --- | --- | --- | --- | --- | --- | --- |
| cache_controller | APIRouterPro | /monitor/cache | 系统监控-缓存监控 | 15 |  | ruoyi-fastapi-backend/module_admin/controller/cache_controller.py |
| captcha_controller | APIRouterPro | (none) | 验证码模块 | 2 |  | ruoyi-fastapi-backend/module_admin/controller/captcha_controller.py |
| common_controller | APIRouterPro | /common | 通用模块 | 16 |  | ruoyi-fastapi-backend/module_admin/controller/common_controller.py |
| config_controller | APIRouterPro | /system/config | 系统管理-参数管理 | 9 |  | ruoyi-fastapi-backend/module_admin/controller/config_controller.py |
| dept_controller | APIRouterPro | /system/dept | 系统管理-部门管理 | 6 |  | ruoyi-fastapi-backend/module_admin/controller/dept_controller.py |
| dict_controller | APIRouterPro | /system/dict | 系统管理-字典管理 | 8 |  | ruoyi-fastapi-backend/module_admin/controller/dict_controller.py |
| job_controller | APIRouterPro | /monitor | 系统监控-定时任务 | 13 |  | ruoyi-fastapi-backend/module_admin/controller/job_controller.py |
| log_controller | APIRouterPro | /monitor | 系统管理-日志管理 | 11 |  | ruoyi-fastapi-backend/module_admin/controller/log_controller.py |
| login_controller | APIRouterPro | (none) | 登录模块 | 1 |  | ruoyi-fastapi-backend/module_admin/controller/login_controller.py |
| menu_controller | APIRouterPro | /system/menu | 系统管理-菜单管理 | 5 |  | ruoyi-fastapi-backend/module_admin/controller/menu_controller.py |
| notice_controller | APIRouterPro | /system/notice | 系统管理-通知公告管理 | 10 |  | ruoyi-fastapi-backend/module_admin/controller/notice_controller.py |
| online_controller | APIRouterPro | /monitor/online | 系统监控-在线用户 | 12 |  | ruoyi-fastapi-backend/module_admin/controller/online_controller.py |
| post_controller | APIRouterPro | /system/post | 系统管理-岗位管理 | 7 |  | ruoyi-fastapi-backend/module_admin/controller/post_controller.py |
| role_controller | APIRouterPro | /system/role | 系统管理-角色管理 | 4 |  | ruoyi-fastapi-backend/module_admin/controller/role_controller.py |
| server_controller | APIRouterPro | /monitor/server | 系统监控-服务监控 | 14 |  | ruoyi-fastapi-backend/module_admin/controller/server_controller.py |
| user_controller | APIRouterPro | /system/user | 系统管理-用户管理 | 3 |  | ruoyi-fastapi-backend/module_admin/controller/user_controller.py |
| ai_chat_controller | APIRouterPro | /ai/chat | AI管理-AI对话 | 19 |  | ruoyi-fastapi-backend/module_ai/controller/ai_chat_controller.py |
| ai_model_controller | APIRouterPro | /ai/model | AI管理-模型管理 | 18 |  | ruoyi-fastapi-backend/module_ai/controller/ai_model_controller.py |
| gen_controller | APIRouterPro | /tool/gen | 代码生成 | 17 |  | ruoyi-fastapi-backend/module_generator/controller/gen_controller.py |

---

## 2) 接口明细（按 Router 分组）

### cache_controller
- Source: `ruoyi-fastapi-backend/module_admin/controller/cache_controller.py`
- tags: 系统监控-缓存监控
- prefix: `/monitor/cache`
- order_num: `15`

| Method | Path（不含 APP_ROOT_PATH） | Summary | Description | Handler | Source |
| --- | --- | --- | --- | --- | --- |
| GET | /monitor/cache | 获取缓存监控信息接口 | 用于获取缓存监控信息 | get_monitor_cache_info | ruoyi-fastapi-backend/module_admin/controller/cache_controller.py#get_monitor_cache_info |
| DELETE | /monitor/cache/clearCacheAll | 清除所有缓存接口 | 用于清除所有缓存键值对 | clear_monitor_cache_all | ruoyi-fastapi-backend/module_admin/controller/cache_controller.py#clear_monitor_cache_all |
| DELETE | /monitor/cache/clearCacheKey/{cache_key} | 清除缓存键接口 | 用于清除指定缓存键对应的值 | clear_monitor_cache_key | ruoyi-fastapi-backend/module_admin/controller/cache_controller.py#clear_monitor_cache_key |
| DELETE | /monitor/cache/clearCacheName/{cache_name} | 清除缓存名称接口 | 用于清除指定缓存名称下的所有缓存键值对 | clear_monitor_cache_name | ruoyi-fastapi-backend/module_admin/controller/cache_controller.py#clear_monitor_cache_name |
| GET | /monitor/cache/getKeys/{cache_name} | 获取缓存键列表接口 | 用于获取指定缓存名称下的所有缓存键列表 | get_monitor_cache_key | ruoyi-fastapi-backend/module_admin/controller/cache_controller.py#get_monitor_cache_key |
| GET | /monitor/cache/getNames | 获取缓存名称列表接口 | 用于获取缓存名称列表 | get_monitor_cache_name | ruoyi-fastapi-backend/module_admin/controller/cache_controller.py#get_monitor_cache_name |
| GET | /monitor/cache/getValue/{cache_name}/{cache_key} | 获取缓存值接口 | 用于获取指定缓存名称下的指定缓存键对应的值 | get_monitor_cache_value | ruoyi-fastapi-backend/module_admin/controller/cache_controller.py#get_monitor_cache_value |

### captcha_controller
- Source: `ruoyi-fastapi-backend/module_admin/controller/captcha_controller.py`
- tags: 验证码模块
- order_num: `2`

| Method | Path（不含 APP_ROOT_PATH） | Summary | Description | Handler | Source |
| --- | --- | --- | --- | --- | --- |
| GET | /captchaImage | 获取图片验证码接口 | 用于获取图片验证码 | get_captcha_image | ruoyi-fastapi-backend/module_admin/controller/captcha_controller.py#get_captcha_image |

### common_controller
- Source: `ruoyi-fastapi-backend/module_admin/controller/common_controller.py`
- tags: 通用模块
- prefix: `/common`
- order_num: `16`

| Method | Path（不含 APP_ROOT_PATH） | Summary | Description | Handler | Source |
| --- | --- | --- | --- | --- | --- |
| GET | /common/download | 通用文件下载接口 | 用于下载下载目录中的文件 | common_download | ruoyi-fastapi-backend/module_admin/controller/common_controller.py#common_download |
| GET | /common/download/resource | 通用资源文件下载接口 | 用于下载上传目录中的资源文件 | common_download_resource | ruoyi-fastapi-backend/module_admin/controller/common_controller.py#common_download_resource |
| POST | /common/upload | 通用文件上传接口 | 用于上传文件 | common_upload | ruoyi-fastapi-backend/module_admin/controller/common_controller.py#common_upload |

### config_controller
- Source: `ruoyi-fastapi-backend/module_admin/controller/config_controller.py`
- tags: 系统管理-参数管理
- prefix: `/system/config`
- order_num: `9`

| Method | Path（不含 APP_ROOT_PATH） | Summary | Description | Handler | Source |
| --- | --- | --- | --- | --- | --- |
| POST | /system/config | 新增参数接口 | 用于新增参数 | add_system_config | ruoyi-fastapi-backend/module_admin/controller/config_controller.py#add_system_config |
| PUT | /system/config | 编辑参数接口 | 用于编辑参数 | edit_system_config | ruoyi-fastapi-backend/module_admin/controller/config_controller.py#edit_system_config |
| GET | /system/config/configKey/{config_key} | 根据参数键查询参数值接口 | 用于根据参数键从缓存中查询参数值 | query_system_config | ruoyi-fastapi-backend/module_admin/controller/config_controller.py#query_system_config |
| POST | /system/config/export | 导出参数列表接口 | 用于导出当前符合查询条件的参数列表数据 | export_system_config_list | ruoyi-fastapi-backend/module_admin/controller/config_controller.py#export_system_config_list |
| GET | /system/config/list | 获取参数分页列表接口 | 用于获取参数分页列表 | get_system_config_list | ruoyi-fastapi-backend/module_admin/controller/config_controller.py#get_system_config_list |
| DELETE | /system/config/refreshCache | 刷新参数缓存接口 | 用于刷新参数缓存 | refresh_system_config | ruoyi-fastapi-backend/module_admin/controller/config_controller.py#refresh_system_config |
| DELETE | /system/config/{config_ids} | 删除参数接口 | 用于删除参数 | delete_system_config | ruoyi-fastapi-backend/module_admin/controller/config_controller.py#delete_system_config |
| GET | /system/config/{config_id} | 获取参数详情接口 | 用于获取指定参数的详细信息 | query_detail_system_config | ruoyi-fastapi-backend/module_admin/controller/config_controller.py#query_detail_system_config |

### dept_controller
- Source: `ruoyi-fastapi-backend/module_admin/controller/dept_controller.py`
- tags: 系统管理-部门管理
- prefix: `/system/dept`
- order_num: `6`

| Method | Path（不含 APP_ROOT_PATH） | Summary | Description | Handler | Source |
| --- | --- | --- | --- | --- | --- |
| POST | /system/dept | 新增部门接口 | 用于新增部门 | add_system_dept | ruoyi-fastapi-backend/module_admin/controller/dept_controller.py#add_system_dept |
| PUT | /system/dept | 编辑部门接口 | 用于编辑部门 | edit_system_dept | ruoyi-fastapi-backend/module_admin/controller/dept_controller.py#edit_system_dept |
| GET | /system/dept/list | 获取部门列表接口 | 用于获取部门列表 | get_system_dept_list | ruoyi-fastapi-backend/module_admin/controller/dept_controller.py#get_system_dept_list |
| GET | /system/dept/list/exclude/{dept_id} | 获取编辑部门的下拉树接口 | 用于获取部门下拉树，不包含指定部门及其子部门 | get_system_dept_tree_for_edit_option | ruoyi-fastapi-backend/module_admin/controller/dept_controller.py#get_system_dept_tree_for_edit_option |
| DELETE | /system/dept/{dept_ids} | 删除部门接口 | 用于删除部门 | delete_system_dept | ruoyi-fastapi-backend/module_admin/controller/dept_controller.py#delete_system_dept |
| GET | /system/dept/{dept_id} | 获取部门详情接口 | 用于获取指定部门的详情信息 | query_detail_system_dept | ruoyi-fastapi-backend/module_admin/controller/dept_controller.py#query_detail_system_dept |

### dict_controller
- Source: `ruoyi-fastapi-backend/module_admin/controller/dict_controller.py`
- tags: 系统管理-字典管理
- prefix: `/system/dict`
- order_num: `8`

| Method | Path（不含 APP_ROOT_PATH） | Summary | Description | Handler | Source |
| --- | --- | --- | --- | --- | --- |
| POST | /system/dict/data | 新增字典数据接口 | 用于新增字典数据 | add_system_dict_data | ruoyi-fastapi-backend/module_admin/controller/dict_controller.py#add_system_dict_data |
| PUT | /system/dict/data | 编辑字典数据接口 | 用于编辑字典数据 | edit_system_dict_data | ruoyi-fastapi-backend/module_admin/controller/dict_controller.py#edit_system_dict_data |
| POST | /system/dict/data/export | 导出字典数据列表接口 | 用于导出当前符合查询条件的字典数据列表数据 | export_system_dict_data_list | ruoyi-fastapi-backend/module_admin/controller/dict_controller.py#export_system_dict_data_list |
| GET | /system/dict/data/list | 获取字典数据分页列表接口 | 用于获取字典数据分页列表 | get_system_dict_data_list | ruoyi-fastapi-backend/module_admin/controller/dict_controller.py#get_system_dict_data_list |
| GET | /system/dict/data/type/{dict_type} | 获取指定字典类型的数据列表接口 | 用于从缓存中获取指定字典类型的所有数据项 | query_system_dict_type_data | ruoyi-fastapi-backend/module_admin/controller/dict_controller.py#query_system_dict_type_data |
| DELETE | /system/dict/data/{dict_codes} | 删除字典数据接口 | 用于删除字典数据 | delete_system_dict_data | ruoyi-fastapi-backend/module_admin/controller/dict_controller.py#delete_system_dict_data |
| GET | /system/dict/data/{dict_code} | 获取字典数据详情接口 | 用于获取指定字典数据的详细信息 | query_detail_system_dict_data | ruoyi-fastapi-backend/module_admin/controller/dict_controller.py#query_detail_system_dict_data |
| POST | /system/dict/type | 新增字典类型接口 | 用于新增字典类型 | add_system_dict_type | ruoyi-fastapi-backend/module_admin/controller/dict_controller.py#add_system_dict_type |
| PUT | /system/dict/type | 编辑字典类型接口 | 用于编辑字典类型 | edit_system_dict_type | ruoyi-fastapi-backend/module_admin/controller/dict_controller.py#edit_system_dict_type |
| POST | /system/dict/type/export | 导出字典类型列表接口 | 用于导出当前符合查询条件的字典类型列表数据 | export_system_dict_type_list | ruoyi-fastapi-backend/module_admin/controller/dict_controller.py#export_system_dict_type_list |
| GET | /system/dict/type/list | 获取字典类型分页列表接口 | 用于获取字典类型分页列表 | get_system_dict_type_list | ruoyi-fastapi-backend/module_admin/controller/dict_controller.py#get_system_dict_type_list |
| GET | /system/dict/type/optionselect | 获取字典类型下拉列表接口 | 用于获取字典类型下拉列表 | query_system_dict_type_options | ruoyi-fastapi-backend/module_admin/controller/dict_controller.py#query_system_dict_type_options |
| DELETE | /system/dict/type/refreshCache | 刷新字典缓存接口 | 用于刷新字典缓存 | refresh_system_dict | ruoyi-fastapi-backend/module_admin/controller/dict_controller.py#refresh_system_dict |
| DELETE | /system/dict/type/{dict_ids} | 删除字典类型接口 | 用于删除字典类型 | delete_system_dict_type | ruoyi-fastapi-backend/module_admin/controller/dict_controller.py#delete_system_dict_type |
| GET | /system/dict/type/{dict_id} | 获取字典类型详情接口 | 用于获取指定字典类型的详细信息 | query_detail_system_dict_type | ruoyi-fastapi-backend/module_admin/controller/dict_controller.py#query_detail_system_dict_type |

### job_controller
- Source: `ruoyi-fastapi-backend/module_admin/controller/job_controller.py`
- tags: 系统监控-定时任务
- prefix: `/monitor`
- order_num: `13`

| Method | Path（不含 APP_ROOT_PATH） | Summary | Description | Handler | Source |
| --- | --- | --- | --- | --- | --- |
| POST | /monitor/job | 新增定时任务接口 | 用于新增定时任务 | add_system_job | ruoyi-fastapi-backend/module_admin/controller/job_controller.py#add_system_job |
| PUT | /monitor/job | 编辑定时任务接口 | 用于编辑定时任务 | edit_system_job | ruoyi-fastapi-backend/module_admin/controller/job_controller.py#edit_system_job |
| PUT | /monitor/job/changeStatus | 修改定时任务状态接口 | 用于修改定时任务状态 | change_system_job_status | ruoyi-fastapi-backend/module_admin/controller/job_controller.py#change_system_job_status |
| POST | /monitor/job/export | 导出定时任务列表接口 | 用于导出当前符合查询条件的定时任务列表数据 | export_system_job_list | ruoyi-fastapi-backend/module_admin/controller/job_controller.py#export_system_job_list |
| GET | /monitor/job/list | 获取定时任务分页列表接口 | 用于获取定时任务分页列表 | get_system_job_list | ruoyi-fastapi-backend/module_admin/controller/job_controller.py#get_system_job_list |
| PUT | /monitor/job/run | 执行定时任务接口 | 用于执行指定的定时任务 | execute_system_job | ruoyi-fastapi-backend/module_admin/controller/job_controller.py#execute_system_job |
| DELETE | /monitor/job/{job_ids} | 删除定时任务接口 | 用于删除定时任务 | delete_system_job | ruoyi-fastapi-backend/module_admin/controller/job_controller.py#delete_system_job |
| GET | /monitor/job/{job_id} | 获取定时任务详情接口 | 用于获取指定定时任务的详情信息 | query_detail_system_job | ruoyi-fastapi-backend/module_admin/controller/job_controller.py#query_detail_system_job |
| DELETE | /monitor/jobLog/clean | 清空定时任务调度日志接口 | 用于清空所有定时任务调度日志 | clear_system_job_log | ruoyi-fastapi-backend/module_admin/controller/job_controller.py#clear_system_job_log |
| POST | /monitor/jobLog/export | 导出定时任务调度日志列表接口 | 用于导出当前符合查询条件的定时任务调度日志列表数据 | export_system_job_log_list | ruoyi-fastapi-backend/module_admin/controller/job_controller.py#export_system_job_log_list |
| GET | /monitor/jobLog/list | 获取定时任务调度日志分页列表接口 | 用于获取定时任务调度日志分页列表 | get_system_job_log_list | ruoyi-fastapi-backend/module_admin/controller/job_controller.py#get_system_job_log_list |
| DELETE | /monitor/jobLog/{job_log_ids} | 删除定时任务调度日志接口 | 用于删除定时任务调度日志 | delete_system_job_log | ruoyi-fastapi-backend/module_admin/controller/job_controller.py#delete_system_job_log |

### log_controller
- Source: `ruoyi-fastapi-backend/module_admin/controller/log_controller.py`
- tags: 系统管理-日志管理
- prefix: `/monitor`
- order_num: `11`

| Method | Path（不含 APP_ROOT_PATH） | Summary | Description | Handler | Source |
| --- | --- | --- | --- | --- | --- |
| DELETE | /monitor/logininfor/clean | 清空登录日志接口 | 用于清空所有登录日志 | clear_system_login_log | ruoyi-fastapi-backend/module_admin/controller/log_controller.py#clear_system_login_log |
| POST | /monitor/logininfor/export | 导出登录日志接口 | 用于导出当前符合查询条件的登录日志数据 | export_system_login_log_list | ruoyi-fastapi-backend/module_admin/controller/log_controller.py#export_system_login_log_list |
| GET | /monitor/logininfor/list | 获取登录日志分页列表接口 | 用于获取登录日志分页列表 | get_system_login_log_list | ruoyi-fastapi-backend/module_admin/controller/log_controller.py#get_system_login_log_list |
| GET | /monitor/logininfor/unlock/{user_name} | 解锁账户接口 | 用于解锁指定用户账户 | unlock_system_user | ruoyi-fastapi-backend/module_admin/controller/log_controller.py#unlock_system_user |
| DELETE | /monitor/logininfor/{info_ids} | 删除登录日志接口 | 用于删除登录日志 | delete_system_login_log | ruoyi-fastapi-backend/module_admin/controller/log_controller.py#delete_system_login_log |
| DELETE | /monitor/operlog/clean | 清空操作日志接口 | 用于清空所有操作日志 | clear_system_operation_log | ruoyi-fastapi-backend/module_admin/controller/log_controller.py#clear_system_operation_log |
| POST | /monitor/operlog/export | 导出操作日志接口 | 用于导出当前符合查询条件的操作日志数据 | export_system_operation_log_list | ruoyi-fastapi-backend/module_admin/controller/log_controller.py#export_system_operation_log_list |
| GET | /monitor/operlog/list | 获取操作日志分页列表接口 | 用于获取操作日志分页列表 | get_system_operation_log_list | ruoyi-fastapi-backend/module_admin/controller/log_controller.py#get_system_operation_log_list |
| DELETE | /monitor/operlog/{oper_ids} | 删除操作日志接口 | 用于删除操作日志 | delete_system_operation_log | ruoyi-fastapi-backend/module_admin/controller/log_controller.py#delete_system_operation_log |

### login_controller
- Source: `ruoyi-fastapi-backend/module_admin/controller/login_controller.py`
- tags: 登录模块
- order_num: `1`

| Method | Path（不含 APP_ROOT_PATH） | Summary | Description | Handler | Source |
| --- | --- | --- | --- | --- | --- |
| GET | /getInfo | 获取用户信息接口 | 用于获取当前登录用户的信息 | get_login_user_info | ruoyi-fastapi-backend/module_admin/controller/login_controller.py#get_login_user_info |
| GET | /getRouters | 获取用户路由接口 | 用于获取当前登录用户的路由信息 | get_login_user_routers | ruoyi-fastapi-backend/module_admin/controller/login_controller.py#get_login_user_routers |
| POST | /login | 登录接口 | 用于用户登录 | login | ruoyi-fastapi-backend/module_admin/controller/login_controller.py#login |
| POST | /logout | 退出登录接口 | 用于用户退出登录 | logout | ruoyi-fastapi-backend/module_admin/controller/login_controller.py#logout |
| POST | /register | 注册接口 | 用于用户注册 | register_user | ruoyi-fastapi-backend/module_admin/controller/login_controller.py#register_user |

### menu_controller
- Source: `ruoyi-fastapi-backend/module_admin/controller/menu_controller.py`
- tags: 系统管理-菜单管理
- prefix: `/system/menu`
- order_num: `5`

| Method | Path（不含 APP_ROOT_PATH） | Summary | Description | Handler | Source |
| --- | --- | --- | --- | --- | --- |
| POST | /system/menu | 新增菜单接口 | 用于新增菜单 | add_system_menu | ruoyi-fastapi-backend/module_admin/controller/menu_controller.py#add_system_menu |
| PUT | /system/menu | 编辑菜单接口 | 用于编辑菜单 | edit_system_menu | ruoyi-fastapi-backend/module_admin/controller/menu_controller.py#edit_system_menu |
| GET | /system/menu/list | 获取菜单列表接口 | 用于获取当前用户可见的菜单列表 | get_system_menu_list | ruoyi-fastapi-backend/module_admin/controller/menu_controller.py#get_system_menu_list |
| GET | /system/menu/roleMenuTreeselect/{role_id} | 获取角色菜单树接口 | 用于获取指定角色可见的菜单树 | get_system_role_menu_tree | ruoyi-fastapi-backend/module_admin/controller/menu_controller.py#get_system_role_menu_tree |
| GET | /system/menu/treeselect | 获取菜单树接口 | 用于获取当前用户可见的菜单树 | get_system_menu_tree | ruoyi-fastapi-backend/module_admin/controller/menu_controller.py#get_system_menu_tree |
| DELETE | /system/menu/{menu_ids} | 删除菜单接口 | 用于删除菜单 | delete_system_menu | ruoyi-fastapi-backend/module_admin/controller/menu_controller.py#delete_system_menu |
| GET | /system/menu/{menu_id} | 获取菜单详情接口 | 用于获取指定菜单的详情信息 | query_detail_system_menu | ruoyi-fastapi-backend/module_admin/controller/menu_controller.py#query_detail_system_menu |

### notice_controller
- Source: `ruoyi-fastapi-backend/module_admin/controller/notice_controller.py`
- tags: 系统管理-通知公告管理
- prefix: `/system/notice`
- order_num: `10`

| Method | Path（不含 APP_ROOT_PATH） | Summary | Description | Handler | Source |
| --- | --- | --- | --- | --- | --- |
| POST | /system/notice | 新增通知公告接口 | 用于新增通知公告 | add_system_notice | ruoyi-fastapi-backend/module_admin/controller/notice_controller.py#add_system_notice |
| PUT | /system/notice | 编辑通知公告接口 | 用于编辑通知公告 | edit_system_notice | ruoyi-fastapi-backend/module_admin/controller/notice_controller.py#edit_system_notice |
| GET | /system/notice/list | 获取通知公告分页列表接口 | 用于获取通知公告分页列表 | get_system_notice_list | ruoyi-fastapi-backend/module_admin/controller/notice_controller.py#get_system_notice_list |
| DELETE | /system/notice/{notice_ids} | 删除通知公告接口 | 用于删除通知公告 | delete_system_notice | ruoyi-fastapi-backend/module_admin/controller/notice_controller.py#delete_system_notice |
| GET | /system/notice/{notice_id} | 获取通知公告详情接口 | 用于获取指定通知公告的详细信息 | query_detail_system_post | ruoyi-fastapi-backend/module_admin/controller/notice_controller.py#query_detail_system_post |

### online_controller
- Source: `ruoyi-fastapi-backend/module_admin/controller/online_controller.py`
- tags: 系统监控-在线用户
- prefix: `/monitor/online`
- order_num: `12`

| Method | Path（不含 APP_ROOT_PATH） | Summary | Description | Handler | Source |
| --- | --- | --- | --- | --- | --- |
| GET | /monitor/online/list | 获取在线用户分页列表接口 | 用于获取在线用户分页列表 | get_monitor_online_list | ruoyi-fastapi-backend/module_admin/controller/online_controller.py#get_monitor_online_list |
| DELETE | /monitor/online/{token_ids} | 强退在线用户接口 | 用于强退指定会话编号的在线用户 | delete_monitor_online | ruoyi-fastapi-backend/module_admin/controller/online_controller.py#delete_monitor_online |

### post_controller
- Source: `ruoyi-fastapi-backend/module_admin/controller/post_controller.py`
- tags: 系统管理-岗位管理
- prefix: `/system/post`
- order_num: `7`

| Method | Path（不含 APP_ROOT_PATH） | Summary | Description | Handler | Source |
| --- | --- | --- | --- | --- | --- |
| POST | /system/post | 新增岗位接口 | 用于新增岗位 | add_system_post | ruoyi-fastapi-backend/module_admin/controller/post_controller.py#add_system_post |
| PUT | /system/post | 编辑岗位接口 | 用于编辑岗位 | edit_system_post | ruoyi-fastapi-backend/module_admin/controller/post_controller.py#edit_system_post |
| POST | /system/post/export | 导出岗位列表接口 | 用于导出当前符合查询条件的岗位列表数据 | export_system_post_list | ruoyi-fastapi-backend/module_admin/controller/post_controller.py#export_system_post_list |
| GET | /system/post/list | 获取岗位分页列表接口 | 用于获取岗位分页列表 | get_system_post_list | ruoyi-fastapi-backend/module_admin/controller/post_controller.py#get_system_post_list |
| DELETE | /system/post/{post_ids} | 删除岗位接口 | 用于删除岗位 | delete_system_post | ruoyi-fastapi-backend/module_admin/controller/post_controller.py#delete_system_post |
| GET | /system/post/{post_id} | 获取岗位详情接口 | 用于获取指定岗位的详细信息 | query_detail_system_post | ruoyi-fastapi-backend/module_admin/controller/post_controller.py#query_detail_system_post |

### role_controller
- Source: `ruoyi-fastapi-backend/module_admin/controller/role_controller.py`
- tags: 系统管理-角色管理
- prefix: `/system/role`
- order_num: `4`

| Method | Path（不含 APP_ROOT_PATH） | Summary | Description | Handler | Source |
| --- | --- | --- | --- | --- | --- |
| POST | /system/role | 新增角色接口 | 用于新增角色 | add_system_role | ruoyi-fastapi-backend/module_admin/controller/role_controller.py#add_system_role |
| PUT | /system/role | 编辑角色接口 | 用于编辑角色 | edit_system_role | ruoyi-fastapi-backend/module_admin/controller/role_controller.py#edit_system_role |
| GET | /system/role/authUser/allocatedList | 获取已分配用户分页列表接口 | 用于获取指定角色已分配的用户分页列表 | get_system_allocated_user_list | ruoyi-fastapi-backend/module_admin/controller/role_controller.py#get_system_allocated_user_list |
| PUT | /system/role/authUser/cancel | 取消分配用户给角色接口 | 用于取消指定用户分配给角色 | cancel_system_role_user | ruoyi-fastapi-backend/module_admin/controller/role_controller.py#cancel_system_role_user |
| PUT | /system/role/authUser/cancelAll | 批量取消分配用户给角色接口 | 用于批量取消用户分配给角色 | batch_cancel_system_role_user | ruoyi-fastapi-backend/module_admin/controller/role_controller.py#batch_cancel_system_role_user |
| PUT | /system/role/authUser/selectAll | 分配用户给角色接口 | 用于给指定角色分配用户 | add_system_role_user | ruoyi-fastapi-backend/module_admin/controller/role_controller.py#add_system_role_user |
| GET | /system/role/authUser/unallocatedList | 获取未分配用户分页列表接口 | 用于获取指定角色未分配的用户分页列表 | get_system_unallocated_user_list | ruoyi-fastapi-backend/module_admin/controller/role_controller.py#get_system_unallocated_user_list |
| PUT | /system/role/changeStatus | 修改角色状态接口 | 用于修改角色状态 | reset_system_role_status | ruoyi-fastapi-backend/module_admin/controller/role_controller.py#reset_system_role_status |
| PUT | /system/role/dataScope | 编辑角色数据权限接口 | 用于编辑角色数据权限 | edit_system_role_datascope | ruoyi-fastapi-backend/module_admin/controller/role_controller.py#edit_system_role_datascope |
| GET | /system/role/deptTree/{role_id} | 获取自定义数据权限时可见的部门树接口 | 用于自定义数据权限时获取当前用户可见的部门树 | get_system_role_dept_tree | ruoyi-fastapi-backend/module_admin/controller/role_controller.py#get_system_role_dept_tree |
| POST | /system/role/export | 导出角色列表接口 | 用于导出当前符合查询条件的角色列表数据 | export_system_role_list | ruoyi-fastapi-backend/module_admin/controller/role_controller.py#export_system_role_list |
| GET | /system/role/list | 获取角色分页列表接口 | 用于获取角色分页列表 | get_system_role_list | ruoyi-fastapi-backend/module_admin/controller/role_controller.py#get_system_role_list |
| DELETE | /system/role/{role_ids} | 删除角色接口 | 用于删除角色 | delete_system_role | ruoyi-fastapi-backend/module_admin/controller/role_controller.py#delete_system_role |
| GET | /system/role/{role_id} | 获取角色详情接口 | 用于获取指定角色的详细信息 | query_detail_system_role | ruoyi-fastapi-backend/module_admin/controller/role_controller.py#query_detail_system_role |

### server_controller
- Source: `ruoyi-fastapi-backend/module_admin/controller/server_controller.py`
- tags: 系统监控-服务监控
- prefix: `/monitor/server`
- order_num: `14`

| Method | Path（不含 APP_ROOT_PATH） | Summary | Description | Handler | Source |
| --- | --- | --- | --- | --- | --- |
| GET | /monitor/server | 获取服务器监控信息接口 | 用于获取当前服务器的监控信息 | get_monitor_server_info | ruoyi-fastapi-backend/module_admin/controller/server_controller.py#get_monitor_server_info |

### user_controller
- Source: `ruoyi-fastapi-backend/module_admin/controller/user_controller.py`
- tags: 系统管理-用户管理
- prefix: `/system/user`
- order_num: `3`

| Method | Path（不含 APP_ROOT_PATH） | Summary | Description | Handler | Source |
| --- | --- | --- | --- | --- | --- |
| POST | /system/user | 新增用户接口 | 用于新增用户 | add_system_user | ruoyi-fastapi-backend/module_admin/controller/user_controller.py#add_system_user |
| PUT | /system/user | 编辑用户接口 | 用于编辑用户 | edit_system_user | ruoyi-fastapi-backend/module_admin/controller/user_controller.py#edit_system_user |
| GET | /system/user/ | 获取用户岗位和角色列表接口 | 用于获取当前登录用户可见的岗位和角色列表 | query_detail_system_user | ruoyi-fastapi-backend/module_admin/controller/user_controller.py#query_detail_system_user |
| PUT | /system/user/authRole | 给用户分配角色接口 | 用于给指定用户分配角色 | update_system_role_user | ruoyi-fastapi-backend/module_admin/controller/user_controller.py#update_system_role_user |
| GET | /system/user/authRole/{user_id} | 获取用户已分配角色列表接口 | 用于获取指定用户已分配的角色列表 | get_system_allocated_role_list | ruoyi-fastapi-backend/module_admin/controller/user_controller.py#get_system_allocated_role_list |
| PUT | /system/user/changeStatus | 修改用户状态接口 | 用于修改用户状态 | change_system_user_status | ruoyi-fastapi-backend/module_admin/controller/user_controller.py#change_system_user_status |
| GET | /system/user/deptTree | 获取部门树接口 | 用于获取当前登录用户可见的部门树 | get_system_dept_tree | ruoyi-fastapi-backend/module_admin/controller/user_controller.py#get_system_dept_tree |
| POST | /system/user/export | 导出用户列表接口 | 用于导出当前符合查询条件的用户列表数据 | export_system_user_list | ruoyi-fastapi-backend/module_admin/controller/user_controller.py#export_system_user_list |
| POST | /system/user/importData | 批量导入用户接口 | 用于批量导入用户数据 | batch_import_system_user | ruoyi-fastapi-backend/module_admin/controller/user_controller.py#batch_import_system_user |
| POST | /system/user/importTemplate | 获取用户导入模板接口 | 用于获取用户导入模板excel文件 | export_system_user_template | ruoyi-fastapi-backend/module_admin/controller/user_controller.py#export_system_user_template |
| GET | /system/user/list | 获取用户分页列表接口 | 用于获取用户分页列表 | get_system_user_list | ruoyi-fastapi-backend/module_admin/controller/user_controller.py#get_system_user_list |
| GET | /system/user/profile | 获取用户个人信息接口 | 用于获取当前登录用户的个人信息 | query_detail_system_user_profile | ruoyi-fastapi-backend/module_admin/controller/user_controller.py#query_detail_system_user_profile |
| PUT | /system/user/profile | 修改用户个人信息接口 | 用于修改当前登录用户的个人信息 | change_system_user_profile_info | ruoyi-fastapi-backend/module_admin/controller/user_controller.py#change_system_user_profile_info |
| POST | /system/user/profile/avatar | 修改用户头像接口 | 用于修改当前登录用户的头像 | change_system_user_profile_avatar | ruoyi-fastapi-backend/module_admin/controller/user_controller.py#change_system_user_profile_avatar |
| PUT | /system/user/profile/updatePwd | 修改用户密码接口 | 用于修改当前登录用户的密码 | reset_system_user_password | ruoyi-fastapi-backend/module_admin/controller/user_controller.py#reset_system_user_password |
| PUT | /system/user/resetPwd | 重置用户密码接口 | 用于重置用户密码 | reset_system_user_pwd | ruoyi-fastapi-backend/module_admin/controller/user_controller.py#reset_system_user_pwd |
| DELETE | /system/user/{user_ids} | 删除用户接口 | 用于删除用户 | delete_system_user | ruoyi-fastapi-backend/module_admin/controller/user_controller.py#delete_system_user |
| GET | /system/user/{user_id} | 获取用户详情接口 | 用于获取指定用户的详情信息 | query_detail_system_user | ruoyi-fastapi-backend/module_admin/controller/user_controller.py#query_detail_system_user |

### ai_chat_controller
- Source: `ruoyi-fastapi-backend/module_ai/controller/ai_chat_controller.py`
- tags: AI管理-AI对话
- prefix: `/ai/chat`
- order_num: `19`

| Method | Path（不含 APP_ROOT_PATH） | Summary | Description | Handler | Source |
| --- | --- | --- | --- | --- | --- |
| POST | /ai/chat/cancel | 取消对话 | 取消正在进行的对话 | cancel_chat_run | ruoyi-fastapi-backend/module_ai/controller/ai_chat_controller.py#cancel_chat_run |
| GET | /ai/chat/config | 获取用户对话配置 | 获取当前用户的AI对话配置 | get_user_chat_config | ruoyi-fastapi-backend/module_ai/controller/ai_chat_controller.py#get_user_chat_config |
| PUT | /ai/chat/config | 保存用户对话配置 | 保存当前用户的AI对话配置 | save_user_chat_config | ruoyi-fastapi-backend/module_ai/controller/ai_chat_controller.py#save_user_chat_config |
| POST | /ai/chat/send | 发送对话消息 | 流式返回对话结果 | send_chat_message | ruoyi-fastapi-backend/module_ai/controller/ai_chat_controller.py#send_chat_message |
| GET | /ai/chat/session/list | 获取会话列表 | 获取用户的会话列表 | get_chat_session_list | ruoyi-fastapi-backend/module_ai/controller/ai_chat_controller.py#get_chat_session_list |
| DELETE | /ai/chat/session/{session_id} | 删除会话 | 删除指定会话 | delete_chat_session | ruoyi-fastapi-backend/module_ai/controller/ai_chat_controller.py#delete_chat_session |
| GET | /ai/chat/session/{session_id} | 获取会话消息详情 | 获取指定会话的消息详情 | get_chat_session_detail | ruoyi-fastapi-backend/module_ai/controller/ai_chat_controller.py#get_chat_session_detail |

### ai_model_controller
- Source: `ruoyi-fastapi-backend/module_ai/controller/ai_model_controller.py`
- tags: AI管理-模型管理
- prefix: `/ai/model`
- order_num: `18`

| Method | Path（不含 APP_ROOT_PATH） | Summary | Description | Handler | Source |
| --- | --- | --- | --- | --- | --- |
| POST | /ai/model | 新增AI模型接口 | 用于新增AI模型 | add_ai_model | ruoyi-fastapi-backend/module_ai/controller/ai_model_controller.py#add_ai_model |
| PUT | /ai/model | 编辑AI模型接口 | 用于编辑AI模型 | edit_ai_model | ruoyi-fastapi-backend/module_ai/controller/ai_model_controller.py#edit_ai_model |
| GET | /ai/model/all | 获取AI模型不分页列表接口 | 用于获取AI模型不分页列表 | get_ai_model_all | ruoyi-fastapi-backend/module_ai/controller/ai_model_controller.py#get_ai_model_all |
| GET | /ai/model/list | 获取AI模型分页列表接口 | 用于获取AI模型分页列表 | get_ai_model_list | ruoyi-fastapi-backend/module_ai/controller/ai_model_controller.py#get_ai_model_list |
| DELETE | /ai/model/{model_ids} | 删除AI模型接口 | 用于删除AI模型 | delete_ai_model | ruoyi-fastapi-backend/module_ai/controller/ai_model_controller.py#delete_ai_model |
| GET | /ai/model/{model_id} | 获取AI模型详情接口 | 用于获取指定AI模型的详细信息 | get_ai_model_detail | ruoyi-fastapi-backend/module_ai/controller/ai_model_controller.py#get_ai_model_detail |

### gen_controller
- Source: `ruoyi-fastapi-backend/module_generator/controller/gen_controller.py`
- tags: 代码生成
- prefix: `/tool/gen`
- order_num: `17`

| Method | Path（不含 APP_ROOT_PATH） | Summary | Description | Handler | Source |
| --- | --- | --- | --- | --- | --- |
| PUT | /tool/gen | 编辑代码生成表接口 | 用于编辑代码生成表 | edit_gen_table | ruoyi-fastapi-backend/module_generator/controller/gen_controller.py#edit_gen_table |
| GET | /tool/gen/batchGenCode | 生成代码文件接口 | 用于生成代码文件 | batch_gen_code | ruoyi-fastapi-backend/module_generator/controller/gen_controller.py#batch_gen_code |
| POST | /tool/gen/createTable | 创建数据库表接口 | 用于创建数据库表 | create_table | ruoyi-fastapi-backend/module_generator/controller/gen_controller.py#create_table |
| GET | /tool/gen/db/list | 获取数据库表分页列表接口 | 用于获取数据库表分页列表 | get_gen_db_table_list | ruoyi-fastapi-backend/module_generator/controller/gen_controller.py#get_gen_db_table_list |
| GET | /tool/gen/genCode/{table_name} | 生成代码文件到本地接口 | 用于生成代码文件到本地 | gen_code_local | ruoyi-fastapi-backend/module_generator/controller/gen_controller.py#gen_code_local |
| POST | /tool/gen/importTable | 导入数据库表接口 | 用于导入数据库表 | import_gen_table | ruoyi-fastapi-backend/module_generator/controller/gen_controller.py#import_gen_table |
| GET | /tool/gen/list | 获取代码生成表分页列表接口 | 用于获取代码生成表分页列表 | get_gen_table_list | ruoyi-fastapi-backend/module_generator/controller/gen_controller.py#get_gen_table_list |
| GET | /tool/gen/preview/{table_id} | 预览生成的代码接口 | 用于预览指定代码生成表生成的代码 | preview_code | ruoyi-fastapi-backend/module_generator/controller/gen_controller.py#preview_code |
| GET | /tool/gen/synchDb/{table_name} | 同步数据库接口 | 用于同步指定数据库信息到指定代码生成表 | sync_db | ruoyi-fastapi-backend/module_generator/controller/gen_controller.py#sync_db |
| DELETE | /tool/gen/{table_ids} | 删除代码生成表接口 | 用于删除代码生成表 | delete_gen_table | ruoyi-fastapi-backend/module_generator/controller/gen_controller.py#delete_gen_table |
| GET | /tool/gen/{table_id} | 获取代码生成表详情接口 | 用于获取指定代码生成表的详细信息 | query_detail_gen_table | ruoyi-fastapi-backend/module_generator/controller/gen_controller.py#query_detail_gen_table |
