# Mobile Routing（pages.json + 路由守卫）

Source：
- `ruoyi-fastapi-app/src/pages.json`
- `ruoyi-fastapi-app/src/permission.js`
- `ruoyi-fastapi-app/src/plugins/tab.js`

---

## 1) 路由定义（pages.json）

移动端页面路由由 uni-app 的 `pages.json` 定义，约束：
- 页面路径以 `pages/<name>.vue` 为基准
- TabBar 与普通页面由 uni-app 运行时决定渲染与跳转能力

复刻要求：
- 页面 path 与实际文件路径必须严格一致（否则运行时报错）。

---

## 2) 路由守卫（permission.js）

白名单（无需登录）：
- `/pages/login`
- `/pages/register`

拦截策略（高层）：
- 如果存在 token：
  - 访问登录页：重定向到首页（避免反复登录）
- 如果不存在 token：
  - 访问白名单：放行
  - 否则：`uni.reLaunch({ url: '/pages/login' })`

复刻要求：
- token 的“存在性判断”必须与 `utils/auth.js` 一致（存储 key/读取方式一致）。

---

## 3) 跳转封装（tab.js）

项目通过 `$tab` 插件封装了常用导航方法（如 `navigateTo`、`reLaunch` 等），复刻时应保持：
- 登录态失效统一回到 `/pages/login`
- 关键页面跳转使用统一封装，便于未来埋点/权限控制扩展

