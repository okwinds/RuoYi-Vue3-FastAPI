from __future__ import annotations

import hashlib
import json
import os
from dataclasses import dataclass
from io import BytesIO
from pathlib import Path
from typing import TYPE_CHECKING

import pytest
import requests
from PIL import Image
from playwright.async_api import async_playwright, expect

from common.config import Config
from common.login_helper import LoginHelper

if TYPE_CHECKING:
    from playwright.async_api import Browser, BrowserContext, Page, Playwright


@dataclass(frozen=True)
class VisualCase:
    theme: str  # "light" | "dark"
    nav_type: int  # 1 | 2 | 3
    page_id: str
    url_path: str
    wait: tuple[str, ...]
    collapsed: bool = False


ROOT_DIR = Path(__file__).resolve().parents[2]
BASELINE_DIR = ROOT_DIR / 'docs' / 'ui-ux-spec' / '08_Visual_Baseline' / 'screenshots'
ARTIFACT_DIR = ROOT_DIR / 'ruoyi-fastapi-test' / '.artifacts' / 'visual'
AUTH_ARTIFACT_DIR = ROOT_DIR / 'ruoyi-fastapi-test' / '.artifacts' / 'auth'

HTTP_STATUS_OK = 200
RESPONSE_CODE_OK = 200

_VISUAL_DETERMINISM_CSS = """
* {
  transition-duration: 0s !important;
  transition-delay: 0s !important;
  animation-duration: 0s !important;
  animation-delay: 0s !important;
  caret-color: transparent !important;
}

/* Hide scrollbars to avoid tiny cross-run raster diffs */
*::-webkit-scrollbar {
  width: 0 !important;
  height: 0 !important;
}
* {
  scrollbar-width: none !important;
}
"""


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _pixel_sha256(png_bytes: bytes) -> tuple[str, tuple[int, int]]:
    """
    计算截图的“像素级”hash，忽略 PNG 元数据差异（例如 tIME chunk）。

    :return: (sha256_hex, (width, height))
    """
    with Image.open(BytesIO(png_bytes)) as im:
        rgba = im.convert('RGBA')
        pixel_bytes = rgba.tobytes()
        return _sha256(pixel_bytes), rgba.size


def _pixel_diff_stats(expected_png: bytes, actual_png: bytes, *, max_scan_pixels: int | None = None) -> dict:
    """
    计算两张 PNG 的像素差异统计（用于“极小抖动容忍”）。

    :param max_scan_pixels: 允许提前中止扫描的阈值（非严格 diff count），用于避免全量遍历耗时。
    :return: dict(diff_pixels, max_diff_sum_rgba, bbox)
    """
    expected_sha, expected_size = _pixel_sha256(expected_png)
    actual_sha, actual_size = _pixel_sha256(actual_png)
    if expected_size != actual_size:
        return {
            'size_mismatch': True,
            'expected_size': expected_size,
            'actual_size': actual_size,
            'expected_pixel_sha256': expected_sha,
            'actual_pixel_sha256': actual_sha,
        }

    with Image.open(BytesIO(expected_png)) as expected_im, Image.open(BytesIO(actual_png)) as actual_im:
        expected_rgba = expected_im.convert('RGBA')
        actual_rgba = actual_im.convert('RGBA')
        w, h = expected_rgba.size
        a = expected_rgba.tobytes()
        b = actual_rgba.tobytes()

    minx = miny = 10**9
    maxx = maxy = -1
    diff_pixels = 0
    max_diff_sum_rgba = 0

    for i in range(0, len(a), 4):
        if a[i : i + 4] == b[i : i + 4]:
            continue
        diff_pixels += 1
        px = (i // 4) % w
        py = (i // 4) // w
        minx = min(minx, px)
        miny = min(miny, py)
        maxx = max(maxx, px)
        maxy = max(maxy, py)
        diff_sum = sum(abs(a[i + j] - b[i + j]) for j in range(4))
        max_diff_sum_rgba = max(max_diff_sum_rgba, diff_sum)
        if max_scan_pixels is not None and diff_pixels > max_scan_pixels:
            break

    bbox = None
    if diff_pixels > 0 and maxx >= 0 and maxy >= 0:
        bbox = (minx, miny, maxx, maxy)

    return {
        'size_mismatch': False,
        'diff_pixels': diff_pixels,
        'max_diff_sum_rgba': max_diff_sum_rgba,
        'bbox': bbox,
        'expected_pixel_sha256': expected_sha,
        'actual_pixel_sha256': actual_sha,
        'size': (w, h),
    }


def _baseline_name(case: VisualCase) -> str:
    suffix = '_collapsed' if case.collapsed else ''
    return f'{case.theme}_{case.nav_type}_{case.page_id}{suffix}.png'


def _layout_setting(nav_type: int) -> dict:
    return {
        'navType': nav_type,
        'tagsView': True,
        'tagsIcon': False,
        'fixedHeader': True,
        'sidebarLogo': True,
        'dynamicTitle': False,
        'footerVisible': False,
        'sideTheme': 'theme-dark',
        'theme': '#409EFF',
    }


def _init_script(theme: str, nav_type: int) -> str:
    # localStorage 只能存字符串；前端侧通常会 JSON.parse 读取该值
    layout_setting_json = json.dumps(_layout_setting(nav_type), ensure_ascii=False)
    layout_setting_js_string = json.dumps(layout_setting_json, ensure_ascii=False)
    scheme = 'dark' if theme == 'dark' else 'light'
    frozen_now_ms = 1735689600000  # 2025-01-01T00:00:00Z

    return f"""
(() => {{
  try {{
    localStorage.setItem('layout-setting', {layout_setting_js_string});
    localStorage.setItem('vueuse-color-scheme', '{scheme}');
  }} catch (e) {{}}

  // Freeze time (best-effort)
  try {{
    const OriginalDate = Date;
    class FrozenDate extends OriginalDate {{
      constructor(...args) {{
        if (args.length === 0) {{
          super({frozen_now_ms});
        }} else {{
          super(...args);
        }}
      }}
      static now() {{ return {frozen_now_ms}; }}
    }}
    // @ts-ignore
    window.Date = FrozenDate;
  }} catch (e) {{}}

  // Make randomness deterministic (best-effort)
  try {{
    let seed = 42;
    // xorshift32
    function prng() {{
      seed ^= seed << 13;
      seed ^= seed >>> 17;
      seed ^= seed << 5;
      return ((seed >>> 0) / 4294967296);
    }}
    Math.random = prng;
  }} catch (e) {{}}

  // Apply theme class + determinism CSS when DOM is ready (document.head may be null at init_script time)
  const apply = () => {{
    try {{
      const el = document.documentElement;
      if (el) {{
        if ('{scheme}' === 'dark') el.classList.add('dark');
        else el.classList.remove('dark');
      }}
    }} catch (e) {{}}

    try {{
      const head = document.head;
      if (!head) return;
      if (document.querySelector('style[data-visual-baseline=\"1\"]')) return;
      const style = document.createElement('style');
      style.setAttribute('data-visual-baseline', '1');
      style.textContent = {json.dumps(_VISUAL_DETERMINISM_CSS)};
      head.appendChild(style);
    }} catch (e) {{}}
  }};

  try {{
    if (document.readyState === 'loading') {{
      document.addEventListener('DOMContentLoaded', apply, {{ once: true }});
    }} else {{
      apply();
    }}
  }} catch (e) {{}}
}})();
"""


async def _get_admin_token() -> str:
    """
    获取 admin token（尽量复用缓存，避免每次 /login 产生新 session 造成页面数据波动）。

    策略：
    - 优先读取本地缓存 token；
    - 若 token 可用（/getInfo 200 且 code==200）则直接复用；
    - 否则走 /login 重新获取并覆盖缓存。
    """

    AUTH_ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    cache_path = AUTH_ARTIFACT_DIR / 'admin_token.json'

    def _is_token_valid(token: str) -> bool:
        try:
            r = requests.get(
                Config.backend_url + '/getInfo',
                headers={'Authorization': 'Bearer ' + token},
                timeout=5,
            )
            if r.status_code != HTTP_STATUS_OK:
                return False
            payload = r.json()
            return payload.get('code') == RESPONSE_CODE_OK or payload.get('success') is True
        except Exception:
            return False

    if cache_path.exists():
        try:
            cached = json.loads(cache_path.read_text(encoding='utf-8'))
            token = cached.get('token')
            if isinstance(token, str) and token and _is_token_valid(token):
                return token
        except Exception:
            pass

    helper = LoginHelper()
    token = helper.login(username='admin', password='admin123')
    assert token, '获取 Admin token 失败（请确认后端已启动且测试环境禁用验证码）'
    cache_path.write_text(json.dumps({'token': token}, ensure_ascii=False), encoding='utf-8')
    return token


async def _new_context(
    playwright: Playwright,
    theme: str,
    nav_type: int,
    token: str | None,
) -> tuple[Browser, BrowserContext]:
    browser = await playwright.chromium.launch(
        headless=True,
        args=[
            '--force-color-profile=srgb',
            '--disable-lcd-text',
            '--disable-font-subpixel-positioning',
            '--disable-skia-runtime-opts',
        ],
    )
    context = await browser.new_context(
        viewport={'width': 1440, 'height': 900},
        device_scale_factor=1,
        locale='zh-CN',
        reduced_motion='reduce',
        color_scheme='dark' if theme == 'dark' else 'light',
        timezone_id='UTC',
    )
    await context.add_init_script(_init_script(theme, nav_type))
    if token:
        # 前端通过 js-cookie 读取 Admin-Token；这里用 url 写入 host-only cookie，避免 localhost domain 行为差异
        await context.add_cookies([{'name': 'Admin-Token', 'value': token, 'url': Config.frontend_url}])
    return browser, context


async def _ensure_deterministic_dom(page: Page, case: VisualCase) -> None:
    """
    确保截图前的 DOM/样式进入“可复现”状态。

    说明：
    - `add_init_script` 是 best-effort，可能因 `document.head` 尚未就绪导致 CSS 未注入；
    - 部分页面（尤其包含 canvas 图表）在首屏会有短暂动画/渲染波动；
    - 这里在每次截图前补一层“兜底”处理，降低跨运行像素差异。
    """
    scheme = 'dark' if case.theme == 'dark' else 'light'

    # Theme class must match the screenshot case.
    try:
        await page.evaluate(
            """(scheme) => {
  const el = document.documentElement;
  if (!el) return;
  if (scheme === 'dark') el.classList.add('dark');
  else el.classList.remove('dark');
}""",
            scheme,
        )
    except Exception:
        pass

    # Disable transitions/animations again (in case init_script missed).
    try:
        await page.add_style_tag(content=_VISUAL_DETERMINISM_CSS)
    except Exception:
        pass

    # Avoid focus-ring/caret variability.
    try:
        await page.evaluate(
            """() => {
  const el = document.activeElement;
  if (el && typeof el.blur === 'function') el.blur();
}"""
        )
    except Exception:
        pass

    # Wait for webfonts to be ready to avoid fallback font jitter.
    try:
        await page.evaluate('() => (document.fonts ? document.fonts.ready : null)')
    except Exception:
        pass

    # Ensure deterministic scroll position (some pages use .app-main as the scroll container).
    try:
        await page.evaluate(
            """() => {
  try { window.scrollTo(0, 0); } catch (e) {}
  try {
    const el = document.querySelector('.app-main');
    if (el && typeof el.scrollTo === 'function') el.scrollTo(0, 0);
  } catch (e) {}
}"""
        )
    except Exception:
        pass

    # Mask inherently dynamic monitoring pages (CPU/mem/disk/redis metrics, charts).
    if case.page_id == 'monitor-cache':
        try:
            await page.add_style_tag(
                content="""
/* Make column widths deterministic (dynamic text would otherwise shift table layout) */
.app-container table {
  table-layout: fixed !important;
}

/* Hide dynamic values in the basic info table (keep labels) */
.app-container table tbody td:nth-child(2n) .cell {
  visibility: hidden !important;
}

/* Hide charts (ECharts canvas + SVG) to avoid raster diffs */
.app-container canvas,
.app-container svg {
  visibility: hidden !important;
}

/* Ensure chart containers keep their height */
.app-container [style*="height: 420px"] {
  background: transparent !important;
}
"""
            )
        except Exception:
            pass

    if case.page_id == 'monitor-server':
        try:
            # Hide non-label columns for all tables; then additionally hide disk table body.
            await page.add_style_tag(
                content="""
.app-container table {
  table-layout: fixed !important;
}

.app-container table tbody td:not(:first-child) .cell {
  visibility: hidden !important;
}
"""
            )
        except Exception:
            pass
        try:
            await page.evaluate(
                """() => {
  const tables = Array.from(document.querySelectorAll('.app-container table'));
  for (const table of tables) {
    const headerText = (table.querySelector('thead')?.innerText || '').trim();
    if (headerText.includes('盘符路径')) {
      const tbody = table.querySelector('tbody');
      if (tbody) tbody.style.visibility = 'hidden';
    }
  }
}"""
            )
        except Exception:
            pass


async def _capture(page: Page, case: VisualCase) -> bytes:
    await page.goto(Config.frontend_url + case.url_path, wait_until='domcontentloaded')

    # Best-effort: wait for resources and initial render to settle.
    try:
        await page.wait_for_load_state('load', timeout=15000)
    except Exception:
        pass

    for selector in case.wait:
        if selector.startswith('frame:'):
            # frame:<css iframe selector>::<css inside frame selector>::<expected text>
            _prefix, rest = selector.split('frame:', 1)
            iframe_css, inner_css, expected_text = rest.split('::', 2)
            iframe = page.locator(iframe_css)
            await expect(iframe).to_be_visible()
            frame = page.frame_locator(iframe_css)
            await expect(frame.locator(inner_css)).to_contain_text(expected_text, timeout=30000)
        else:
            await page.wait_for_selector(selector, timeout=30000)

    # Wait for Element Plus loading mask to disappear (monitor pages use $modal.loading()).
    try:
        await page.wait_for_selector('.el-loading-mask', state='hidden', timeout=15000)
    except Exception:
        pass

    if case.collapsed:
        # Only meaningful for navType=1 on pages using the layout shell.
        await page.locator('#hamburger-container').click()
        await page.wait_for_selector('.app-wrapper.hideSidebar', timeout=30000)
        # Ensure the collapsed sidebar width has settled.
        try:
            await page.wait_for_function(
                """() => {
  const el = document.querySelector('.sidebar-container');
  if (!el) return true;
  const w = el.getBoundingClientRect().width;
  return w > 0 && Math.abs(w - 54) < 0.5;
}""",
                timeout=8000,
            )
        except Exception:
            pass

    await _ensure_deterministic_dom(page, case)
    await page.wait_for_timeout(1200)  # settle layout + charts
    return await page.screenshot(full_page=False)


def _cases() -> list[VisualCase]:
    return [
        # login (no auth)
        VisualCase('light', 1, 'login', '/login', ('input[placeholder="账号"]', 'input[placeholder="密码"]')),
        VisualCase('dark', 1, 'login', '/login', ('input[placeholder="账号"]', 'input[placeholder="密码"]')),
        # dashboard
        VisualCase('light', 1, 'dashboard', '/index', ('.pageHeaderContent',)),
        VisualCase('dark', 1, 'dashboard', '/index', ('.pageHeaderContent',)),
        VisualCase('light', 2, 'dashboard', '/index', ('.pageHeaderContent',)),
        VisualCase('dark', 2, 'dashboard', '/index', ('.pageHeaderContent',)),
        VisualCase('light', 3, 'dashboard', '/index', ('.pageHeaderContent',)),
        VisualCase('dark', 3, 'dashboard', '/index', ('.pageHeaderContent',)),
        VisualCase('light', 1, 'dashboard', '/index', ('.pageHeaderContent',), collapsed=True),
        VisualCase('dark', 1, 'dashboard', '/index', ('.pageHeaderContent',), collapsed=True),
        # key pages navType=1
        VisualCase('light', 1, 'system-user', '/system/user', ('div:has-text("用户管理")', '.app-container')),
        VisualCase('dark', 1, 'system-user', '/system/user', ('div:has-text("用户管理")', '.app-container')),
        VisualCase('light', 1, 'system-role', '/system/role', ('div:has-text("角色管理")', '.app-container')),
        VisualCase('dark', 1, 'system-role', '/system/role', ('div:has-text("角色管理")', '.app-container')),
        VisualCase('light', 1, 'system-menu', '/system/menu', ('div:has-text("菜单管理")', '.app-container')),
        VisualCase('dark', 1, 'system-menu', '/system/menu', ('div:has-text("菜单管理")', '.app-container')),
        VisualCase(
            'light',
            1,
            'monitor-online',
            '/monitor/online',
            ('.app-container', 'button:has-text("搜索")'),
        ),
        VisualCase(
            'dark',
            1,
            'monitor-online',
            '/monitor/online',
            ('.app-container', 'button:has-text("搜索")'),
        ),
        VisualCase(
            'light',
            1,
            'monitor-cache',
            '/monitor/cache',
            ('text=基本信息', 'text=Redis版本', 'text=内存信息'),
        ),
        VisualCase(
            'dark',
            1,
            'monitor-cache',
            '/monitor/cache',
            ('text=基本信息', 'text=Redis版本', 'text=内存信息'),
        ),
        VisualCase(
            'light',
            1,
            'monitor-server',
            '/monitor/server',
            ('text=CPU', 'text=内存', 'text=服务器信息', 'text=磁盘状态'),
        ),
        VisualCase(
            'dark',
            1,
            'monitor-server',
            '/monitor/server',
            ('text=CPU', 'text=内存', 'text=服务器信息', 'text=磁盘状态'),
        ),
        VisualCase(
            'light',
            1,
            'monitor-job',
            '/monitor/job',
            ('text=任务名称', '.app-container'),
        ),
        VisualCase(
            'dark',
            1,
            'monitor-job',
            '/monitor/job',
            ('text=任务名称', '.app-container'),
        ),
        VisualCase(
            'light',
            1,
            'tool-swagger',
            '/tool/swagger',
            ('frame:iframe::h1::Swagger UI has been disabled. Please enable it first.',),
        ),
        VisualCase(
            'dark',
            1,
            'tool-swagger',
            '/tool/swagger',
            ('frame:iframe::h1::Swagger UI has been disabled. Please enable it first.',),
        ),
        VisualCase('light', 1, 'tool-gen', '/tool/gen', ('.app-container', 'button:has-text("导入")')),
        VisualCase('dark', 1, 'tool-gen', '/tool/gen', ('.app-container', 'button:has-text("导入")')),
        VisualCase('light', 1, 'ai-chat', '/ai/chat', ('.app-container.chat-container', 'text=AI 智能助手')),
        VisualCase('dark', 1, 'ai-chat', '/ai/chat', ('.app-container.chat-container', 'text=AI 智能助手')),
        VisualCase('light', 1, 'ai-model', '/ai/model', ('.app-container', 'text=模型编码')),
        VisualCase('dark', 1, 'ai-model', '/ai/model', ('.app-container', 'text=模型编码')),
    ]


@pytest.mark.asyncio
async def test_visual_baseline() -> None:
    update = os.environ.get('UPDATE_BASELINE') in {'1', 'true', 'TRUE', 'yes', 'YES'}
    # 默认允许极小像素抖动：用于抵抗渲染/抗锯齿带来的 1~数个像素差异（同机也可能发生）。
    # 若需要“严格像素一致”，将两个 env 都设置为 0。
    max_tolerated_pixels = int(os.environ.get('VISUAL_MAX_TOLERATED_PIXELS', '10') or '10')
    max_tolerated_diff_sum_rgba = int(os.environ.get('VISUAL_MAX_TOLERATED_DIFF_SUM_RGBA', '120') or '120')
    BASELINE_DIR.mkdir(parents=True, exist_ok=True)
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)

    token = await _get_admin_token()
    cases = _cases()
    errors: list[str] = []

    async with async_playwright() as p:
        for case in cases:
            needs_auth = case.page_id != 'login'
            browser = None
            context = None
            try:
                browser, context = await _new_context(p, case.theme, case.nav_type, token if needs_auth else None)
                page = await context.new_page()
                actual = await _capture(page, case)

                baseline_path = BASELINE_DIR / _baseline_name(case)
                if update or not baseline_path.exists():
                    baseline_path.write_bytes(actual)
                    continue

                expected = baseline_path.read_bytes()
                actual_pixel_sha, actual_size = _pixel_sha256(actual)
                expected_pixel_sha, expected_size = _pixel_sha256(expected)
                if actual_size != expected_size or actual_pixel_sha != expected_pixel_sha:
                    if max_tolerated_pixels > 0:
                        stats = _pixel_diff_stats(
                            expected,
                            actual,
                            max_scan_pixels=max_tolerated_pixels,
                        )
                        if (
                            stats.get('size_mismatch') is False
                            and stats.get('diff_pixels', max_tolerated_pixels + 1) <= max_tolerated_pixels
                            and (
                                max_tolerated_diff_sum_rgba <= 0
                                or stats.get('max_diff_sum_rgba', max_tolerated_diff_sum_rgba + 1)
                                <= max_tolerated_diff_sum_rgba
                            )
                        ):
                            continue

                    actual_path = ARTIFACT_DIR / (baseline_path.stem + '.actual.png')
                    actual_path.write_bytes(actual)
                    errors.append(
                        '视觉基线不一致: '
                        f'{baseline_path.as_posix()} '
                        f'(expected_size={expected_size}, actual_size={actual_size}, '
                        f'expected_pixel_sha256={expected_pixel_sha}, actual_pixel_sha256={actual_pixel_sha}, '
                        f'actual_saved={actual_path.as_posix()})'
                    )
            finally:
                if context:
                    await context.close()
                if browser:
                    await browser.close()

    if errors:
        raise AssertionError('\\n'.join(errors))
