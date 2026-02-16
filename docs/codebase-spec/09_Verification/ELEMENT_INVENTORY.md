# Element Inventory
root: <repo_root>
generated: 2026-02-07T16:08:14Z

## 1. API Layer

### Route Definitions
Files likely containing route/endpoint definitions:


### Controllers

Controller files:
- ruoyi-fastapi-backend/module_admin/controller/cache_controller.py
- ruoyi-fastapi-backend/module_admin/controller/captcha_controller.py
- ruoyi-fastapi-backend/module_admin/controller/common_controller.py
- ruoyi-fastapi-backend/module_admin/controller/config_controller.py
- ruoyi-fastapi-backend/module_admin/controller/dept_controller.py
- ruoyi-fastapi-backend/module_admin/controller/dict_controller.py
- ruoyi-fastapi-backend/module_admin/controller/job_controller.py
- ruoyi-fastapi-backend/module_admin/controller/log_controller.py
- ruoyi-fastapi-backend/module_admin/controller/login_controller.py
- ruoyi-fastapi-backend/module_admin/controller/menu_controller.py
- ruoyi-fastapi-backend/module_admin/controller/notice_controller.py
- ruoyi-fastapi-backend/module_admin/controller/online_controller.py
- ruoyi-fastapi-backend/module_admin/controller/post_controller.py
- ruoyi-fastapi-backend/module_admin/controller/role_controller.py
- ruoyi-fastapi-backend/module_admin/controller/server_controller.py
- ruoyi-fastapi-backend/module_admin/controller/user_controller.py
- ruoyi-fastapi-backend/module_ai/controller/ai_chat_controller.py
- ruoyi-fastapi-backend/module_ai/controller/ai_model_controller.py
- ruoyi-fastapi-backend/module_generator/controller/gen_controller.py

### Middleware
Middleware files:
- ruoyi-fastapi-backend/middlewares/context_middleware.py
- ruoyi-fastapi-backend/middlewares/cors_middleware.py
- ruoyi-fastapi-backend/middlewares/gzip_middleware.py

## 2. Data Layer

### Models/Entities

### Migrations

SQL files:
- ruoyi-fastapi-backend/sql/ruoyi-fastapi-pg.sql
- ruoyi-fastapi-backend/sql/ruoyi-fastapi.sql
- ruoyi-fastapi-test/disable_captcha.sql

### Schemas/DTOs

## 3. Business Logic

### Services
Service directories:
- ruoyi-fastapi-backend/module_admin/service/
  - ruoyi-fastapi-backend/module_admin/service/login_service.py
  - ruoyi-fastapi-backend/module_admin/service/notice_service.py
  - ruoyi-fastapi-backend/module_admin/service/post_service.py
  - ruoyi-fastapi-backend/module_admin/service/job_log_service.py
  - ruoyi-fastapi-backend/module_admin/service/server_service.py
  - ruoyi-fastapi-backend/module_admin/service/common_service.py
  - ruoyi-fastapi-backend/module_admin/service/job_service.py
  - ruoyi-fastapi-backend/module_admin/service/log_service.py
  - ruoyi-fastapi-backend/module_admin/service/captcha_service.py
  - ruoyi-fastapi-backend/module_admin/service/online_service.py
  - ruoyi-fastapi-backend/module_admin/service/dept_service.py
  - ruoyi-fastapi-backend/module_admin/service/user_service.py
  - ruoyi-fastapi-backend/module_admin/service/role_service.py
  - ruoyi-fastapi-backend/module_admin/service/cache_service.py
  - ruoyi-fastapi-backend/module_admin/service/dict_service.py
  - ruoyi-fastapi-backend/module_admin/service/config_service.py
  - ruoyi-fastapi-backend/module_admin/service/menu_service.py
- ruoyi-fastapi-backend/module_ai/service/
  - ruoyi-fastapi-backend/module_ai/service/ai_chat_service.py
  - ruoyi-fastapi-backend/module_ai/service/ai_model_service.py
- ruoyi-fastapi-backend/module_generator/service/
  - ruoyi-fastapi-backend/module_generator/service/gen_service.py

Service files:
- ruoyi-fastapi-backend/module_admin/service/cache_service.py
- ruoyi-fastapi-backend/module_admin/service/captcha_service.py
- ruoyi-fastapi-backend/module_admin/service/common_service.py
- ruoyi-fastapi-backend/module_admin/service/config_service.py
- ruoyi-fastapi-backend/module_admin/service/dept_service.py
- ruoyi-fastapi-backend/module_admin/service/dict_service.py
- ruoyi-fastapi-backend/module_admin/service/job_log_service.py
- ruoyi-fastapi-backend/module_admin/service/job_service.py
- ruoyi-fastapi-backend/module_admin/service/log_service.py
- ruoyi-fastapi-backend/module_admin/service/login_service.py
- ruoyi-fastapi-backend/module_admin/service/menu_service.py
- ruoyi-fastapi-backend/module_admin/service/notice_service.py
- ruoyi-fastapi-backend/module_admin/service/online_service.py
- ruoyi-fastapi-backend/module_admin/service/post_service.py
- ruoyi-fastapi-backend/module_admin/service/role_service.py
- ruoyi-fastapi-backend/module_admin/service/server_service.py
- ruoyi-fastapi-backend/module_admin/service/user_service.py
- ruoyi-fastapi-backend/module_ai/service/ai_chat_service.py
- ruoyi-fastapi-backend/module_ai/service/ai_model_service.py
- ruoyi-fastapi-backend/module_generator/service/gen_service.py

### Use Cases / Domain

### Utils/Helpers
Utility directories:
- ruoyi-fastapi-app/src/utils/
- ruoyi-fastapi-backend/utils/
- ruoyi-fastapi-frontend/src/utils/

## 4. UI Layer (if applicable)

### Components
Component directories:
- ruoyi-fastapi-frontend/src/components/
  (28 component files)
- ruoyi-fastapi-frontend/src/layout/components/
  (13 component files)
- ruoyi-fastapi-frontend/src/views/ai/chat/components/
  (1 component files)

### Pages/Views
Page directories:
- ruoyi-fastapi-app/src/pages/
  - ruoyi-fastapi-app/src/pages/index.vue
  - ruoyi-fastapi-app/src/pages/login.vue
  - ruoyi-fastapi-app/src/pages/register.vue
  - ruoyi-fastapi-app/src/pages/common/textview/index.vue
  - ruoyi-fastapi-app/src/pages/common/privacy/index.vue
  - ruoyi-fastapi-app/src/pages/common/webview/index.vue
  - ruoyi-fastapi-app/src/pages/common/agreement/index.vue
  - ruoyi-fastapi-app/src/pages/work/index.vue
  - ruoyi-fastapi-app/src/pages/mine/index.vue
  - ruoyi-fastapi-app/src/pages/mine/pwd/index.vue
  - ruoyi-fastapi-app/src/pages/mine/about/index.vue
  - ruoyi-fastapi-app/src/pages/mine/info/index.vue
  - ruoyi-fastapi-app/src/pages/mine/info/edit.vue
  - ruoyi-fastapi-app/src/pages/mine/avatar/index.vue
  - ruoyi-fastapi-app/src/pages/mine/setting/index.vue
  - ruoyi-fastapi-app/src/pages/mine/help/index.vue
- ruoyi-fastapi-frontend/src/views/
  - ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue
  - ruoyi-fastapi-frontend/src/views/monitor/cache/list.vue
  - ruoyi-fastapi-frontend/src/views/monitor/operlog/index.vue
  - ruoyi-fastapi-frontend/src/views/monitor/server/index.vue
  - ruoyi-fastapi-frontend/src/views/monitor/druid/index.vue
  - ruoyi-fastapi-frontend/src/views/monitor/job/index.vue
  - ruoyi-fastapi-frontend/src/views/monitor/job/log.vue
  - ruoyi-fastapi-frontend/src/views/monitor/online/index.vue
  - ruoyi-fastapi-frontend/src/views/monitor/logininfor/index.vue
  - ruoyi-fastapi-frontend/src/views/login.vue
  - ruoyi-fastapi-frontend/src/views/register.vue
  - ruoyi-fastapi-frontend/src/views/dashboard/index.vue
  - ruoyi-fastapi-frontend/src/views/dashboard/editable-link-group.vue
  - ruoyi-fastapi-frontend/src/views/system/role/index.vue
  - ruoyi-fastapi-frontend/src/views/system/role/authUser.vue
  - ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue
  - ruoyi-fastapi-frontend/src/views/system/post/index.vue
  - ruoyi-fastapi-frontend/src/views/system/config/index.vue
  - ruoyi-fastapi-frontend/src/views/system/user/index.vue
  - ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue

### State Management

## 5. Integrations

### External API Clients

### Queue/Worker

## 6. Configuration

### Environment Variables
Environment files:
- ruoyi-fastapi-backend/.env.dev
- ruoyi-fastapi-backend/.env.dockermy
- ruoyi-fastapi-backend/.env.dockerpg
- ruoyi-fastapi-backend/.env.prod
- ruoyi-fastapi-frontend/.env.development
- ruoyi-fastapi-frontend/.env.docker
- ruoyi-fastapi-frontend/.env.production
- ruoyi-fastapi-frontend/.env.staging

### Config Files
Config files:
- ruoyi-fastapi-app/src/config.js
- ruoyi-fastapi-app/src/store/modules/config.js
- ruoyi-fastapi-frontend/src/api/system/config.js
- ruoyi-fastapi-frontend/src/utils/generator/config.js
- ruoyi-fastapi-app/postcss.config.ts
- ruoyi-fastapi-app/tailwind.config.ts
- ruoyi-fastapi-app/vite.config.ts
- ruoyi-fastapi-frontend/vite.config.js

## 7. Testing

Test files found: 19
- ruoyi-fastapi-test/monitor/test_cache_list.py
- ruoyi-fastapi-test/monitor/test_cache_monitor.py
- ruoyi-fastapi-test/monitor/test_job_management.py
- ruoyi-fastapi-test/monitor/test_online_user.py
- ruoyi-fastapi-test/monitor/test_server_monitor.py
- ruoyi-fastapi-test/system/test_config_management.py
- ruoyi-fastapi-test/system/test_dept_management.py
- ruoyi-fastapi-test/system/test_dict_management.py
- ruoyi-fastapi-test/system/test_log_management.py
- ruoyi-fastapi-test/system/test_menu_management.py
- ruoyi-fastapi-test/system/test_notice_management.py
- ruoyi-fastapi-test/system/test_post_management.py
- ruoyi-fastapi-test/system/test_role_management.py
- ruoyi-fastapi-test/system/test_user_management.py
- ruoyi-fastapi-test/test_login.py
- ruoyi-fastapi-test/test_pages.py
- ruoyi-fastapi-test/tool/test_code_gen.py
- ruoyi-fastapi-test/tool/test_swagger.py
- ruoyi-fastapi-test/visual/test_visual_baseline.py

## 8. Infrastructure

### Docker
Docker files:
- ruoyi-fastapi-backend/Dockerfile.my
- ruoyi-fastapi-backend/Dockerfile.pg
- ruoyi-fastapi-frontend/Dockerfile
- docker-compose.my.yml
- docker-compose.pg.yml
- ruoyi-fastapi-test/docker-compose.test.my.yml
- ruoyi-fastapi-test/docker-compose.test.pg.yml

### CI/CD
CI/CD directories:
- .github/
CI/CD files:
- .github/FUNDING.yml
- .github/workflows/playwright.yml
- .github/workflows/ruff.yml

## Summary

This inventory provides a starting point for specification extraction.
Review each category and identify which elements require detailed documentation.

Priority order recommendation:
1. Data models (foundation for understanding the domain)
2. API endpoints (external interface contract)
3. Business logic services (core behavior)
4. UI components (if applicable)
5. Integrations (external dependencies)
6. Infrastructure (deployment requirements)
