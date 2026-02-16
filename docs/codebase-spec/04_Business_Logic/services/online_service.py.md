# online_service.py（Service）

## Source
- Source: `ruoyi-fastapi-backend/module_admin/service/online_service.py`

## Imports（依赖概览）

```python
from typing import Any
import jwt
from fastapi import Request
from common.enums import RedisInitKeyConfig
from common.vo import CrudResponseModel
from config.env import AppConfig, JwtConfig
from exceptions.exception import ServiceException
from module_admin.entity.vo.online_vo import DeleteOnlineModel, OnlineQueryModel
from utils.common_util import CamelCaseUtil
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `get_online_list_services` | Y | `Request request, OnlineQueryModel query_object` | `list[dict[str, Any]]` | 获取在线用户表信息service |  |  |
| `delete_online_services` | Y | `Request request, DeleteOnlineModel page_object` | `CrudResponseModel` | 强退在线用户信息service |  | '传入session_id为空' |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
