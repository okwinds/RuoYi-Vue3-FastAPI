# Method Spec：CommonService 上传/下载路径规则（可复刻级）

目标：复刻上传文件命名、静态访问路径、resource 下载的文件名校验规则。

Source：
- Source: `ruoyi-fastapi-backend/module_admin/service/common_service.py`
- Source: `ruoyi-fastapi-backend/utils/upload_util.py`
- Source: `ruoyi-fastapi-backend/config/env.py`

---

## 1) 上传命名规则（upload_service）

输入：`UploadFile file`

规则：
1) 后缀必须在白名单 `DEFAULT_ALLOWED_EXTENSION`
2) 相对目录：`upload/YYYY/MM/DD`
3) 文件名：
   - `<basename>_<YYYYMMDDHHMMSS><UPLOAD_MACHINE><RRR>.<ext>`
   - `UPLOAD_MACHINE`：配置值（默认 `A`）
   - `RRR`：三位随机数字字符串（`001..999`）
4) 返回 `fileName`（URL 路径）：
   - `<UPLOAD_PREFIX>/<relative_path>/<filename>`（默认 `/profile/...`）

---

## 2) resource 下载文件名校验（download_resource_services）

从 `resource` 提取文件名并校验三件事：
- timestamp：能解析 `%Y%m%d%H%M%S`
- machine：倒数第 4 位为 `UPLOAD_MACHINE`
- random：最后三位为 `001..999`

复刻约束：
- 必须保持相同的校验，否则会出现“历史 URL 无法下载”或“安全绕过”。

