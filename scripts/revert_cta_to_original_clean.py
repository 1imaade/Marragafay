import re
import glob

# 1. Localized strings for the original CTA box
cta_translations = {
    "en": {
        "title": "Experience Agafay with Marragafay",
        "desc": "Private desert dinners, quad adventures, and sunset camel rides — curated for those who seek extraordinary experiences.",
        "btn": "Explore Experiences →",
        "url": "/en/activities"
    },
    "fr": {
        "title": "Vivez l'Expérience Agafay avec Marragafay",
        "desc": "Dîners privés dans le désert, aventures en quad et balades à dos de chameau au coucher du soleil — créés pour ceux qui recherchent des moments extraordinaires.",
        "btn": "Explorer les Expériences →",
        "url": "/fr/activities"
    },
    "es": {
        "title": "Vive la Experiencia Agafay con Marragafay",
        "desc": "Cenas privadas en el desierto, aventuras en quad y paseos en camello al atardecer, diseñados para quienes buscan experiencias extraordinarias.",
        "btn": "Explorar Experiencias →",
        "url": "/es/activities"
    },
    "ar": {
        "title": "عش تجربة أكافاي الفاخرة مع مراكافاي",
        "desc": "عشاء صحراوي خاص، مغامرات بالدراجات الرباعية، وجولات على الجمال وقت الغروب — مصممة خصيصاً للباحثين عن التميز.",
        "btn": "← استكشف التجارب",
        "url": "/ar/activities"
    }
}

# 2. Clean CTA CSS
original_cta_css = """
    /* In-Article Booking CTA */
    .article-cta-box {
      background-color: #272724 !important;
      color: #F6F7EA !important;
      padding: 44px 32px;
      border-radius: 8px;
      margin: 3.5rem 0;
      text-align: center;
      box-sizing: border-box;
    }
    .article-cta-box h3 {
      color: #F6F7EA !important;
      font-size: clamp(1.4rem, 2.5vw, 1.85rem) !important;
      font-weight: 700 !important;
      margin-top: 0 !important;
      margin-bottom: 12px !important;
      line-height: 1.25 !important;
    }
    .article-cta-box p {
      color: rgba(246, 247, 234, 0.8) !important;
      font-size: 16px !important;
      line-height: 1.65 !important;
      max-width: 540px !important;
      margin: 0 auto 24px !important;
    }
    .article-cta-btn {
      display: inline-flex !important;
      align-items: center !important;
      justify-content: center !important;
      gap: 8px !important;
      background-color: #523225 !important;
      color: #F6F7EA !important;
      padding: 13px 30px !important;
      border-radius: 100px !important;
      font-weight: 700 !important;
      text-decoration: none !important;
      font-size: 13px !important;
      letter-spacing: 0.08em !important;
      text-transform: uppercase !important;
      transition: all 0.25s ease !important;
    }
    .article-cta-btn:hover {
      background-color: #3d241a !important;
      color: #F6F7EA !important;
      transform: translateY(-1px) !important;
    }
    @media (max-width: 768px) {
      .article-cta-box { padding: 32px 20px; margin: 2.5rem 0; }
      .article-cta-btn { width: 100%; box-sizing: border-box; }
    }
"""

files = glob.glob("*/blog/*.html")
articles = [f for f in files if not f.endswith("index.html")]

for fpath in articles:
    lang = fpath.split("/")[0]
    cta_data = cta_translations.get(lang, cta_translations["en"])
    
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    new_cta_html = f"""<div class="article-cta-box">
        <h3>{cta_data['title']}</h3>
        <p>{cta_data['desc']}</p>
        <a href="{cta_data['url']}" class="article-cta-btn">{cta_data['btn']}</a>
      </div>"""

    # Replace any existing .article-experience-inset or .article-cta-box with the original clean CTA
    html = re.sub(r'<div class="(article-experience-inset|article-cta-box)">.*?</div>\s*</div>', new_cta_html, html, flags=re.DOTALL)
    
    # Also replace in CSS if .article-experience-inset styling exists
    if ".article-experience-inset" in html:
        # Replace the entire IN-ARTICLE EXPERIENCE inset CSS block
        html = re.sub(r'/\* ═══+\s*IN-ARTICLE EXPERIENCE BOOKING INSET.*?article-tags-wrap', original_cta_css + "\n    .article-tags-wrap", html, flags=re.DOTALL)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Reverted CTA in {fpath}")

print("Done reverting CTA across all 28 articles!")
