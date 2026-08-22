import re
import glob

print("==========================================================")
print("1. AUDITING MONEY PAGES ON-PAGE SEO (TITLES, H1s, METAS)")
print("==========================================================")

money_pages = [
    "packages/comfort.html",
    "packages/luxe.html",
    "packages/basic.html",
    "packs.html",
    "activities/quad-biking.html",
    "activities/camel-ride.html",
    "activities/dinner-show.html",
    "activities/buggy.html",
    "activities/hot-air-balloon.html",
    "activities/paragliding.html",
    "activities.html"
]

all_passed = True

for page in money_pages:
    for lang in ["en", "fr", "es", "ar"]:
        fpath = f"{lang}/{page}"
        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()

        m_title = re.search(r'<title>(.*?)</title>', html)
        m_h1 = re.search(r'<h1[^>]*>(.*?)</h1>', html, flags=re.DOTALL)
        m_desc = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', html)

        title = m_title.group(1) if m_title else "MISSING"
        h1 = re.sub(r'<[^>]+>', '', m_h1.group(1)).strip() if m_h1 else "MISSING"
        desc = m_desc.group(1) if m_desc else "MISSING"

        if "MISSING" in [title, h1, desc]:
            print(f"❌ ERROR in {fpath}: Title={title} | H1={h1} | Desc={desc}")
            all_passed = False
        else:
            print(f"✅ {fpath}:")
            print(f"   Title: {title[:70]}...")
            print(f"   H1:    {h1}")

print("\n==========================================================")
print("2. AUDITING BLOG INTERNAL LINKING (CONVERSION BRIDGE)")
print("==========================================================")

articles = [f for f in glob.glob("*/blog/*.html") if not f.endswith("index.html")]

for art in sorted(articles):
    with open(art, "r", encoding="utf-8") as f:
        html = f.read()

    links_to_commercial = re.findall(r'href="(/[^"]+/(?:packages|activities|packs)[^"]*)"', html)
    unique_links = list(set(links_to_commercial))
    if len(unique_links) >= 1:
        print(f"✅ {art}: {len(unique_links)} commercial Money Page link(s) found -> {unique_links}")
    else:
        print(f"❌ {art}: NO commercial links found!")
        all_passed = False

if all_passed:
    print("\n🎉 ALL CHECKS PASSED PERFECTLY! The commercial SEO architecture is 100% active.")
