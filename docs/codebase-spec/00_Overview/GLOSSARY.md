# Glossary（术语表）

> 目标：统一名词含义，便于文档、代码、测试一致理解。

---

## 1) 域名/产品相关术语

| 术语 | 定义 | 使用位置 |
| --- | --- | --- |
| RuoYi（若依） | 国内常见的后台管理系统/权限管理脚手架体系 | 上游项目命名与表结构 |
| vfadmin | 上游前端项目名/页面标题（可配置） | `ruoyi-fastapi-frontend/package.json`、`.env.*`、页面标题 |
| 管理后台 | PC 管理端 Web 应用 | `ruoyi-fastapi-frontend/` |

---

## 2) 系统模块术语（Backend）

| 术语 | 定义 | 备注 |
| --- | --- | --- |
| controller | FastAPI 路由入口层（HTTP handler） | 位于 `module_*/controller/*.py`，自动注册 |
| service | 业务服务层（组合 dao/规则/工具） | 位于 `module_*/service/*.py` |
| dao | 数据访问层 | 位于 `module_*/dao/*.py`（用于 DB 读写） |
| vo | View Object / 请求响应模型 | 位于 `module_*/entity/vo/*.py` |
| APIRouterPro | 扩展版 APIRouter，支持 `order_num`、`auto_register` | `common/router.py` |

---

## 3) 鉴权与权限术语

| 术语 | 定义 |
| --- | --- |
| JWT | JSON Web Token，用于登录态与接口认证 |
| OAuth2 Password Flow | 用户名密码换 token 的标准流程 |
| RBAC | Role-Based Access Control，基于角色的权限控制 |
| Data Scope | 数据范围权限（如全量/本部门/自定义等） |

---

## 4) 常用缩写

| 缩写 | 全称 |
| --- | --- |
| FE | Frontend（前端） |
| BE | Backend（后端） |
| DB | Database（数据库） |
| E2E | End-to-End（端到端测试） |
| CI | Continuous Integration（持续集成） |
