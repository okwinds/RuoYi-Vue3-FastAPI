# cache_service.py（Service）

## Source
- Source: `ruoyi-fastapi-backend/module_admin/service/cache_service.py`

## Imports（依赖概览）

```python
from fastapi import Request
from common.enums import RedisInitKeyConfig
from common.vo import CrudResponseModel
from config.get_redis import RedisUtil
from module_admin.entity.vo.cache_vo import CacheInfoModel, CacheMonitorModel
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `get_cache_monitor_statistical_info_services` | Y | `Request request` | `CacheMonitorModel` | 获取缓存监控信息service |  |  |
| `get_cache_monitor_cache_name_services` | Y | `` | `list[CacheInfoModel]` | 获取缓存名称列表信息service |  |  |
| `get_cache_monitor_cache_key_services` | Y | `Request request, str cache_name` | `list[str]` | 获取缓存键名列表信息service |  |  |
| `get_cache_monitor_cache_value_services` | Y | `Request request, str cache_name, str cache_key` | `CacheInfoModel` | 获取缓存内容信息service |  |  |
| `clear_cache_monitor_cache_name_services` | Y | `Request request, str cache_name` | `CrudResponseModel` | 清除缓存名称对应所有键值service |  |  |
| `clear_cache_monitor_cache_key_services` | Y | `Request request, str cache_key` | `CrudResponseModel` | 清除缓存名称对应所有键值service |  |  |
| `clear_cache_monitor_all_services` | Y | `Request request` | `CrudResponseModel` | 清除所有缓存service |  |  |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
