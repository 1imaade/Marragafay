import re
from rebuild_all_multilingual_articles_master import articles_meta

for filename in articles_meta.keys():
    en_path = f"en/blog/{filename}"
    with open(en_path, "r", encoding="utf-8") as f:
        html = f.read()

    m = re.search(r'<article class="article-body">(.*?)(</article>|</main>|<div class="related-grid">|<section class="related|<footer)', html, flags=re.DOTALL)
    if m:
        raw = m.group(1).strip()
        # Clean out any old CTA blocks or related grids if they got included
        raw = re.sub(r'<div class="(article-experience-inset|article-cta-box)">.*?</div>\s*</div>', '<!-- CTA_PLACEHOLDER -->', raw, flags=re.DOTALL)
        raw = re.sub(r'<div class="related-grid">.*', '', raw, flags=re.DOTALL)
        raw = re.sub(r'<div class="article-tags-wrap">.*', '', raw, flags=re.DOTALL)
        raw = re.sub(r'<section class="related-articles-section".*', '', raw, flags=re.DOTALL)
        print(f"SUCCESS {filename}: {len(raw)} chars, has_cta_placeholder: {'<!-- CTA_PLACEHOLDER -->' in raw}")
    else:
        print(f"FAILED {filename}")

