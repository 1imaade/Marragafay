import os
import re

from generate_all_multilingual_articles import ui_translations, articles_meta
from build_multilingual_articles_engine import build_article_html
from redesign_in_article_cta import new_cta_css, cta_content

# We extract each of the 7 English articles' rich bodies from en/blog/
en_articles = {}
for filename in articles_meta.keys():
    filepath = f"en/blog/{filename}"
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract body content between <div class="article-body"> and </div>
    m = re.search(r'<div class="article-body">(.*?)</div>\s*</article>', content, flags=re.DOTALL)
    if m:
        en_articles[filename] = m.group(1).strip()
    else:
        print(f"Warning: Could not extract body from {filepath}")

print(f"Extracted {len(en_articles)} English article bodies.")

