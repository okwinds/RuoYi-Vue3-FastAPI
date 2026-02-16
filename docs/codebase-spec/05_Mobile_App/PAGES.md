# Mobile Pages（页面模板与状态）

Source：
- `ruoyi-fastapi-app/src/pages/**`

---

## 1) Auth Pages

- 登录：`src/pages/login.vue`
  - 账号/密码输入
  - 验证码（受后端 `captchaEnabled` 控制）
  - 成功后跳转首页/工作台
- 注册：`src/pages/register.vue`

---

## 2) Workbench

- `src/pages/work/index.vue`：工作台/首页（具体模块随业务扩展）

---

## 3) Mine（我的）

入口：`src/pages/mine/index.vue`

包含：
- 个人信息：`src/pages/mine/info/index.vue` / `edit.vue`
- 头像：`src/pages/mine/avatar/index.vue`（上传/裁剪/保存，依赖 `utils/upload.js`）
- 密码：`src/pages/mine/pwd/index.vue`
- 设置：`src/pages/mine/setting/index.vue`
- 关于/帮助：`src/pages/mine/about/index.vue`、`help/index.vue`

---

## 4) Common

用于承载协议/隐私政策/webview/文本展示：
- `src/pages/common/*`

