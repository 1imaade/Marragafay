import re
import glob

key_pages = [
    "en/index.html", "en/about.html", "en/activities.html", "en/packs.html", 
    "en/reviews.html", "en/contact.html", "en/cancellation.html", "en/terms.html", "en/privacy.html"
]

for p in key_pages:
    with open(p, "r", encoding="utf-8") as f:
        text = f.read()
    
    # Strip HTML tags
    clean_text = re.sub(r'<script.*?</script>', '', text, flags=re.DOTALL)
    clean_text = re.sub(r'<style.*?</style>', '', clean_text, flags=re.DOTALL)
    clean_text = re.sub(r'<[^>]+>', ' ', clean_text)
    clean_text = re.sub(r'\s+', ' ', clean_text)
    
    print(f"\n==========================================")
    print(f"PAGE: {p} (Length: {len(clean_text)} chars)")
    print(f"==========================================")
    print(clean_text[:1200])

