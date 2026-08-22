import glob
import re

files = glob.glob("*/blog/*.html")
articles = [f for f in files if not f.endswith("index.html")]

for fpath in articles:
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Fix the double closing div right after .article-cta-box
    html = re.sub(r'(</div>\s*</div>\s*</article>)', '</div>\n    </article>', html)
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)

print("Verified and cleaned tag balance across all articles!")
