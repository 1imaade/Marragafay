import re

for p in ["en/index.html", "en/about.html", "en/activities.html"]:
    with open(p, "r", encoding="utf-8") as f:
        text = f.read()
    
    clean_text = re.sub(r'<script.*?</script>', '', text, flags=re.DOTALL)
    clean_text = re.sub(r'<style.*?</style>', '', clean_text, flags=re.DOTALL)
    clean_text = re.sub(r'<[^>]+>', ' ', clean_text)
    clean_text = re.sub(r'\s+', ' ', clean_text)
    
    print(f"\n==========================================")
    print(f"PAGE: {p}")
    print(f"==========================================")
    print(clean_text[:2500])

