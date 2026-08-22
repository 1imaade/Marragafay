import re

about_copy = {
    "en": {
        "hero_sub": "Marragafay was founded with a clear standard: extraordinary desert landscapes deserve uncompromising safety, modern certified vehicles, and genuine local hospitality. We operate exclusively where the Agafay stone plateau meets the High Atlas horizon.",
        "section_title": "curated encounters in the stone plateau",
        "desc1": "Based in Marrakech and operating directly in the Agafay stone desert, Marragafay provides bespoke, private desert experiences designed for travelers who value safety, punctuality, and authentic Berber hospitality.",
        "desc2": "From private door-to-door Marrakech hotel transfers in air-conditioned 4x4s to high-performance quad fleets and gourmet fireside dinners under the stars, every moment is curated with personal attention and complete transparency.",
        "cta": "Explore our experiences"
    },
    "fr": {
        "hero_sub": "Marragafay est né d'une exigence simple : offrir une expérience d'exception dans le désert d'Agafay sans aucun compromis sur la sécurité, la qualité des véhicules et l'authenticité de l'accueil local.",
        "section_title": "des moments d'exception dans le désert de pierre",
        "desc1": "Basé à Marrakech et présent directement dans le désert d'Agafay, Marragafay conçoit des escapades privées sur-mesure pour les voyageurs en quête d'aventure raffinée et d'hospitalité berbère authentique.",
        "desc2": "Des transferts privés porte-à-porte en 4x4 climatisés aux flottes de quads et buggys récents, en passant par les dîners gastronomiques sous les étoiles, chaque détail est orchestré avec rigueur et totale transparence.",
        "cta": "Découvrir nos expériences"
    },
    "es": {
        "hero_sub": "Marragafay nació con un estándar claro: ofrecer una experiencia extraordinaria en el desierto de piedra de Agafay con total seguridad, vehículos de última generación y la auténtica hospitalidad bereber.",
        "section_title": "experiencias exclusivas en la meseta de piedra",
        "desc1": "Con sede en Marrakech y operaciones directas en el desierto de Agafay, Marragafay diseña excursiones privadas y personalizadas para viajeros que buscan aventura, confort y total tranquilidad.",
        "desc2": "Desde traslados privados puerta a puerta en 4x4 con aire acondicionado hasta modernas flotas de quads y cenas gastronómicas junto al fuego bajo las estrellas, cuidamos cada detalle con total transparencia.",
        "cta": "Explorar nuestras experiencias"
    },
    "ar": {
        "hero_sub": "تأسست مراكافاي بمعايير دقيقة: تقديم تجارب صحراوية استثنائية في أكافاي دون أي مساومة على معايير السلامة، جودة الآليات الحديثة، وأصالة الضيافة الأمازيغية العريقة.",
        "section_title": "تجارب خاصة وفاخرة في قلب الصحراء الصخرية",
        "desc1": "انطلاقاً من مراكش وبحضور مباشر في صحراء أكافاي، توفر مراكافاي رحلات وجولات خاصة مصممة للباحثين عن المغامرة الراقية، الالتزام التام بالمواعيد، والراحة المطلقة.",
        "desc2": "من النقل الخاص ذهاباً وإياباً بسيارات 4x4 مريحة ومكيفة، إلى أحدث الدراجات الرباعية (كواد وبوغي) ووجبات العشاء الفاخرة تحت قبة النجوم، نعتني بأدق التفاصيل بكل شفافية ومصداقية.",
        "cta": "استكشف تجاربنا"
    }
}

for lang in ["en", "fr", "es", "ar"]:
    fpath = f"{lang}/about.html"
    d = about_copy[lang]
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update hero subtitle
    html = re.sub(
        r'<p class="text-white/80 max-w-xl text-\[16px\] md:text-\[18px\] leading-\[28px\]"[^>]*>.*?</p>',
        f'<p class="text-white/80 max-w-xl text-[16px] md:text-[18px] leading-[28px]" style="font-family: \'Lay Grotesk\', sans-serif;">{d["hero_sub"]}</p>',
        html,
        flags=re.DOTALL,
        count=1
    )

    # 2. Update brutalist title and desc
    html = re.sub(
        r'<h2 class="brutalist-title">.*?</h2>',
        f'<h2 class="brutalist-title">{d["section_title"]}</h2>',
        html,
        flags=re.DOTALL
    )

    desc_block = f"""<div class="brutalist-desc-wrapper">
            <p class="brutalist-desc">
              {d["desc1"]}
            </p>
            <p class="brutalist-desc">
              {d["desc2"]}
            </p>
          </div>"""

    html = re.sub(
        r'<div class="brutalist-desc-wrapper">.*?</div>',
        desc_block,
        html,
        flags=re.DOTALL
    )

    html = re.sub(
        r'<a href="[^"]*" class="brutalist-cta">.*?</a>',
        f'<a href="/{lang}/activities" class="brutalist-cta">{d["cta"]} <span class="brutalist-cta-icon"><svg class="w-4 h-4 ml-1 inline-block fill-current" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"/></svg></span></a>',
        html,
        flags=re.DOTALL
    )

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Polished copy in {fpath}")

print("About page copy polished across all languages!")
