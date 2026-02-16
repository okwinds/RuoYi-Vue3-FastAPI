# Schema Catalog（Pydantic/OpenAPI Schemas 清单）

用途：给出 `openapi.json#/components/schemas` 的 **schema 名称清单**，用于复刻时对齐模型命名与字段归属。

说明：
- 该清单是名称级索引；字段级定义请直接查 `openapi.json`。
- 若要生成字段级“人类可读版”，可在后续任务将重点 schema（如 `ResponseModel*`、`*PageQueryModel`）整理成专门文档。

统计：共 130 个 schema。

| Schema Name | Type | Required Props | Description |
| --- | --- | ---: | --- |
| AddRoleModel | object | 0 | 新增角色模型 |
| AddUserModel | object | 0 | 新增用户模型 |
| AgentDataModel | object | 0 | 对话会话数据模型-智能体数据模型 |
| AiChatConfigModel | object | 0 | AI对话配置模型 |
| AiChatRequestModel | object | 2 | AI对话请求模型 |
| AiChatSessionBaseModel | object | 1 | AI对话会话基础模型 |
| AiChatSessionModel | object | 1 | AI对话会话模型 |
| AiModelModel | object | 0 | AI模型表对应pydantic模型 |
| Body_batch_import_system_user_system_user_importData_post | object | 1 |  |
| Body_cancel_chat_run_ai_chat_cancel_post | object | 1 |  |
| Body_change_system_user_profile_avatar_system_user_profile_avatar_post | object | 1 |  |
| Body_common_upload_common_upload_post | object | 1 |  |
| Body_login_login_post | object | 2 |  |
| CacheInfoModel | object | 0 | 缓存监控对象对应pydantic模型 |
| CacheMonitorModel | object | 0 | 缓存监控信息对应pydantic模型 |
| ChatMessageModel | object | 0 | 对话消息模型 |
| ConfigModel | object | 0 | 参数配置表对应pydantic模型 |
| ConfigPageQueryModel | object | 0 | 参数配置管理分页查询模型 |
| CpuInfo | object | 0 |  |
| CrudResponseModel | object | 2 | 操作响应模型 |
| CrudUserRoleModel | object | 0 | 新增、删除用户关联角色及角色关联用户模型 |
| DataResponseModel_AiChatConfigModel_ | object | 1 |  |
| DataResponseModel_AiChatSessionModel_ | object | 1 |  |
| DataResponseModel_AiModelModel_ | object | 1 |  |
| DataResponseModel_CacheInfoModel_ | object | 1 |  |
| DataResponseModel_CacheMonitorModel_ | object | 1 |  |
| DataResponseModel_ConfigModel_ | object | 1 |  |
| DataResponseModel_CrudResponseModel_ | object | 1 |  |
| DataResponseModel_DeptModel_ | object | 1 |  |
| DataResponseModel_DictDataModel_ | object | 1 |  |
| DataResponseModel_DictTypeModel_ | object | 1 |  |
| DataResponseModel_GenTableDetailModel_ | object | 1 |  |
| DataResponseModel_JobModel_ | object | 1 |  |
| DataResponseModel_MenuModel_ | object | 1 |  |
| DataResponseModel_NoticeModel_ | object | 1 |  |
| DataResponseModel_PostModel_ | object | 1 |  |
| DataResponseModel_RoleModel_ | object | 1 |  |
| DataResponseModel_ServerMonitorModel_ | object | 1 |  |
| DataResponseModel_dict_str__str__ | object | 1 |  |
| DataResponseModel_list_AiChatSessionBaseModel__ | object | 1 |  |
| DataResponseModel_list_CacheInfoModel__ | object | 1 |  |
| DataResponseModel_list_DeptModel__ | object | 1 |  |
| DataResponseModel_list_DeptTreeModel__ | object | 1 |  |
| DataResponseModel_list_DictDataModel__ | object | 1 |  |
| DataResponseModel_list_DictTypeModel__ | object | 1 |  |
| DataResponseModel_list_MenuModel__ | object | 1 |  |
| DataResponseModel_list_MenuTreeModel__ | object | 1 |  |
| DataResponseModel_list_RouterModel__ | object | 1 |  |
| DataResponseModel_list_str__ | object | 1 |  |
| DataResponseModel_str_ | object | 1 |  |
| DeptModel | object | 0 | 部门表对应pydantic模型 |
| DeptTreeModel | object | 3 | 部门树模型 |
| DictDataModel | object | 0 | 字典数据表对应pydantic模型 |
| DictDataPageQueryModel | object | 0 | 字典数据管理分页查询模型 |
| DictTypeModel | object | 0 | 字典类型表对应pydantic模型 |
| DictTypePageQueryModel | object | 0 | 字典类型管理分页查询模型 |
| DynamicResponseModel_AvatarModel_ | object | 1 |  |
| DynamicResponseModel_CaptchaCode_ | object | 4 |  |
| DynamicResponseModel_CurrentUserModel_ | object | 3 |  |
| DynamicResponseModel_LoginToken_ | object | 1 |  |
| DynamicResponseModel_RoleDeptQueryModel_ | object | 0 |  |
| DynamicResponseModel_RoleMenuQueryModel_ | object | 0 |  |
| DynamicResponseModel_UploadResponseModel_ | object | 0 |  |
| DynamicResponseModel_UserDetailModel_ | object | 2 |  |
| DynamicResponseModel_UserProfileModel_ | object | 3 |  |
| DynamicResponseModel_UserRoleResponseModel_ | object | 1 |  |
| EditGenTableModel | object | 0 | 修改代码生成业务表模型 |
| EditJobModel | object | 0 | 编辑定时任务模型 |
| EditUserModel | object | 0 | 编辑用户模型 |
| GenTableColumnBaseModel | object | 0 | 代码生成业务表字段对应pydantic模型 |
| GenTableColumnModel | object | 0 | 代码生成业务表字段模型 |
| GenTableDbRowModel | object | 0 | 代码生成业务表数据库行数据模型 |
| GenTableDetailModel | object | 0 | 代码生成业务表详情模型 |
| GenTableModel-Input | object | 0 | 代码生成业务表模型 |
| GenTableModel-Output | object | 0 | 代码生成业务表模型 |
| GenTableParamsModel | object | 0 | 代码生成业务表参数模型 |
| GenTableRowModel | object | 0 | 代码生成业务表行数据模型 |
| HTTPValidationError | object | 0 |  |
| JobLogModel | object | 0 | 定时任务调度日志表对应pydantic模型 |
| JobLogPageQueryModel | object | 0 | 定时任务日志管理分页查询模型 |
| JobModel | object | 0 | 定时任务调度表对应pydantic模型 |
| JobPageQueryModel | object | 0 | 定时任务管理分页查询模型 |
| LoginLogPageQueryModel | object | 0 | 登录日志管理分页查询模型 |
| LogininforModel | object | 0 | 登录日志表对应pydantic模型 |
| MemoryInfo | object | 0 |  |
| MenuModel | object | 0 | 菜单表对应pydantic模型 |
| MenuTreeModel | object | 3 | 菜单树模型 |
| MessageMetrics | object | 0 | 对话消息模型-消息指标模型 |
| MetaModel | object | 0 |  |
| ModelInfoModel | object | 0 | 对话会话数据模型-模型信息模型 |
| NoticeModel | object | 0 | 通知公告表对应pydantic模型 |
| OnlineModel | object | 0 | 在线用户对应pydantic模型 |
| OnlinePageResponseModel | object | 2 | 在线用户分页响应模型 |
| OperLogModel | object | 0 | 操作日志表对应pydantic模型 |
| OperLogPageQueryModel | object | 0 | 操作日志管理分页查询模型 |
| PageResponseModel_AiModelModel_ | object | 5 |  |
| PageResponseModel_ConfigModel_ | object | 5 |  |
| PageResponseModel_DictDataModel_ | object | 5 |  |
| PageResponseModel_DictTypeModel_ | object | 5 |  |
| PageResponseModel_GenTableDbRowModel_ | object | 5 |  |
| PageResponseModel_GenTableRowModel_ | object | 5 |  |
| PageResponseModel_JobLogModel_ | object | 5 |  |
| PageResponseModel_JobModel_ | object | 5 |  |
| PageResponseModel_LogininforModel_ | object | 5 |  |
| PageResponseModel_NoticeModel_ | object | 5 |  |
| PageResponseModel_OperLogModel_ | object | 5 |  |
| PageResponseModel_PostModel_ | object | 5 |  |
| PageResponseModel_RoleModel_ | object | 5 |  |
| PageResponseModel_UserInfoModel_ | object | 5 |  |
| PageResponseModel_UserRowModel_ | object | 5 |  |
| PostModel | object | 0 | 岗位信息表对应pydantic模型 |
| PostPageQueryModel | object | 0 | 岗位管理分页查询模型 |
| PyInfo | object | 0 |  |
| ResetPasswordModel | object | 0 | 重置密码模型 |
| ResponseBaseModel | object | 0 | 响应模型 |
| RoleModel | object | 0 | 角色表对应pydantic模型 |
| RolePageQueryModel | object | 0 | 角色管理分页查询模型 |
| RouterModel | object | 0 |  |
| SelectedRoleModel | object | 0 | 是否选择角色模型 |
| ServerMonitorModel | object | 5 | 服务监控对应pydantic模型 |
| SessionDataModel | object | 0 | 对话会话数据模型 |
| SessionMetricsModel | object | 0 | 对话会话数据模型-会话指标模型 |
| SysFiles | object | 0 |  |
| SysInfo | object | 0 |  |
| Token | object | 2 |  |
| UserInfoModel | object | 0 |  |
| UserPageQueryModel | object | 0 | 用户管理分页查询模型 |
| UserRegister | object | 3 |  |
| UserRowModel | object | 0 | 用户列表行数据模型 |
| ValidationError | object | 3 |  |
