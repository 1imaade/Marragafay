import re

languages = {
    "fr": {
        "path": "fr/blog/index.html",
        "h1": "Récits du<br>désert de pierre.",
        "sub": "Carnets de terrain, guides exclusifs et rencontres choisies au cœur d'Agafay.",
        "h1_title": "Le Grand Récit",
        "h1_sub": "Récit d'Honneur",
        "badge": "Choix de la Rédaction",
        "read_story": "Lire le Récit →",
        "read_article": "Lire l'Article →",
        "curator_title": "La Sélection du Conservateur",
        "curator_sub": "Rencontres & Traditions",
        "quote_eyebrow": "Philosophie du Désert",
        "quote_text": "« Le désert de pierre n'est pas vide — il est immense, silencieux et éternel. Quarante-cinq minutes de route qui ressemblent à une parenthèse hors du temps. »",
        "quote_author": "Carnets Marragafay · Marrakech",
        "dispatches_title": "Dépêches du Désert",
        "dispatches_sub": "Guides, Itinéraires & Gastronomie"
    },
    "es": {
        "path": "es/blog/index.html",
        "h1": "Relatos del<br>desierto de piedra.",
        "sub": "Notas de campo, guías exclusivas y encuentros selectos en Agafay.",
        "h1_title": "La Historia Principal",
        "h1_sub": "Nota Destacada",
        "badge": "Selección Editorial",
        "read_story": "Leer Historia →",
        "read_article": "Leer Artículo →",
        "curator_title": "Selección del Comisario",
        "curator_sub": "Encuentros y Tradiciones",
        "quote_eyebrow": "Filosofía de Agafay",
        "quote_text": "« El desierto de piedra no está vacío: es vasto, silencioso y antiguo. Un viaje de 45 minutos que se siente como una despedida del propio tiempo. »",
        "quote_author": "Notas de Campo Marragafay · Marrakech",
        "dispatches_title": "Crónicas del Desierto",
        "dispatches_sub": "Guías, Rutas y Gastronomía"
    },
    "ar": {
        "path": "ar/blog/index.html",
        "h1": "قصص وتجارب من<br>صحراء الحجارة.",
        "sub": "ملاحظات ميدانية، أدلة استكشافية وتجارب استثنائية من صحراء أكافاي.",
        "h1_title": "القصة الرئيسية",
        "h1_sub": "المقالة الافتتاحية",
        "badge": "اختيار المحرر",
        "read_story": "اقرأ القصة ←",
        "read_article": "اقرأ المقال الكامل ←",
        "curator_title": "مختارات المجلة",
        "curator_sub": "تراث وتقاليد عريقة",
        "quote_eyebrow": "فلسفة صحراء أكافاي",
        "quote_text": "«صحراء أكافاي ليست فراغاً، بل هدوء ساحر وتاريخ أصيل ممتد. مسافة 45 دقيقة تنقلك خارج حدود الزمن.»",
        "quote_author": "ملاحظات مراكافاي الميدانية · مراكش",
        "dispatches_title": "أوراق الصحراء",
        "dispatches_sub": "أدلة، مسارات وتجارب طهي فاخرة"
    }
}

# Read English file as template for CSS and structure
with open("en/blog/index.html", "r", encoding="utf-8") as f:
    en_content = f.read()

# Extract CSS from en/blog/index.html
css_match = re.search(r'/\* ═══════════════════════════════════════════════\s*LUXURY EDITORIAL MAGAZINE SECTIONS.*?(?=/\* Newsletter Section)', en_content, re.DOTALL)
if not css_match:
    print("Could not extract CSS from EN file.")
    exit(1)

editorial_css = css_match.group(0)

# Synchronize across fr, es, ar
for lang, d in languages.items():
    filepath = d["path"]
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Update CSS
    content = re.sub(r'/\*\s*Sections\s*\*/.*?/\*\s*Newsletter Section', editorial_css + "\n\n    /* Newsletter Section", content, flags=re.DOTALL)
    content = re.sub(r'/\* ═══════════════════════════════════════════════\s*LUXURY EDITORIAL MAGAZINE SECTIONS.*?(?=/\* Newsletter Section)', editorial_css + "\n\n    ", content, flags=re.DOTALL)

    # Replace middle HTML
    middle_html = f"""    <!-- 1. COVER STORY -->
    <section class="journal-section-wrap" style="padding-bottom: 30px;">
      <div class="journal-section">
        <div class="editorial-header">
          <div class="editorial-header__left">
            <span class="editorial-header__num">01 /</span>
            <h2 class="editorial-header__title">{d['h1_title']}</h2>
          </div>
          <span class="editorial-header__sub">{d['h1_sub']}</span>
        </div>

        <a href="agafay-desert-guide.html" class="cover-story" data-category="desert-guide">
          <div class="cover-story__media">
            <img src="/images/Slider-images/slider-1.webp" alt="Agafay Desert" loading="eager" fetchpriority="high" decoding="async" />
            <span class="cover-story__badge">{d['badge']}</span>
          </div>
          <div class="cover-story__body">
            <div class="cover-story__tag-row">
              <span class="cover-story__tag">Desert Guide</span>
              <span class="cover-story__read-time">8 min</span>
            </div>
            <h3 class="cover-story__title">The Complete Guide to Agafay Desert — Morocco’s Stone Desert Explained</h3>
            <p class="cover-story__standfirst">What makes Agafay different from the Sahara, and why travelers are increasingly choosing this 45-minute drive from Marrakech over a 10-hour journey south.</p>
            <div class="cover-story__footer">
              <span class="cover-story__author">Marragafay Editorial</span>
              <span class="cover-story__cta">{d['read_article']}</span>
            </div>
          </div>
        </a>
      </div>
    </section>

    <!-- 2. ASYMMETRIC STORY DUO -->
    <section class="journal-section-wrap" style="padding-top: 30px; padding-bottom: 30px;">
      <div class="journal-section">
        <div class="editorial-header">
          <div class="editorial-header__left">
            <span class="editorial-header__num">02 /</span>
            <h2 class="editorial-header__title">{d['curator_title']}</h2>
          </div>
          <span class="editorial-header__sub">{d['curator_sub']}</span>
        </div>

        <div class="story-duo">
          <a href="agafay-camel-ride.html" class="story-card-tall" data-category="experience">
            <div class="story-card-tall__media">
              <img src="/images/Slider-images/slider-3.webp" alt="Sunset Camel Ride in Agafay" loading="lazy" decoding="async" />
            </div>
            <div class="story-card-tall__body">
              <span class="story-card-tall__tag">Experience</span>
              <h3 class="story-card-tall__title">Sunset Camel Ride in Agafay: What to Expect</h3>
              <p class="story-card-tall__excerpt">The silence before sunset in the desert is not empty — it is full. Our field guide on authentic dromedary crossings.</p>
              <div class="story-card-tall__footer">
                <span>5 min</span>
                <span style="font-weight: 700; color: #523225;">{d['read_story']}</span>
              </div>
            </div>
          </a>

          <a href="berber-culture-agafay.html" class="story-card-stacked" data-category="culture">
            <div class="story-card-stacked__media">
              <img src="/images/Slider-images/slider-4.webp" alt="Berber heritage in Agafay" loading="lazy" decoding="async" />
            </div>
            <div class="story-card-stacked__body">
              <span class="story-card-stacked__tag">Culture & Heritage</span>
              <h3 class="story-card-stacked__title">Berber Heritage and the Agafay: A Culture That Predates Tourism</h3>
              <p class="story-card-stacked__excerpt">Long before desert camps arrived, the stone hills sustained Berber communities whose dry-stone traditions survive intact.</p>
              <div class="story-card-stacked__footer">
                <span>6 min</span>
                <span style="font-weight: 700; color: #523225;">{d['read_story']}</span>
              </div>
            </div>
          </a>
        </div>
      </div>
    </section>

    <!-- 3. EDITORIAL INTERLUDE -->
    <section class="journal-section-wrap" style="padding-top: 20px; padding-bottom: 20px;">
      <div class="journal-section">
        <div class="quote-interlude">
          <div class="quote-interlude__inner">
            <span class="quote-interlude__eyebrow">{d['quote_eyebrow']}</span>
            <p class="quote-interlude__text">{d['quote_text']}</p>
            <span class="quote-interlude__author">{d['quote_author']}</span>
          </div>
        </div>
      </div>
    </section>

    <!-- 4. FIELD DISPATCHES -->
    <section class="journal-section-wrap" style="padding-top: 30px;">
      <div class="journal-section">
        <div class="editorial-header">
          <div class="editorial-header__left">
            <span class="editorial-header__num">03 /</span>
            <h2 class="editorial-header__title">{d['dispatches_title']}</h2>
          </div>
          <span class="editorial-header__sub">{d['dispatches_sub']}</span>
        </div>

        <div class="field-grid" id="article-grid">
          <a href="marrakech-to-agafay.html" class="field-card" data-category="travel-tips">
            <div class="field-card__media">
              <img src="/images/gallery/gal1.webp" alt="Marrakech to Agafay" loading="lazy" decoding="async" />
            </div>
            <div class="field-card__body">
              <div class="field-card__tag-row">
                <span class="field-card__tag">Travel Tips</span>
                <span class="field-card__num">01</span>
              </div>
              <h3 class="field-card__title">Marrakech to Agafay Desert: Every Way to Get There</h3>
              <p class="field-card__excerpt">From private transfers to scenic backcountry roads, the 45-kilometer journey separates the medina from stillness.</p>
              <div class="field-card__footer">
                <span>4 min</span>
                <span class="field-card__arrow">→</span>
              </div>
            </div>
          </a>

          <a href="agafay-dinner-experience.html" class="field-card" data-category="experience">
            <div class="field-card__media">
              <img src="/images/activites/show.webp" alt="Agafay dinner" loading="lazy" decoding="async" />
            </div>
            <div class="field-card__body">
              <div class="field-card__tag-row">
                <span class="field-card__tag">Night Experiences</span>
                <span class="field-card__num">02</span>
              </div>
              <h3 class="field-card__title">The Agafay Dinner Experience: Luxury Under a Moroccan Sky</h3>
              <p class="field-card__excerpt">How a candlelit desert dinner became Marragafay’s most coveted evening ritual.</p>
              <div class="field-card__footer">
                <span>7 min</span>
                <span class="field-card__arrow">→</span>
              </div>
            </div>
          </a>

          <a href="agafay-quad-biking-guide.html" class="field-card" data-category="experience">
            <div class="field-card__media">
              <img src="/images/activites/quad.webp" alt="Quad biking in Agafay" loading="lazy" decoding="async" />
            </div>
            <div class="field-card__body">
              <div class="field-card__tag-row">
                <span class="field-card__tag">Adventure</span>
                <span class="field-card__num">03</span>
              </div>
              <h3 class="field-card__title">Quad Biking in Agafay Desert: Safety, Tips & What You'll See</h3>
              <p class="field-card__excerpt">Piloting 4x4 machines across Morocco’s most exhilarating stone canyons.</p>
              <div class="field-card__footer">
                <span>6 min</span>
                <span class="field-card__arrow">→</span>
              </div>
            </div>
          </a>
        </div>
      </div>
    </section>"""

    content = re.sub(r'<!-- FEATURED ARTICLE -->.*?<!-- NEWSLETTER -->', middle_html + "\n\n    <!-- NEWSLETTER -->", content, flags=re.DOTALL)
    content = re.sub(r'<!-- 1\. COVER STORY -->.*?<!-- NEWSLETTER -->', middle_html + "\n\n    <!-- NEWSLETTER -->", content, flags=re.DOTALL)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Synchronized editorial magazine layout in: {filepath}")

print("All language pages synchronized successfully!")
