# Method Spec：AiModelService api_key 处理（可复刻级）

目标：复刻 AI 模型管理中 `api_key` 的安全语义与编辑行为（加密入库、对外掩码、编辑保持原值）。

Source：
- Source: `ruoyi-fastapi-backend/module_ai/service/ai_model_service.py`
- Source: `ruoyi-fastapi-backend/utils/crypto_util.py`

---

## 1) 读：列表与详情（掩码规则）

列表接口（`get_ai_model_list_services`）：
- 对 rows 中每个 item：
  - 若存在 key `apiKey` → 覆盖为 `'********' * 3`

详情接口（`ai_model_detail_services`）：
- 若 `result.api_key` 存在 → 覆盖为 `'********' * 3`

复刻约束：
- 外部永远拿不到明文 api_key（除非绕过接口直接查 DB）。

---

## 2) 写：新增（加密入库）

`add_ai_model_services`：
- 若 `page_object.api_key` 非空：
  - `page_object.api_key = CryptoUtil.encrypt(page_object.api_key)`
- 入库后 commit；异常 rollback 并抛出

---

## 3) 写：编辑（保持原值 vs 更新）

`edit_ai_model_services` 的关键分支：
- `edit_ai_model = page_object.model_dump(exclude_unset=True)`
- 若用户传了 `api_key`：
  - 若 `api_key == '********' * 3`：
    - 视为“保持原值”，必须删除 `edit_ai_model['api_key']`（不更新 DB）
  - 否则：
    - `edit_ai_model['api_key'] = CryptoUtil.encrypt(page_object.api_key)`

然后校验模型存在（`ai_model_detail_services`）：
- 存在：执行更新并 commit
- 不存在：抛 `ServiceException("AI模型不存在")`

复刻约束：
- 前端回传掩码字符串时必须被识别为“保持原值”，否则会把掩码写入 DB 导致密钥永久丢失。

---

## 4) 验收与测试计划

- [ ] 新增后 DB 中 api_key 为密文，接口返回为掩码
- [ ] 编辑时 api_key 传掩码 → DB 不变化
- [ ] 编辑时 api_key 传新值 → DB 更新为新密文且对话时可成功解密使用

