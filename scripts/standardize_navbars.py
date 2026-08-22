import re
import os
import glob

nav_definitions = {
    "en": {
        "lang_code": "en",
        "lang_name": "EN",
        "items": [
            ("Home", "/en/", "home"),
            ("Activities", "/en/activities", "activities"),
            ("Packs", "/en/packs", "packs"),
            ("About", "/en/about", "about"),
            ("Reviews", "/en/reviews", "reviews"),
            ("Journal", "/en/blog", "blog"),
            ("Contact", "/en/contact", "contact"),
            ("Booking", "/en/packs", "booking")
        ]
    },
    "fr": {
        "lang_code": "fr",
        "lang_name": "FR",
        "items": [
            ("Accueil", "/fr/", "home"),
            ("Activités", "/fr/activities", "activities"),
            ("Packs", "/fr/packs", "packs"),
            ("À Propos", "/fr/about", "about"),
            ("Avis", "/fr/reviews", "reviews"),
            ("La Revue", "/fr/blog", "blog"),
            ("Contact", "/fr/contact", "contact"),
            ("Réservation", "/fr/packs", "booking")
        ]
    },
    "es": {
        "lang_code": "es",
        "lang_name": "ES",
        "items": [
            ("Inicio", "/es/", "home"),
            ("Actividades", "/es/activities", "activities"),
            ("Paquetes", "/es/packs", "packs"),
            ("Sobre Nosotros", "/es/about", "about"),
            ("Reseñas", "/es/reviews", "reviews"),
            ("El Diario", "/es/blog", "blog"),
            ("Contacto", "/es/contact", "contact"),
            ("Reservar", "/es/packs", "booking")
        ]
    },
    "ar": {
        "lang_code": "ar",
        "lang_name": "AR",
        "items": [
            ("الرئيسية", "/ar/", "home"),
            ("الأنشطة", "/ar/activities", "activities"),
            ("الباقات", "/ar/packs", "packs"),
            ("من نحن", "/ar/about", "about"),
            ("التقييمات", "/ar/reviews", "reviews"),
            ("المجلة", "/ar/blog", "blog"),
            ("اتصل بنا", "/ar/contact", "contact"),
            ("الحجز", "/ar/packs", "booking")
        ]
    }
}

for lang in ["en", "fr", "es", "ar"]:
    nav_def = nav_definitions[lang]
    files = glob.glob(f"{lang}/**/*.html", recursive=True)

    for fpath in files:
        # Determine page type
        fname = os.path.basename(fpath).replace(".html", "")
        parent_dir = os.path.basename(os.path.dirname(fpath))
        
        page_type = "other"
        if fname == "index" and parent_dir == lang:
            page_type = "home"
        elif fname in ["activities", "packs", "about", "reviews", "contact"]:
            page_type = fname
        elif "blog" in fpath:
            page_type = "blog"
        elif "activities" in fpath:
            page_type = "activities"
        elif "packages" in fpath or "packs" in fpath:
            page_type = "packs"

        with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
            html = f.read()

        # Build nav links
        links_html = ""
        for label, url, item_key in nav_def["items"]:
            if item_key == "booking":
                links_html += f'\n          <li class="nav-item"><a href="{url}" class="nav-link booking-btn">{label}</a></li>'
            else:
                active_cls = ' active' if item_key == page_type else ''
                links_html += f'\n          <li class="nav-item{active_cls}"><a href="{url}" class="nav-link">{label}</a></li>'

        # Construct full standardized navbar
        full_navbar = f"""<nav style="height: var(--nav-height, 72px);" class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light" id="ftco-navbar">
    <div class="container">
      <a class="navbar-brand" href="/{lang}/"><img src="/images/logo-trensparent.webp" alt="Marragafay" style="width: 70px; height: 70px;" width="70" height="70"></a>
      <div class="mobile-language-switcher">
        <a href="#" class="language-toggle" id="languageDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          <i class="icon-globe"></i> <span>{nav_def['lang_name']}</span>
        </a>
        <div class="dropdown-menu dropdown-menu-right" aria-labelledby="languageDropdown">
          <a class="dropdown-item lang-option" href="#" data-lang="en">English</a>
          <a class="dropdown-item lang-option" href="#" data-lang="fr">Français</a>
          <a class="dropdown-item lang-option" href="#" data-lang="es">Español</a>
          <a class="dropdown-item lang-option" href="#" data-lang="ar" dir="rtl">العربية</a>
        </div>
      </div>
      <button class="navbar-toggler" type="button" aria-label="Toggle navigation">
        <span class="icon-menu"></span>
      </button>
      <div class="collapse navbar-collapse">
        <ul class="navbar-nav ml-auto">{links_html}
        </ul>
      </div>
    </div>
  </nav>"""

        # Replace navbar if present
        if "<nav" in html and "</nav>" in html:
            new_html = re.sub(r'<nav.*?</nav>', full_navbar, html, flags=re.DOTALL, count=1)
            if new_html != html:
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(new_html)
                print(f"Standardized navbar in {fpath} (active: {page_type})")

print("All navbars successfully standardized across all languages!")
