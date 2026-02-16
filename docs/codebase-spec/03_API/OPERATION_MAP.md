# API Operation Map（端点 → Schema/权限 映射）

用途：将 `openapi.json` 中的 **每个 operation** 按 tag 分组整理，便于：
- 复刻 API（method/path/summary）
- 快速定位请求/响应 schema（`$ref`）
- 快速判断是否需要认证（`security`）

数据来源：`docs/codebase-spec/03_API/openapi.json`（由 FastAPI app 导出）。

字段说明：
- `ReqSchema/RespSchema`：`$ref` 指向 `#/components/schemas/<Name>`；若为空表示无 JSON body 或未定义 schema。
- `Auth`：`Y` 表示 operation 定义了 `security`（通常需要 Bearer token）。

统计：共 143 个 operation，按 19 个 tag 分组。

## AI管理-AI对话（7）

| Method | Path | Summary | Auth | ReqSchema | RespSchema | operationId |
| --- | --- | --- | --- | --- | --- | --- |
| POST | /ai/chat/cancel | 取消对话 | N | #/components/schemas/Body_cancel_chat_run_ai_chat_cancel_post | #/components/schemas/ResponseBaseModel | cancel_chat_run_ai_chat_cancel_post |
| GET | /ai/chat/config | 获取用户对话配置 | Y |  | #/components/schemas/DataResponseModel_AiChatConfigModel_ | get_user_chat_config_ai_chat_config_get |
| PUT | /ai/chat/config | 保存用户对话配置 | Y | #/components/schemas/AiChatConfigModel | #/components/schemas/DataResponseModel_AiChatConfigModel_ | save_user_chat_config_ai_chat_config_put |
| POST | /ai/chat/send | 发送对话消息 | Y | #/components/schemas/AiChatRequestModel |  | send_chat_message_ai_chat_send_post |
| GET | /ai/chat/session/list | 获取会话列表 | Y |  | #/components/schemas/DataResponseModel_list_AiChatSessionBaseModel__ | get_chat_session_list_ai_chat_session_list_get |
| DELETE | /ai/chat/session/{session_id} | 删除会话 | N |  | #/components/schemas/ResponseBaseModel | delete_chat_session_ai_chat_session__session_id__delete |
| GET | /ai/chat/session/{session_id} | 获取会话消息详情 | N |  | #/components/schemas/DataResponseModel_AiChatSessionModel_ | get_chat_session_detail_ai_chat_session__session_id__get |

## AI管理-模型管理（6）

| Method | Path | Summary | Auth | ReqSchema | RespSchema | operationId |
| --- | --- | --- | --- | --- | --- | --- |
| POST | /ai/model | 新增AI模型接口 | Y | #/components/schemas/AiModelModel | #/components/schemas/ResponseBaseModel | add_ai_model_ai_model_post |
| PUT | /ai/model | 编辑AI模型接口 | Y | #/components/schemas/AiModelModel | #/components/schemas/ResponseBaseModel | edit_ai_model_ai_model_put |
| GET | /ai/model/all | 获取AI模型不分页列表接口 | N |  | #/components/schemas/DataResponseModel_AiModelModel_ | get_ai_model_all_ai_model_all_get |
| GET | /ai/model/list | 获取AI模型分页列表接口 | N |  | #/components/schemas/PageResponseModel_AiModelModel_ | get_ai_model_list_ai_model_list_get |
| DELETE | /ai/model/{model_ids} | 删除AI模型接口 | Y |  | #/components/schemas/ResponseBaseModel | delete_ai_model_ai_model__model_ids__delete |
| GET | /ai/model/{model_id} | 获取AI模型详情接口 | Y |  | #/components/schemas/DataResponseModel_AiModelModel_ | get_ai_model_detail_ai_model__model_id__get |

## 代码生成（11）

| Method | Path | Summary | Auth | ReqSchema | RespSchema | operationId |
| --- | --- | --- | --- | --- | --- | --- |
| PUT | /tool/gen | 编辑代码生成表接口 | Y | #/components/schemas/EditGenTableModel | #/components/schemas/ResponseBaseModel | edit_gen_table_tool_gen_put |
| GET | /tool/gen/batchGenCode | 生成代码文件接口 | N |  |  | batch_gen_code_tool_gen_batchGenCode_get |
| POST | /tool/gen/createTable | 创建数据库表接口 | Y |  | #/components/schemas/ResponseBaseModel | create_table_tool_gen_createTable_post |
| GET | /tool/gen/db/list | 获取数据库表分页列表接口 | N |  | #/components/schemas/PageResponseModel_GenTableDbRowModel_ | get_gen_db_table_list_tool_gen_db_list_get |
| GET | /tool/gen/genCode/{table_name} | 生成代码文件到本地接口 | N |  | #/components/schemas/ResponseBaseModel | gen_code_local_tool_gen_genCode__table_name__get |
| POST | /tool/gen/importTable | 导入数据库表接口 | Y |  | #/components/schemas/ResponseBaseModel | import_gen_table_tool_gen_importTable_post |
| GET | /tool/gen/list | 获取代码生成表分页列表接口 | N |  | #/components/schemas/PageResponseModel_GenTableRowModel_ | get_gen_table_list_tool_gen_list_get |
| GET | /tool/gen/preview/{table_id} | 预览生成的代码接口 | N |  | #/components/schemas/DataResponseModel_dict_str__str__ | preview_code_tool_gen_preview__table_id__get |
| GET | /tool/gen/synchDb/{table_name} | 同步数据库接口 | N |  | #/components/schemas/DataResponseModel_str_ | sync_db_tool_gen_synchDb__table_name__get |
| DELETE | /tool/gen/{table_ids} | 删除代码生成表接口 | N |  | #/components/schemas/ResponseBaseModel | delete_gen_table_tool_gen__table_ids__delete |
| GET | /tool/gen/{table_id} | 获取代码生成表详情接口 | N |  | #/components/schemas/DataResponseModel_GenTableDetailModel_ | query_detail_gen_table_tool_gen__table_id__get |

## 登录模块（5）

| Method | Path | Summary | Auth | ReqSchema | RespSchema | operationId |
| --- | --- | --- | --- | --- | --- | --- |
| GET | /getInfo | 获取用户信息接口 | Y |  | #/components/schemas/DynamicResponseModel_CurrentUserModel_ | get_login_user_info_getInfo_get |
| GET | /getRouters | 获取用户路由接口 | Y |  | #/components/schemas/DataResponseModel_list_RouterModel__ | get_login_user_routers_getRouters_get |
| POST | /login | 登录接口 | N |  | Response Login Login Post | login_login_post |
| POST | /logout | 退出登录接口 | Y |  | #/components/schemas/ResponseBaseModel | logout_logout_post |
| POST | /register | 注册接口 | N | #/components/schemas/UserRegister | #/components/schemas/DataResponseModel_CrudResponseModel_ | register_user_register_post |

## 系统监控-在线用户（2）

| Method | Path | Summary | Auth | ReqSchema | RespSchema | operationId |
| --- | --- | --- | --- | --- | --- | --- |
| GET | /monitor/online/list | 获取在线用户分页列表接口 | N |  | #/components/schemas/OnlinePageResponseModel | get_monitor_online_list_monitor_online_list_get |
| DELETE | /monitor/online/{token_ids} | 强退在线用户接口 | N |  | #/components/schemas/ResponseBaseModel | delete_monitor_online_monitor_online__token_ids__delete |

## 系统监控-定时任务（12）

| Method | Path | Summary | Auth | ReqSchema | RespSchema | operationId |
| --- | --- | --- | --- | --- | --- | --- |
| POST | /monitor/job | 新增定时任务接口 | Y | #/components/schemas/JobModel | #/components/schemas/ResponseBaseModel | add_system_job_monitor_job_post |
| PUT | /monitor/job | 编辑定时任务接口 | Y | #/components/schemas/EditJobModel | #/components/schemas/ResponseBaseModel | edit_system_job_monitor_job_put |
| PUT | /monitor/job/changeStatus | 修改定时任务状态接口 | Y | #/components/schemas/EditJobModel | #/components/schemas/ResponseBaseModel | change_system_job_status_monitor_job_changeStatus_put |
| POST | /monitor/job/export | 导出定时任务列表接口 | N |  |  | export_system_job_list_monitor_job_export_post |
| GET | /monitor/job/list | 获取定时任务分页列表接口 | N |  | #/components/schemas/PageResponseModel_JobModel_ | get_system_job_list_monitor_job_list_get |
| PUT | /monitor/job/run | 执行定时任务接口 | N | #/components/schemas/JobModel | #/components/schemas/ResponseBaseModel | execute_system_job_monitor_job_run_put |
| DELETE | /monitor/job/{job_ids} | 删除定时任务接口 | N |  | #/components/schemas/ResponseBaseModel | delete_system_job_monitor_job__job_ids__delete |
| GET | /monitor/job/{job_id} | 获取定时任务详情接口 | N |  | #/components/schemas/DataResponseModel_JobModel_ | query_detail_system_job_monitor_job__job_id__get |
| DELETE | /monitor/jobLog/clean | 清空定时任务调度日志接口 | N |  | #/components/schemas/ResponseBaseModel | clear_system_job_log_monitor_jobLog_clean_delete |
| POST | /monitor/jobLog/export | 导出定时任务调度日志列表接口 | N |  |  | export_system_job_log_list_monitor_jobLog_export_post |
| GET | /monitor/jobLog/list | 获取定时任务调度日志分页列表接口 | N |  | #/components/schemas/PageResponseModel_JobLogModel_ | get_system_job_log_list_monitor_jobLog_list_get |
| DELETE | /monitor/jobLog/{job_log_ids} | 删除定时任务调度日志接口 | N |  | #/components/schemas/ResponseBaseModel | delete_system_job_log_monitor_jobLog__job_log_ids__delete |

## 系统监控-服务监控（1）

| Method | Path | Summary | Auth | ReqSchema | RespSchema | operationId |
| --- | --- | --- | --- | --- | --- | --- |
| GET | /monitor/server | 获取服务器监控信息接口 | N |  | #/components/schemas/DataResponseModel_ServerMonitorModel_ | get_monitor_server_info_monitor_server_get |

## 系统监控-缓存监控（7）

| Method | Path | Summary | Auth | ReqSchema | RespSchema | operationId |
| --- | --- | --- | --- | --- | --- | --- |
| GET | /monitor/cache | 获取缓存监控信息接口 | N |  | #/components/schemas/DataResponseModel_CacheMonitorModel_ | get_monitor_cache_info_monitor_cache_get |
| DELETE | /monitor/cache/clearCacheAll | 清除所有缓存接口 | N |  | #/components/schemas/ResponseBaseModel | clear_monitor_cache_all_monitor_cache_clearCacheAll_delete |
| DELETE | /monitor/cache/clearCacheKey/{cache_key} | 清除缓存键接口 | N |  | #/components/schemas/ResponseBaseModel | clear_monitor_cache_key_monitor_cache_clearCacheKey__cache_key__delete |
| DELETE | /monitor/cache/clearCacheName/{cache_name} | 清除缓存名称接口 | N |  | #/components/schemas/ResponseBaseModel | clear_monitor_cache_name_monitor_cache_clearCacheName__cache_name__delete |
| GET | /monitor/cache/getKeys/{cache_name} | 获取缓存键列表接口 | N |  | #/components/schemas/DataResponseModel_list_str__ | get_monitor_cache_key_monitor_cache_getKeys__cache_name__get |
| GET | /monitor/cache/getNames | 获取缓存名称列表接口 | N |  | #/components/schemas/DataResponseModel_list_CacheInfoModel__ | get_monitor_cache_name_monitor_cache_getNames_get |
| GET | /monitor/cache/getValue/{cache_name}/{cache_key} | 获取缓存值接口 | N |  | #/components/schemas/DataResponseModel_CacheInfoModel_ | get_monitor_cache_value_monitor_cache_getValue__cache_name___cache_key__get |

## 系统管理-参数管理（8）

| Method | Path | Summary | Auth | ReqSchema | RespSchema | operationId |
| --- | --- | --- | --- | --- | --- | --- |
| POST | /system/config | 新增参数接口 | Y | #/components/schemas/ConfigModel | #/components/schemas/ResponseBaseModel | add_system_config_system_config_post |
| PUT | /system/config | 编辑参数接口 | Y | #/components/schemas/ConfigModel | #/components/schemas/ResponseBaseModel | edit_system_config_system_config_put |
| GET | /system/config/configKey/{config_key} | 根据参数键查询参数值接口 | N |  | #/components/schemas/ResponseBaseModel | query_system_config_system_config_configKey__config_key__get |
| POST | /system/config/export | 导出参数列表接口 | N |  |  | export_system_config_list_system_config_export_post |
| GET | /system/config/list | 获取参数分页列表接口 | N |  | #/components/schemas/PageResponseModel_ConfigModel_ | get_system_config_list_system_config_list_get |
| DELETE | /system/config/refreshCache | 刷新参数缓存接口 | N |  | #/components/schemas/ResponseBaseModel | refresh_system_config_system_config_refreshCache_delete |
| DELETE | /system/config/{config_ids} | 删除参数接口 | N |  | #/components/schemas/ResponseBaseModel | delete_system_config_system_config__config_ids__delete |
| GET | /system/config/{config_id} | 获取参数详情接口 | N |  | #/components/schemas/DataResponseModel_ConfigModel_ | query_detail_system_config_system_config__config_id__get |

## 系统管理-字典管理（15）

| Method | Path | Summary | Auth | ReqSchema | RespSchema | operationId |
| --- | --- | --- | --- | --- | --- | --- |
| POST | /system/dict/data | 新增字典数据接口 | Y | #/components/schemas/DictDataModel | #/components/schemas/ResponseBaseModel | add_system_dict_data_system_dict_data_post |
| PUT | /system/dict/data | 编辑字典数据接口 | Y | #/components/schemas/DictDataModel | #/components/schemas/ResponseBaseModel | edit_system_dict_data_system_dict_data_put |
| POST | /system/dict/data/export | 导出字典数据列表接口 | N |  |  | export_system_dict_data_list_system_dict_data_export_post |
| GET | /system/dict/data/list | 获取字典数据分页列表接口 | N |  | #/components/schemas/PageResponseModel_DictDataModel_ | get_system_dict_data_list_system_dict_data_list_get |
| GET | /system/dict/data/type/{dict_type} | 获取指定字典类型的数据列表接口 | N |  | #/components/schemas/DataResponseModel_list_DictDataModel__ | query_system_dict_type_data_system_dict_data_type__dict_type__get |
| DELETE | /system/dict/data/{dict_codes} | 删除字典数据接口 | N |  | #/components/schemas/ResponseBaseModel | delete_system_dict_data_system_dict_data__dict_codes__delete |
| GET | /system/dict/data/{dict_code} | 获取字典数据详情接口 | N |  | #/components/schemas/DataResponseModel_DictDataModel_ | query_detail_system_dict_data_system_dict_data__dict_code__get |
| POST | /system/dict/type | 新增字典类型接口 | Y | #/components/schemas/DictTypeModel | #/components/schemas/ResponseBaseModel | add_system_dict_type_system_dict_type_post |
| PUT | /system/dict/type | 编辑字典类型接口 | Y | #/components/schemas/DictTypeModel | #/components/schemas/ResponseBaseModel | edit_system_dict_type_system_dict_type_put |
| POST | /system/dict/type/export | 导出字典类型列表接口 | N |  |  | export_system_dict_type_list_system_dict_type_export_post |
| GET | /system/dict/type/list | 获取字典类型分页列表接口 | N |  | #/components/schemas/PageResponseModel_DictTypeModel_ | get_system_dict_type_list_system_dict_type_list_get |
| GET | /system/dict/type/optionselect | 获取字典类型下拉列表接口 | N |  | #/components/schemas/DataResponseModel_list_DictTypeModel__ | query_system_dict_type_options_system_dict_type_optionselect_get |
| DELETE | /system/dict/type/refreshCache | 刷新字典缓存接口 | N |  | #/components/schemas/ResponseBaseModel | refresh_system_dict_system_dict_type_refreshCache_delete |
| DELETE | /system/dict/type/{dict_ids} | 删除字典类型接口 | N |  | #/components/schemas/ResponseBaseModel | delete_system_dict_type_system_dict_type__dict_ids__delete |
| GET | /system/dict/type/{dict_id} | 获取字典类型详情接口 | N |  | #/components/schemas/DataResponseModel_DictTypeModel_ | query_detail_system_dict_type_system_dict_type__dict_id__get |

## 系统管理-岗位管理（6）

| Method | Path | Summary | Auth | ReqSchema | RespSchema | operationId |
| --- | --- | --- | --- | --- | --- | --- |
| POST | /system/post | 新增岗位接口 | Y | #/components/schemas/PostModel | #/components/schemas/ResponseBaseModel | add_system_post_system_post_post |
| PUT | /system/post | 编辑岗位接口 | Y | #/components/schemas/PostModel | #/components/schemas/ResponseBaseModel | edit_system_post_system_post_put |
| POST | /system/post/export | 导出岗位列表接口 | N |  |  | export_system_post_list_system_post_export_post |
| GET | /system/post/list | 获取岗位分页列表接口 | N |  | #/components/schemas/PageResponseModel_PostModel_ | get_system_post_list_system_post_list_get |
| DELETE | /system/post/{post_ids} | 删除岗位接口 | N |  | #/components/schemas/ResponseBaseModel | delete_system_post_system_post__post_ids__delete |
| GET | /system/post/{post_id} | 获取岗位详情接口 | N |  | #/components/schemas/DataResponseModel_PostModel_ | query_detail_system_post_system_post__post_id__get |

## 系统管理-日志管理（9）

| Method | Path | Summary | Auth | ReqSchema | RespSchema | operationId |
| --- | --- | --- | --- | --- | --- | --- |
| DELETE | /monitor/logininfor/clean | 清空登录日志接口 | N |  | #/components/schemas/ResponseBaseModel | clear_system_login_log_monitor_logininfor_clean_delete |
| POST | /monitor/logininfor/export | 导出登录日志接口 | N |  |  | export_system_login_log_list_monitor_logininfor_export_post |
| GET | /monitor/logininfor/list | 获取登录日志分页列表接口 | N |  | #/components/schemas/PageResponseModel_LogininforModel_ | get_system_login_log_list_monitor_logininfor_list_get |
| GET | /monitor/logininfor/unlock/{user_name} | 解锁账户接口 | N |  | #/components/schemas/ResponseBaseModel | unlock_system_user_monitor_logininfor_unlock__user_name__get |
| DELETE | /monitor/logininfor/{info_ids} | 删除登录日志接口 | N |  | #/components/schemas/ResponseBaseModel | delete_system_login_log_monitor_logininfor__info_ids__delete |
| DELETE | /monitor/operlog/clean | 清空操作日志接口 | N |  | #/components/schemas/ResponseBaseModel | clear_system_operation_log_monitor_operlog_clean_delete |
| POST | /monitor/operlog/export | 导出操作日志接口 | N |  |  | export_system_operation_log_list_monitor_operlog_export_post |
| GET | /monitor/operlog/list | 获取操作日志分页列表接口 | N |  | #/components/schemas/PageResponseModel_OperLogModel_ | get_system_operation_log_list_monitor_operlog_list_get |
| DELETE | /monitor/operlog/{oper_ids} | 删除操作日志接口 | N |  | #/components/schemas/ResponseBaseModel | delete_system_operation_log_monitor_operlog__oper_ids__delete |

## 系统管理-用户管理（18）

| Method | Path | Summary | Auth | ReqSchema | RespSchema | operationId |
| --- | --- | --- | --- | --- | --- | --- |
| POST | /system/user | 新增用户接口 | Y | #/components/schemas/AddUserModel | #/components/schemas/ResponseBaseModel | add_system_user_system_user_post |
| PUT | /system/user | 编辑用户接口 | Y | #/components/schemas/EditUserModel | #/components/schemas/ResponseBaseModel | edit_system_user_system_user_put |
| GET | /system/user/ | 获取用户岗位和角色列表接口 | Y |  | #/components/schemas/DynamicResponseModel_UserDetailModel_ | query_detail_system_user_system_user__get |
| PUT | /system/user/authRole | 给用户分配角色接口 | Y |  | #/components/schemas/ResponseBaseModel | update_system_role_user_system_user_authRole_put |
| GET | /system/user/authRole/{user_id} | 获取用户已分配角色列表接口 | N |  | #/components/schemas/DynamicResponseModel_UserRoleResponseModel_ | get_system_allocated_role_list_system_user_authRole__user_id__get |
| PUT | /system/user/changeStatus | 修改用户状态接口 | Y | #/components/schemas/EditUserModel | #/components/schemas/ResponseBaseModel | change_system_user_status_system_user_changeStatus_put |
| GET | /system/user/deptTree | 获取部门树接口 | N |  | #/components/schemas/DataResponseModel_list_DeptTreeModel__ | get_system_dept_tree_system_user_deptTree_get |
| POST | /system/user/export | 导出用户列表接口 | N |  |  | export_system_user_list_system_user_export_post |
| POST | /system/user/importData | 批量导入用户接口 | Y |  | #/components/schemas/ResponseBaseModel | batch_import_system_user_system_user_importData_post |
| POST | /system/user/importTemplate | 获取用户导入模板接口 | N |  |  | export_system_user_template_system_user_importTemplate_post |
| GET | /system/user/list | 获取用户分页列表接口 | N |  | #/components/schemas/PageResponseModel_UserRowModel_ | get_system_user_list_system_user_list_get |
| GET | /system/user/profile | 获取用户个人信息接口 | Y |  | #/components/schemas/DynamicResponseModel_UserProfileModel_ | query_detail_system_user_profile_system_user_profile_get |
| PUT | /system/user/profile | 修改用户个人信息接口 | Y | #/components/schemas/UserInfoModel | #/components/schemas/ResponseBaseModel | change_system_user_profile_info_system_user_profile_put |
| POST | /system/user/profile/avatar | 修改用户头像接口 | Y |  | #/components/schemas/DynamicResponseModel_AvatarModel_ | change_system_user_profile_avatar_system_user_profile_avatar_post |
| PUT | /system/user/profile/updatePwd | 修改用户密码接口 | Y | #/components/schemas/ResetPasswordModel | #/components/schemas/ResponseBaseModel | reset_system_user_password_system_user_profile_updatePwd_put |
| PUT | /system/user/resetPwd | 重置用户密码接口 | Y | #/components/schemas/EditUserModel | #/components/schemas/ResponseBaseModel | reset_system_user_pwd_system_user_resetPwd_put |
| DELETE | /system/user/{user_ids} | 删除用户接口 | Y |  | #/components/schemas/ResponseBaseModel | delete_system_user_system_user__user_ids__delete |
| GET | /system/user/{user_id} | 获取用户详情接口 | Y |  | #/components/schemas/DynamicResponseModel_UserDetailModel_ | query_detail_system_user_system_user__user_id__get |

## 系统管理-菜单管理（7）

| Method | Path | Summary | Auth | ReqSchema | RespSchema | operationId |
| --- | --- | --- | --- | --- | --- | --- |
| POST | /system/menu | 新增菜单接口 | Y | #/components/schemas/MenuModel | #/components/schemas/ResponseBaseModel | add_system_menu_system_menu_post |
| PUT | /system/menu | 编辑菜单接口 | Y | #/components/schemas/MenuModel | #/components/schemas/ResponseBaseModel | edit_system_menu_system_menu_put |
| GET | /system/menu/list | 获取菜单列表接口 | Y |  | #/components/schemas/DataResponseModel_list_MenuModel__ | get_system_menu_list_system_menu_list_get |
| GET | /system/menu/roleMenuTreeselect/{role_id} | 获取角色菜单树接口 | Y |  | #/components/schemas/DynamicResponseModel_RoleMenuQueryModel_ | get_system_role_menu_tree_system_menu_roleMenuTreeselect__role_id__get |
| GET | /system/menu/treeselect | 获取菜单树接口 | Y |  | #/components/schemas/DataResponseModel_list_MenuTreeModel__ | get_system_menu_tree_system_menu_treeselect_get |
| DELETE | /system/menu/{menu_ids} | 删除菜单接口 | N |  | #/components/schemas/ResponseBaseModel | delete_system_menu_system_menu__menu_ids__delete |
| GET | /system/menu/{menu_id} | 获取菜单详情接口 | N |  | #/components/schemas/DataResponseModel_MenuModel_ | query_detail_system_menu_system_menu__menu_id__get |

## 系统管理-角色管理（14）

| Method | Path | Summary | Auth | ReqSchema | RespSchema | operationId |
| --- | --- | --- | --- | --- | --- | --- |
| POST | /system/role | 新增角色接口 | Y | #/components/schemas/AddRoleModel | #/components/schemas/ResponseBaseModel | add_system_role_system_role_post |
| PUT | /system/role | 编辑角色接口 | Y | #/components/schemas/AddRoleModel | #/components/schemas/ResponseBaseModel | edit_system_role_system_role_put |
| GET | /system/role/authUser/allocatedList | 获取已分配用户分页列表接口 | N |  | #/components/schemas/PageResponseModel_UserInfoModel_ | get_system_allocated_user_list_system_role_authUser_allocatedList_get |
| PUT | /system/role/authUser/cancel | 取消分配用户给角色接口 | N | #/components/schemas/CrudUserRoleModel | #/components/schemas/ResponseBaseModel | cancel_system_role_user_system_role_authUser_cancel_put |
| PUT | /system/role/authUser/cancelAll | 批量取消分配用户给角色接口 | N |  | #/components/schemas/ResponseBaseModel | batch_cancel_system_role_user_system_role_authUser_cancelAll_put |
| PUT | /system/role/authUser/selectAll | 分配用户给角色接口 | Y |  | #/components/schemas/ResponseBaseModel | add_system_role_user_system_role_authUser_selectAll_put |
| GET | /system/role/authUser/unallocatedList | 获取未分配用户分页列表接口 | N |  | #/components/schemas/PageResponseModel_UserInfoModel_ | get_system_unallocated_user_list_system_role_authUser_unallocatedList_get |
| PUT | /system/role/changeStatus | 修改角色状态接口 | Y | #/components/schemas/AddRoleModel | #/components/schemas/ResponseBaseModel | reset_system_role_status_system_role_changeStatus_put |
| PUT | /system/role/dataScope | 编辑角色数据权限接口 | Y | #/components/schemas/AddRoleModel | #/components/schemas/ResponseBaseModel | edit_system_role_datascope_system_role_dataScope_put |
| GET | /system/role/deptTree/{role_id} | 获取自定义数据权限时可见的部门树接口 | N |  | #/components/schemas/DynamicResponseModel_RoleDeptQueryModel_ | get_system_role_dept_tree_system_role_deptTree__role_id__get |
| POST | /system/role/export | 导出角色列表接口 | N |  |  | export_system_role_list_system_role_export_post |
| GET | /system/role/list | 获取角色分页列表接口 | N |  | #/components/schemas/PageResponseModel_RoleModel_ | get_system_role_list_system_role_list_get |
| DELETE | /system/role/{role_ids} | 删除角色接口 | Y |  | #/components/schemas/ResponseBaseModel | delete_system_role_system_role__role_ids__delete |
| GET | /system/role/{role_id} | 获取角色详情接口 | Y |  | #/components/schemas/DataResponseModel_RoleModel_ | query_detail_system_role_system_role__role_id__get |

## 系统管理-通知公告管理（5）

| Method | Path | Summary | Auth | ReqSchema | RespSchema | operationId |
| --- | --- | --- | --- | --- | --- | --- |
| POST | /system/notice | 新增通知公告接口 | Y | #/components/schemas/NoticeModel | #/components/schemas/ResponseBaseModel | add_system_notice_system_notice_post |
| PUT | /system/notice | 编辑通知公告接口 | Y | #/components/schemas/NoticeModel | #/components/schemas/ResponseBaseModel | edit_system_notice_system_notice_put |
| GET | /system/notice/list | 获取通知公告分页列表接口 | N |  | #/components/schemas/PageResponseModel_NoticeModel_ | get_system_notice_list_system_notice_list_get |
| DELETE | /system/notice/{notice_ids} | 删除通知公告接口 | N |  | #/components/schemas/ResponseBaseModel | delete_system_notice_system_notice__notice_ids__delete |
| GET | /system/notice/{notice_id} | 获取通知公告详情接口 | N |  | #/components/schemas/DataResponseModel_NoticeModel_ | query_detail_system_post_system_notice__notice_id__get |

## 系统管理-部门管理（6）

| Method | Path | Summary | Auth | ReqSchema | RespSchema | operationId |
| --- | --- | --- | --- | --- | --- | --- |
| POST | /system/dept | 新增部门接口 | Y | #/components/schemas/DeptModel | #/components/schemas/ResponseBaseModel | add_system_dept_system_dept_post |
| PUT | /system/dept | 编辑部门接口 | Y | #/components/schemas/DeptModel | #/components/schemas/ResponseBaseModel | edit_system_dept_system_dept_put |
| GET | /system/dept/list | 获取部门列表接口 | N |  | #/components/schemas/DataResponseModel_list_DeptModel__ | get_system_dept_list_system_dept_list_get |
| GET | /system/dept/list/exclude/{dept_id} | 获取编辑部门的下拉树接口 | N |  | #/components/schemas/DataResponseModel_list_DeptModel__ | get_system_dept_tree_for_edit_option_system_dept_list_exclude__dept_id__get |
| DELETE | /system/dept/{dept_ids} | 删除部门接口 | Y |  | #/components/schemas/ResponseBaseModel | delete_system_dept_system_dept__dept_ids__delete |
| GET | /system/dept/{dept_id} | 获取部门详情接口 | Y |  | #/components/schemas/DataResponseModel_DeptModel_ | query_detail_system_dept_system_dept__dept_id__get |

## 通用模块（3）

| Method | Path | Summary | Auth | ReqSchema | RespSchema | operationId |
| --- | --- | --- | --- | --- | --- | --- |
| GET | /common/download | 通用文件下载接口 | N |  |  | common_download_common_download_get |
| GET | /common/download/resource | 通用资源文件下载接口 | N |  |  | common_download_resource_common_download_resource_get |
| POST | /common/upload | 通用文件上传接口 | N |  | #/components/schemas/DynamicResponseModel_UploadResponseModel_ | common_upload_common_upload_post |

## 验证码模块（1）

| Method | Path | Summary | Auth | ReqSchema | RespSchema | operationId |
| --- | --- | --- | --- | --- | --- | --- |
| GET | /captchaImage | 获取图片验证码接口 | N |  | #/components/schemas/DynamicResponseModel_CaptchaCode_ | get_captcha_image_captchaImage_get |

