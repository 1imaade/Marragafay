import re
import glob

files = sorted(glob.glob("en/blog/*.html"))
articles = [f for f in files if not f.endswith("index.html")]

for fpath in articles:
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    # Find the content between the first <main> and </main>
    m = re.search(r'<main[^>]*>(.*?)</main>', html, flags=re.DOTALL)
    if m:
        main_content = m.group(1)
        # Remove any opening <article class="article-body-wrap"> and <div class="article-body">
        clean = re.sub(r'<article class="article-body-wrap">', '', main_content)
        clean = re.sub(r'<div class="article-body">', '', clean)
        # Remove any trailing </article> and </div> that were paired with those wrappers
        # Also remove the in-article CTA box so we can insert it cleanly
        clean = re.sub(r'<div class="article-cta-box">.*?</div>\s*</div>?', '', clean, flags=re.DOTALL)
        clean = re.sub(r'</article>', '', clean)
        clean = re.sub(r'</div>\s*$', '', clean.strip())
        clean = clean.strip()
        print(f"Cleaned {fpath}: {len(clean)} chars. Starts with: {clean[:60]}... Ends with: ...{clean[-60:]}")

