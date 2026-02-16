# UI Source Scan
root: `ruoyi-fastapi-frontend/`
scan_roots:
- `ruoyi-fastapi-frontend/`
generated: 2026-02-14

说明：
- 本文件是“UI/UX 规格提取”的索引层：列出前端 UI 相关的**真实源码位置**，用于后续逐条补齐像素级规格（tokens/组件/页面/资产）。
- 复跑方式（示例命令，输出需手动整理成下文结构）：
  - `cd ruoyi-fastapi-frontend && find src/assets/styles -maxdepth 1 -type f | sort`
  - `cd ruoyi-fastapi-frontend && find src/components -type f | sort`
  - `cd ruoyi-fastapi-frontend && find src/layout -type f | sort`
  - `cd ruoyi-fastapi-frontend && find src/views -type f -name '*.vue' | sort`
- 推荐复跑（更全、可复现、可 diff）：
  - `~/.claude/skills/ui-ux-spec-genome/scripts/scan_ui_sources.sh --root ruoyi-fastapi-frontend --out /tmp/ui_scan.md --force`
  - 然后把 `/tmp/ui_scan.md` 的结果人工归并到下文结构（本文件不直接保存 scan script 的绝对路径输出，避免把本机路径写入仓库）。

## Design tokens / themes / styles
src/assets/icons/svg/theme.svg
src/utils/theme.js

## App entry / router / state（布局与导航“工程骨架”）
src/App.vue
src/main.js
src/settings.js
src/router/index.js
src/store/index.js
src/store/modules/app.js
src/store/modules/permission.js
src/store/modules/settings.js
src/store/modules/tagsView.js
src/store/modules/user.js

## Keyword hits (themes/tokens/providers)
src/api/monitor/online.js
src/permission.js
src/store/modules/settings.js
src/store/modules/user.js
src/utils/auth.js
src/utils/request.js

## Keyword hits (CSS variables / theming)
src/assets/styles/ruoyi.scss
src/assets/styles/variables.module.scss

## Keyword hits (styling systems)
(none)

## Directives / plugins（UI 行为辅助）
src/directive/hasPermi.js
src/directive/index.js
src/plugins/auth.js
src/plugins/cache.js
src/plugins/download.js
src/plugins/index.js
src/plugins/modal.js
src/plugins/print.js
src/plugins/tab.js

## Global styles / resets
src/assets/styles/index.scss

## Tailwind / PostCSS
(none)

## Component sources
src/components/Breadcrumb/index.vue
src/components/Crontab/day.vue
src/components/Crontab/hour.vue
src/components/Crontab/index.vue
src/components/Crontab/min.vue
src/components/Crontab/month.vue
src/components/Crontab/result.vue
src/components/Crontab/second.vue
src/components/Crontab/week.vue
src/components/Crontab/year.vue
src/components/DictTag/index.vue
src/components/Editor/index.vue
src/components/FileUpload/index.vue
src/components/Hamburger/index.vue
src/components/HeaderSearch/index.vue
src/components/IconSelect/index.vue
src/components/IconSelect/requireIcons.js
src/components/ImagePreview/index.vue
src/components/ImageUpload/index.vue
src/components/Pagination/index.vue
src/components/ParentView/index.vue
src/components/RightToolbar/index.vue
src/components/RuoYi/Doc/index.vue
src/components/RuoYi/Git/index.vue
src/components/Screenfull/index.vue
src/components/SizeSelect/index.vue
src/components/SvgIcon/index.vue
src/components/SvgIcon/svgicon.js
src/components/TopNav/index.vue
src/components/iFrame/index.vue
src/layout/components/AppMain.vue
src/layout/components/Copyright/index.vue
src/layout/components/IframeToggle/index.vue
src/layout/components/InnerLink/index.vue
src/layout/components/Navbar.vue
src/layout/components/Settings/index.vue
src/layout/components/Sidebar/Link.vue
src/layout/components/Sidebar/Logo.vue
src/layout/components/Sidebar/SidebarItem.vue
src/layout/components/Sidebar/index.vue
src/layout/components/TagsView/ScrollPane.vue
src/layout/components/TagsView/index.vue
src/layout/components/TopBar/index.vue
src/layout/components/index.js
src/layout/index.vue
src/views/ai/chat/components/AiMessage.vue

## Pages / routes / layouts
src/views/ai/chat/components/AiMessage.vue
src/views/ai/chat/index.vue
src/views/ai/model/index.vue
src/views/dashboard/editable-link-group.vue
src/views/dashboard/index.vue
src/views/error/401.vue
src/views/error/404.vue
src/views/login.vue
src/views/monitor/cache/index.vue
src/views/monitor/cache/list.vue
src/views/monitor/druid/index.vue
src/views/monitor/job/index.vue
src/views/monitor/job/log.vue
src/views/monitor/logininfor/index.vue
src/views/monitor/online/index.vue
src/views/monitor/operlog/index.vue
src/views/monitor/server/index.vue
src/views/redirect/index.vue
src/views/register.vue
src/views/system/config/index.vue
src/views/system/dept/index.vue
src/views/system/dict/data.vue
src/views/system/dict/index.vue
src/views/system/menu/index.vue
src/views/system/notice/index.vue
src/views/system/post/index.vue
src/views/system/role/authUser.vue
src/views/system/role/index.vue
src/views/system/role/selectUser.vue
src/views/system/user/authRole.vue
src/views/system/user/index.vue
src/views/system/user/profile/index.vue
src/views/system/user/profile/resetPwd.vue
src/views/system/user/profile/userAvatar.vue
src/views/system/user/profile/userInfo.vue
src/views/tool/build/CodeTypeDialog.vue
src/views/tool/build/DraggableItem.vue
src/views/tool/build/IconsDialog.vue
src/views/tool/build/RightPanel.vue
src/views/tool/build/TreeNodeDialog.vue
src/views/tool/build/index.vue
src/views/tool/gen/basicInfoForm.vue
src/views/tool/gen/createTable.vue
src/views/tool/gen/editTable.vue
src/views/tool/gen/genInfoForm.vue
src/views/tool/gen/importTable.vue
src/views/tool/gen/index.vue
src/views/tool/swagger/index.vue

## Storybook / stories
(none)

## Assets (icons/images)
public/favicon.ico
src/assets/401_images/401.gif
src/assets/404_images/404.png
src/assets/404_images/404_cloud.png
src/assets/icons/svg/404.svg
src/assets/icons/svg/ai-chat.svg
src/assets/icons/svg/ai-manage.svg
src/assets/icons/svg/ai-model.svg
src/assets/icons/svg/bug.svg
src/assets/icons/svg/build.svg
src/assets/icons/svg/button.svg
src/assets/icons/svg/cascader.svg
src/assets/icons/svg/chart.svg
src/assets/icons/svg/checkbox.svg
src/assets/icons/svg/clipboard.svg
src/assets/icons/svg/code.svg
src/assets/icons/svg/color.svg
src/assets/icons/svg/component.svg
src/assets/icons/svg/dashboard.svg
src/assets/icons/svg/date-range.svg
src/assets/icons/svg/date.svg
src/assets/icons/svg/deepthink.svg
src/assets/icons/svg/dict.svg
src/assets/icons/svg/documentation.svg
src/assets/icons/svg/download.svg
src/assets/icons/svg/drag.svg
src/assets/icons/svg/druid.svg
src/assets/icons/svg/edit.svg
src/assets/icons/svg/education.svg
src/assets/icons/svg/email.svg
src/assets/icons/svg/enter.svg
src/assets/icons/svg/example.svg
src/assets/icons/svg/excel.svg
src/assets/icons/svg/exit-fullscreen.svg
src/assets/icons/svg/eye-open.svg
src/assets/icons/svg/eye.svg
src/assets/icons/svg/form.svg
src/assets/icons/svg/fullscreen.svg
src/assets/icons/svg/github.svg
src/assets/icons/svg/guide.svg
src/assets/icons/svg/icon.svg
src/assets/icons/svg/input.svg
src/assets/icons/svg/international.svg
src/assets/icons/svg/job.svg
src/assets/icons/svg/language.svg
src/assets/icons/svg/link.svg
src/assets/icons/svg/list.svg
src/assets/icons/svg/lock.svg
src/assets/icons/svg/log.svg
src/assets/icons/svg/logininfor.svg
src/assets/icons/svg/message.svg
src/assets/icons/svg/money.svg
src/assets/icons/svg/monitor.svg
src/assets/icons/svg/moon.svg
src/assets/icons/svg/more-up.svg
src/assets/icons/svg/nested.svg
src/assets/icons/svg/number.svg
src/assets/icons/svg/online.svg
src/assets/icons/svg/password.svg
src/assets/icons/svg/pdf.svg
src/assets/icons/svg/people.svg
src/assets/icons/svg/peoples.svg
src/assets/icons/svg/phone.svg
src/assets/icons/svg/post.svg
src/assets/icons/svg/qq.svg
src/assets/icons/svg/question.svg
src/assets/icons/svg/radio.svg
src/assets/icons/svg/rate.svg
src/assets/icons/svg/redis-list.svg
src/assets/icons/svg/redis.svg
src/assets/icons/svg/row.svg
src/assets/icons/svg/search.svg
src/assets/icons/svg/select.svg
src/assets/icons/svg/server.svg
src/assets/icons/svg/shopping.svg
src/assets/icons/svg/size.svg
src/assets/icons/svg/skill.svg
src/assets/icons/svg/slider.svg
src/assets/icons/svg/star.svg
src/assets/icons/svg/sunny.svg
src/assets/icons/svg/swagger.svg
src/assets/icons/svg/switch.svg
src/assets/icons/svg/system.svg
src/assets/icons/svg/tab.svg
src/assets/icons/svg/table.svg
src/assets/icons/svg/textarea.svg
src/assets/icons/svg/theme.svg
src/assets/icons/svg/time-range.svg
src/assets/icons/svg/time.svg
src/assets/icons/svg/tool.svg
src/assets/icons/svg/tree-table.svg
src/assets/icons/svg/tree.svg
src/assets/icons/svg/upload.svg
src/assets/icons/svg/user.svg
src/assets/icons/svg/validCode.svg
src/assets/icons/svg/wechat.svg
src/assets/icons/svg/zip.svg
src/assets/images/dark.svg
src/assets/images/light.svg
src/assets/images/login-background.jpg
src/assets/images/profile.jpg
src/assets/logo/logo.png
src/assets/styles/btn.scss
src/assets/styles/element-ui.scss
src/assets/styles/index.scss
src/assets/styles/mixin.scss
src/assets/styles/ruoyi.scss
src/assets/styles/sidebar.scss
src/assets/styles/transition.scss
src/assets/styles/variables.module.scss

## i18n / copy
(none)

## A11y / visual regression / tests
- 视觉基线（像素级验收真源）：
  - `docs/ui-ux-spec/08_Visual_Baseline/README.md`
  - `ruoyi-fastapi-test/visual/test_visual_baseline.py`
