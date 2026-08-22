import re

indexes = {
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

new_css = """    /* Newsletter Section — Contained Luxury Card */
    .newsletter-wrap { padding: 40px 0 100px; }
    .newsletter-card {
      background: #EEF0E2;
      border-radius: 6px;
      padding: 72px 48px;
      text-align: center;
      box-sizing: border-box;
      border: 1px solid rgba(39, 39, 36, 0.08);
    }
    .newsletter-eyebrow {
      display: inline-block;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.3em;
      text-transform: uppercase;
      color: #523225;
      margin-bottom: 18px;
    }
    .newsletter-headline {
      font-size: clamp(2rem, 4vw, 3.2rem);
      font-weight: 700;
      line-height: 1.1;
      letter-spacing: -0.025em;
      color: #272724;
      margin: 0 0 16px;
    }
    .newsletter-subtext {
      font-size: 1.05rem;
      line-height: 1.7;
      color: #5a5a54;
      max-width: 540px;
      margin: 0 auto 36px;
    }
    .newsletter-form {
      display: flex;
      gap: 0;
      max-width: 480px;
      margin: 0 auto;
      border: 1px solid rgba(39, 39, 36, 0.2);
      border-radius: 4px;
      overflow: hidden;
      background: #F6F7EA;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    }
    .newsletter-form__input {
      flex: 1;
      background: #F6F7EA !important;
      border: none !important;
      outline: none !important;
      padding: 16px 20px;
      font-size: 14px;
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
      padding: 16px 30px;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      cursor: pointer;
      font-family: 'Clash Grotesk', sans-serif !important;
      transition: background 0.2s ease;
      white-space: nowrap;
    }
    .newsletter-form__btn:hover {
      background-color: #523225 !important;
    }
    .newsletter-note {
      font-size: 12px;
      color: #7a756e;
      margin-top: 16px;
      letter-spacing: 0.02em;
    }"""

for lang, data in indexes.items():
    with open(data["path"], "r", encoding="utf-8") as f:
        content = f.read()

    # Replace CSS
    content = re.sub(
        r'/\*\s*Newsletter\s*\*/\s*\.newsletter-section\s*\{[^}]*\}.*?\.newsletter-note\s*\{[^}]*\}',
        new_css,
        content,
        flags=re.DOTALL
    )

    # HTML structure
    html_block = f"""    <!-- NEWSLETTER -->
    <section class="newsletter-wrap">
      <div class="journal-section">
        <div class="newsletter-card">
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
        r'<!-- NEWSLETTER -->\s*<section class="newsletter-section".*?</section>',
        html_block,
        content,
        flags=re.DOTALL
    )

    with open(data["path"], "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated newsletter section in: {data['path']}")

print("All newsletter sections updated to luxury contained card design.")
