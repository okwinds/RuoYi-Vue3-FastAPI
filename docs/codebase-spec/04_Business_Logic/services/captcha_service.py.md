# captcha_service.py（Service）

## Source
- Source: `ruoyi-fastapi-backend/module_admin/service/captcha_service.py`

## Imports（依赖概览）

```python
import base64
import io
import os
import random
from PIL import Image, ImageDraw, ImageFont
```

## Public Methods（对外方法）

| Method | Async | Args | Returns | Doc (first line) | DAO calls | ServiceException messages |
| --- | --- | --- | --- | --- | --- | --- |
| `create_captcha_image_service` | Y | `` | `list[str, int]` |  |  |  |

## Replication Notes（复刻要点）

- 本文件为自动抽取的“方法级目录 + 关键耦合点（DAO/异常文案）”。
- 完整复刻时：
  - 以 `ServiceException` 的 message 作为前端可见错误提示的语义来源之一；
  - 以 `DAO calls` 作为数据访问边界；
  - 结合 `openapi.json` 对齐请求/响应 schema（VO 模型）。
