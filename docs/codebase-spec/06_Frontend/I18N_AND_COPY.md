# i18n & Microcopy（多语言/文案规范现状）

范围：`ruoyi-fastapi-frontend/`。

结论（当前仓库快照）：
- 前端整体以中文文案为主，未发现独立的 i18n 框架目录（如 `i18n/`、`locales/`）与运行时切换机制。
- 错误提示文案主要来自两处：
  1) 后端返回的 `msg`（ServiceException/ResponseUtil）
  2) 前端本地 `errorCode` 映射（`src/utils/errorCode.js`）与 axios interceptor 的网络异常兜底文案（`src/utils/request.js`）

复刻约束：
- 若未来引入多语言，必须确保“后端 message 是否直接展示”策略不变（否则会导致用户可见文案语义漂移）。

