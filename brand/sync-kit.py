"""Copy the brand-kit block (fonts, tokens, grid, hand marks) from brand/index.html into every page.
Run from the repo root after editing the block between <!-- BRAND:START … --> and <!-- BRAND:END -->:
    python3 brand/sync-kit.py
"""
import io, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
def block(s):
    a = s.index("<!-- BRAND:START"); b = s.index("<!-- BRAND:END -->") + len("<!-- BRAND:END -->")
    return a, b
src = io.open(root / "brand/index.html", encoding="utf-8").read()
kit = src[slice(*block(src))]
for page in ["index.html", "clifton/index.html", "enneagram/index.html"]:
    p = root / page; s = io.open(p, encoding="utf-8").read(); a, b = block(s)
    if s[a:b] != kit:
        io.open(p, "w", encoding="utf-8").write(s[:a] + kit + s[b:]); print("updated", page)
    else:
        print("in sync", page)
