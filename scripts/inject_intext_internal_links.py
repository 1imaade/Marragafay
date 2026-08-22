import re
import glob

link_rules = {
    "en": [
        (r'\b(quad biking|quad adventure|quad tour)\b', r'<a href="/en/activities/quad-biking" style="color: #523225; font-weight: 600; text-decoration: underline;">\1</a>', 1),
        (r'\b(sunset camel ride|camel ride|camel trek)\b', r'<a href="/en/activities/camel-ride" style="color: #523225; font-weight: 600; text-decoration: underline;">\1</a>', 1),
        (r'\b(desert dinner|candlelit dinner|dinner show)\b', r'<a href="/en/activities/dinner-show" style="color: #523225; font-weight: 600; text-decoration: underline;">\1</a>', 1),
        (r'\b(dune buggy|buggy adventure)\b', r'<a href="/en/activities/buggy" style="color: #523225; font-weight: 600; text-decoration: underline;">\1</a>', 1),
        (r'\b(hot air balloon)\b', r'<a href="/en/activities/hot-air-balloon" style="color: #523225; font-weight: 600; text-decoration: underline;">\1</a>', 1),
        (r'\b(Signature package|Agafay Desert tour)\b', r'<a href="/en/packages/comfort" style="color: #523225; font-weight: 600; text-decoration: underline;">\1</a>', 1),
        (r'\b(private transfer|private VIP tour)\b', r'<a href="/en/packages/luxe" style="color: #523225; font-weight: 600; text-decoration: underline;">\1</a>', 1)
    ],
    "fr": [
        (r'\b(randonnée en quad|tour en quad|quad)\b', r'<a href="/fr/activities/quad-biking" style="color: #523225; font-weight: 600; text-decoration: underline;">\1</a>', 1),
        (r'\b(balade en dromadaire|dromadaire)\b', r'<a href="/fr/activities/camel-ride" style="color: #523225; font-weight: 600; text-decoration: underline;">\1</a>', 1),
        (r'\b(dîner spectacle|dîner dans le désert)\b', r'<a href="/fr/activities/dinner-show" style="color: #523225; font-weight: 600; text-decoration: underline;">\1</a>', 1),
        (r'\b(aventure en buggy|buggy)\b', r'<a href="/fr/activities/buggy" style="color: #523225; font-weight: 600; text-decoration: underline;">\1</a>', 1),
        (r'\b(vol en montgolfière|montgolfière)\b', r'<a href="/fr/activities/hot-air-balloon" style="color: #523225; font-weight: 600; text-decoration: underline;">\1</a>', 1),
        (r'\b(excursion dans le désert d\'Agafay|forfait Signature)\b', r'<a href="/fr/packages/comfort" style="color: #523225; font-weight: 600; text-decoration: underline;">\1</a>', 1),
        (r'\b(transfert privé|pack VIP)\b', r'<a href="/fr/packages/luxe" style="color: #523225; font-weight: 600; text-decoration: underline;">\1</a>', 1)
    ],
    "es": [
        (r'\b(tour en quad|paseo en quad|quad)\b', r'<a href="/es/activities/quad-biking" style="color: #523225; font-weight: 600; text-decoration: underline;">\1</a>', 1),
        (r'\b(paseo en camello|camello)\b', r'<a href="/es/activities/camel-ride" style="color: #523225; font-weight: 600; text-decoration: underline;">\1</a>', 1),
        (r'\b(cena espectáculo|cena en el desierto)\b', r'<a href="/es/activities/dinner-show" style="color: #523225; font-weight: 600; text-decoration: underline;">\1</a>', 1),
        (r'\b(aventura en buggy|buggy)\b', r'<a href="/es/activities/buggy" style="color: #523225; font-weight: 600; text-decoration: underline;">\1</a>', 1),
        (r'\b(vuelo en globo|globo aerostático)\b', r'<a href="/es/activities/hot-air-balloon" style="color: #523225; font-weight: 600; text-decoration: underline;">\1</a>', 1),
        (r'\b(excursión al desierto de Agafay|paquete Signature)\b', r'<a href="/es/packages/comfort" style="color: #523225; font-weight: 600; text-decoration: underline;">\1</a>', 1),
        (r'\b(traslado privado|tour privado VIP)\b', r'<a href="/es/packages/luxe" style="color: #523225; font-weight: 600; text-decoration: underline;">\1</a>', 1)
    ],
    "ar": [
        (r'\b(دراجات الكواد|جولة الكواد|الكواد)\b', r'<a href="/ar/activities/quad-biking" style="color: #523225; font-weight: 600; text-decoration: underline;">\1</a>', 1),
        (r'\b(ركوب الجمال|جولة الجمال|الجمال)\b', r'<a href="/ar/activities/camel-ride" style="color: #523225; font-weight: 600; text-decoration: underline;">\1</a>', 1),
        (r'\b(عشاء صحراوي|سهرة العشاء|عشاء مع عرض)\b', r'<a href="/ar/activities/dinner-show" style="color: #523225; font-weight: 600; text-decoration: underline;">\1</a>', 1),
        (r'\b(مركبات البوغي|جولة البوغي|البوغي)\b', r'<a href="/ar/activities/buggy" style="color: #523225; font-weight: 600; text-decoration: underline;">\1</a>', 1),
        (r'\b(المنطاد الهوائي|رحلة المنطاد)\b', r'<a href="/ar/activities/hot-air-balloon" style="color: #523225; font-weight: 600; text-decoration: underline;">\1</a>', 1),
        (r'\b(رحلة صحراء أكافاي|باقة سيغنتشر)\b', r'<a href="/ar/packages/comfort" style="color: #523225; font-weight: 600; text-decoration: underline;">\1</a>', 1),
        (r'\b(النقل الخاص|باقة VIP الخاصة)\b', r'<a href="/ar/packages/luxe" style="color: #523225; font-weight: 600; text-decoration: underline;">\1</a>', 1)
    ]
}

files = glob.glob("*/blog/*.html")
articles = [f for f in files if not f.endswith("index.html")]

for fpath in articles:
    lang = fpath.split("/")[0]
    rules = link_rules.get(lang, [])

    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    # Extract body content between <div class="article-body"> and <div class="article-cta-box">
    parts = html.split('<div class="article-cta-box">')
    if len(parts) == 2:
        top_part, cta_part = parts[0], parts[1]

        # Apply substitutions only inside top_part (to avoid modifying CTA or footer)
        for pattern, replacement, count in rules:
            # Check if this link target is already in top_part
            m_target = re.search(r'href="([^"]+)"', replacement)
            if m_target and m_target.group(1) in top_part:
                continue
            # Replace only the first occurrence outside of existing tags
            # Simple replacement on text
            top_part = re.sub(pattern, replacement, top_part, count=count, flags=re.IGNORECASE)

        new_html = top_part + '<div class="article-cta-box">' + cta_part
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_html)
        print(f"Injected in-text contextual links into {fpath}")

print("\nContextual in-text internal linking complete across all 28 articles!")
