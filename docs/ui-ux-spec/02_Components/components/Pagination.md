# Pagination（分页组件）

Source：
- `ruoyi-fastapi-frontend/src/components/Pagination/index.vue`
- `ruoyi-fastapi-frontend/src/assets/styles/ruoyi.scss`
- `ruoyi-fastapi-frontend/src/utils/scroll-to`

---

## 1) Purpose（目的）

Pagination 统一封装 Element Plus 的 `<el-pagination>`，提供：
- 页码/每页条数双向绑定；
- 切换后可选自动滚动到顶部；
- 移动端紧凑显示策略（sizes/jumper 隐藏）。

---

## 2) Props / Emits 契约

Props（默认值必须保持）：
- `total`（required）
- `page`：默认 `1`（支持 `v-model:page`）
- `limit`：默认 `20`（支持 `v-model:limit`）
- `pageSizes`：默认 `[10, 20, 30, 50]`
- `pagerCount`：
  - `< 992px` 默认 `5`
  - 否则默认 `7`
- `layout`：默认 `total, sizes, prev, pager, next, jumper`
- `background`：默认 `true`
- `autoScroll`：默认 `true`
- `hidden`：默认 `false`（隐藏整个分页容器）

Emits：
- `update:page`
- `update:limit`
- `pagination`：payload `{ page, limit }`

---

## 3) 行为（Behavior）

### 3.1 切换 pageSize

`handleSizeChange(val)`：
- 若 `currentPage * val > total`：强制 `currentPage = 1`
- emit `pagination({ page: currentPage, limit: val })`
- 若 `autoScroll=true`：调用 `scrollTo(0, 800)`

### 3.2 切换 currentPage

`handleCurrentChange(val)`：
- emit `pagination({ page: val, limit: pageSize })`
- 若 `autoScroll=true`：调用 `scrollTo(0, 800)`

---

## 4) Responsive（移动端）

移动端隐藏：
- `< 768px` 下隐藏 sizes/jumper（见 `src/assets/styles/ruoyi.scss`）

复刻要求：
- 在小屏下分页仍可用（prev/next/pager），但减少占位。
