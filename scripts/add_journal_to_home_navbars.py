import re

lang_nav_items = {
    "en": ('<li class="nav-item"><a href="reviews" class="nav-link">Reviews</a></li>', '<li class="nav-item"><a href="reviews" class="nav-link">Reviews</a></li>\n          <li class="nav-item"><a href="blog" class="nav-link">Journal</a></li>'),
    "fr": ('<li class="nav-item"><a href="reviews" class="nav-link">Avis</a></li>', '<li class="nav-item"><a href="reviews" class="nav-link">Avis</a></li>\n          <li class="nav-item"><a href="blog" class="nav-link">La Revue</a></li>'),
    "es": ('<li class="nav-item"><a href="reviews" class="nav-link">Reseñas</a></li>', '<li class="nav-item"><a href="reviews" class="nav-link">Reseñas</a></li>\n          <li class="nav-item"><a href="blog" class="nav-link">El Diario</a></li>'),
    "ar": ('<li class="nav-item"><a href="reviews" class="nav-link">التقييمات</a></li>', '<li class="nav-item"><a href="reviews" class="nav-link">التقييمات</a></li>\n          <li class="nav-item"><a href="blog" class="nav-link">المجلة</a></li>')
}

for lang, (target, replacement) in lang_nav_items.items():
    filepath = f"{lang}/index.html"
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        if 'href="blog"' not in content:
            content = content.replace(target, replacement)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Added Journal link to navbar in {filepath}")
        else:
            print(f"Journal link already in {filepath}")
    except Exception as e:
        print(f"Error updating {filepath}: {e}")

