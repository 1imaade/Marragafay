import re

languages = {
    "en": {
        "path": "en/blog/index.html",
        "h1_title": "The Lead Story", "h1_sub": "Flagship Field Note",
        "badge": "Editor’s Pick", "read_story": "Read Story →", "read_article": "Read Full Story →",
        "curator_title": "Curator’s Selection", "curator_sub": "Encounters & Traditions",
        "quote_eyebrow": "Agafay Field Philosophy",
        "quote": "“The stone desert is not empty — it is vast, silent, and ancient. A forty-five minute drive that feels like a quiet departure from time itself.”",
        "author": "Marragafay Field Notes · Marrakech",
        "title": "Field Dispatches", "sub": "Guides, Routes & Gastronomy",
        "c1_tag": "Travel Logistics", "c1_title": "Marrakech to Agafay Desert: Every Way to Get There", "c1_excerpt": "From private transfers to scenic backcountry roads, the 45-kilometer journey separates the bustling medina from absolute stillness. Full cost and timing breakdown.", "c1_meta": "July 2026 · 4 min read",
        "c2_tag": "Night Experiences", "c2_title": "The Agafay Dinner Experience: Luxury Under a Moroccan Sky", "c2_excerpt": "How a candlelit desert dinner became Marragafay’s most coveted evening ritual — and the subtle gastronomic details that make it unforgettable.", "c2_meta": "June 2026 · 7 min read",
        "c3_tag": "Adventure Trails", "c3_title": "Quad Biking in Agafay Desert: Safety, Tips & What You'll See", "c3_excerpt": "Everything you need to know about navigating high-performance 4x4 machines across Morocco’s most exhilarating stone canyons and panoramic ridges.", "c3_meta": "August 2026 · 6 min read",
        "read": "Read →", "no_results": "No articles found in this category. More stories coming soon."
    },
    "fr": {
        "path": "fr/blog/index.html",
        "h1_title": "Le Grand Récit", "h1_sub": "Récit d'Honneur",
        "badge": "Choix de la Rédaction", "read_story": "Lire le Récit →", "read_article": "Lire l'Article →",
        "curator_title": "La Sélection du Conservateur", "curator_sub": "Rencontres & Traditions",
        "quote_eyebrow": "Philosophie du Désert",
        "quote": "« Le désert de pierre n'est pas vide — il est immense, silencieux et éternel. Quarante-cinq minutes de route qui ressemblent à une parenthèse hors du temps. »",
        "author": "Carnets Marragafay · Marrakech",
        "title": "Dépêches du Désert", "sub": "Guides, Itinéraires & Gastronomie",
        "c1_tag": "Conseils Voyage", "c1_title": "De Marrakech au Désert d'Agafay : Tous les Moyens d'Accès", "c1_excerpt": "Du transfert privé aux pistes panoramiques, les 45 kilomètres séparent l'effervescence de la médina du silence absolu.", "c1_meta": "Juillet 2026 · 4 min",
        "c2_tag": "Expériences Nocturnes", "c2_title": "L'Expérience Dîner à Agafay : Le Luxe sous le Ciel Marocain", "c2_excerpt": "Comment un dîner aux chandelles dans le désert est devenu le rituel le plus prisé de Marragafay.", "c2_meta": "Juin 2026 · 7 min",
        "c3_tag": "Aventure & Pistes", "c3_title": "Quad dans le Désert d'Agafay : Sécurité, Conseils et Parcours", "c3_excerpt": "Tout ce que vous devez savoir pour piloter des quads 4x4 à travers les canyons minéraux du désert.", "c3_meta": "Août 2026 · 6 min",
        "read": "Lire →", "no_results": "Aucun article trouvé dans cette catégorie."
    },
    "es": {
        "path": "es/blog/index.html",
        "h1_title": "La Historia Principal", "h1_sub": "Nota Destacada",
        "badge": "Selección Editorial", "read_story": "Leer Historia →", "read_article": "Leer Artículo →",
        "curator_title": "Selección del Comisario", "curator_sub": "Encuentros y Tradiciones",
        "quote_eyebrow": "Filosofía de Agafay",
        "quote": "« El desierto de piedra no está vacío: es vasto, silencioso y antiguo. Un viaje de 45 minutos que se siente como una despedida del propio tiempo. »",
        "author": "Notas de Campo Marragafay · Marrakech",
        "title": "Crónicas del Desierto", "sub": "Guías, Rutas y Gastronomía",
        "c1_tag": "Logística de Viaje", "c1_title": "De Marrakech al Desierto de Agafay: Todas las Formas de Llegar", "c1_excerpt": "Desde traslados privados hasta caminos panorámicos, el trayecto de 45 km separa la medina del silencio total.", "c1_meta": "Julio 2026 · 4 min",
        "c2_tag": "Experiencias Nocturnes", "c2_title": "Cena en Agafay: Lujo bajo el Cielo Marroquí", "c2_excerpt": "Cómo una cena privada en el desierto se convirtió en la experiencia más codiciada de Marragafay.", "c2_meta": "Junio 2026 · 7 min",
        "c3_tag": "Rutas de Aventura", "c3_title": "Rutas en Quad por el Desierto de Agafay: Consejos y Seguridad", "c3_excerpt": "Todo lo que necesitas saber para pilotar potentes quads 4x4 por los cañones de piedra de Marruecos.", "c3_meta": "Agosto 2026 · 6 min",
        "read": "Leer →", "no_results": "No se encontraron artículos en esta categoría."
    },
    "ar": {
        "path": "ar/blog/index.html",
        "h1_title": "القصة الرئيسية", "h1_sub": "المقالة الافتتاحية",
        "badge": "اختيار المحرر", "read_story": "اقرأ القصة ←", "read_article": "اقرأ المقال الكامل ←",
        "curator_title": "مختارات المجلة", "curator_sub": "تراث وتقاليد عريقة",
        "quote_eyebrow": "فلسفة صحراء أكافاي",
        "quote": "«صحراء أكافاي ليست فراغاً، بل هدوء ساحر وتاريخ أصيل ممتد. مسافة 45 دقيقة تنقلك خارج حدود الزمن.»",
        "author": "ملاحظات مراكافاي الميدانية · مراكش",
        "title": "أوراق الصحراء", "sub": "أدلة، مسارات وتجارب طهي فاخرة",
        "c1_tag": "نصائح السفر", "c1_title": "من مراكش إلى صحراء أكافاي: كافة خيارات التنقل والوصول", "c1_excerpt": "من النقل الخاص إلى المسارات الصحراوية، 45 كيلومتراً تفصل بين صخب المدينة العتيقة والهدوء التام.", "c1_meta": "يوليو 2026 · 4 دقائق",
        "c2_tag": "تجارب مسائية", "c2_title": "تجربة العشاء في أكافاي: فخامة استثنائية تحت سماء المغرب", "c2_excerpt": "كيف أصبح العشاء على ضوء الشموع في الصحراء التجربة المسائية الأكثر طلباً في مراكافاي.", "c2_meta": "يونيو 2026 · 7 دقائق",
        "c3_tag": "مغامرات الدراجات", "c3_title": "قيادة الكواد في صحراء أكافاي: إرشادات السلامة والمسارات", "c3_excerpt": "كل ما تحتاج معرفته عن قيادة دراجات الدفع الرباعي 4x4 عبر المسارات الصخرية المذهلة.", "c3_meta": "أغسطس 2026 · 6 دقائق",
        "read": "← اقرأ", "no_results": "لم يتم العثور على مقالات في هذا القسم حالياً."
    }
}

new_css = """    /* ═══════════════════════════════════════════════
       ULTRA-CLEAN EDITORIAL LAYOUT (FRAMELESS)
    ═══════════════════════════════════════════════ */
    .journal-section { max-width: 1440px; margin: 0 auto; padding: 0 32px; box-sizing: border-box; }

    .editorial-band {
      background-color: #F6F7EA !important;
      padding: 60px 0;
      width: 100%;
      box-sizing: border-box;
    }

    /* Editorial Section Header */
    .editorial-header {
      display: flex;
      align-items: flex-end;
      justify-content: space-between;
      margin-bottom: 40px;
      padding-bottom: 20px;
      border-bottom: 1px solid rgba(39, 39, 36, 0.15);
    }
    .editorial-header__left { display: flex; align-items: baseline; gap: 16px; }
    .editorial-header__num { font-size: 13px; font-weight: 700; color: #523225; letter-spacing: 0.15em; }
    .editorial-header__title { font-size: 1.4rem; font-weight: 700; color: #272724; letter-spacing: -0.015em; margin: 0; text-transform: uppercase; }
    .editorial-header__sub { font-size: 12px; font-weight: 500; color: #7a756e; letter-spacing: 0.05em; text-transform: uppercase; }

    /* ─── FRAMELESS COVER STORY ─── */
    .cover-story {
      display: grid;
      grid-template-columns: 1.4fr 1fr;
      gap: 60px;
      align-items: center;
      text-decoration: none;
      color: inherit;
    }
    .cover-story:hover { text-decoration: none; color: inherit; }
    .cover-story__media { position: relative; overflow: hidden; aspect-ratio: 16/10; }
    .cover-story__media img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.8s ease; }
    .cover-story:hover .cover-story__media img { transform: scale(1.03); }
    .cover-story__badge { position: absolute; top: 24px; left: 24px; background: #272724; color: #F6F7EA; font-size: 10px; font-weight: 700; letter-spacing: 0.25em; text-transform: uppercase; padding: 7px 18px; border-radius: 100px; }
    .cover-story__body { display: flex; flex-direction: column; justify-content: center; }
    .cover-story__tag-row { display: flex; align-items: center; gap: 12px; margin-bottom: 24px; }
    .cover-story__tag { font-size: 11px; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase; color: #523225; }
    .cover-story__read-time { font-size: 12px; font-weight: 500; color: #7a756e; }
    .cover-story__title { font-size: clamp(2.4rem, 3.8vw, 3.4rem); font-weight: 700; line-height: 1.05; letter-spacing: -0.025em; color: #272724; margin: 0 0 24px; }
    .cover-story__standfirst { font-size: 1.15rem; line-height: 1.6; color: #4e4e48; margin: 0 0 40px; }
    .cover-story__footer { display: flex; align-items: center; justify-content: space-between; padding-top: 24px; border-top: 1px solid rgba(39, 39, 36, 0.1); }
    .cover-story__author { font-size: 11.5px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: #272724; }
    .cover-story__cta { display: inline-flex; align-items: center; gap: 10px; font-size: 13px; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: #523225; transition: gap 0.25s ease; }
    .cover-story:hover .cover-story__cta { gap: 16px; }

    /* ─── FRAMELESS DUO ─── */
    .story-duo { display: grid; grid-template-columns: 1.3fr 1fr; gap: 48px; }
    .story-card-tall, .story-card-stacked { display: flex; flex-direction: column; text-decoration: none; color: inherit; }
    .story-card-tall:hover, .story-card-stacked:hover { text-decoration: none; color: inherit; }
    .story-card-tall__media { aspect-ratio: 4/5; overflow: hidden; margin-bottom: 24px; }
    .story-card-stacked__media { aspect-ratio: 16/10; overflow: hidden; margin-bottom: 24px; }
    .story-card-tall__media img, .story-card-stacked__media img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.6s ease; }
    .story-card-tall:hover .story-card-tall__media img, .story-card-stacked:hover .story-card-stacked__media img { transform: scale(1.03); }
    .story-card-tall__tag, .story-card-stacked__tag { font-size: 11px; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: #523225; margin-bottom: 12px; display: block; }
    .story-card-tall__title { font-size: 2rem; font-weight: 700; line-height: 1.1; letter-spacing: -0.02em; color: #272724; margin: 0 0 16px; }
    .story-card-stacked__title { font-size: 1.6rem; font-weight: 700; line-height: 1.15; letter-spacing: -0.015em; color: #272724; margin: 0 0 14px; }
    .story-card-tall__excerpt, .story-card-stacked__excerpt { font-size: 1.05rem; line-height: 1.6; color: #5a5a54; margin: 0 0 24px; }
    .story-card-tall__footer, .story-card-stacked__footer { display: flex; align-items: center; justify-content: space-between; margin-top: auto; padding-top: 18px; border-top: 1px solid rgba(39, 39, 36, 0.1); font-size: 12px; color: #7a756e; }

    /* ─── FRAMELESS QUOTE ─── */
    .quote-interlude { padding: 80px 0; text-align: center; max-width: 900px; margin: 0 auto; position: relative; }
    .quote-interlude::before, .quote-interlude::after { content: ''; display: block; width: 60px; height: 1.5px; background: #523225; margin: 0 auto; }
    .quote-interlude::before { margin-bottom: 40px; }
    .quote-interlude::after { margin-top: 40px; }
    .quote-interlude__eyebrow { font-size: 11px; font-weight: 700; letter-spacing: 0.3em; text-transform: uppercase; color: #523225; margin-bottom: 24px; display: block; }
    .quote-interlude__text { font-size: clamp(1.8rem, 3vw, 2.6rem); font-weight: 600; line-height: 1.3; letter-spacing: -0.02em; color: #272724; margin: 0 0 32px; font-family: 'Clash Grotesk', sans-serif; font-style: italic; }
    .quote-interlude__author { font-size: 12px; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase; color: #7a756e; }

    /* ─── FRAMELESS FIELD GRID ─── */
    .field-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 40px; }
    .field-card { display: flex; flex-direction: column; text-decoration: none; color: inherit; }
    .field-card:hover { text-decoration: none; color: inherit; }
    .field-card__media { aspect-ratio: 16/10; overflow: hidden; margin-bottom: 20px; }
    .field-card__media img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.6s ease; }
    .field-card:hover .field-card__media img { transform: scale(1.03); }
    .field-card__tag-row { display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; }
    .field-card__tag { font-size: 10.5px; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: #523225; }
    .field-card__num { font-size: 11px; font-weight: 700; color: #a19d96; letter-spacing: 0.1em; }
    .field-card__title { font-size: 1.3rem; font-weight: 700; line-height: 1.2; letter-spacing: -0.015em; color: #272724; margin: 0 0 12px; }
    .field-card__excerpt { font-size: 1rem; line-height: 1.6; color: #6e6a64; margin: 0 0 20px; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }
    .field-card__footer { display: flex; align-items: center; justify-content: space-between; margin-top: auto; padding-top: 16px; border-top: 1px solid rgba(39, 39, 36, 0.1); font-size: 12px; color: #7a756e; }
    .field-card__arrow { font-size: 13px; font-weight: 700; color: #523225; transition: transform 0.2s ease; }
    .field-card:hover .field-card__arrow { transform: translateX(4px); }

    /* ─── 4. NEWSLETTER FORM (Warm Sand Band) ─── */
    .band-newsletter {
      background-color: #F6F7EA !important;
      padding: 64px 0 72px;
      width: 100%;
      box-sizing: border-box;
      border-top: 1px solid rgba(39, 39, 36, 0.15);
    }
    .newsletter-inner {
      max-width: 640px;
      margin: 0 auto;
      text-align: center;
      box-sizing: border-box;
    }
    .newsletter-eyebrow {
      display: inline-block;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.3em;
      text-transform: uppercase;
      color: #523225;
      margin-bottom: 20px;
    }
    .newsletter-headline {
      font-size: clamp(2.2rem, 4.2vw, 3.4rem);
      font-weight: 700;
      line-height: 1.08;
      letter-spacing: -0.025em;
      color: #272724;
      margin: 0 0 14px;
    }
    .newsletter-subtext {
      font-size: 1.05rem;
      line-height: 1.7;
      color: #5a5a54;
      max-width: 540px;
      margin: 0 auto 28px;
    }
    .newsletter-form {
      display: flex;
      max-width: 520px;
      margin: 0 auto;
      border: 1px solid rgba(39, 39, 36, 0.18);
      border-radius: 100px;
      overflow: hidden;
      background: #F6F7EA;
      box-shadow: 0 4px 16px rgba(39, 39, 36, 0.05);
      padding: 4px 4px 4px 20px;
      align-items: center;
    }
    .newsletter-form__input {
      flex: 1;
      background: transparent !important;
      border: none !important;
      outline: none !important;
      padding: 12px 14px;
      font-size: 15px;
      color: #272724 !important;
      font-family: 'Clash Grotesk', sans-serif !important;
    }
    .newsletter-form__input::placeholder { color: #8e8e88; }
    .newsletter-form__btn {
      background-color: #272724 !important;
      color: #F6F7EA !important;
      border: none !important;
      padding: 14px 32px;
      border-radius: 100px;
      font-size: 12.5px;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      cursor: pointer;
      font-family: 'Clash Grotesk', sans-serif !important;
      transition: background 0.2s ease, transform 0.2s ease;
      white-space: nowrap;
    }
    .newsletter-form__btn:hover {
      background-color: #523225 !important;
      transform: translateY(-1px);
    }
    .newsletter-note {
      font-size: 12.5px;
      color: #7a756e;
      margin-top: 18px;
      letter-spacing: 0.02em;
    }

    /* Responsive */
    @media (max-width: 1024px) {
      .cover-story, .story-duo { grid-template-columns: 1fr; gap: 40px; }
      .field-grid { grid-template-columns: repeat(2, 1fr); }
      .story-card-tall__media { aspect-ratio: 16/10; }
    }
    @media (max-width: 768px) {
      .field-grid { grid-template-columns: 1fr; }
      .editorial-band { padding: 40px 0; }
      .newsletter-form { flex-direction: column; border-radius: 8px; padding: 0; }
      .newsletter-form__input { width: 100%; padding: 14px 16px; border-bottom: 1px solid rgba(39,39,36,0.1) !important; }
      .newsletter-form__btn { width: 100%; border-radius: 0; padding: 14px 20px; }
    }"""


for lang, d in languages.items():
    filepath = d["path"]
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update CSS
    content = re.sub(
        r'/\*\s*═══════════════════════════════════════════════\s*ALTERNATING EDITORIAL SECTION BANDS.*?(?=\s*</style>)',
        new_css,
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'/\*\s*═══════════════════════════════════════════════\s*ULTRA-CLEAN EDITORIAL LAYOUT \(FRAMELESS\).*?(?=\s*</style>)',
        new_css,
        content,
        flags=re.DOTALL
    )
    
    # 2. Build new clean frameless HTML structure
    clean_html = f"""    <!-- ═══════════════════════════════════════════════
         ULTRA-CLEAN EDITORIAL LAYOUT
    ═══════════════════════════════════════════════ -->

    <section class="editorial-band">
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
            <img src="/images/Slider-images/slider-1.webp" alt="Agafay stone desert plateau" loading="eager" fetchpriority="high" decoding="async" />
            <span class="cover-story__badge">{d['badge']}</span>
          </div>
          <div class="cover-story__body">
            <div class="cover-story__tag-row">
              <span class="cover-story__tag">Desert Guide</span>
              <span class="cover-story__read-time">8 min read</span>
            </div>
            <h3 class="cover-story__title">The Complete Guide to Agafay Desert — Morocco’s Stone Desert Explained</h3>
            <p class="cover-story__standfirst">What makes Agafay different from the Sahara, and why travelers are increasingly choosing this 45-minute drive from Marrakech over a 10-hour journey south. A comprehensive primer on the mineral plateau redefining Moroccan desert travel.</p>
            <div class="cover-story__footer">
              <span class="cover-story__author">Marragafay Editorial</span>
              <span class="cover-story__cta">{d['read_article']}</span>
            </div>
          </div>
        </a>
      </div>
    </section>

    <section class="editorial-band">
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
            <span class="story-card-tall__tag">Experience</span>
            <h3 class="story-card-tall__title">Sunset Camel Ride in Agafay: What to Expect</h3>
            <p class="story-card-tall__excerpt">The silence before sunset in the desert is not empty — it is full. Our field guide on what every traveler should understand before mounting the camel for an authentic sunset crossing.</p>
            <div class="story-card-tall__footer">
              <span>August 2026 · 5 min read</span>
              <span style="font-weight: 700; color: #523225;">{d['read_story']}</span>
            </div>
          </a>

          <a href="berber-culture-agafay.html" class="story-card-stacked" data-category="culture">
            <div class="story-card-stacked__media">
              <img src="/images/Slider-images/slider-4.webp" alt="Berber heritage and culture in Agafay" loading="lazy" decoding="async" />
            </div>
            <span class="story-card-stacked__tag">Culture & Heritage</span>
            <h3 class="story-card-stacked__title">Berber Heritage and the Agafay: A Culture That Predates Tourism</h3>
            <p class="story-card-stacked__excerpt">Long before modern desert camps arrived, the stone hills of Agafay sustained Berber communities whose dry-stone architecture and hospitality rituals survive intact.</p>
            <div class="story-card-stacked__footer">
              <span>July 2026 · 6 min read</span>
              <span style="font-weight: 700; color: #523225;">{d['read_story']}</span>
            </div>
          </a>
        </div>
      </div>
    </section>

    <section class="editorial-band">
      <div class="journal-section">
        
        <div class="quote-interlude">
          <span class="quote-interlude__eyebrow">{d['quote_eyebrow']}</span>
          <p class="quote-interlude__text">{d['quote']}</p>
          <span class="quote-interlude__author">{d['author']}</span>
        </div>

        <div class="editorial-header">
          <div class="editorial-header__left">
            <span class="editorial-header__num">03 /</span>
            <h2 class="editorial-header__title">{d['title']}</h2>
          </div>
          <span class="editorial-header__sub">{d['sub']}</span>
        </div>

        <div class="field-grid" id="article-grid">
          <a href="marrakech-to-agafay.html" class="field-card" data-category="travel-tips">
            <div class="field-card__media">
              <img src="/images/gallery/gal1.webp" alt="Route from Marrakech to Agafay" loading="lazy" decoding="async" />
            </div>
            <div class="field-card__tag-row">
              <span class="field-card__tag">{d['c1_tag']}</span>
              <span class="field-card__num">01</span>
            </div>
            <h3 class="field-card__title">{d['c1_title']}</h3>
            <p class="field-card__excerpt">{d['c1_excerpt']}</p>
            <div class="field-card__footer">
              <span>{d['c1_meta']}</span>
              <span class="field-card__arrow">{d['read']}</span>
            </div>
          </a>

          <a href="agafay-dinner-experience.html" class="field-card" data-category="experience">
            <div class="field-card__media">
              <img src="/images/activites/show.webp" alt="Agafay dinner under the stars" loading="lazy" decoding="async" />
            </div>
            <div class="field-card__tag-row">
              <span class="field-card__tag">{d['c2_tag']}</span>
              <span class="field-card__num">02</span>
            </div>
            <h3 class="field-card__title">{d['c2_title']}</h3>
            <p class="field-card__excerpt">{d['c2_excerpt']}</p>
            <div class="field-card__footer">
              <span>{d['c2_meta']}</span>
              <span class="field-card__arrow">{d['read']}</span>
            </div>
          </a>

          <a href="agafay-quad-biking-guide.html" class="field-card" data-category="experience">
            <div class="field-card__media">
              <img src="/images/activites/quad.webp" alt="Quad biking in Agafay Desert" loading="lazy" decoding="async" />
            </div>
            <div class="field-card__tag-row">
              <span class="field-card__tag">{d['c3_tag']}</span>
              <span class="field-card__num">03</span>
            </div>
            <h3 class="field-card__title">{d['c3_title']}</h3>
            <p class="field-card__excerpt">{d['c3_excerpt']}</p>
            <div class="field-card__footer">
              <span>{d['c3_meta']}</span>
              <span class="field-card__arrow">{d['read']}</span>
            </div>
          </a>
        </div>

        <div class="no-results" id="no-results" style="text-align: center; padding: 60px 20px; color: #7a756e; display: none;">
          {d['no_results']}
        </div>
      </div>
    </section>"""

    # Replace everything from the start of bands to the newsletter
    content = re.sub(
        r'<!-- ═══════════════════════════════════════════════\s*ALTERNATING EDITORIAL BANDS.*?(?=<!-- BAND 4: WARM SANDSTONE \(NEWSLETTER FLUSH TO FOOTER\)|<section class="band-newsletter")',
        clean_html + "\n\n    ",
        content,
        flags=re.DOTALL
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Reverted to clean frameless design in: {filepath}")

print("All language pages updated to ultra-clean frameless editorial layout!")
