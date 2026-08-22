import glob
import re

# Localized strings for the new CTA component
cta_content = {
    "en": {
        "eyebrow": "✦ Curated Desert Experience",
        "badge": "Private VIP",
        "perk1": "Private Marrakech Hotel Transfer",
        "perk2": "Certified Local Expert Guide",
        "perk3": "100% Tailored Private Route",
        "btn": "Explore All Packs",
        "whatsapp": "Instant WhatsApp Booking",
        "wa_text": "Hello Marragafay, I am reading your Journal and would like to inquire about booking a private desert experience."
    },
    "fr": {
        "eyebrow": "✦ Expérience Désert Sur Mesure",
        "badge": "VIP Privé",
        "perk1": "Transfert Privé depuis Marrakech Inclus",
        "perk2": "Guide Local Expert & Certifié",
        "perk3": "Itinéraire 100% Privatisé",
        "btn": "Découvrir les Packs",
        "whatsapp": "Réservation Directe WhatsApp",
        "wa_text": "Bonjour Marragafay, je lis votre Revue et souhaite réserver une expérience privée dans le désert."
    },
    "es": {
        "eyebrow": "✦ Experiencia Exclusiva en el Desierto",
        "badge": "VIP Privado",
        "perk1": "Traslado Privado desde Marrakech Incluido",
        "perk2": "Guía Local Experto y Certificado",
        "perk3": "Ruta 100% Privada a Medida",
        "btn": "Explorar Todos los Paquetes",
        "whatsapp": "Reserva Directa por WhatsApp",
        "wa_text": "Hola Marragafay, estoy leyendo su Diario y me gustaría consultar sobre una experiencia privada en el desierto."
    },
    "ar": {
        "eyebrow": "✦ تجربة صحراوية استثنائية",
        "badge": "خدمة خاصة VIP",
        "perk1": "نقل خاص من وإلى مقر إقامتك بمراكش",
        "perk2": "مرشد محلي خبير ومعتمد",
        "perk3": "مسار خاص مخصص بالكامل",
        "btn": "استكشف كافة الباقات",
        "whatsapp": "حجز مباشر عبر واتساب",
        "wa_text": "مرحباً مراكافاي، أقرأ مقالكم في المجلة وأرغب في الاستفسار عن حجز تجربة صحراوية خاصة."
    }
}

new_cta_css = """
    /* ═══════════════════════════════════════════════
       IN-ARTICLE EXPERIENCE BOOKING INSET (REDESIGNED)
    ═══════════════════════════════════════════════ */
    .article-cta-box,
    .article-experience-inset {
      background: #181816 !important;
      border: 1px solid rgba(207, 189, 165, 0.2);
      border-radius: 12px;
      padding: 40px 38px;
      margin: 3.5rem 0;
      box-sizing: border-box;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.16);
      position: relative;
      overflow: hidden;
      text-align: left;
    }
    .article-cta-box::before,
    .article-experience-inset::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 3px;
      background: linear-gradient(90deg, #523225, #cfbda5, #523225);
    }
    .experience-inset__header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 16px;
    }
    .experience-inset__eyebrow {
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: #cfbda5;
    }
    .experience-inset__badge {
      font-size: 9.5px;
      font-weight: 700;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      background: rgba(207, 189, 165, 0.12);
      color: #cfbda5;
      padding: 4px 12px;
      border-radius: 100px;
      border: 1px solid rgba(207, 189, 165, 0.25);
    }
    .article-cta-box h3,
    .experience-inset__title {
      color: #F6F7EA !important;
      font-size: clamp(1.5rem, 2.5vw, 1.95rem);
      font-weight: 700;
      line-height: 1.18;
      letter-spacing: -0.02em;
      margin: 0 0 12px 0;
      font-family: 'Clash Grotesk', sans-serif !important;
    }
    .article-cta-box p,
    .experience-inset__desc {
      color: rgba(246, 247, 234, 0.8) !important;
      font-size: 15.5px;
      line-height: 1.65;
      margin: 0 0 22px 0;
      max-width: 680px;
    }
    .experience-inset__perks {
      display: flex;
      flex-wrap: wrap;
      gap: 10px 20px;
      margin-bottom: 26px;
      padding-bottom: 22px;
      border-bottom: 1px solid rgba(246, 247, 234, 0.08);
    }
    .inset-perk {
      display: inline-flex;
      align-items: center;
      gap: 7px;
      font-size: 12.5px;
      font-weight: 500;
      color: #cfbda5;
    }
    .inset-perk svg {
      color: #C69438;
      flex-shrink: 0;
    }
    .experience-inset__actions,
    .experience-inset__footer {
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 14px;
    }
    .article-cta-btn,
    .experience-inset__btn {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background-color: #523225 !important;
      color: #F6F7EA !important;
      font-size: 12.5px;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      text-decoration: none;
      padding: 13px 28px;
      border-radius: 100px;
      transition: all 0.25s ease;
      font-family: 'Clash Grotesk', sans-serif !important;
      border: 1px solid transparent;
    }
    .article-cta-btn:hover,
    .experience-inset__btn:hover {
      background-color: #3d241a !important;
      color: #F6F7EA !important;
      transform: translateY(-1px);
      box-shadow: 0 6px 18px rgba(82, 50, 37, 0.35);
    }
    .experience-inset__whatsapp {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(37, 211, 102, 0.1) !important;
      color: #25D366 !important;
      border: 1px solid rgba(37, 211, 102, 0.35);
      font-size: 12.5px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      text-decoration: none;
      padding: 12px 22px;
      border-radius: 100px;
      transition: all 0.25s ease;
      font-family: 'Clash Grotesk', sans-serif !important;
    }
    .experience-inset__whatsapp:hover {
      background: rgba(37, 211, 102, 0.2) !important;
      color: #25D366 !important;
      transform: translateY(-1px);
    }
"""

all_article_files = [f for f in glob.glob("*/blog/*.html") if not f.endswith("index.html")]

for filepath in all_article_files:
    lang = filepath.split("/")[0]
    t = cta_content[lang]

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update CSS
    if "/* ── In-Article Booking CTA ── */" in content:
        content = re.sub(
            r'/\*\s*──\s*In-Article Booking CTA\s*──\s*\*/.*?(?=/\*\s*──\s*Article Tags\s*──\s*\*/)',
            new_cta_css + "\n    ",
            content,
            flags=re.DOTALL
        )
    elif "/* ═══════════════════════════════════════════════\n       IN-ARTICLE EXPERIENCE BOOKING INSET" in content:
        content = re.sub(
            r'/\*\s*═══════════════════════════════════════════════\s*IN-ARTICLE EXPERIENCE BOOKING INSET.*?(?=/\*\s*──\s*Article Tags\s*──\s*\*/|\.article-tags-wrap)',
            new_cta_css + "\n    ",
            content,
            flags=re.DOTALL
        )

    # 2. Extract existing title & desc from the old HTML
    old_cta_match = re.search(r'<div class="(article-cta-box|article-experience-inset)">\s*<h3>(.*?)</h3>\s*<p>(.*?)</p>.*?(<a.*?</a>)\s*</div>', content, flags=re.DOTALL)
    
    if old_cta_match:
        current_title = old_cta_match.group(2).strip()
        current_desc = old_cta_match.group(3).strip()
        
        # Build the new luxury HTML component
        new_html = f"""<div class="article-experience-inset">
        <div class="experience-inset__header">
          <span class="experience-inset__eyebrow">{t['eyebrow']}</span>
          <span class="experience-inset__badge">{t['badge']}</span>
        </div>
        <h3 class="experience-inset__title">{current_title}</h3>
        <p class="experience-inset__desc">{current_desc}</p>
        
        <div class="experience-inset__perks">
          <span class="inset-perk">
            <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
            {t['perk1']}
          </span>
          <span class="inset-perk">
            <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
            {t['perk2']}
          </span>
          <span class="inset-perk">
            <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
            {t['perk3']}
          </span>
        </div>

        <div class="experience-inset__actions">
          <a href="/{lang}/packs" class="experience-inset__btn">
            <span>{t['btn']}</span>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
          </a>
          <a href="https://wa.me/212672531624?text={t['wa_text']}" target="_blank" class="experience-inset__whatsapp">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.771-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.312.045-.694.072-2.148-.526-1.857-.764-3.045-2.658-3.137-2.781-.092-.123-.75-1-.75-1.909 0-.909.477-1.355.646-1.541.17-.186.371-.233.495-.233.124 0 .248.002.355.008.113.006.264-.043.413.315.155.371.531 1.298.577 1.391.046.093.078.202.015.326-.062.124-.093.202-.186.311-.093.109-.196.243-.28.326-.093.093-.19.195-.082.381.109.186.482.795 1.034 1.286.711.633 1.31.829 1.496.922.186.093.295.078.404-.046.11-.124.466-.543.59-.729.124-.186.249-.155.419-.093.17.062 1.084.511 1.27.604.186.093.31.14.356.217.047.078.047.45-.097.855z"/></svg>
            <span>{t['whatsapp']}</span>
          </a>
        </div>
      </div>"""

        content = re.sub(r'<div class="(article-cta-box|article-experience-inset)">.*?</div>\s*(?=<h2|<p|<div|<section|<!--)', new_html + "\n\n      ", content, flags=re.DOTALL)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Redesigned CTA in {filepath}")
    else:
        print(f"Could not find CTA block in {filepath}")

print("Completed in-article CTA redesign across all 28 articles!")
