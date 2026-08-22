import re

languages = {
    "en": {
        "path": "en/blog/index.html",
        "eyebrow": "Agafay Field Philosophy",
        "quote": "“The stone desert is not empty — it is vast, silent, and ancient. A forty-five minute drive that feels like a quiet departure from time itself.”",
        "author": "Marragafay Field Notes · Marrakech",
        "title": "Field Dispatches",
        "sub": "Guides, Routes & Gastronomy"
    },
    "fr": {
        "path": "fr/blog/index.html",
        "eyebrow": "Philosophie du Désert",
        "quote": "« Le désert de pierre n'est pas vide — il est immense, silencieux et éternel. Quarante-cinq minutes de route qui ressemblent à une parenthèse hors du temps. »",
        "author": "Carnets Marragafay · Marrakech",
        "title": "Dépêches du Désert",
        "sub": "Guides, Itinéraires & Gastronomie"
    },
    "es": {
        "path": "es/blog/index.html",
        "eyebrow": "Filosofía de Agafay",
        "quote": "« El desierto de piedra no está vacío: es vasto, silencioso y antiguo. Un viaje de 45 minutos que se siente como una despedida del propio tiempo. »",
        "author": "Notas de Campo Marragafay · Marrakech",
        "title": "Crónicas del Desierto",
        "sub": "Guías, Rutas y Gastronomía"
    },
    "ar": {
        "path": "ar/blog/index.html",
        "eyebrow": "فلسفة صحراء أكافاي",
        "quote": "«صحراء أكافاي ليست فراغاً، بل هدوء ساحر وتاريخ أصيل ممتد. مسافة 45 دقيقة تنقلك خارج حدود الزمن.»",
        "author": "ملاحظات مراكافاي الميدانية · مراكش",
        "title": "أوراق الصحراء",
        "sub": "أدلة، مسارات وتجارب طهي فاخرة"
    }
}

for lang, d in languages.items():
    filepath = d["path"]
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Enforce inline styles on section bands
    content = content.replace(
        '<section class="band-sandstone">',
        '<section class="band-sandstone" style="background-color: #E8E2D5 !important; width: 100%;">'
    )
    content = content.replace(
        '<section class="band-mineral">',
        '<section class="band-mineral" style="background-color: #DDD5C3 !important; width: 100%;">'
    )
    content = content.replace(
        '<section class="band-dark-luxury">',
        '<section class="band-dark-luxury" style="background-color: #1E1E1C !important; color: #F6F7EA !important; width: 100%;">'
    )

    # 2. Build high-contrast philosophy quote block
    quote_markup = f"""        <!-- Embedded Philosophy Quote -->
        <div class="quote-interlude-dark" style="background-color: #272724 !important; border: 1px solid rgba(246, 247, 234, 0.15) !important; color: #F6F7EA !important; border-radius: 8px; padding: 60px 48px; margin-bottom: 64px; box-shadow: 0 16px 40px rgba(0, 0, 0, 0.3);">
          <div class="quote-interlude-dark__inner" style="max-width: 860px; margin: 0 auto; text-align: center;">
            <span class="quote-interlude-dark__eyebrow" style="color: #d4af37 !important; font-size: 11px; font-weight: 700; letter-spacing: 0.3em; text-transform: uppercase; margin-bottom: 20px; display: block;">{d['eyebrow']}</span>
            <p class="quote-interlude-dark__text" style="color: #F6F7EA !important; font-size: clamp(1.4rem, 2.6vw, 2.1rem); font-weight: 600; line-height: 1.4; font-style: italic; margin: 0 0 24px;">{d['quote']} </p>
            <span class="quote-interlude-dark__author" style="color: rgba(246, 247, 234, 0.7) !important; font-size: 12px; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase; display: flex; align-items: center; justify-content: center; gap: 12px;">{d['author']}</span>
          </div>
        </div>

        <div class="editorial-header editorial-header--dark" style="border-bottom: 1.5px solid rgba(246, 247, 234, 0.15) !important;">
          <div class="editorial-header__left">
            <span class="editorial-header__num" style="color: #d4af37 !important;">03 /</span>
            <h2 class="editorial-header__title" style="color: #F6F7EA !important;">{d['title']}</h2>
          </div>
          <span class="editorial-header__sub" style="color: rgba(246, 247, 234, 0.6) !important;">{d['sub']}</span>
        </div>"""

    # Replace existing quote + header
    pattern = re.compile(r'<!-- Embedded Philosophy Quote -->.*?<div class="editorial-header editorial-header--dark">.*?</div>\s*</div>', re.DOTALL)
    if pattern.search(content):
        content = pattern.sub(quote_markup, content)
    else:
        # Fallback replacement
        content = re.sub(
            r'<div class="quote-interlude-dark">.*?<div class="editorial-header editorial-header--dark">.*?</div>\s*</div>',
            quote_markup,
            content,
            flags=re.DOTALL
        )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Fixed philosophy & dark band in: {filepath}")

print("All language index files updated!")
