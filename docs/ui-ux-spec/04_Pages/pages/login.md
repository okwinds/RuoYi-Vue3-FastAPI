# Page Spec: 登录（login）

PageId：`login`  
Route：`/login`

Source：
- `ruoyi-fastapi-frontend/src/views/login.vue`

视觉基线（截图 ID）：
- `light_1_login.png`
- `dark_1_login.png`

> 注：登录页不受 NavType 影响（未登录状态下不展示后台 Layout Shell）。

---

## 1) 目的（Purpose）

提供账号密码登录入口，并在验证码开启时展示验证码输入与图片。

---

## 2) 前置条件（Preconditions）

- 未登录（或 token 失效）访问受保护路由会跳转到 `/login`（路由守卫见 `docs/codebase-spec/06_Frontend/PERMISSION_AND_ROUTING.md`）。

---

## 3) 像素级结构（Structure）

根容器：
- `.login`：全屏居中，背景图铺满（login-background.jpg）

登录表单卡片：
- `.login-form`
  - `width: 400px`
  - `border-radius: 6px`
  - `padding: 25px 25px 5px 25px`
  - 背景白色

表单字段（顺序必须保持）：
1) 账号（`placeholder="账号"`）
2) 密码（`placeholder="密码"`，Enter 触发登录）
3) 验证码（可选，`placeholder="验证码"` + 图片）
4) 记住密码（checkbox）
5) 登录按钮（文本为 `登 录` 或 `登 录 中...`）
6) 立即注册（可选，右侧链接）

底部：
- `.el-login-footer`：固定底部，高 40px，白色文字，展示 `defaultSettings.footerContent`

---

## 4) 稳定 Selector（用于截图/自动化等待）

页面可视稳定判定：
- `input[placeholder="账号"]`
- `input[placeholder="密码"]`
- `button:has-text("登 录")`

验证码开启时额外应出现：
- `input[placeholder="验证码"]`
- `.login-code-img`

---

## 5) 关键交互（Interactions）

### 5.1 登录

- 点击登录按钮会触发表单校验（Element Plus form rules）
- rememberMe=true 时写入 cookie：
  - `username`
  - `password`（加密）
  - `rememberMe`
- 登录成功后跳转：
  - `redirect` query 存在则跳转 `redirect`
  - 否则跳转 `/`

### 5.2 验证码

- 页面初始化会请求验证码信息并决定是否显示验证码输入框。
- 登录失败时若验证码开启，会重新获取验证码。

---

## 6) 主题/暗黑模式（Theme）

登录页的卡片背景固定为白色（当前实现未对 `.login-form` 做暗黑适配），复刻时需保持最终视觉一致。
