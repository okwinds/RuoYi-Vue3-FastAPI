# Data Entities（数据实体 / 表结构）

本文件抽取了系统初始化 SQL 中的表结构，目标是：即使不阅读源码，也能完整复刻数据库结构与初始化数据。

来源：
- MySQL：`ruoyi-fastapi-backend/sql/ruoyi-fastapi.sql`
- PostgreSQL：`ruoyi-fastapi-backend/sql/ruoyi-fastapi-pg.sql`

说明：
- 本仓库同时提供 MySQL 与 PostgreSQL 初始化脚本；两者表名基本一致，但字段类型/自增策略有差异（如 `bigserial`）。
- 业务层 ORM（SQLAlchemy）在应用启动时也会执行 `Base.metadata.create_all` 以确保表存在（见 `ruoyi-fastapi-backend/config/get_db.py`）。

---

## 1) 表清单

| 表名 | 说明（comment） |
| --- | --- |
| sys_dept | 部门表 |
| sys_user | 用户信息表 |
| sys_post | 岗位信息表 |
| sys_role | 角色信息表 |
| sys_menu | 菜单权限表 |
| sys_user_role | 用户和角色关联表 |
| sys_role_menu | 角色和菜单关联表 |
| sys_role_dept | 角色和部门关联表 |
| sys_user_post | 用户与岗位关联表 |
| sys_oper_log | 操作日志记录 |
| sys_dict_type | 字典类型表 |
| sys_dict_data | 字典数据表 |
| sys_config | 参数配置表 |
| sys_logininfor | 系统访问记录 |
| sys_job | 定时任务调度表 |
| sys_job_log | 定时任务调度日志表 |
| sys_notice | 通知公告表 |
| gen_table | 代码生成业务表 |
| gen_table_column | 代码生成业务表字段 |
| ai_models | AI模型表 |
| ai_chat_config | AI对话配置表 |

---

## 2) MySQL 表结构（字段级）

### sys_dept（部门表）

- Source: `ruoyi-fastapi-backend/sql/ruoyi-fastapi.sql`
- Primary Key: `primary key (dept_id)`

| 字段 | 类型 | 可空 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| dept_id | bigint(20) | NOT NULL |  | 部门id |
| parent_id | bigint(20) | NULL | 0 | 父部门id |
| ancestors | varchar(50) | NULL | '' | 祖级列表 |
| dept_name | varchar(30) | NULL | '' | 部门名称 |
| order_num | int(4) | NULL | 0 | 显示顺序 |
| leader | varchar(20) | NULL | null | 负责人 |
| phone | varchar(11) | NULL | null | 联系电话 |
| email | varchar(50) | NULL | null | 邮箱 |
| status | char(1) | NULL | '0' | 部门状态（0正常 1停用） |
| del_flag | char(1) | NULL | '0' | 删除标志（0代表存在 2代表删除） |
| create_by | varchar(64) | NULL | '' | 创建者 |
| create_time | datetime | NULL |  | 创建时间 |
| update_by | varchar(64) | NULL | '' | 更新者 |
| update_time | datetime | NULL |  | 更新时间 |

### sys_user（用户信息表）

- Source: `ruoyi-fastapi-backend/sql/ruoyi-fastapi.sql`
- Primary Key: `primary key (user_id)`

| 字段 | 类型 | 可空 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| user_id | bigint(20) | NOT NULL |  | 用户ID |
| dept_id | bigint(20) | NULL | null | 部门ID |
| user_name | varchar(30) | NOT NULL |  | 用户账号 |
| nick_name | varchar(30) | NOT NULL |  | 用户昵称 |
| user_type | varchar(2) | NULL | '00' | 用户类型（00系统用户） |
| email | varchar(50) | NULL | '' | 用户邮箱 |
| phonenumber | varchar(11) | NULL | '' | 手机号码 |
| sex | char(1) | NULL | '0' | 用户性别（0男 1女 2未知） |
| avatar | varchar(100) | NULL | '' | 头像地址 |
| password | varchar(100) | NULL | '' | 密码 |
| status | char(1) | NULL | '0' | 帐号状态（0正常 1停用） |
| del_flag | char(1) | NULL | '0' | 删除标志（0代表存在 2代表删除） |
| login_ip | varchar(128) | NULL | '' | 最后登录IP |
| login_date | datetime | NULL |  | 最后登录时间 |
| pwd_update_date | datetime | NULL |  | 密码最后更新时间 |
| create_by | varchar(64) | NULL | '' | 创建者 |
| create_time | datetime | NULL |  | 创建时间 |
| update_by | varchar(64) | NULL | '' | 更新者 |
| update_time | datetime | NULL |  | 更新时间 |
| remark | varchar(500) | NULL | null | 备注 |

### sys_post（岗位信息表）

- Source: `ruoyi-fastapi-backend/sql/ruoyi-fastapi.sql`
- Primary Key: `primary key (post_id)`

| 字段 | 类型 | 可空 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| post_id | bigint(20) | NOT NULL |  | 岗位ID |
| post_code | varchar(64) | NOT NULL |  | 岗位编码 |
| post_name | varchar(50) | NOT NULL |  | 岗位名称 |
| post_sort | int(4) | NOT NULL |  | 显示顺序 |
| status | char(1) | NOT NULL |  | 状态（0正常 1停用） |
| create_by | varchar(64) | NULL | '' | 创建者 |
| create_time | datetime | NULL |  | 创建时间 |
| update_by | varchar(64) | NULL | '' | 更新者 |
| update_time | datetime | NULL |  | 更新时间 |
| remark | varchar(500) | NULL | null | 备注 |

### sys_role（角色信息表）

- Source: `ruoyi-fastapi-backend/sql/ruoyi-fastapi.sql`
- Primary Key: `primary key (role_id)`

| 字段 | 类型 | 可空 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| role_id | bigint(20) | NOT NULL |  | 角色ID |
| role_name | varchar(30) | NOT NULL |  | 角色名称 |
| role_key | varchar(100) | NOT NULL |  | 角色权限字符串 |
| role_sort | int(4) | NOT NULL |  | 显示顺序 |
| data_scope | char(1) | NULL | '1' | 数据范围（1：全部数据权限 2：自定数据权限 3：本部门数据权限 4：本部门及以下数据权限） |
| menu_check_strictly | tinyint(1) | NULL | 1 | 菜单树选择项是否关联显示 |
| dept_check_strictly | tinyint(1) | NULL | 1 | 部门树选择项是否关联显示 |
| status | char(1) | NOT NULL |  | 角色状态（0正常 1停用） |
| del_flag | char(1) | NULL | '0' | 删除标志（0代表存在 2代表删除） |
| create_by | varchar(64) | NULL | '' | 创建者 |
| create_time | datetime | NULL |  | 创建时间 |
| update_by | varchar(64) | NULL | '' | 更新者 |
| update_time | datetime | NULL |  | 更新时间 |
| remark | varchar(500) | NULL | null | 备注 |

### sys_menu（菜单权限表）

- Source: `ruoyi-fastapi-backend/sql/ruoyi-fastapi.sql`
- Primary Key: `primary key (menu_id)`

| 字段 | 类型 | 可空 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| menu_id | bigint(20) | NOT NULL |  | 菜单ID |
| menu_name | varchar(50) | NOT NULL |  | 菜单名称 |
| parent_id | bigint(20) | NULL | 0 | 父菜单ID |
| order_num | int(4) | NULL | 0 | 显示顺序 |
| path | varchar(200) | NULL | '' | 路由地址 |
| component | varchar(255) | NULL | null | 组件路径 |
| query | varchar(255) | NULL | null | 路由参数 |
| route_name | varchar(50) | NULL | '' | 路由名称 |
| is_frame | int(1) | NULL | 1 | 是否为外链（0是 1否） |
| is_cache | int(1) | NULL | 0 | 是否缓存（0缓存 1不缓存） |
| menu_type | char(1) | NULL | '' | 菜单类型（M目录 C菜单 F按钮） |
| visible | char(1) | NULL | 0 | 菜单状态（0显示 1隐藏） |
| status | char(1) | NULL | 0 | 菜单状态（0正常 1停用） |
| perms | varchar(100) | NULL | null | 权限标识 |
| icon | varchar(100) | NULL | '#' | 菜单图标 |
| create_by | varchar(64) | NULL | '' | 创建者 |
| create_time | datetime | NULL |  | 创建时间 |
| update_by | varchar(64) | NULL | '' | 更新者 |
| update_time | datetime | NULL |  | 更新时间 |
| remark | varchar(500) | NULL | '' | 备注 |

### sys_user_role（用户和角色关联表）

- Source: `ruoyi-fastapi-backend/sql/ruoyi-fastapi.sql`
- Primary Key: `primary key(user_id, role_id)`

| 字段 | 类型 | 可空 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| user_id | bigint(20) | NOT NULL |  | 用户ID |
| role_id | bigint(20) | NOT NULL |  | 角色ID |

### sys_role_menu（角色和菜单关联表）

- Source: `ruoyi-fastapi-backend/sql/ruoyi-fastapi.sql`
- Primary Key: `primary key(role_id, menu_id)`

| 字段 | 类型 | 可空 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| role_id | bigint(20) | NOT NULL |  | 角色ID |
| menu_id | bigint(20) | NOT NULL |  | 菜单ID |

### sys_role_dept（角色和部门关联表）

- Source: `ruoyi-fastapi-backend/sql/ruoyi-fastapi.sql`
- Primary Key: `primary key(role_id, dept_id)`

| 字段 | 类型 | 可空 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| role_id | bigint(20) | NOT NULL |  | 角色ID |
| dept_id | bigint(20) | NOT NULL |  | 部门ID |

### sys_user_post（用户与岗位关联表）

- Source: `ruoyi-fastapi-backend/sql/ruoyi-fastapi.sql`
- Primary Key: `primary key (user_id, post_id)`

| 字段 | 类型 | 可空 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| user_id | bigint(20) | NOT NULL |  | 用户ID |
| post_id | bigint(20) | NOT NULL |  | 岗位ID |

### sys_oper_log（操作日志记录）

- Source: `ruoyi-fastapi-backend/sql/ruoyi-fastapi.sql`
- Primary Key: `primary key (oper_id)`

| 字段 | 类型 | 可空 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| oper_id | bigint(20) | NOT NULL |  | 日志主键 |
| title | varchar(50) | NULL | '' | 模块标题 |
| business_type | int(2) | NULL | 0 | 业务类型（0其它 1新增 2修改 3删除） |
| method | varchar(100) | NULL | '' | 方法名称 |
| request_method | varchar(10) | NULL | '' | 请求方式 |
| operator_type | int(1) | NULL | 0 | 操作类别（0其它 1后台用户 2手机端用户） |
| oper_name | varchar(50) | NULL | '' | 操作人员 |
| dept_name | varchar(50) | NULL | '' | 部门名称 |
| oper_url | varchar(255) | NULL | '' | 请求URL |
| oper_ip | varchar(128) | NULL | '' | 主机地址 |
| oper_location | varchar(255) | NULL | '' | 操作地点 |
| oper_param | varchar(2000) | NULL | '' | 请求参数 |
| json_result | varchar(2000) | NULL | '' | 返回参数 |
| status | int(1) | NULL | 0 | 操作状态（0正常 1异常） |
| error_msg | varchar(2000) | NULL | '' | 错误消息 |
| oper_time | datetime | NULL |  | 操作时间 |
| cost_time | bigint(20) | NULL | 0 | 消耗时间 |

### sys_dict_type（字典类型表）

- Source: `ruoyi-fastapi-backend/sql/ruoyi-fastapi.sql`
- Primary Key: `primary key (dict_id)`

| 字段 | 类型 | 可空 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| dict_id | bigint(20) | NOT NULL |  | 字典主键 |
| dict_name | varchar(100) | NULL | '' | 字典名称 |
| dict_type | varchar(100) | NULL | '' | 字典类型 |
| status | char(1) | NULL | '0' | 状态（0正常 1停用） |
| create_by | varchar(64) | NULL | '' | 创建者 |
| create_time | datetime | NULL |  | 创建时间 |
| update_by | varchar(64) | NULL | '' | 更新者 |
| update_time | datetime | NULL |  | 更新时间 |
| remark | varchar(500) | NULL | null | 备注 |
| unique | (dict_type) | NULL |  |  |

### sys_dict_data（字典数据表）

- Source: `ruoyi-fastapi-backend/sql/ruoyi-fastapi.sql`
- Primary Key: `primary key (dict_code)`

| 字段 | 类型 | 可空 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| dict_code | bigint(20) | NOT NULL |  | 字典编码 |
| dict_sort | int(4) | NULL | 0 | 字典排序 |
| dict_label | varchar(100) | NULL | '' | 字典标签 |
| dict_value | varchar(100) | NULL | '' | 字典键值 |
| dict_type | varchar(100) | NULL | '' | 字典类型 |
| css_class | varchar(100) | NULL | null | 样式属性（其他样式扩展） |
| list_class | varchar(100) | NULL | null | 表格回显样式 |
| is_default | char(1) | NULL | 'N' | 是否默认（Y是 N否） |
| status | char(1) | NULL | '0' | 状态（0正常 1停用） |
| create_by | varchar(64) | NULL | '' | 创建者 |
| create_time | datetime | NULL |  | 创建时间 |
| update_by | varchar(64) | NULL | '' | 更新者 |
| update_time | datetime | NULL |  | 更新时间 |
| remark | varchar(500) | NULL | null | 备注 |

### sys_config（参数配置表）

- Source: `ruoyi-fastapi-backend/sql/ruoyi-fastapi.sql`
- Primary Key: `primary key (config_id)`

| 字段 | 类型 | 可空 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| config_id | int(5) | NOT NULL |  | 参数主键 |
| config_name | varchar(100) | NULL | '' | 参数名称 |
| config_key | varchar(100) | NULL | '' | 参数键名 |
| config_value | varchar(500) | NULL | '' | 参数键值 |
| config_type | char(1) | NULL | 'N' | 系统内置（Y是 N否） |
| create_by | varchar(64) | NULL | '' | 创建者 |
| create_time | datetime | NULL |  | 创建时间 |
| update_by | varchar(64) | NULL | '' | 更新者 |
| update_time | datetime | NULL |  | 更新时间 |
| remark | varchar(500) | NULL | null | 备注 |

### sys_logininfor（系统访问记录）

- Source: `ruoyi-fastapi-backend/sql/ruoyi-fastapi.sql`
- Primary Key: `primary key (info_id)`

| 字段 | 类型 | 可空 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| info_id | bigint(20) | NOT NULL |  | 访问ID |
| user_name | varchar(50) | NULL | '' | 用户账号 |
| ipaddr | varchar(128) | NULL | '' | 登录IP地址 |
| login_location | varchar(255) | NULL | '' | 登录地点 |
| browser | varchar(50) | NULL | '' | 浏览器类型 |
| os | varchar(50) | NULL | '' | 操作系统 |
| status | char(1) | NULL | '0' | 登录状态（0成功 1失败） |
| msg | varchar(255) | NULL | '' | 提示消息 |
| login_time | datetime | NULL |  | 访问时间 |

### sys_job（定时任务调度表）

- Source: `ruoyi-fastapi-backend/sql/ruoyi-fastapi.sql`
- Primary Key: `primary key (job_id, job_name, job_group)`

| 字段 | 类型 | 可空 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| job_id | bigint(20) | NOT NULL |  | 任务ID |
| job_name | varchar(64) | NULL | '' | 任务名称 |
| job_group | varchar(64) | NULL | 'default' | 任务组名 |
| job_executor | varchar(64) | NULL | 'default' | 任务执行器 |
| invoke_target | varchar(500) | NOT NULL |  | 调用目标字符串 |
| job_args | varchar(255) | NULL | '' | 位置参数 |
| job_kwargs | varchar(255) | NULL | '' | 关键字参数 |
| cron_expression | varchar(255) | NULL | '' | cron执行表达式 |
| misfire_policy | varchar(20) | NULL | '3' | 计划执行错误策略（1立即执行 2执行一次 3放弃执行） |
| concurrent | char(1) | NULL | '1' | 是否并发执行（0允许 1禁止） |
| status | char(1) | NULL | '0' | 状态（0正常 1暂停） |
| create_by | varchar(64) | NULL | '' | 创建者 |
| create_time | datetime | NULL |  | 创建时间 |
| update_by | varchar(64) | NULL | '' | 更新者 |
| update_time | datetime | NULL |  | 更新时间 |
| remark | varchar(500) | NULL | '' | 备注信息 |

### sys_job_log（定时任务调度日志表）

- Source: `ruoyi-fastapi-backend/sql/ruoyi-fastapi.sql`
- Primary Key: `primary key (job_log_id)`

| 字段 | 类型 | 可空 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| job_log_id | bigint(20) | NOT NULL |  | 任务日志ID |
| job_name | varchar(64) | NOT NULL |  | 任务名称 |
| job_group | varchar(64) | NOT NULL |  | 任务组名 |
| job_executor | varchar(64) | NOT NULL |  | 任务执行器 |
| invoke_target | varchar(500) | NOT NULL |  | 调用目标字符串 |
| job_args | varchar(255) | NULL | '' | 位置参数 |
| job_kwargs | varchar(255) | NULL | '' | 关键字参数 |
| job_trigger | varchar(255) | NULL | '' | 任务触发器 |
| job_message | varchar(500) | NULL |  | 日志信息 |
| status | char(1) | NULL | '0' | 执行状态（0正常 1失败） |
| exception_info | varchar(2000) | NULL | '' | 异常信息 |
| create_time | datetime | NULL |  | 创建时间 |

### sys_notice（通知公告表）

- Source: `ruoyi-fastapi-backend/sql/ruoyi-fastapi.sql`
- Primary Key: `primary key (notice_id)`

| 字段 | 类型 | 可空 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| notice_id | int(4) | NOT NULL |  | 公告ID |
| notice_title | varchar(50) | NOT NULL |  | 公告标题 |
| notice_type | char(1) | NOT NULL |  | 公告类型（1通知 2公告） |
| notice_content | longblob | NULL | null | 公告内容 |
| status | char(1) | NULL | '0' | 公告状态（0正常 1关闭） |
| create_by | varchar(64) | NULL | '' | 创建者 |
| create_time | datetime | NULL |  | 创建时间 |
| update_by | varchar(64) | NULL | '' | 更新者 |
| update_time | datetime | NULL |  | 更新时间 |
| remark | varchar(255) | NULL | null | 备注 |

### gen_table（代码生成业务表）

- Source: `ruoyi-fastapi-backend/sql/ruoyi-fastapi.sql`
- Primary Key: `primary key (table_id)`

| 字段 | 类型 | 可空 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| table_id | bigint(20) | NOT NULL |  | 编号 |
| table_name | varchar(200) | NULL | '' | 表名称 |
| table_comment | varchar(500) | NULL | '' | 表描述 |
| sub_table_name | varchar(64) | NULL | null | 关联子表的表名 |
| sub_table_fk_name | varchar(64) | NULL | null | 子表关联的外键名 |
| class_name | varchar(100) | NULL | '' | 实体类名称 |
| tpl_category | varchar(200) | NULL | 'crud' | 使用的模板（crud单表操作 tree树表操作） |
| tpl_web_type | varchar(30) | NULL | '' | 前端模板类型（element-ui模版 element-plus模版） |
| package_name | varchar(100) | NULL |  | 生成包路径 |
| module_name | varchar(30) | NULL |  | 生成模块名 |
| business_name | varchar(30) | NULL |  | 生成业务名 |
| function_name | varchar(50) | NULL |  | 生成功能名 |
| function_author | varchar(50) | NULL |  | 生成功能作者 |
| gen_type | char(1) | NULL | '0' | 生成代码方式（0zip压缩包 1自定义路径） |
| gen_path | varchar(200) | NULL | '/' | 生成路径（不填默认项目路径） |
| options | varchar(1000) | NULL |  | 其它生成选项 |
| create_by | varchar(64) | NULL | '' | 创建者 |
| create_time | datetime | NULL |  | 创建时间 |
| update_by | varchar(64) | NULL | '' | 更新者 |
| update_time | datetime | NULL |  | 更新时间 |
| remark | varchar(500) | NULL | null | 备注 |

### gen_table_column（代码生成业务表字段）

- Source: `ruoyi-fastapi-backend/sql/ruoyi-fastapi.sql`
- Primary Key: `primary key (column_id)`

| 字段 | 类型 | 可空 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| column_id | bigint(20) | NOT NULL |  | 编号 |
| table_id | bigint(20) | NULL |  | 归属表编号 |
| column_name | varchar(200) | NULL |  | 列名称 |
| column_comment | varchar(500) | NULL |  | 列描述 |
| column_type | varchar(100) | NULL |  | 列类型 |
| python_type | varchar(500) | NULL |  | PYTHON类型 |
| python_field | varchar(200) | NULL |  | PYTHON字段名 |
| is_pk | char(1) | NULL |  | 是否主键（1是） |
| is_increment | char(1) | NULL |  | 是否自增（1是） |
| is_required | char(1) | NULL |  | 是否必填（1是） |
| is_unique | char(1) | NULL |  | 是否唯一（1是） |
| is_insert | char(1) | NULL |  | 是否为插入字段（1是） |
| is_edit | char(1) | NULL |  | 是否编辑字段（1是） |
| is_list | char(1) | NULL |  | 是否列表字段（1是） |
| is_query | char(1) | NULL |  | 是否查询字段（1是） |
| query_type | varchar(200) | NULL | 'EQ' | 查询方式（等于、不等于、大于、小于、范围） |
| html_type | varchar(200) | NULL |  | 显示类型（文本框、文本域、下拉框、复选框、单选框、日期控件） |
| dict_type | varchar(200) | NULL | '' | 字典类型 |
| sort | int | NULL |  | 排序 |
| create_by | varchar(64) | NULL | '' | 创建者 |
| create_time | datetime | NULL |  | 创建时间 |
| update_by | varchar(64) | NULL | '' | 更新者 |
| update_time | datetime | NULL |  | 更新时间 |

### ai_models（AI模型表）

- Source: `ruoyi-fastapi-backend/sql/ruoyi-fastapi.sql`
- Primary Key: `primary key (model_id)`

| 字段 | 类型 | 可空 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| model_id | bigint(20) | NOT NULL |  | 模型主键 |
| model_code | varchar(100) | NOT NULL |  | 模型编码 |
| model_name | varchar(100) | NULL | null | 模型名称 |
| provider | varchar(50) | NOT NULL |  | 提供商 |
| model_sort | int(4) | NOT NULL |  | 显示顺序 |
| api_key | varchar(255) | NULL | null | API Key |
| base_url | varchar(255) | NULL | null | Base URL |
| model_type | varchar(50) | NULL | null | 模型类型 |
| max_tokens | int(11) | NULL | null | 最大输出token |
| temperature | float | NULL | null | 默认温度 |
| support_reasoning | char(1) | NULL | 'N' | 是否支持推理 |
| support_images | char(1) | NULL | 'N' | 是否支持图片 |
| status | char(1) | NULL | '0' | 模型状态 |
| user_id | bigint(20) | NULL |  | 用户ID |
| dept_id | bigint(20) | NULL |  | 部门ID |
| create_by | varchar(64) | NULL | '' | 创建者 |
| create_time | datetime | NULL |  | 创建时间 |
| update_by | varchar(64) | NULL | '' | 更新者 |
| update_time | datetime | NULL |  | 更新时间 |
| remark | varchar(500) | NULL | null | 备注 |

### ai_chat_config（AI对话配置表）

- Source: `ruoyi-fastapi-backend/sql/ruoyi-fastapi.sql`
- Primary Key: `primary key (chat_config_id)`

| 字段 | 类型 | 可空 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| chat_config_id | bigint(20) | NOT NULL |  | 配置主键 |
| user_id | bigint(20) | NOT NULL |  | 用户ID |
| temperature | float | NULL | null | 默认温度 |
| add_history_to_context | char(1) | NULL | '0' | 是否添加历史记录(0是, 1否) |
| num_history_runs | int(4) | NULL | null | 历史记录条数 |
| system_prompt | text | NULL | null | 系统提示词 |
| metrics_default_visible | char(1) | NULL | '0' | 默认显示指标(0是, 1否) |
| vision_enabled | char(1) | NULL | '1' | 是否开启视觉(0是, 1否) |
| image_max_size_mb | int(4) | NULL | null | 图片最大大小(MB) |
| create_time | datetime | NULL |  | 创建时间 |
| update_time | datetime | NULL |  | 更新时间 |

---

## 3) PostgreSQL 对齐说明

PostgreSQL 初始化脚本与 MySQL 脚本在“表名/字段语义/初始化数据”上保持一致，但常见差异包括：
- 自增字段：MySQL 常用 `auto_increment`；PostgreSQL 常用 `bigserial` + `alter sequence ... restart`。
- 时间字段：MySQL 使用 `datetime`；PostgreSQL 使用 `timestamp(0)`。
- 部分整型类型：MySQL `int(4)` 对应 PostgreSQL `int4`。

为便于复刻，这里给出 PostgreSQL 侧的表 comment 对照：

| 表名 | PostgreSQL comment |
| --- | --- |
| sys_dept | 部门表 |
| sys_user | 用户信息表 |
| sys_post | 岗位信息表 |
| sys_role | 角色信息表 |
| sys_menu | 菜单权限表 |
| sys_user_role | 用户和角色关联表 |
| sys_role_menu | 角色和菜单关联表 |
| sys_role_dept | 角色和部门关联表 |
| sys_user_post | 用户与岗位关联表 |
| sys_oper_log | 操作日志记录 |
| sys_dict_type | 字典类型表 |
| sys_dict_data | 字典数据表 |
| sys_config | 参数配置表 |
| sys_logininfor | 系统访问记录 |
| sys_job | 定时任务调度表 |
| sys_job_log | 定时任务调度日志表 |
| sys_notice | 通知公告表 |
| gen_table | 代码生成业务表 |
| gen_table_column | 代码生成业务表字段 |
| ai_models | AI模型表 |
| ai_chat_config | AI对话配置表 |
