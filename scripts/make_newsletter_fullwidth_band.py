import re

languages = {
    "en": {
        "path": "en/blog/index.html",
        "eyebrow": "The Desert Letter",
        "headline": "Desert dispatches, delivered.",
        "subtext": "One monthly letter. No noise. Stories, field notes, and private seasonal offers from the stone desert.",
        "placeholder": "Enter your email address",
        "btn": "Subscribe",
        "note": "Zero spam. Unsubscribe with one click at any time."
    },
    "fr": {
        "path": "fr/blog/index.html",
        "eyebrow": "La Lettre du Désert",
        "headline": "Les nouvelles du désert, livrées chez vous.",
        "subtext": "Une lettre par mois. Récits, inspirations et offres privées depuis le désert d'Agafay.",
        "placeholder": "Votre adresse e-mail",
        "btn": "S'inscrire",
        "note": "Zéro spam. Désabonnement en un clic à tout moment."
    },
    "es": {
        "path": "es/blog/index.html",
        "eyebrow": "La Carta del Desierto",
        "headline": "Noticias del desierto, en tu bandeja.",
        "subtext": "Una carta al mes. Sin ruido. Historias, guías y ofertas exclusivas desde el desierto de piedra.",
        "placeholder": "Tu correo electrónico",
        "btn": "Suscribirse",
        "note": "Cero spam. Cancela la suscripción en cualquier momento."
    },
    "ar": {
        "path": "ar/blog/index.html",
        "eyebrow": "رسالة الصحراء",
        "headline": "قصص وتحديثات الصحراء في بريدك.",
        "subtext": "رسالة شهرية واحدة. قصص حصرية، تجارب فاخرة وعروض خاصة من صحراء أكافاي.",
        "placeholder": "أدخل بريدك الإلكتروني",
        "btn": "اشتراك",
        "note": "بدون إعلانات مزعجة. يمكنك إلغاء الاشتراك في أي وقت."
    }
}

new_css = """    /* Newsletter Section — Full-Width Band Flush to Footer */
    .newsletter-section {
      width: 100%;
      background-color: #EEF0E2 !important;
      padding: 96px 0 106px;
      margin: 0;
      border-top: 1px solid rgba(39, 39, 36, 0.08);
      box-sizing: border-box;
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
      box-shadow: 0 4px 16px rgba(39, 39, 36, 0.04);
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
    .newsletter-form__input::placeholder {
      color: #8e8e88;
    }
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
    @media (max-width: 640px) {
      .newsletter-form { flex-direction: column; border-radius: 8px; padding: 0; }
      .newsletter-form__input { width: 100%; padding: 14px 16px; border-bottom: 1px solid rgba(39,39,36,0.1) !important; }
      .newsletter-form__btn { width: 100%; border-radius: 0; padding: 14px 20px; }
      .newsletter-section { padding: 64px 0 72px; }
    }"""

for lang, data in languages.items():
    filepath = data["path"]
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace CSS
    content = re.sub(
        r'/\*\s*Newsletter Section.*?(?=\s*</style>)',
        new_css,
        content,
        flags=re.DOTALL
    )

    # HTML replacement
    new_html = f"""    <!-- NEWSLETTER (FULL-WIDTH BAND FLUSH TO FOOTER) -->
    <section class="newsletter-section">
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
        r'<!-- NEWSLETTER.*?-->\s*<section class="newsletter-wrap">.*?</section>',
        new_html,
        content,
        flags=re.DOTALL
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated newsletter section to full-width band in: {filepath}")

print("All language index pages updated!")
