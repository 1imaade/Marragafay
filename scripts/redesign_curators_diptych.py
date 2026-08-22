import re

languages = {
    "en": {
        "path": "en/blog/index.html",
        "header_title": "Curator’s Selection", "header_sub": "Encounters & Traditions",
        "l_tag": "Experience", "l_title": "Sunset Camel Ride in Agafay: What to Expect", 
        "l_excerpt": "The silence before sunset in the desert is not empty — it is full. Our field guide on what every traveler should understand before mounting the camel for an authentic sunset crossing.", 
        "l_date": "August 2026 · 5 min read", "l_read": "Read Story →",
        "r_tag": "Culture & Heritage", "r_title": "Berber Heritage and the Agafay: A Culture That Predates Tourism", 
        "r_excerpt": "Long before modern desert camps arrived, the stone hills of Agafay sustained Berber communities whose dry-stone architecture and hospitality rituals survive intact.", 
        "r_date": "July 2026 · 6 min read", "r_read": "Read Story →"
    },
    "fr": {
        "path": "fr/blog/index.html",
        "header_title": "La Sélection du Conservateur", "header_sub": "Rencontres & Traditions",
        "l_tag": "Expérience", "l_title": "Balade en Chameau au Coucher du Soleil à Agafay : À Quoi s'Attendre", 
        "l_excerpt": "Le silence avant le coucher du soleil dans le désert n'est pas vide — il est plein. Notre guide de terrain sur ce que tout voyageur doit comprendre avant de monter à dos de chameau.", 
        "l_date": "Août 2026 · 5 min", "l_read": "Lire le Récit →",
        "r_tag": "Culture & Patrimoine", "r_title": "L'Héritage Berbère et Agafay : Une Culture Antérieure au Tourisme", 
        "r_excerpt": "Bien avant l'arrivée des camps modernes dans le désert, les collines de pierre d'Agafay abritaient des communautés berbères dont l'architecture et les rituels d'hospitalité survivent intacts.", 
        "r_date": "Juillet 2026 · 6 min", "r_read": "Lire le Récit →"
    },
    "es": {
        "path": "es/blog/index.html",
        "header_title": "Selección del Comisario", "header_sub": "Encuentros y Tradiciones",
        "l_tag": "Experiencia", "l_title": "Paseo en Camello al Atardecer en Agafay: Qué Esperar", 
        "l_excerpt": "El silencio antes del atardecer en el desierto no está vacío, está lleno. Nuestra guía de campo sobre lo que todo viajero debe entender antes de montar en camello.", 
        "l_date": "Agosto 2026 · 5 min", "l_read": "Leer Historia →",
        "r_tag": "Cultura y Patrimonio", "r_title": "El Patrimonio Bereber y Agafay: Una Cultura Anterior al Turismo", 
        "r_excerpt": "Mucho antes de que llegaran los modernos campamentos del desierto, las colinas de piedra de Agafay sustentaban a comunidades bereberes cuya arquitectura y hospitalidad sobreviven intactas.", 
        "r_date": "Julio 2026 · 6 min", "r_read": "Leer Historia →"
    },
    "ar": {
        "path": "ar/blog/index.html",
        "header_title": "مختارات المجلة", "header_sub": "تراث وتقاليد عريقة",
        "l_tag": "تجربة", "l_title": "جولة على الجمال وقت الغروب في أكافاي: ماذا تتوقع", 
        "l_excerpt": "الصمت قبل الغروب في الصحراء ليس فارغاً — بل هو مليء بالحياة. دليلنا الميداني حول ما يجب أن يفهمه كل مسافر قبل ركوب الجمل في جولة أصيلة عند الغروب.", 
        "l_date": "أغسطس 2026 · 5 دقائق", "l_read": "اقرأ القصة ←",
        "r_tag": "ثقافة وتراث", "r_title": "التراث الأمازيغي وأكافاي: ثقافة تسبق السياحة", 
        "r_excerpt": "قبل وقت طويل من وصول المخيمات الصحراوية الحديثة، كانت تلال أكافاي الحجرية تحتضن مجتمعات أمازيغية لا تزال هندستها المعمارية وطقوس الضيافة باقية حتى اليوم.", 
        "r_date": "يوليو 2026 · 6 دقائق", "r_read": "اقرأ القصة ←"
    }
}

diptych_css = """    /* ═══════════════════════════════════════════════
       02 / CURATOR'S SELECTION: EDITORIAL DIPTYCH
    ═══════════════════════════════════════════════ */
    .curator-diptych {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0;
      border-top: 1px solid rgba(39, 39, 36, 0.15);
      border-bottom: 1px solid rgba(39, 39, 36, 0.15);
      margin-top: 10px;
    }
    .diptych-card {
      display: flex;
      flex-direction: column;
      text-decoration: none;
      color: inherit;
      padding: 36px 44px 44px 0;
      transition: background-color 0.3s ease;
    }
    .diptych-card:last-child {
      padding: 36px 0 44px 44px;
      border-left: 1px solid rgba(39, 39, 36, 0.15);
    }
    .diptych-card:hover {
      text-decoration: none;
      color: inherit;
    }
    .diptych-card__media {
      position: relative;
      overflow: hidden;
      aspect-ratio: 16/10;
      margin-bottom: 26px;
      background: #e8e8dc;
    }
    .diptych-card__media img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.8s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .diptych-card:hover .diptych-card__media img {
      transform: scale(1.04);
    }
    .diptych-card__tag {
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: #523225;
      margin-bottom: 12px;
      display: block;
    }
    .diptych-card__title {
      font-size: clamp(1.5rem, 2vw, 1.85rem);
      font-weight: 700;
      line-height: 1.15;
      letter-spacing: -0.02em;
      color: #272724;
      margin: 0 0 16px;
      font-family: 'Clash Grotesk', sans-serif;
    }
    .diptych-card__excerpt {
      font-size: 1.05rem;
      line-height: 1.65;
      color: #4e4e48;
      margin: 0 0 28px;
      flex-grow: 1;
    }
    .diptych-card__footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-top: 18px;
      border-top: 1px solid rgba(39, 39, 36, 0.1);
      font-size: 12px;
      font-weight: 500;
      color: #7a756e;
    }
    .diptych-card__read {
      font-weight: 700;
      color: #272724;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      transition: color 0.2s ease, transform 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .diptych-card:hover .diptych-card__read {
      color: #523225;
      transform: translateX(4px);
    }

    @media (max-width: 900px) {
      .curator-diptych {
        grid-template-columns: 1fr;
      }
      .diptych-card {
        padding: 32px 0 !important;
        border-left: none !important;
        border-bottom: 1px solid rgba(39, 39, 36, 0.15);
      }
      .diptych-card:last-child {
        border-bottom: none;
      }
    }"""

for lang, d in languages.items():
    filepath = d["path"]
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Replace the CSS block for story-duo / frameless duo with diptych_css
    content = re.sub(
        r'/\*\s*─── FRAMELESS DUO.*?/\*\s*─── FRAMELESS QUOTE ───\s*\*/',
        diptych_css + "\n\n    /* ─── FRAMELESS QUOTE ─── */",
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'/\*\s*═══════════════════════════════════════════════\s*02 / CURATOR\'S SELECTION.*?/\*\s*─── FRAMELESS QUOTE ───\s*\*/',
        diptych_css + "\n\n    /* ─── FRAMELESS QUOTE ─── */",
        content,
        flags=re.DOTALL
    )

    # 2. Build the new Diptych HTML
    diptych_html = f"""<div class="curator-diptych">
          <!-- Left Column -->
          <a href="agafay-camel-ride.html" class="diptych-card" data-category="experience">
            <div class="diptych-card__media">
              <img src="/images/Slider-images/slider-3.webp" alt="Sunset Camel Ride in Agafay" loading="lazy" decoding="async" />
            </div>
            <span class="diptych-card__tag">{d['l_tag']}</span>
            <h3 class="diptych-card__title">{d['l_title']}</h3>
            <p class="diptych-card__excerpt">{d['l_excerpt']}</p>
            <div class="diptych-card__footer">
              <span>{d['l_date']}</span>
              <span class="diptych-card__read">{d['l_read']}</span>
            </div>
          </a>

          <!-- Right Column -->
          <a href="berber-culture-agafay.html" class="diptych-card" data-category="culture">
            <div class="diptych-card__media">
              <img src="/images/gallery/gal4.webp" alt="Berber heritage and culture in Agafay" loading="lazy" decoding="async" />
            </div>
            <span class="diptych-card__tag">{d['r_tag']}</span>
            <h3 class="diptych-card__title">{d['r_title']}</h3>
            <p class="diptych-card__excerpt">{d['r_excerpt']}</p>
            <div class="diptych-card__footer">
              <span>{d['r_date']}</span>
              <span class="diptych-card__read">{d['r_read']}</span>
            </div>
          </a>
        </div>"""

    # Replace the HTML for section 02
    content = re.sub(
        r'<div class="(story-duo|curator-diptych)">.*?</div>\s*</div>\s*</section>',
        diptych_html + "\n      </div>\n    </section>",
        content,
        flags=re.DOTALL
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Applied Curator's Diptych redesign to {filepath}")

print("Done redesigning Section 02 across all languages!")
