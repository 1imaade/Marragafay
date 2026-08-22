import re
import os

article_cta_targets = {
    "agafay-desert-guide.html": {
        "en": ("/en/packages/comfort", "Explore Signature Desert Tour →"),
        "fr": ("/fr/packages/comfort", "Découvrir l'Excursion Signature →"),
        "es": ("/es/packages/comfort", "Ver Excursión Signature →"),
        "ar": ("/ar/packages/comfort", "← اكتشف رحلة سيغنتشر المتكاملة")
    },
    "agafay-camel-ride.html": {
        "en": ("/en/activities/camel-ride", "Book Sunset Camel Ride →"),
        "fr": ("/fr/activities/camel-ride", "Réserver la Balade en Dromadaire →"),
        "es": ("/es/activities/camel-ride", "Reservar Paseo en Camello →"),
        "ar": ("/ar/activities/camel-ride", "← احجز جولة ركوب الجمال")
    },
    "agafay-quad-biking-guide.html": {
        "en": ("/en/activities/quad-biking", "Book Quad Biking Tour →"),
        "fr": ("/fr/activities/quad-biking", "Réserver la Randonnée Quad →"),
        "es": ("/es/activities/quad-biking", "Reservar Tour en Quad →"),
        "ar": ("/ar/activities/quad-biking", "← احجز مغامرة الكواد")
    },
    "agafay-dinner-experience.html": {
        "en": ("/en/activities/dinner-show", "Book Desert Dinner & Show →"),
        "fr": ("/fr/activities/dinner-show", "Réserver le Dîner Spectacle →"),
        "es": ("/es/activities/dinner-show", "Reservar Cena y Espectáculo →"),
        "ar": ("/ar/activities/dinner-show", "← احجز عشاء وسهرة أكافاي")
    },
    "marrakech-to-agafay.html": {
        "en": ("/en/packages/luxe", "Explore Private VIP Tour with Pickup →"),
        "fr": ("/fr/packages/luxe", "Découvrir le Pack VIP avec Chauffeur →"),
        "es": ("/es/packages/luxe", "Ver Tour Privado VIP con Recogida →"),
        "ar": ("/ar/packages/luxe", "← استكشف الباقة الخاصة VIP مع السائق")
    },
    "agafay-desert-vs-sahara.html": {
        "en": ("/en/packages/comfort", "Book Agafay Half-Day Tour →"),
        "fr": ("/fr/packages/comfort", "Réserver l'Excursion Demi-Journée →"),
        "es": ("/es/packages/comfort", "Reservar Excursión de Medio Día →"),
        "ar": ("/ar/packages/comfort", "← احجز رحلة نصف يوم إلى أكافاي")
    },
    "berber-culture-agafay.html": {
        "en": ("/en/packages/comfort", "Experience Agafay Culture & Dinner →"),
        "fr": ("/fr/packages/comfort", "Vivre l'Expérience & Dîner Nomade →"),
        "es": ("/es/packages/comfort", "Vivir la Experiencia y Cena Bereber →"),
        "ar": ("/ar/packages/comfort", "← عش أصالة الضيافة والعشاء البدوي")
    }
}

for filename, target_dict in article_cta_targets.items():
    for lang in ["en", "fr", "es", "ar"]:
        fpath = f"{lang}/blog/{filename}"
        if not os.path.exists(fpath):
            continue

        url, btn_text = target_dict[lang]

        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()

        # Update the article-cta-box button URL and Text
        html = re.sub(
            r'<a href="[^"]*" class="article-cta-btn">.*?</a>',
            f'<a href="{url}" class="article-cta-btn">{btn_text}</a>',
            html,
            count=1,
            flags=re.DOTALL
        )

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Connected targeted CTA in {fpath} -> {url}")

print("\nAll blog article CTAs successfully connected to their respective commercial Money Pages!")
