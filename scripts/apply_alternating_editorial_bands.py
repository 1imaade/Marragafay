import re

languages = {
    "en": {
        "path": "en/blog/index.html",
        "h1_title": "The Lead Story",
        "h1_sub": "Flagship Field Note",
        "badge": "Editor’s Pick",
        "read_story": "Read Story →",
        "read_article": "Read Full Story →",
        "curator_title": "Curator’s Selection",
        "curator_sub": "Encounters & Traditions",
        "quote_eyebrow": "Agafay Field Philosophy",
        "quote_text": "“The stone desert is not empty — it is vast, silent, and ancient. A forty-five minute drive that feels like a quiet departure from time itself.”",
        "quote_author": "Marragafay Field Notes · Marrakech",
        "dispatches_title": "Field Dispatches",
        "dispatches_sub": "Guides, Routes & Gastronomy",
        "eyebrow": "The Desert Letter",
        "headline": "Desert dispatches, delivered.",
        "subtext": "One monthly letter. No noise. Stories, field notes, and private seasonal offers from the stone desert.",
        "placeholder": "Enter your email address",
        "btn": "Subscribe",
        "note": "Zero spam. Unsubscribe with one click at any time."
    },
    "fr": {
        "path": "fr/blog/index.html",
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
        "dispatches_sub": "Guides, Itinéraires & Gastronomie",
        "eyebrow": "La Lettre du Désert",
        "headline": "Les nouvelles du désert, livrées chez vous.",
        "subtext": "Une lettre par mois. Récits, inspirations et offres privées depuis le désert d'Agafay.",
        "placeholder": "Votre adresse e-mail",
        "btn": "S'inscrire",
        "note": "Zéro spam. Désabonnement en un clic à tout moment."
    },
    "es": {
        "path": "es/blog/index.html",
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
        "dispatches_sub": "Guías, Rutas y Gastronomía",
        "eyebrow": "La Carta del Desierto",
        "headline": "Noticias del desierto, en tu bandeja.",
        "subtext": "Una carta al mes. Sin ruido. Historias, guías y ofertas exclusivas desde el desierto de piedra.",
        "placeholder": "Tu correo electrónico",
        "btn": "Suscribirse",
        "note": "Cero spam. Cancela la suscripción en cualquier momento."
    },
    "ar": {
        "path": "ar/blog/index.html",
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
        "dispatches_sub": "أدلة، مسارات وتجارب طهي فاخرة",
        "eyebrow": "رسالة الصحراء",
        "headline": "قصص وتحديثات الصحراء في بريدك.",
        "subtext": "رسالة شهرية واحدة. قصص حصرية، تجارب فاخرة وعروض خاصة من صحراء أكافاي.",
        "placeholder": "أدخل بريدك الإلكتروني",
        "btn": "اشتراك",
        "note": "بدون إعلانات مزعجة. يمكنك إلغاء الاشتراك في أي وقت."
    }
}

new_css = """    /* ═══════════════════════════════════════════════
       ALTERNATING EDITORIAL SECTION BANDS
    ═══════════════════════════════════════════════ */
    .journal-section { max-width: 1440px; margin: 0 auto; padding: 0 32px; box-sizing: border-box; }

    /* Band 1: Warm Sandstone (Cover Story) */
    .band-sandstone {
      background-color: #E8E2D5 !important;
      padding: 80px 0 90px;
      border-top: 1px solid rgba(39, 39, 36, 0.08);
      border-bottom: 1px solid rgba(39, 39, 36, 0.08);
      width: 100%;
      box-sizing: border-box;
    }

    /* Band 2: Earthy Mineral Sand (Curator's Duo) */
    .band-mineral {
      background-color: #DDD5C3 !important;
      padding: 80px 0 90px;
      border-bottom: 1px solid rgba(39, 39, 36, 0.1);
      width: 100%;
      box-sizing: border-box;
    }

    /* Band 3: Dark Luxury Night (Dispatches & Philosophy) */
    .band-dark-luxury {
      background-color: #1E1E1C !important;
      color: #F6F7EA !important;
      padding: 90px 0 100px;
      width: 100%;
      box-sizing: border-box;
    }

    /* Band 4: Newsletter Warm Sand (Flush to Dark Footer) */
    .band-newsletter {
      background-color: #E8E2D5 !important;
      padding: 96px 0 106px;
      width: 100%;
      box-sizing: border-box;
      border-top: 1px solid rgba(39, 39, 36, 0.08);
    }

    /* Editorial Section Header (Light Bands) */
    .editorial-header {
      display: flex;
      align-items: flex-end;
      justify-content: space-between;
      margin-bottom: 36px;
      padding-bottom: 18px;
      border-bottom: 1.5px solid rgba(39, 39, 36, 0.15);
    }
    .editorial-header__left { display: flex; align-items: baseline; gap: 16px; }
    .editorial-header__num {
      font-size: 13px;
      font-weight: 700;
      color: #523225;
      letter-spacing: 0.15em;
    }
    .editorial-header__title {
      font-size: 1.4rem;
      font-weight: 700;
      color: #272724;
      letter-spacing: -0.015em;
      margin: 0;
      text-transform: uppercase;
    }
    .editorial-header__sub {
      font-size: 12px;
      font-weight: 500;
      color: #7a756e;
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }

    /* Editorial Header (Dark Band) */
    .editorial-header--dark {
      border-bottom-color: rgba(246, 247, 234, 0.15);
    }
    .editorial-header--dark .editorial-header__num {
      color: #d4af37;
    }
    .editorial-header--dark .editorial-header__title {
      color: #F6F7EA;
    }
    .editorial-header--dark .editorial-header__sub {
      color: rgba(246, 247, 234, 0.6);
    }

    /* ─── 1. COVER STORY CARD ─── */
    .cover-story {
      display: grid;
      grid-template-columns: 1.25fr 1fr;
      background: #F6F7EA;
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid rgba(39, 39, 36, 0.08);
      box-shadow: 0 14px 40px rgba(39, 39, 36, 0.07);
      transition: box-shadow 0.35s ease, transform 0.35s ease;
      text-decoration: none;
      color: inherit;
    }
    .cover-story:hover {
      transform: translateY(-4px);
      box-shadow: 0 22px 50px rgba(39, 39, 36, 0.12);
      text-decoration: none;
      color: inherit;
    }
    .cover-story__media {
      position: relative;
      overflow: hidden;
      min-height: 480px;
    }
    .cover-story__media img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.8s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .cover-story:hover .cover-story__media img { transform: scale(1.04); }
    .cover-story__badge {
      position: absolute;
      top: 24px;
      left: 24px;
      background: rgba(39, 39, 36, 0.92);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      color: #F6F7EA;
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.25em;
      text-transform: uppercase;
      padding: 7px 18px;
      border-radius: 100px;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.2);
      z-index: 2;
    }
    .cover-story__body {
      padding: 64px 56px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      background: #F6F7EA;
      box-sizing: border-box;
    }
    .cover-story__tag-row {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 22px;
    }
    .cover-story__tag {
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: #523225;
      background: rgba(82, 50, 37, 0.08);
      padding: 5px 14px;
      border-radius: 100px;
    }
    .cover-story__read-time {
      font-size: 12px;
      font-weight: 500;
      color: #7a756e;
    }
    .cover-story__title {
      font-size: clamp(2rem, 3.4vw, 2.9rem);
      font-weight: 700;
      line-height: 1.1;
      letter-spacing: -0.025em;
      color: #272724;
      margin: 0 0 20px;
    }
    .cover-story__standfirst {
      font-size: 1.08rem;
      line-height: 1.75;
      color: #4e4e48;
      margin: 0 0 36px;
      max-width: 540px;
    }
    .cover-story__footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-top: 24px;
      border-top: 1px solid rgba(39, 39, 36, 0.1);
      margin-top: auto;
    }
    .cover-story__author {
      font-size: 11.5px;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: #272724;
    }
    .cover-story__cta {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: #523225;
      transition: gap 0.25s ease;
    }
    .cover-story:hover .cover-story__cta { gap: 16px; }

    /* ─── 2. CURATOR'S DUO (On Mineral Sand) ─── */
    .story-duo {
      display: grid;
      grid-template-columns: 1.3fr 1fr;
      gap: 36px;
    }
    .story-card-tall,
    .story-card-stacked {
      background: #F6F7EA;
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid rgba(39, 39, 36, 0.08);
      display: flex;
      flex-direction: column;
      text-decoration: none;
      color: inherit;
      box-shadow: 0 12px 36px rgba(39, 39, 36, 0.06);
      transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.3s ease;
    }
    .story-card-tall:hover,
    .story-card-stacked:hover {
      transform: translateY(-6px);
      box-shadow: 0 20px 48px rgba(39, 39, 36, 0.12);
      text-decoration: none;
      color: inherit;
    }
    .story-card-tall__media,
    .story-card-stacked__media {
      position: relative;
      aspect-ratio: 16/10;
      overflow: hidden;
    }
    .story-card-tall__media img,
    .story-card-stacked__media img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .story-card-tall:hover .story-card-tall__media img,
    .story-card-stacked:hover .story-card-stacked__media img {
      transform: scale(1.05);
    }
    .story-card-tall__body {
      padding: 36px 36px 32px;
      display: flex;
      flex-direction: column;
      flex: 1;
    }
    .story-card-stacked__body {
      padding: 32px 32px 28px;
      display: flex;
      flex-direction: column;
      flex: 1;
    }
    .story-card-tall__tag,
    .story-card-stacked__tag {
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: #523225;
      margin-bottom: 12px;
    }
    .story-card-tall__title {
      font-size: 1.55rem;
      font-weight: 700;
      line-height: 1.22;
      letter-spacing: -0.02em;
      color: #272724;
      margin: 0 0 16px;
    }
    .story-card-stacked__title {
      font-size: 1.35rem;
      font-weight: 700;
      line-height: 1.25;
      letter-spacing: -0.015em;
      color: #272724;
      margin: 0 0 14px;
    }
    .story-card-tall__excerpt,
    .story-card-stacked__excerpt {
      font-size: 0.98rem;
      line-height: 1.7;
      color: #5a5a54;
      margin: 0 0 26px;
    }
    .story-card-tall__footer,
    .story-card-stacked__footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-top: auto;
      padding-top: 18px;
      border-top: 1px solid rgba(39, 39, 36, 0.08);
      font-size: 12px;
      color: #7a756e;
    }

    /* ─── 3. DARK LUXURY NIGHT BAND ─── */
    .quote-interlude-dark {
      margin-bottom: 64px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(246, 247, 234, 0.1);
      color: #F6F7EA;
      border-radius: 8px;
      padding: 60px 48px;
      position: relative;
      overflow: hidden;
    }
    .quote-interlude-dark::before {
      content: '“';
      position: absolute;
      top: -30px;
      left: 36px;
      font-size: 180px;
      font-family: serif;
      color: rgba(246, 247, 234, 0.04);
      line-height: 1;
      pointer-events: none;
    }
    .quote-interlude-dark__inner {
      max-width: 860px;
      margin: 0 auto;
      text-align: center;
      position: relative;
      z-index: 1;
    }
    .quote-interlude-dark__eyebrow {
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.3em;
      text-transform: uppercase;
      color: #d4af37;
      margin-bottom: 20px;
      display: block;
    }
    .quote-interlude-dark__text {
      font-size: clamp(1.35rem, 2.6vw, 2rem);
      font-weight: 600;
      line-height: 1.4;
      letter-spacing: -0.015em;
      color: #F6F7EA;
      margin: 0 0 24px;
      font-style: italic;
    }
    .quote-interlude-dark__author {
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: rgba(246, 247, 234, 0.6);
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
    }
    .quote-interlude-dark__author::before,
    .quote-interlude-dark__author::after {
      content: '';
      width: 24px;
      height: 1px;
      background: rgba(246, 247, 234, 0.2);
    }

    .field-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 32px;
    }
    .field-card-dark {
      background: #272724;
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid rgba(246, 247, 234, 0.12);
      display: flex;
      flex-direction: column;
      text-decoration: none;
      color: #F6F7EA;
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.25);
      transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.3s ease, border-color 0.3s ease;
    }
    .field-card-dark:hover {
      transform: translateY(-6px);
      box-shadow: 0 20px 48px rgba(0, 0, 0, 0.4);
      border-color: rgba(212, 175, 55, 0.4);
      text-decoration: none;
      color: #F6F7EA;
    }
    .field-card-dark__media {
      position: relative;
      aspect-ratio: 16/10;
      overflow: hidden;
    }
    .field-card-dark__media img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .field-card-dark:hover .field-card-dark__media img { transform: scale(1.05); }
    .field-card-dark__body {
      padding: 30px 28px 26px;
      display: flex;
      flex-direction: column;
      flex: 1;
    }
    .field-card-dark__tag-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 14px;
    }
    .field-card-dark__tag {
      font-size: 10.5px;
      font-weight: 700;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: #d4af37;
    }
    .field-card-dark__num {
      font-size: 11px;
      font-weight: 700;
      color: rgba(246, 247, 234, 0.4);
      letter-spacing: 0.1em;
    }
    .field-card-dark__title {
      font-size: 1.22rem;
      font-weight: 700;
      line-height: 1.28;
      letter-spacing: -0.015em;
      color: #F6F7EA;
      margin: 0 0 14px;
    }
    .field-card-dark__excerpt {
      font-size: 0.95rem;
      line-height: 1.7;
      color: rgba(246, 247, 234, 0.75);
      margin: 0 0 24px;
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }
    .field-card-dark__footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-top: auto;
      padding-top: 18px;
      border-top: 1px solid rgba(246, 247, 234, 0.1);
      font-size: 12px;
      color: rgba(246, 247, 234, 0.5);
    }
    .field-card-dark__arrow {
      font-size: 13px;
      font-weight: 700;
      color: #d4af37;
      transition: transform 0.2s ease;
    }
    .field-card-dark:hover .field-card-dark__arrow {
      transform: translateX(4px);
    }

    /* ─── 4. NEWSLETTER FORM (Warm Sand Band) ─── */
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
      margin: 0 0 18px;
    }
    .newsletter-subtext {
      font-size: 1.05rem;
      line-height: 1.7;
      color: #5a5a54;
      max-width: 540px;
      margin: 0 auto 40px;
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
      .cover-story { grid-template-columns: 1fr; }
      .cover-story__media { min-height: 340px; }
      .cover-story__body { padding: 44px 36px; }
      .story-duo { grid-template-columns: 1fr; }
      .field-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 768px) {
      .journal-section { padding: 0 20px; }
      .band-sandstone, .band-mineral, .band-dark-luxury, .band-newsletter { padding: 56px 0; }
      .quote-interlude-dark { padding: 40px 20px; margin-bottom: 40px; }
      .field-grid { grid-template-columns: 1fr; }
      .newsletter-form { flex-direction: column; border-radius: 8px; padding: 0; }
      .newsletter-form__input { width: 100%; padding: 14px 16px; border-bottom: 1px solid rgba(39,39,36,0.1) !important; }
      .newsletter-form__btn { width: 100%; border-radius: 0; padding: 14px 20px; }
    }"""

for lang, data in languages.items():
    filepath = data["path"]
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update CSS
    content = re.sub(
        r'/\*\s*═══════════════════════════════════════════════\s*LUXURY EDITORIAL MAGAZINE SECTIONS.*?(?=\s*</style>)',
        new_css,
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'/\*\s*═══════════════════════════════════════════════\s*ALTERNATING EDITORIAL SECTION BANDS.*?(?=\s*</style>)',
        new_css,
        content,
        flags=re.DOTALL
    )

    # 2. Build HTML with full-width alternating bands
    html_bands = f"""    <!-- ═══════════════════════════════════════════════
         ALTERNATING EDITORIAL BANDS
    ═══════════════════════════════════════════════ -->

    <!-- BAND 1: WARM SANDSTONE (THE LEAD STORY) -->
    <section class="band-sandstone">
      <div class="journal-section">
        <div class="editorial-header">
          <div class="editorial-header__left">
            <span class="editorial-header__num">01 /</span>
            <h2 class="editorial-header__title">{data['h1_title']}</h2>
          </div>
          <span class="editorial-header__sub">{data['h1_sub']}</span>
        </div>

        <a href="agafay-desert-guide.html" class="cover-story" data-category="desert-guide">
          <div class="cover-story__media">
            <img src="/images/Slider-images/slider-1.webp" alt="Agafay stone desert plateau" loading="eager" fetchpriority="high" decoding="async" />
            <span class="cover-story__badge">{data['badge']}</span>
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
              <span class="cover-story__cta">{data['read_article']}</span>
            </div>
          </div>
        </a>
      </div>
    </section>

    <!-- BAND 2: EARTHY MINERAL SAND (CURATOR’S SELECTION) -->
    <section class="band-mineral">
      <div class="journal-section">
        <div class="editorial-header">
          <div class="editorial-header__left">
            <span class="editorial-header__num">02 /</span>
            <h2 class="editorial-header__title">{data['curator_title']}</h2>
          </div>
          <span class="editorial-header__sub">{data['curator_sub']}</span>
        </div>

        <div class="story-duo">
          <!-- Story 1 (Tall) -->
          <a href="agafay-camel-ride.html" class="story-card-tall" data-category="experience">
            <div class="story-card-tall__media">
              <img src="/images/Slider-images/slider-3.webp" alt="Sunset Camel Ride in Agafay" loading="lazy" decoding="async" />
            </div>
            <div class="story-card-tall__body">
              <span class="story-card-tall__tag">Experience</span>
              <h3 class="story-card-tall__title">Sunset Camel Ride in Agafay: What to Expect</h3>
              <p class="story-card-tall__excerpt">The silence before sunset in the desert is not empty — it is full. Our field guide on what every traveler should understand before mounting the camel for an authentic sunset crossing.</p>
              <div class="story-card-tall__footer">
                <span>August 2026 · 5 min read</span>
                <span style="font-weight: 700; color: #523225;">{data['read_story']}</span>
              </div>
            </div>
          </a>

          <!-- Story 2 (Stacked) -->
          <a href="berber-culture-agafay.html" class="story-card-stacked" data-category="culture">
            <div class="story-card-stacked__media">
              <img src="/images/Slider-images/slider-4.webp" alt="Berber heritage and culture in Agafay" loading="lazy" decoding="async" />
            </div>
            <div class="story-card-stacked__body">
              <span class="story-card-stacked__tag">Culture & Heritage</span>
              <h3 class="story-card-stacked__title">Berber Heritage and the Agafay: A Culture That Predates Tourism</h3>
              <p class="story-card-stacked__excerpt">Long before modern desert camps arrived, the stone hills of Agafay sustained Berber communities whose dry-stone architecture and hospitality rituals survive intact.</p>
              <div class="story-card-stacked__footer">
                <span>July 2026 · 6 min read</span>
                <span style="font-weight: 700; color: #523225;">{data['read_story']}</span>
              </div>
            </div>
          </a>
        </div>
      </div>
    </section>

    <!-- BAND 3: DARK LUXURY NIGHT (FIELD DISPATCHES & PHILOSOPHY) -->
    <section class="band-dark-luxury">
      <div class="journal-section">
        
        <!-- Embedded Philosophy Quote -->
        <div class="quote-interlude-dark">
          <div class="quote-interlude-dark__inner">
            <span class="quote-interlude-dark__eyebrow">{data['quote_eyebrow']}</span>
            <p class="quote-interlude-dark__text">{data['quote_text']}</p>
            <span class="quote-interlude-dark__author">{data['quote_author']}</span>
          </div>
        </div>

        <div class="editorial-header editorial-header--dark">
          <div class="editorial-header__left">
            <span class="editorial-header__num">03 /</span>
            <h2 class="editorial-header__title">{data['dispatches_title']}</h2>
          </div>
          <span class="editorial-header__sub">{data['dispatches_sub']}</span>
        </div>

        <div class="field-grid" id="article-grid">
          <!-- Card 1 -->
          <a href="marrakech-to-agafay.html" class="field-card-dark" data-category="travel-tips">
            <div class="field-card-dark__media">
              <img src="/images/gallery/gal1.webp" alt="Route from Marrakech to Agafay" loading="lazy" decoding="async" />
            </div>
            <div class="field-card-dark__body">
              <div class="field-card-dark__tag-row">
                <span class="field-card-dark__tag">Travel Logistics</span>
                <span class="field-card-dark__num">01</span>
              </div>
              <h3 class="field-card-dark__title">Marrakech to Agafay Desert: Every Way to Get There</h3>
              <p class="field-card-dark__excerpt">From private transfers to scenic backcountry roads, the 45-kilometer journey separates the bustling medina from absolute stillness. Full cost and timing breakdown.</p>
              <div class="field-card-dark__footer">
                <span>July 2026 · 4 min read</span>
                <span class="field-card-dark__arrow">Read →</span>
              </div>
            </div>
          </a>

          <!-- Card 2 -->
          <a href="agafay-dinner-experience.html" class="field-card-dark" data-category="experience">
            <div class="field-card-dark__media">
              <img src="/images/activites/show.webp" alt="Agafay dinner under the stars" loading="lazy" decoding="async" />
            </div>
            <div class="field-card-dark__body">
              <div class="field-card-dark__tag-row">
                <span class="field-card-dark__tag">Night Experiences</span>
                <span class="field-card-dark__num">02</span>
              </div>
              <h3 class="field-card-dark__title">The Agafay Dinner Experience: Luxury Under a Moroccan Sky</h3>
              <p class="field-card-dark__excerpt">How a candlelit desert dinner became Marragafay’s most coveted evening ritual — and the subtle gastronomic details that make it unforgettable.</p>
              <div class="field-card-dark__footer">
                <span>June 2026 · 7 min read</span>
                <span class="field-card-dark__arrow">Read →</span>
              </div>
            </div>
          </a>

          <!-- Card 3 -->
          <a href="agafay-quad-biking-guide.html" class="field-card-dark" data-category="experience">
            <div class="field-card-dark__media">
              <img src="/images/activites/quad.webp" alt="Quad biking in Agafay Desert" loading="lazy" decoding="async" />
            </div>
            <div class="field-card-dark__body">
              <div class="field-card-dark__tag-row">
                <span class="field-card-dark__tag">Adventure Trails</span>
                <span class="field-card-dark__num">03</span>
              </div>
              <h3 class="field-card-dark__title">Quad Biking in Agafay Desert: Safety, Tips & What You'll See</h3>
              <p class="field-card-dark__excerpt">Everything you need to know about navigating high-performance 4x4 machines across Morocco’s most exhilarating stone canyons and panoramic ridges.</p>
              <div class="field-card-dark__footer">
                <span>August 2026 · 6 min read</span>
                <span class="field-card-dark__arrow">Read →</span>
              </div>
            </div>
          </a>
        </div>

        <div class="no-results" id="no-results" style="text-align: center; padding: 60px 20px; color: rgba(246, 247, 234, 0.6); display: none;">
          No articles found in this category. More stories coming soon.
        </div>
      </div>
    </section>

    <!-- BAND 4: WARM SANDSTONE (NEWSLETTER FLUSH TO FOOTER) -->
    <section class="band-newsletter">
      <div class="journal-section">
        <div class="newsletter-inner">
          <span class="newsletter-eyebrow">{data['eyebrow']}</span>
          <h2 class="newsletter-headline">{data['headline']}</h2>
          <p class="newsletter-subtext">{data['subtext']}</p>
          <form class="newsletter-form" action="#" method="post" onsubmit="handleNewsletterSubmit(event);" novalidate aria-label="Newsletter signup">
            <label for="newsletter-email" class="sr-only">Email</label>
            <input type="email" id="newsletter-email" name="email" class="newsletter-form__input" placeholder="{data['placeholder']}" autocomplete="email" required aria-required="true" />
            <button type="submit" class="newsletter-form__btn" aria-label="Subscribe">{data['btn']}</button>
          </form>
          <p class="newsletter-note">{data['note']}</p>
        </div>
      </div>
    </section>"""

    content = re.sub(
        r'<!-- 1\. COVER STORY -->.*?<!-- FOOTER -->',
        html_bands + "\n\n  </div>\n\n  <!-- FOOTER -->",
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'<!-- ═══════════════════════════════════════════════\s*ALTERNATING EDITORIAL BANDS.*?(?=\s*<!-- FOOTER -->)',
        html_bands + "\n\n  </div>\n\n  ",
        content,
        flags=re.DOTALL
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Applied alternating editorial bands in: {filepath}")

print("All language pages updated with rich alternating editorial bands!")
