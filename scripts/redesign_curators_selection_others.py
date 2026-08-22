import re

languages = {
    "fr": {
        "l_tag": "Expérience", "l_title": "Balade en Chameau au Coucher du Soleil à Agafay : À Quoi s'Attendre", "l_excerpt": "Le silence avant le coucher du soleil dans le désert n'est pas vide — il est plein. Notre guide de terrain sur ce que tout voyageur doit comprendre avant de monter à dos de chameau pour une traversée authentique au crépuscule.", "l_date": "Août 2026 · 5 min", "l_read": "Lire le Récit →",
        "r_tag": "Culture & Patrimoine", "r_title": "L'Héritage Berbère et Agafay : Une Culture Antérieure au Tourisme", "r_excerpt": "Bien avant l'arrivée des camps modernes dans le désert, les collines de pierre d'Agafay abritaient des communautés berbères dont l'architecture en pierre sèche et les rituels d'hospitalité survivent intacts.", "r_date": "Juillet 2026 · 6 min", "r_read": "Lire le Récit →"
    },
    "es": {
        "l_tag": "Experiencia", "l_title": "Paseo en Camello al Atardecer en Agafay: Qué Esperar", "l_excerpt": "El silencio antes del atardecer en el desierto no está vacío, está lleno. Nuestra guía de campo sobre lo que todo viajero debe entender antes de montar en camello para una auténtica travesía al atardecer.", "l_date": "Agosto 2026 · 5 min", "l_read": "Leer Historia →",
        "r_tag": "Cultura y Patrimonio", "r_title": "El Patrimonio Bereber y Agafay: Una Cultura Anterior al Turismo", "r_excerpt": "Mucho antes de que llegaran los modernos campamentos del desierto, las colinas de piedra de Agafay sustentaban a comunidades bereberes cuya arquitectura de piedra seca y rituales de hospitalidad sobreviven intactos.", "r_date": "Julio 2026 · 6 min", "r_read": "Leer Historia →"
    },
    "ar": {
        "l_tag": "تجربة", "l_title": "جولة على الجمال وقت الغروب في أكافاي: ماذا تتوقع", "l_excerpt": "الصمت قبل الغروب في الصحراء ليس فارغاً — بل هو مليء بالحياة. دليلنا الميداني حول ما يجب أن يفهمه كل مسافر قبل ركوب الجمل في جولة أصيلة عند الغروب.", "l_date": "أغسطس 2026 · 5 دقائق", "l_read": "اقرأ القصة ←",
        "r_tag": "ثقافة وتراث", "r_title": "التراث الأمازيغي وأكافاي: ثقافة تسبق السياحة", "r_excerpt": "قبل وقت طويل من وصول المخيمات الصحراوية الحديثة، كانت تلال أكافاي الحجرية تحتضن مجتمعات أمازيغية لا تزال هندستها المعمارية الحجرية وطقوس الضيافة الخاصة بها باقية حتى اليوم.", "r_date": "يوليو 2026 · 6 دقائق", "r_read": "اقرأ القصة ←"
    }
}

for lang, data in languages.items():
    filepath = f"{lang}/blog/index.html"
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    css_to_replace_regex = r'/\*\s*─── FRAMELESS DUO ───\s*\*/.*?(?=\/\*\s*─── FRAMELESS QUOTE ───\s*\*/)'
    new_css = """/* ─── FRAMELESS DUO (REFINED) ─── */
    .story-duo { 
      display: grid; 
      grid-template-columns: 1.15fr 0.85fr;
      gap: 80px; 
      align-items: start;
      margin-top: 24px;
    }

    .story-card { display: flex; flex-direction: column; text-decoration: none; color: inherit; }
    .story-card:hover { text-decoration: none; color: inherit; }

    .story-card--primary .story-card__media { aspect-ratio: 4/5; margin-bottom: 32px; }
    .story-card--primary .story-card__title { font-size: clamp(2rem, 3vw, 2.4rem); line-height: 1.1; }

    .story-card--secondary { margin-top: 160px; }
    .story-card--secondary .story-card__media { aspect-ratio: 4/3; margin-bottom: 28px; }
    .story-card--secondary .story-card__title { font-size: clamp(1.6rem, 2vw, 1.8rem); line-height: 1.15; }

    .story-card__media { overflow: hidden; position: relative; }
    .story-card__media img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.8s cubic-bezier(0.4, 0, 0.2, 1); }
    .story-card:hover .story-card__media img { transform: scale(1.03); }

    .story-card__tag { font-size: 11px; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: #523225; margin-bottom: 16px; display: block; }
    .story-card__title { font-weight: 700; letter-spacing: -0.02em; color: #272724; margin: 0 0 16px; font-family: 'Clash Grotesk', sans-serif; }
    .story-card__excerpt { font-size: 1.1rem; line-height: 1.65; color: #4e4e48; margin: 0 0 32px; }
    .story-card__footer { display: flex; align-items: center; justify-content: space-between; padding-top: 18px; border-top: 1px solid rgba(39, 39, 36, 0.15); font-size: 12.5px; font-weight: 500; color: #7a756e; }
    .story-card__read { font-weight: 700; color: #272724; text-transform: uppercase; letter-spacing: 0.08em; transition: color 0.2s; }
    .story-card:hover .story-card__read { color: #523225; }

    @media (max-width: 1024px) {
      .story-duo { grid-template-columns: 1fr; gap: 60px; }
      .story-card--secondary { margin-top: 0; }
      .story-card--primary .story-card__media { aspect-ratio: 16/10; }
    }
    """
    
    content = re.sub(css_to_replace_regex, new_css, content, flags=re.DOTALL)
    
    new_duo_html = f"""<div class="story-duo">
          <a href="agafay-camel-ride.html" class="story-card story-card--primary" data-category="experience">
            <div class="story-card__media">
              <img src="/images/Slider-images/slider-3.webp" alt="Sunset Camel Ride in Agafay" loading="lazy" decoding="async" />
            </div>
            <span class="story-card__tag">{data['l_tag']}</span>
            <h3 class="story-card__title">{data['l_title']}</h3>
            <p class="story-card__excerpt">{data['l_excerpt']}</p>
            <div class="story-card__footer">
              <span>{data['l_date']}</span>
              <span class="story-card__read">{data['l_read']}</span>
            </div>
          </a>

          <a href="berber-culture-agafay.html" class="story-card story-card--secondary" data-category="culture">
            <div class="story-card__media">
              <img src="/images/Slider-images/slider-4.webp" alt="Berber heritage and culture in Agafay" loading="lazy" decoding="async" />
            </div>
            <span class="story-card__tag">{data['r_tag']}</span>
            <h3 class="story-card__title">{data['r_title']}</h3>
            <p class="story-card__excerpt">{data['r_excerpt']}</p>
            <div class="story-card__footer">
              <span>{data['r_date']}</span>
              <span class="story-card__read">{data['r_read']}</span>
            </div>
          </a>
        </div>"""

    content = re.sub(r'<div class="story-duo">.*?</div>\s*</section>', new_duo_html + '\n      </div>\n    </section>', content, flags=re.DOTALL)
        
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully redesigned Curator's Selection in {filepath}")
