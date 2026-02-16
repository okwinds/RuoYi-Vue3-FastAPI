# common_service.py（Service）

## Source
- Source: `ruoyi-fastapi-backend/module_admin/service/common_service.py`

## Imports（依赖概览）

```python
import os
from datetime import datetime
import aiofiles
from fastapi import BackgroundTasks, Request, UploadFile
from common.vo import CrudResponseModel
from config.env import UploadConfig
from exceptions.exception import ServiceException
from module_admin.entity.vo.common_vo import UploadResponseModel
from utils.upload_util import UploadUtil
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `upload_service` | Y | `Request request, UploadFile file` | `CrudResponseModel` | 通用上传service |  | '文件类型不合法' |
| `download_services` | Y | `BackgroundTasks background_tasks, str file_name, bool delete` | `CrudResponseModel` | 下载下载目录文件service |  | '文件名称不合法'; '文件不存在' |
| `download_resource_services` | Y | `str resource` | `CrudResponseModel` | 下载上传目录文件service |  | '文件名称不合法'; '文件不存在' |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
