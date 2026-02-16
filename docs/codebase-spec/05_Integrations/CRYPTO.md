# Crypto / 密钥策略规格（可复刻级）

本文件描述本仓库的加密/哈希策略，重点在“**存量数据可解密**”与“**安全语义可复刻**”。

---

## 1) JWT（认证）与密钥

- JWT 算法：`HS256`
- 密钥来源：`JWT_SECRET_KEY`（环境变量；默认值在 `env.py`）

Source：
- Source: `ruoyi-fastapi-backend/config/env.py`
- Source: `ruoyi-fastapi-backend/module_admin/service/login_service.py`

复刻约束：
- 如果替换 JWT 实现，必须保持 payload 字段语义与鉴权流程一致（详见 `03_API/AUTHENTICATION.md`）。

---

## 2) 对称加密（Fernet）用于敏感字段

当前实现用于加密存储一些敏感字段（例如 AI 模型的 `api_key`）：
- 算法：`cryptography.fernet.Fernet`
- key 派生方式（复刻必须项）：
  1) `sha256(JWT_SECRET_KEY)` → 32 bytes
  2) `base64.urlsafe_b64encode(...)` → 44 bytes
  3) 作为 Fernet key

行为约束：
- `encrypt(data)`：空字符串/None 直接返回原值；其他加密失败抛 `ServiceException('加密失败')`
- `decrypt(token)`：空字符串/None 直接返回原值；其他解密失败抛 `ServiceException('解密失败')`

Source：
- Source: `ruoyi-fastapi-backend/utils/crypto_util.py`

兼容性/运维约束（非常重要）：
- 旋转 `JWT_SECRET_KEY` 会导致所有历史密文无法解密（等价于“清空敏感字段”）。
- 若必须旋转密钥，需提供一次性迁移方案（读取旧密钥解密 → 用新密钥重加密）。

---

## 3) 密码哈希（bcrypt）

用户密码使用 bcrypt 哈希：
- `PwdUtil.get_password_hash()`：`bcrypt.gensalt()` 后 hash，存为字符串
- `PwdUtil.verify_password()`：`bcrypt.checkpw(...)`

Source：
- Source: `ruoyi-fastapi-backend/utils/pwd_util.py`

复刻建议：
- bcrypt 参数（cost）由库默认决定；如需跨实现一致性，应显式固定 cost。

---

## 4) 使用点（AI 模型 API key）

AI 模型 `api_key` 的读写语义：
- 新增/编辑时：加密入库
- 列表/详情返回时：对外只返回 `********` 掩码（不返回明文）
- 对话运行时：解密得到真实 key 并注入模型 SDK

Source：
- Source: `ruoyi-fastapi-backend/module_ai/service/ai_model_service.py`
- Source: `ruoyi-fastapi-backend/module_ai/service/ai_chat_service.py`

