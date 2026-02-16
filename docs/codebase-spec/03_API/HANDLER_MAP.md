# Handler Map（Endpoint → Controller → Service.method）

generated: `2026-02-14 18:15:18`

用途：把接口（endpoint）与其实现入口（controller + service 方法）稳定对齐，便于：
- 从任意 endpoint 反查到 controller handler 与 service 入口；
- 将字段级契约（`openapi.json`）与“内部等价复刻”方法规格连接起来；
- 做审查抽样与回归定位。

生成方式（可复跑）：

```bash
python tools/spec/gen_handler_map.py \
  --backend-root ruoyi-fastapi-backend \
  --out docs/codebase-spec/03_API/HANDLER_MAP.md
```

说明：
- 该映射通过 AST 静态解析 controller 文件生成，为启发式结果；当 `service_calls` 为空时，通常表示业务逻辑被封装在 helper/依赖注入中，需要人工补齐。
- 扫描 controller 文件数：`19`；提取路由数：`143`。

## Route Table

| HTTP | Path | Summary | Controller | Handler | Service calls (heuristic) |
| --- | --- | --- | --- | --- | --- |
| `POST` | `/ai/chat/cancel` | 取消对话 | `ruoyi-fastapi-backend/module_ai/controller/ai_chat_controller.py` | `cancel_chat_run` | AiChatService.cancel_run_services |
| `GET` | `/ai/chat/config` | 获取用户对话配置 | `ruoyi-fastapi-backend/module_ai/controller/ai_chat_controller.py` | `get_user_chat_config` | AiChatService.ai_chat_config_detail_services |
| `PUT` | `/ai/chat/config` | 保存用户对话配置 | `ruoyi-fastapi-backend/module_ai/controller/ai_chat_controller.py` | `save_user_chat_config` | AiChatService.save_ai_chat_config_services |
| `POST` | `/ai/chat/send` | 发送对话消息 | `ruoyi-fastapi-backend/module_ai/controller/ai_chat_controller.py` | `send_chat_message` | AiChatService.chat_services |
| `GET` | `/ai/chat/session/list` | 获取会话列表 | `ruoyi-fastapi-backend/module_ai/controller/ai_chat_controller.py` | `get_chat_session_list` | AiChatService.get_chat_session_list_services |
| `DELETE` | `/ai/chat/session/{session_id}` | 删除会话 | `ruoyi-fastapi-backend/module_ai/controller/ai_chat_controller.py` | `delete_chat_session` | AiChatService.delete_chat_session_services |
| `GET` | `/ai/chat/session/{session_id}` | 获取会话消息详情 | `ruoyi-fastapi-backend/module_ai/controller/ai_chat_controller.py` | `get_chat_session_detail` | AiChatService.get_chat_session_detail_services |
| `POST` | `/ai/model` | 新增AI模型接口 | `ruoyi-fastapi-backend/module_ai/controller/ai_model_controller.py` | `add_ai_model` | AiModelService.add_ai_model_services |
| `PUT` | `/ai/model` | 编辑AI模型接口 | `ruoyi-fastapi-backend/module_ai/controller/ai_model_controller.py` | `edit_ai_model` | AiModelService.check_ai_model_data_scope_services<br/>AiModelService.edit_ai_model_services |
| `GET` | `/ai/model/all` | 获取AI模型不分页列表接口 | `ruoyi-fastapi-backend/module_ai/controller/ai_model_controller.py` | `get_ai_model_all` | AiModelService.get_ai_model_list_services |
| `GET` | `/ai/model/list` | 获取AI模型分页列表接口 | `ruoyi-fastapi-backend/module_ai/controller/ai_model_controller.py` | `get_ai_model_list` | AiModelService.get_ai_model_list_services |
| `DELETE` | `/ai/model/{model_ids}` | 删除AI模型接口 | `ruoyi-fastapi-backend/module_ai/controller/ai_model_controller.py` | `delete_ai_model` | AiModelService.check_ai_model_data_scope_services<br/>AiModelService.delete_ai_model_services |
| `GET` | `/ai/model/{model_id}` | 获取AI模型详情接口 | `ruoyi-fastapi-backend/module_ai/controller/ai_model_controller.py` | `get_ai_model_detail` | AiModelService.check_ai_model_data_scope_services<br/>AiModelService.ai_model_detail_services |
| `GET` | `/captchaImage` | 获取图片验证码接口 | `ruoyi-fastapi-backend/module_admin/controller/captcha_controller.py` | `get_captcha_image` | CaptchaService.create_captcha_image_service |
| `GET` | `/common/download` | 通用文件下载接口 | `ruoyi-fastapi-backend/module_admin/controller/common_controller.py` | `common_download` | CommonService.download_services |
| `GET` | `/common/download/resource` | 通用资源文件下载接口 | `ruoyi-fastapi-backend/module_admin/controller/common_controller.py` | `common_download_resource` | CommonService.download_resource_services |
| `POST` | `/common/upload` | 通用文件上传接口 | `ruoyi-fastapi-backend/module_admin/controller/common_controller.py` | `common_upload` | CommonService.upload_service |
| `GET` | `/getInfo` | 获取用户信息接口 | `ruoyi-fastapi-backend/module_admin/controller/login_controller.py` | `get_login_user_info` |  |
| `GET` | `/getRouters` | 获取用户路由接口 | `ruoyi-fastapi-backend/module_admin/controller/login_controller.py` | `get_login_user_routers` | LoginService.get_current_user_routers |
| `POST` | `/login` | 登录接口 | `ruoyi-fastapi-backend/module_admin/controller/login_controller.py` | `login` | LoginService.authenticate_user<br/>LoginService.create_access_token<br/>UserService.edit_user_services |
| `POST` | `/logout` | 退出登录接口 | `ruoyi-fastapi-backend/module_admin/controller/login_controller.py` | `logout` | LoginService.logout_services |
| `GET` | `/monitor/cache` | 获取缓存监控信息接口 | `ruoyi-fastapi-backend/module_admin/controller/cache_controller.py` | `get_monitor_cache_info` | CacheService.get_cache_monitor_statistical_info_services |
| `DELETE` | `/monitor/cache/clearCacheAll` | 清除所有缓存接口 | `ruoyi-fastapi-backend/module_admin/controller/cache_controller.py` | `clear_monitor_cache_all` | CacheService.clear_cache_monitor_all_services |
| `DELETE` | `/monitor/cache/clearCacheKey/{cache_key}` | 清除缓存键接口 | `ruoyi-fastapi-backend/module_admin/controller/cache_controller.py` | `clear_monitor_cache_key` | CacheService.clear_cache_monitor_cache_key_services |
| `DELETE` | `/monitor/cache/clearCacheName/{cache_name}` | 清除缓存名称接口 | `ruoyi-fastapi-backend/module_admin/controller/cache_controller.py` | `clear_monitor_cache_name` | CacheService.clear_cache_monitor_cache_name_services |
| `GET` | `/monitor/cache/getKeys/{cache_name}` | 获取缓存键列表接口 | `ruoyi-fastapi-backend/module_admin/controller/cache_controller.py` | `get_monitor_cache_key` | CacheService.get_cache_monitor_cache_key_services |
| `GET` | `/monitor/cache/getNames` | 获取缓存名称列表接口 | `ruoyi-fastapi-backend/module_admin/controller/cache_controller.py` | `get_monitor_cache_name` | CacheService.get_cache_monitor_cache_name_services |
| `GET` | `/monitor/cache/getValue/{cache_name}/{cache_key}` | 获取缓存值接口 | `ruoyi-fastapi-backend/module_admin/controller/cache_controller.py` | `get_monitor_cache_value` | CacheService.get_cache_monitor_cache_value_services |
| `POST` | `/monitor/job` | 新增定时任务接口 | `ruoyi-fastapi-backend/module_admin/controller/job_controller.py` | `add_system_job` | JobService.add_job_services |
| `PUT` | `/monitor/job` | 编辑定时任务接口 | `ruoyi-fastapi-backend/module_admin/controller/job_controller.py` | `edit_system_job` | JobService.edit_job_services |
| `PUT` | `/monitor/job/changeStatus` | 修改定时任务状态接口 | `ruoyi-fastapi-backend/module_admin/controller/job_controller.py` | `change_system_job_status` | JobService.edit_job_services |
| `POST` | `/monitor/job/export` | 导出定时任务列表接口 | `ruoyi-fastapi-backend/module_admin/controller/job_controller.py` | `export_system_job_list` | JobService.get_job_list_services<br/>JobService.export_job_list_services |
| `GET` | `/monitor/job/list` | 获取定时任务分页列表接口 | `ruoyi-fastapi-backend/module_admin/controller/job_controller.py` | `get_system_job_list` | JobService.get_job_list_services |
| `PUT` | `/monitor/job/run` | 执行定时任务接口 | `ruoyi-fastapi-backend/module_admin/controller/job_controller.py` | `execute_system_job` | JobService.execute_job_once_services |
| `DELETE` | `/monitor/job/{job_ids}` | 删除定时任务接口 | `ruoyi-fastapi-backend/module_admin/controller/job_controller.py` | `delete_system_job` | JobService.delete_job_services |
| `GET` | `/monitor/job/{job_id}` | 获取定时任务详情接口 | `ruoyi-fastapi-backend/module_admin/controller/job_controller.py` | `query_detail_system_job` | JobService.job_detail_services |
| `DELETE` | `/monitor/jobLog/clean` | 清空定时任务调度日志接口 | `ruoyi-fastapi-backend/module_admin/controller/job_controller.py` | `clear_system_job_log` | JobLogService.clear_job_log_services |
| `POST` | `/monitor/jobLog/export` | 导出定时任务调度日志列表接口 | `ruoyi-fastapi-backend/module_admin/controller/job_controller.py` | `export_system_job_log_list` | JobLogService.get_job_log_list_services<br/>JobLogService.export_job_log_list_services |
| `GET` | `/monitor/jobLog/list` | 获取定时任务调度日志分页列表接口 | `ruoyi-fastapi-backend/module_admin/controller/job_controller.py` | `get_system_job_log_list` | JobLogService.get_job_log_list_services |
| `DELETE` | `/monitor/jobLog/{job_log_ids}` | 删除定时任务调度日志接口 | `ruoyi-fastapi-backend/module_admin/controller/job_controller.py` | `delete_system_job_log` | JobLogService.delete_job_log_services |
| `DELETE` | `/monitor/logininfor/clean` | 清空登录日志接口 | `ruoyi-fastapi-backend/module_admin/controller/log_controller.py` | `clear_system_login_log` | LoginLogService.clear_login_log_services |
| `POST` | `/monitor/logininfor/export` | 导出登录日志接口 | `ruoyi-fastapi-backend/module_admin/controller/log_controller.py` | `export_system_login_log_list` | LoginLogService.get_login_log_list_services<br/>LoginLogService.export_login_log_list_services |
| `GET` | `/monitor/logininfor/list` | 获取登录日志分页列表接口 | `ruoyi-fastapi-backend/module_admin/controller/log_controller.py` | `get_system_login_log_list` | LoginLogService.get_login_log_list_services |
| `GET` | `/monitor/logininfor/unlock/{user_name}` | 解锁账户接口 | `ruoyi-fastapi-backend/module_admin/controller/log_controller.py` | `unlock_system_user` | LoginLogService.unlock_user_services |
| `DELETE` | `/monitor/logininfor/{info_ids}` | 删除登录日志接口 | `ruoyi-fastapi-backend/module_admin/controller/log_controller.py` | `delete_system_login_log` | LoginLogService.delete_login_log_services |
| `GET` | `/monitor/online/list` | 获取在线用户分页列表接口 | `ruoyi-fastapi-backend/module_admin/controller/online_controller.py` | `get_monitor_online_list` | OnlineService.get_online_list_services |
| `DELETE` | `/monitor/online/{token_ids}` | 强退在线用户接口 | `ruoyi-fastapi-backend/module_admin/controller/online_controller.py` | `delete_monitor_online` | OnlineService.delete_online_services |
| `DELETE` | `/monitor/operlog/clean` | 清空操作日志接口 | `ruoyi-fastapi-backend/module_admin/controller/log_controller.py` | `clear_system_operation_log` | OperationLogService.clear_operation_log_services |
| `POST` | `/monitor/operlog/export` | 导出操作日志接口 | `ruoyi-fastapi-backend/module_admin/controller/log_controller.py` | `export_system_operation_log_list` | OperationLogService.get_operation_log_list_services<br/>OperationLogService.export_operation_log_list_services |
| `GET` | `/monitor/operlog/list` | 获取操作日志分页列表接口 | `ruoyi-fastapi-backend/module_admin/controller/log_controller.py` | `get_system_operation_log_list` | OperationLogService.get_operation_log_list_services |
| `DELETE` | `/monitor/operlog/{oper_ids}` | 删除操作日志接口 | `ruoyi-fastapi-backend/module_admin/controller/log_controller.py` | `delete_system_operation_log` | OperationLogService.delete_operation_log_services |
| `GET` | `/monitor/server` | 获取服务器监控信息接口 | `ruoyi-fastapi-backend/module_admin/controller/server_controller.py` | `get_monitor_server_info` | ServerService.get_server_monitor_info |
| `POST` | `/register` | 注册接口 | `ruoyi-fastapi-backend/module_admin/controller/login_controller.py` | `register_user` | LoginService.register_user_services |
| `POST` | `/system/config` | 新增参数接口 | `ruoyi-fastapi-backend/module_admin/controller/config_controller.py` | `add_system_config` | ConfigService.add_config_services |
| `PUT` | `/system/config` | 编辑参数接口 | `ruoyi-fastapi-backend/module_admin/controller/config_controller.py` | `edit_system_config` | ConfigService.edit_config_services |
| `GET` | `/system/config/configKey/{config_key}` | 根据参数键查询参数值接口 | `ruoyi-fastapi-backend/module_admin/controller/config_controller.py` | `query_system_config` | ConfigService.query_config_list_from_cache_services |
| `POST` | `/system/config/export` | 导出参数列表接口 | `ruoyi-fastapi-backend/module_admin/controller/config_controller.py` | `export_system_config_list` | ConfigService.get_config_list_services<br/>ConfigService.export_config_list_services |
| `GET` | `/system/config/list` | 获取参数分页列表接口 | `ruoyi-fastapi-backend/module_admin/controller/config_controller.py` | `get_system_config_list` | ConfigService.get_config_list_services |
| `DELETE` | `/system/config/refreshCache` | 刷新参数缓存接口 | `ruoyi-fastapi-backend/module_admin/controller/config_controller.py` | `refresh_system_config` | ConfigService.refresh_sys_config_services |
| `DELETE` | `/system/config/{config_ids}` | 删除参数接口 | `ruoyi-fastapi-backend/module_admin/controller/config_controller.py` | `delete_system_config` | ConfigService.delete_config_services |
| `GET` | `/system/config/{config_id}` | 获取参数详情接口 | `ruoyi-fastapi-backend/module_admin/controller/config_controller.py` | `query_detail_system_config` | ConfigService.config_detail_services |
| `POST` | `/system/dept` | 新增部门接口 | `ruoyi-fastapi-backend/module_admin/controller/dept_controller.py` | `add_system_dept` | DeptService.add_dept_services |
| `PUT` | `/system/dept` | 编辑部门接口 | `ruoyi-fastapi-backend/module_admin/controller/dept_controller.py` | `edit_system_dept` | DeptService.check_dept_data_scope_services<br/>DeptService.edit_dept_services |
| `GET` | `/system/dept/list` | 获取部门列表接口 | `ruoyi-fastapi-backend/module_admin/controller/dept_controller.py` | `get_system_dept_list` | DeptService.get_dept_list_services |
| `GET` | `/system/dept/list/exclude/{dept_id}` | 获取编辑部门的下拉树接口 | `ruoyi-fastapi-backend/module_admin/controller/dept_controller.py` | `get_system_dept_tree_for_edit_option` | DeptService.get_dept_for_edit_option_services |
| `DELETE` | `/system/dept/{dept_ids}` | 删除部门接口 | `ruoyi-fastapi-backend/module_admin/controller/dept_controller.py` | `delete_system_dept` | DeptService.check_dept_data_scope_services<br/>DeptService.delete_dept_services |
| `GET` | `/system/dept/{dept_id}` | 获取部门详情接口 | `ruoyi-fastapi-backend/module_admin/controller/dept_controller.py` | `query_detail_system_dept` | DeptService.check_dept_data_scope_services<br/>DeptService.dept_detail_services |
| `POST` | `/system/dict/data` | 新增字典数据接口 | `ruoyi-fastapi-backend/module_admin/controller/dict_controller.py` | `add_system_dict_data` | DictDataService.add_dict_data_services |
| `PUT` | `/system/dict/data` | 编辑字典数据接口 | `ruoyi-fastapi-backend/module_admin/controller/dict_controller.py` | `edit_system_dict_data` | DictDataService.edit_dict_data_services |
| `POST` | `/system/dict/data/export` | 导出字典数据列表接口 | `ruoyi-fastapi-backend/module_admin/controller/dict_controller.py` | `export_system_dict_data_list` | DictDataService.get_dict_data_list_services<br/>DictDataService.export_dict_data_list_services |
| `GET` | `/system/dict/data/list` | 获取字典数据分页列表接口 | `ruoyi-fastapi-backend/module_admin/controller/dict_controller.py` | `get_system_dict_data_list` | DictDataService.get_dict_data_list_services |
| `GET` | `/system/dict/data/type/{dict_type}` | 获取指定字典类型的数据列表接口 | `ruoyi-fastapi-backend/module_admin/controller/dict_controller.py` | `query_system_dict_type_data` | DictDataService.query_dict_data_list_from_cache_services |
| `DELETE` | `/system/dict/data/{dict_codes}` | 删除字典数据接口 | `ruoyi-fastapi-backend/module_admin/controller/dict_controller.py` | `delete_system_dict_data` | DictDataService.delete_dict_data_services |
| `GET` | `/system/dict/data/{dict_code}` | 获取字典数据详情接口 | `ruoyi-fastapi-backend/module_admin/controller/dict_controller.py` | `query_detail_system_dict_data` | DictDataService.dict_data_detail_services |
| `POST` | `/system/dict/type` | 新增字典类型接口 | `ruoyi-fastapi-backend/module_admin/controller/dict_controller.py` | `add_system_dict_type` | DictTypeService.add_dict_type_services |
| `PUT` | `/system/dict/type` | 编辑字典类型接口 | `ruoyi-fastapi-backend/module_admin/controller/dict_controller.py` | `edit_system_dict_type` | DictTypeService.edit_dict_type_services |
| `POST` | `/system/dict/type/export` | 导出字典类型列表接口 | `ruoyi-fastapi-backend/module_admin/controller/dict_controller.py` | `export_system_dict_type_list` | DictTypeService.get_dict_type_list_services<br/>DictTypeService.export_dict_type_list_services |
| `GET` | `/system/dict/type/list` | 获取字典类型分页列表接口 | `ruoyi-fastapi-backend/module_admin/controller/dict_controller.py` | `get_system_dict_type_list` | DictTypeService.get_dict_type_list_services |
| `GET` | `/system/dict/type/optionselect` | 获取字典类型下拉列表接口 | `ruoyi-fastapi-backend/module_admin/controller/dict_controller.py` | `query_system_dict_type_options` | DictTypeService.get_dict_type_list_services |
| `DELETE` | `/system/dict/type/refreshCache` | 刷新字典缓存接口 | `ruoyi-fastapi-backend/module_admin/controller/dict_controller.py` | `refresh_system_dict` | DictTypeService.refresh_sys_dict_services |
| `DELETE` | `/system/dict/type/{dict_ids}` | 删除字典类型接口 | `ruoyi-fastapi-backend/module_admin/controller/dict_controller.py` | `delete_system_dict_type` | DictTypeService.delete_dict_type_services |
| `GET` | `/system/dict/type/{dict_id}` | 获取字典类型详情接口 | `ruoyi-fastapi-backend/module_admin/controller/dict_controller.py` | `query_detail_system_dict_type` | DictTypeService.dict_type_detail_services |
| `POST` | `/system/menu` | 新增菜单接口 | `ruoyi-fastapi-backend/module_admin/controller/menu_controller.py` | `add_system_menu` | MenuService.add_menu_services |
| `PUT` | `/system/menu` | 编辑菜单接口 | `ruoyi-fastapi-backend/module_admin/controller/menu_controller.py` | `edit_system_menu` | MenuService.edit_menu_services |
| `GET` | `/system/menu/list` | 获取菜单列表接口 | `ruoyi-fastapi-backend/module_admin/controller/menu_controller.py` | `get_system_menu_list` | MenuService.get_menu_list_services |
| `GET` | `/system/menu/roleMenuTreeselect/{role_id}` | 获取角色菜单树接口 | `ruoyi-fastapi-backend/module_admin/controller/menu_controller.py` | `get_system_role_menu_tree` | MenuService.get_role_menu_tree_services |
| `GET` | `/system/menu/treeselect` | 获取菜单树接口 | `ruoyi-fastapi-backend/module_admin/controller/menu_controller.py` | `get_system_menu_tree` | MenuService.get_menu_tree_services |
| `DELETE` | `/system/menu/{menu_ids}` | 删除菜单接口 | `ruoyi-fastapi-backend/module_admin/controller/menu_controller.py` | `delete_system_menu` | MenuService.delete_menu_services |
| `GET` | `/system/menu/{menu_id}` | 获取菜单详情接口 | `ruoyi-fastapi-backend/module_admin/controller/menu_controller.py` | `query_detail_system_menu` | MenuService.menu_detail_services |
| `POST` | `/system/notice` | 新增通知公告接口 | `ruoyi-fastapi-backend/module_admin/controller/notice_controller.py` | `add_system_notice` | NoticeService.add_notice_services |
| `PUT` | `/system/notice` | 编辑通知公告接口 | `ruoyi-fastapi-backend/module_admin/controller/notice_controller.py` | `edit_system_notice` | NoticeService.edit_notice_services |
| `GET` | `/system/notice/list` | 获取通知公告分页列表接口 | `ruoyi-fastapi-backend/module_admin/controller/notice_controller.py` | `get_system_notice_list` | NoticeService.get_notice_list_services |
| `DELETE` | `/system/notice/{notice_ids}` | 删除通知公告接口 | `ruoyi-fastapi-backend/module_admin/controller/notice_controller.py` | `delete_system_notice` | NoticeService.delete_notice_services |
| `GET` | `/system/notice/{notice_id}` | 获取通知公告详情接口 | `ruoyi-fastapi-backend/module_admin/controller/notice_controller.py` | `query_detail_system_post` | NoticeService.notice_detail_services |
| `POST` | `/system/post` | 新增岗位接口 | `ruoyi-fastapi-backend/module_admin/controller/post_controller.py` | `add_system_post` | PostService.add_post_services |
| `PUT` | `/system/post` | 编辑岗位接口 | `ruoyi-fastapi-backend/module_admin/controller/post_controller.py` | `edit_system_post` | PostService.edit_post_services |
| `POST` | `/system/post/export` | 导出岗位列表接口 | `ruoyi-fastapi-backend/module_admin/controller/post_controller.py` | `export_system_post_list` | PostService.get_post_list_services<br/>PostService.export_post_list_services |
| `GET` | `/system/post/list` | 获取岗位分页列表接口 | `ruoyi-fastapi-backend/module_admin/controller/post_controller.py` | `get_system_post_list` | PostService.get_post_list_services |
| `DELETE` | `/system/post/{post_ids}` | 删除岗位接口 | `ruoyi-fastapi-backend/module_admin/controller/post_controller.py` | `delete_system_post` | PostService.delete_post_services |
| `GET` | `/system/post/{post_id}` | 获取岗位详情接口 | `ruoyi-fastapi-backend/module_admin/controller/post_controller.py` | `query_detail_system_post` | PostService.post_detail_services |
| `POST` | `/system/role` | 新增角色接口 | `ruoyi-fastapi-backend/module_admin/controller/role_controller.py` | `add_system_role` | RoleService.add_role_services |
| `PUT` | `/system/role` | 编辑角色接口 | `ruoyi-fastapi-backend/module_admin/controller/role_controller.py` | `edit_system_role` | RoleService.check_role_allowed_services<br/>RoleService.check_role_data_scope_services<br/>RoleService.edit_role_services |
| `GET` | `/system/role/authUser/allocatedList` | 获取已分配用户分页列表接口 | `ruoyi-fastapi-backend/module_admin/controller/role_controller.py` | `get_system_allocated_user_list` | RoleService.get_role_user_allocated_list_services |
| `PUT` | `/system/role/authUser/cancel` | 取消分配用户给角色接口 | `ruoyi-fastapi-backend/module_admin/controller/role_controller.py` | `cancel_system_role_user` | UserService.delete_user_role_services |
| `PUT` | `/system/role/authUser/cancelAll` | 批量取消分配用户给角色接口 | `ruoyi-fastapi-backend/module_admin/controller/role_controller.py` | `batch_cancel_system_role_user` | UserService.delete_user_role_services |
| `PUT` | `/system/role/authUser/selectAll` | 分配用户给角色接口 | `ruoyi-fastapi-backend/module_admin/controller/role_controller.py` | `add_system_role_user` | RoleService.check_role_data_scope_services<br/>UserService.add_user_role_services |
| `GET` | `/system/role/authUser/unallocatedList` | 获取未分配用户分页列表接口 | `ruoyi-fastapi-backend/module_admin/controller/role_controller.py` | `get_system_unallocated_user_list` | RoleService.get_role_user_unallocated_list_services |
| `PUT` | `/system/role/changeStatus` | 修改角色状态接口 | `ruoyi-fastapi-backend/module_admin/controller/role_controller.py` | `reset_system_role_status` | RoleService.check_role_allowed_services<br/>RoleService.check_role_data_scope_services<br/>RoleService.edit_role_services |
| `PUT` | `/system/role/dataScope` | 编辑角色数据权限接口 | `ruoyi-fastapi-backend/module_admin/controller/role_controller.py` | `edit_system_role_datascope` | RoleService.check_role_allowed_services<br/>RoleService.check_role_data_scope_services<br/>RoleService.role_datascope_services |
| `GET` | `/system/role/deptTree/{role_id}` | 获取自定义数据权限时可见的部门树接口 | `ruoyi-fastapi-backend/module_admin/controller/role_controller.py` | `get_system_role_dept_tree` | DeptService.get_dept_tree_services<br/>RoleService.get_role_dept_tree_services |
| `POST` | `/system/role/export` | 导出角色列表接口 | `ruoyi-fastapi-backend/module_admin/controller/role_controller.py` | `export_system_role_list` | RoleService.get_role_list_services<br/>RoleService.export_role_list_services |
| `GET` | `/system/role/list` | 获取角色分页列表接口 | `ruoyi-fastapi-backend/module_admin/controller/role_controller.py` | `get_system_role_list` | RoleService.get_role_list_services |
| `DELETE` | `/system/role/{role_ids}` | 删除角色接口 | `ruoyi-fastapi-backend/module_admin/controller/role_controller.py` | `delete_system_role` | RoleService.check_role_allowed_services<br/>RoleService.check_role_data_scope_services<br/>RoleService.delete_role_services |
| `GET` | `/system/role/{role_id}` | 获取角色详情接口 | `ruoyi-fastapi-backend/module_admin/controller/role_controller.py` | `query_detail_system_role` | RoleService.check_role_data_scope_services<br/>RoleService.role_detail_services |
| `POST` | `/system/user` | 新增用户接口 | `ruoyi-fastapi-backend/module_admin/controller/user_controller.py` | `add_system_user` | DeptService.check_dept_data_scope_services<br/>RoleService.check_role_data_scope_services<br/>PwdUtil.get_password_hash<br/>UserService.add_user_services |
| `PUT` | `/system/user` | 编辑用户接口 | `ruoyi-fastapi-backend/module_admin/controller/user_controller.py` | `edit_system_user` | UserService.check_user_allowed_services<br/>UserService.check_user_data_scope_services<br/>DeptService.check_dept_data_scope_services<br/>RoleService.check_role_data_scope_services<br/>UserService.edit_user_services |
| `GET` | `/system/user/` | 获取用户岗位和角色列表接口 | `ruoyi-fastapi-backend/module_admin/controller/user_controller.py` | `query_detail_system_user` | UserService.check_user_data_scope_services<br/>UserService.user_detail_services |
| `PUT` | `/system/user/authRole` | 给用户分配角色接口 | `ruoyi-fastapi-backend/module_admin/controller/user_controller.py` | `update_system_role_user` | UserService.check_user_data_scope_services<br/>RoleService.check_role_data_scope_services<br/>UserService.add_user_role_services |
| `GET` | `/system/user/authRole/{user_id}` | 获取用户已分配角色列表接口 | `ruoyi-fastapi-backend/module_admin/controller/user_controller.py` | `get_system_allocated_role_list` | UserService.get_user_role_allocated_list_services |
| `PUT` | `/system/user/changeStatus` | 修改用户状态接口 | `ruoyi-fastapi-backend/module_admin/controller/user_controller.py` | `change_system_user_status` | UserService.check_user_allowed_services<br/>UserService.check_user_data_scope_services<br/>UserService.edit_user_services |
| `GET` | `/system/user/deptTree` | 获取部门树接口 | `ruoyi-fastapi-backend/module_admin/controller/user_controller.py` | `get_system_dept_tree` | DeptService.get_dept_tree_services |
| `POST` | `/system/user/export` | 导出用户列表接口 | `ruoyi-fastapi-backend/module_admin/controller/user_controller.py` | `export_system_user_list` | UserService.get_user_list_services<br/>UserService.export_user_list_services |
| `POST` | `/system/user/importData` | 批量导入用户接口 | `ruoyi-fastapi-backend/module_admin/controller/user_controller.py` | `batch_import_system_user` | UserService.batch_import_user_services |
| `POST` | `/system/user/importTemplate` | 获取用户导入模板接口 | `ruoyi-fastapi-backend/module_admin/controller/user_controller.py` | `export_system_user_template` | UserService.get_user_import_template_services |
| `GET` | `/system/user/list` | 获取用户分页列表接口 | `ruoyi-fastapi-backend/module_admin/controller/user_controller.py` | `get_system_user_list` | UserService.get_user_list_services |
| `GET` | `/system/user/profile` | 获取用户个人信息接口 | `ruoyi-fastapi-backend/module_admin/controller/user_controller.py` | `query_detail_system_user_profile` | UserService.user_profile_services |
| `PUT` | `/system/user/profile` | 修改用户个人信息接口 | `ruoyi-fastapi-backend/module_admin/controller/user_controller.py` | `change_system_user_profile_info` | UserService.edit_user_services |
| `POST` | `/system/user/profile/avatar` | 修改用户头像接口 | `ruoyi-fastapi-backend/module_admin/controller/user_controller.py` | `change_system_user_profile_avatar` | UploadUtil.generate_random_number<br/>UserService.edit_user_services |
| `PUT` | `/system/user/profile/updatePwd` | 修改用户密码接口 | `ruoyi-fastapi-backend/module_admin/controller/user_controller.py` | `reset_system_user_password` | UserService.reset_user_services |
| `PUT` | `/system/user/resetPwd` | 重置用户密码接口 | `ruoyi-fastapi-backend/module_admin/controller/user_controller.py` | `reset_system_user_pwd` | UserService.check_user_allowed_services<br/>UserService.check_user_data_scope_services<br/>PwdUtil.get_password_hash<br/>UserService.edit_user_services |
| `DELETE` | `/system/user/{user_ids}` | 删除用户接口 | `ruoyi-fastapi-backend/module_admin/controller/user_controller.py` | `delete_system_user` | UserService.check_user_allowed_services<br/>UserService.check_user_data_scope_services<br/>UserService.delete_user_services |
| `GET` | `/system/user/{user_id}` | 获取用户详情接口 | `ruoyi-fastapi-backend/module_admin/controller/user_controller.py` | `query_detail_system_user` | UserService.check_user_data_scope_services<br/>UserService.user_detail_services |
| `PUT` | `/tool/gen` | 编辑代码生成表接口 | `ruoyi-fastapi-backend/module_generator/controller/gen_controller.py` | `edit_gen_table` | GenTableService.validate_edit<br/>GenTableService.edit_gen_table_services |
| `GET` | `/tool/gen/batchGenCode` | 生成代码文件接口 | `ruoyi-fastapi-backend/module_generator/controller/gen_controller.py` | `batch_gen_code` | GenTableService.batch_gen_code_services |
| `POST` | `/tool/gen/createTable` | 创建数据库表接口 | `ruoyi-fastapi-backend/module_generator/controller/gen_controller.py` | `create_table` | GenTableService.create_table_services |
| `GET` | `/tool/gen/db/list` | 获取数据库表分页列表接口 | `ruoyi-fastapi-backend/module_generator/controller/gen_controller.py` | `get_gen_db_table_list` | GenTableService.get_gen_db_table_list_services |
| `GET` | `/tool/gen/genCode/{table_name}` | 生成代码文件到本地接口 | `ruoyi-fastapi-backend/module_generator/controller/gen_controller.py` | `gen_code_local` | GenTableService.generate_code_services |
| `POST` | `/tool/gen/importTable` | 导入数据库表接口 | `ruoyi-fastapi-backend/module_generator/controller/gen_controller.py` | `import_gen_table` | GenTableService.get_gen_db_table_list_by_name_services<br/>GenTableService.import_gen_table_services |
| `GET` | `/tool/gen/list` | 获取代码生成表分页列表接口 | `ruoyi-fastapi-backend/module_generator/controller/gen_controller.py` | `get_gen_table_list` | GenTableService.get_gen_table_list_services |
| `GET` | `/tool/gen/preview/{table_id}` | 预览生成的代码接口 | `ruoyi-fastapi-backend/module_generator/controller/gen_controller.py` | `preview_code` | GenTableService.preview_code_services |
| `GET` | `/tool/gen/synchDb/{table_name}` | 同步数据库接口 | `ruoyi-fastapi-backend/module_generator/controller/gen_controller.py` | `sync_db` | GenTableService.sync_db_services |
| `DELETE` | `/tool/gen/{table_ids}` | 删除代码生成表接口 | `ruoyi-fastapi-backend/module_generator/controller/gen_controller.py` | `delete_gen_table` | GenTableService.delete_gen_table_services |
| `GET` | `/tool/gen/{table_id}` | 获取代码生成表详情接口 | `ruoyi-fastapi-backend/module_generator/controller/gen_controller.py` | `query_detail_gen_table` | GenTableService.get_gen_table_by_id_services<br/>GenTableService.get_gen_table_all_services<br/>GenTableColumnService.get_gen_table_column_list_by_table_id_services |

## Source

- Controllers root: `ruoyi-fastapi-backend`
- Router auto-registration: `ruoyi-fastapi-backend/common/router.py`（`auto_register_routers`）
