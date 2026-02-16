# Source Anchor 校验报告（Spec → Code）

generated: `2026-02-14 19:47:34 CST`

用途：对 `docs/codebase-spec/**.md` 中的 `Source:` 锚点做存在性校验，确保规格文档能稳定定位到源码文件。

> 说明：本报告聚焦“可复跑/可移植”。为避免泄露本机绝对路径，本报告仅输出仓库相对路径与汇总结论。

---

## 1) 校验口径

被校验的锚点格式（示例）：
- `Source: ruoyi-fastapi-backend/app.py`
- `Source: ruoyi-fastapi-backend/app.py:123`
- `Source: ruoyi-fastapi-backend/app.py#main`
- `Source: ruoyi-fastapi-backend/app.py:123#main`

本次校验仅验证：
- 文件路径存在（存在性）

不强制验证（可选增强项）：
- 行号存在性（需要解析 `:line`）
- symbol 可解析（需要做文本匹配/AST）

---

## 2) 复跑命令（本仓库内可复现）

```bash
python - <<'PY'
import re
from pathlib import Path

spec_root = Path('docs/codebase-spec')
project_root = Path('.')
pattern = re.compile(r'^-\\s*Source:\\s*`([^`]+)`\\s*$')

anchors = []
for md in spec_root.rglob('*.md'):
    for line in md.read_text('utf-8', errors='ignore').splitlines():
        m = pattern.match(line.strip())
        if m:
            anchors.append((md.as_posix(), m.group(1)))

def resolve(src: str) -> Path:
    path_part = src.split('#', 1)[0]
    if ':' in path_part:
        p0, rest = path_part.split(':', 1)
        if rest.isdigit():
            path_part = p0
    return project_root / path_part

missing = []
for md_path, src in anchors:
    if not resolve(src).exists():
        missing.append((md_path, src))

print('anchors_total=', len(anchors))
print('missing_total=', len(missing))
for item in missing[:50]:
    print('MISSING', item)
PY
```

---

## 3) 结果（本次执行）

- anchors_total: `167`
- missing_total: `0`

Verdict: `OK`
