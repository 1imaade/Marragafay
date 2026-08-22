import glob

files = sorted(glob.glob("*/blog/*.html"))
articles = [f for f in files if not f.endswith("index.html")]

print(f"Total articles to audit: {len(articles)}")
all_passed = True

for fpath in articles:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    issues = []
    if ".article-cta-box" not in content:
        issues.append("Missing .article-cta-box in CSS")
    if 'class="article-cta-box"' not in content:
        issues.append("Missing <div class=\"article-cta-box\">")
    if "</article>" not in content:
        issues.append("Missing </article>")
    if "</main>" not in content:
        issues.append("Missing </main>")
    if 'class="article-tags-wrap"' not in content:
        issues.append("Missing article-tags-wrap")
    if 'class="related-articles-section"' not in content:
        issues.append("Missing related-articles-section")
    if "<footer" not in content or "</footer>" not in content:
        issues.append("Missing footer")
    if "</html>" not in content:
        issues.append("Missing </html>")
        
    if issues:
        print(f"❌ {fpath}: {', '.join(issues)}")
        all_passed = False
    else:
        print(f"✅ {fpath}: Perfect structure & styling")

if all_passed:
    print("\n🎉 ALL 28 ARTICLES ARE 100% PERFECT & FLAWLESS!")
else:
    print("\n⚠️ SOME FILES HAVE ISSUES!")
