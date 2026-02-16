# 上传与静态资源集成规格（可复刻级）

本文件描述后端“上传/下载/静态资源挂载”的行为契约，包括：路径约定、文件名校验、返回字段语义。

---

## 1) 配置（UploadConfig）

上传相关配置来自 `UploadSettings`（见 `config/env.py`）：

- `UPLOAD_PREFIX`：默认 `/profile`（静态资源 URL 前缀）
- `UPLOAD_PATH`：默认 `vf_admin/upload_path`（上传落盘目录）
- `DOWNLOAD_PATH`：默认 `vf_admin/download_path`（下载目录）
- `UPLOAD_MACHINE`：默认 `A`（写入文件名的机器码）
- `DEFAULT_ALLOWED_EXTENSION`：允许的文件后缀白名单

Source：
- Source: `ruoyi-fastapi-backend/config/env.py`

---

## 2) 静态资源挂载（StaticFiles）

应用启动时会把上传目录挂载为静态文件服务：
- `app.mount(UPLOAD_PREFIX, StaticFiles(directory=UPLOAD_PATH), name='profile')`

这意味着：
- 只要文件写入到 `UPLOAD_PATH` 下，对外即可以 `UPLOAD_PREFIX` 作为 URL 前缀访问。

Source：
- Source: `ruoyi-fastapi-backend/sub_applications/staticfiles.py`
- Source: `ruoyi-fastapi-backend/sub_applications/handle.py`
- Source: `ruoyi-fastapi-backend/server.py`

---

## 3) 上传接口（/common/upload）

入口：
- `POST /common/upload`
- Content-Type：`multipart/form-data`
- 参数：`file`

核心规则（复刻必须项）：
1) 后缀白名单校验：`UploadUtil.check_file_extension(file)`
2) 目录结构：`upload/YYYY/MM/DD`（相对路径）
3) 文件名生成（严格格式）：
   - `<原文件名basename>_<YYYYMMDDHHMMSS><UPLOAD_MACHINE><随机三位数字>.<ext>`
   - 随机三位数字：`001..999`
4) 写文件：
   - 异步写入，分片大小：10MB（`1024*1024*10`）
5) 返回字段语义（UploadResponseModel）：
   - `fileName`：`<UPLOAD_PREFIX>/<relative_path>/<filename>`（前端用于回显/引用）
   - `newFileName`：`filename`
   - `originalFilename`：原始文件名
   - `url`：`<request.base_url><UPLOAD_PREFIX去掉首个/后的路径>/<relative_path>/<filename>`

Source：
- Source: `ruoyi-fastapi-backend/module_admin/controller/common_controller.py`
- Source: `ruoyi-fastapi-backend/module_admin/service/common_service.py`
- Source: `ruoyi-fastapi-backend/utils/upload_util.py`

---

## 4) 下载接口（/common/download）

入口：
- `GET /common/download`
- Query：
  - `fileName`（alias）
  - `delete`：是否在下载完成后删除

规则：
- 从 `DOWNLOAD_PATH` 下读取文件
- `fileName` 不能包含 `..`
- 文件不存在则报错
- `delete=true`：通过后台任务删除文件
- 返回：StreamingResponse（application/octet-stream）

Source：
- Source: `ruoyi-fastapi-backend/module_admin/controller/common_controller.py`
- Source: `ruoyi-fastapi-backend/module_admin/service/common_service.py`

---

## 5) 资源下载接口（/common/download/resource）

入口：
- `GET /common/download/resource`
- Query：`resource`

规则（复刻必须项）：
1) 将 `resource` 从 URL 前缀转换为本地文件路径：
   - `filepath = resource.replace(UPLOAD_PREFIX, UPLOAD_PATH)`
2) 从 `resource` 提取文件名 `filename = resource.rsplit('/', 1)[-1]`
3) 校验：
   - `filename` 不含 `..`
   - 文件名必须能通过三类校验：
     - timestamp 校验（可解析出 `%Y%m%d%H%M%S`）
     - machine 校验（倒数第 4 位为 `UPLOAD_MACHINE`）
     - random 校验（最后三位 `001..999`）
4) 文件不存在则报错；存在则 Streaming 返回

Source：
- Source: `ruoyi-fastapi-backend/module_admin/service/common_service.py`
- Source: `ruoyi-fastapi-backend/utils/upload_util.py`

---

## 6) 验收与测试计划

- [ ] 上传合法后缀文件，静态访问 URL 可用（`/profile/...` 返回 200）
- [ ] 上传非法后缀文件，返回业务错误“文件类型不合法”
- [ ] resource 下载对非法文件名（无时间戳/机器码/随机码/包含 ..）返回业务错误

