import os
import re

# Import metadata from previous script
from generate_all_multilingual_articles import ui_translations, articles_meta

# Complete localized content body for each article in FR, ES, AR
articles_body = {
    "agafay-desert-guide.html": {
        "fr": """<h2>Qu'est-ce que le Désert d'Agafay ?</h2>
<p>Situé à seulement quarante-cinq minutes au sud-ouest de Marrakech, le désert d'Agafay n'est pas une étendue de dunes de sable doré comme le Sahara. Il s'agit d'un reg minéral — un plateau de pierre vallonné de plus de cent kilomètres carrés, composé d'argile compactée, de roches calcaires blanches et de collines sculptées par les vents de l'Atlas.</p>
<p>Cette topographie unique donne naissance à un paysage quasi lunaire où la lumière change radicalement d'heure en heure. Le matin, les collines arborent des teintes argentées et ocres douces. À midi, le soleil révèle l'immensité brute de la pierre. Mais c'est à l'heure dorée que la magie opère véritablement : le plateau entier s'embrase dans des nuances profondes d'ambre, de cuivre et de pourpre, avec les sommets enneigés du Haut Atlas en arrière-plan.</p>

<div class="article-key-takeaways">
  <h3>Points Clés pour Votre Visite</h3>
  <ul>
    <li><strong>Distance de Marrakech :</strong> Environ 35 à 45 kilomètres (40 à 50 minutes de route).</li>
    <li><strong>Nature du terrain :</strong> Désert de pierre, collines argileuses et canyons arides (pas de dunes de sable).</li>
    <li><strong>Meilleure période :</strong> D'octobre à mai pour des températures idéales ; toute l'année en soirée au coucher du soleil.</li>
    <li><strong>Accès :</strong> Accessible en véhicule standard jusqu'aux camps principaux ; 4x4 recommandé pour les pistes reculées.</li>
  </ul>
</div>

<h2>Pourquoi Choisir Agafay Plutôt que le Sahara ?</h2>
<p>La question se pose fréquemment pour les voyageurs découvrant le Maroc : faut-il consacrer trois jours de voyage pour atteindre les dunes de Merzouga ou de Zagora dans le Sahara, ou opter pour une escapade à Agafay ?</p>
<p>La réponse réside dans la gestion de votre temps et la recherche de sérénité. Rejoindre le Sahara exige au minimum 9 à 10 heures de route à travers les cols de montagne, imposant un séjour d'au moins deux à trois nuits. Le désert d'Agafay, quant à lui, offre une déconnexion totale et un dépaysement spectaculaire en moins d'une heure de trajet depuis la médina de Marrakech.</p>

<blockquote class="article-quote">
  « Le désert de pierre n'est pas un substitut au Sahara — c'est une entité géologique et esthétique à part entière. Une échappée intemporelle à portée de main. »
</blockquote>

<p>Agafay permet ainsi de vivre l'intensité du désert — balade en chameau, sensations en quad, dîner sous la voûte céleste et nuitée en camp de luxe — tout en retournant confortablement à votre riad le soir même ou le lendemain matin.</p>

<figure class="article-figure">
  <img src="/images/Slider-images/slider-2.webp" alt="Paysage minéral du désert d'Agafay au Maroc" loading="lazy" decoding="async" />
  <figcaption>Les crêtes minérales d'Agafay se découpent avec élégance devant la chaîne de l'Atlas.</figcaption>
</figure>

<h2>Les Meilleures Activités à Vivre à Agafay</h2>
<p>L'immensité du plateau offre un terrain de jeu privilégié pour des aventures raffinées :</p>
<ul>
  <li><strong>Balade en Chameau au Coucher du Soleil :</strong> Laissez le rythme lent de la caravane vous immerger dans le calme profond du désert alors que le ciel prend des teintes orangées.</li>
  <li><strong>Randonnée en Quad et Buggy 4x4 :</strong> Pour les amateurs de sensations fortes, pilotez à travers des pistes sinueuses, des lits de rivières asséchées et des belvédères panoramiques inaccessibles en voiture.</li>
  <li><strong>Dîner Privé sous les Étoiles :</strong> Dégustez une cuisine marocaine gastronomique éclairée à la bougie, bercée par les mélodies traditionnelles au coin du feu.</li>
  <li><strong>Vols en Parapente et Montgolfière :</strong> Admirez l'incroyable géométrie du plateau vue du ciel aux premières lueurs de l'aube.</li>
</ul>

<div class="article-cta-box">
  <h3>Vivez l'Expérience Agafay avec Marragafay</h3>
  <p>Dîners privés, aventures personnalisées en quad et balades au coucher du soleil — conçus sur mesure pour une expérience inoubliable.</p>
  <a href="/fr/activities" class="article-cta-btn">
    Explorer les Expériences
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
  </a>
</div>

<h2>Conseils Pratiques : Que Porter et Comment Venir ?</h2>
<p>Pour profiter pleinement de votre excursion, prévoyez des vêtements confortables adaptés aux variations thermiques. En journée, le soleil tape fort : lunettes de soleil UV, chapeau et crème solaire sont indispensables. En soirée, la température chute rapidement dans le désert : apportez toujours une veste chaude ou une étole.</p>
<p>Marragafay organise l'ensemble de votre logistique avec des chauffeurs privés et des véhicules haut de gamme assurant votre prise en charge directe depuis votre hôtel ou riad à Marrakech.</p>""",

        "es": """<h2>¿Qué es el Desierto de Agafay?</h2>
<p>Ubicado a tan solo cuarenta y cinco minutos al suroeste de Marrakech, el desierto de Agafay no es una extensión de dunas de arena dorada como el Sahara. Se trata de un desierto mineral o "reg": una meseta ondulada de más de cien kilómetros cuadrados compuesta de arcilla blanca, piedras calizas y colinas esculpidas por los vientos del Atlas.</p>
<p>Esta topografía singular crea un paisaje casi lunar donde la luz transforma el entorno minuto a minuto. Por la mañana, las colinas adquieren tonos plateados y ocres suaves. Al mediodía, el sol resalta la inmensidad pura de la piedra. Pero es durante la hora dorada cuando surge la verdadera magia: todo el desierto se enciende en intensos tonos ámbar, bronce y púrpura, con las cumbres nevadas del Alto Atlas como telón de fondo.</p>

<div class="article-key-takeaways">
  <h3>Puntos Clave para tu Visita</h3>
  <ul>
    <li><strong>Distancia desde Marrakech:</strong> Entre 35 y 45 kilómetros (40 a 50 minutos de viaje).</li>
    <li><strong>Naturaleza del terreno:</strong> Desierto de piedra, colinas arcillosas y cañones áridos (sin dunas de arena).</li>
    <li><strong>Mejor época:</strong> De octubre a mayo para un clima templado; todo el año durante el atardecer y la noche.</li>
    <li><strong>Acceso:</strong> Vehículo estándar apto para los accesos principales; se recomienda 4x4 para rutas exclusivas.</li>
  </ul>
</div>

<h2>¿Por qué Elegir Agafay en Lugar del Sahara?</h2>
<p>Una pregunta frecuente entre los viajeros que visitan Marruecos es si vale la pena dedicar tres días para viajar hasta las dunas de Merzouga o Zagora en el Sahara, o si es mejor optar por una experiencia en Agafay.</p>
<p>La clave radica en el tiempo y la comodidad. Llegar al Sahara requiere al menos 9 o 10 horas de trayecto en coche cruzando puertos de montaña, lo que exige un viaje mínimo de dos o tres noches. El desierto de Agafay, por el contrario, ofrece una desconexión total y un entorno desértico impactante a menos de una hora de la medina de Marrakech.</p>

<blockquote class="article-quote">
  «El desierto de piedra no es un sustituto del Sahara: es un ecosistema estético y geológico único. Una desconexión atemporal al alcance de la mano.»
</blockquote>

<p>Agafay permite disfrutar de paseos en camello, adrenalina en quad, cenas gourmet a la luz de las velas y noches en campamentos de lujo sin perder valiosos días de viaje en carretera.</p>

<figure class="article-figure">
  <img src="/images/Slider-images/slider-2.webp" alt="Paisaje mineral del desierto de Agafay en Marruecos" loading="lazy" decoding="async" />
  <figcaption>Las colinas minerales de Agafay con la imponente cordillera del Atlas al fondo.</figcaption>
</figure>

<h2>Las Mejores Actividades en Agafay</h2>
<p>La inmensidad de la meseta ofrece un escenario perfecto para vivir aventuras inolvidables:</p>
<ul>
  <li><strong>Paseo en Camello al Atardecer:</strong> Disfruta del ritmo pausado de la caravana mientras el cielo se tiñe de colores rojizos y dorados.</li>
  <li><strong>Rutas en Quad y Buggy 4x4:</strong> Recorre cañones, lechos de ríos secos y miradores panorámicos inaccesibles para vehículos convencionales.</li>
  <li><strong>Cena Privada bajo las Estrellas:</strong> Degusta alta gastronomía marroquí a la luz de las velas, acompañada de música tradicional junto a la hoguera.</li>
  <li><strong>Vuelo en Globo y Parapente:</strong> Contempla la geometría del desierto desde las alturas al amanecer.</li>
</ul>

<div class="article-cta-box">
  <h3>Vive la Experiencia Agafay con Marragafay</h3>
  <p>Cenas privadas en el desierto, rutas personalizadas en quad y paseos en camello al atardecer, organizados a tu medida.</p>
  <a href="/es/activities" class="article-cta-btn">
    Explorar Experiencias
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
  </a>
</div>

<h2>Consejos Prácticos: Qué Llevar y Cómo Llegar</h2>
<p>Para disfrutar al máximo de tu visita, viste ropa cómoda y adecuada para los cambios de temperatura. Durante el día es esencial protegerse del sol con gafas UV, sombrero y crema solar. Por la noche, las temperaturas descienden notablemente, por lo que es imprescindible llevar una chaqueta o abrigo ligero.</p>
<p>Marragafay se encarga de toda la logística con traslados privados de alta gama directamente desde tu hotel o riad en Marrakech.</p>""",

        "ar": """<h2>ما هي صحراء أكافاي الحجرية؟</h2>
<p>تقع صحراء أكافاي على بعد 45 دقيقة فقط جنوب غرب مراكش، وهي ليست صحراء ذات كثبان رملية ممتدة مثل الصحراء الكبرى، بل هي هضبة صخرية فريدة تمتد على مساحة تزيد عن 100 كيلومتر مربع، وتتألف من تلال جيرية بيضاء وتربة طينية نحتتها الرياح القادمة من جبال الأطلس.</p>
<p>تمنح هذه الطبيعة الجغرافية لأكافاي طابعاً قمرياً ساحراً تتغير ألوانه على مدار ساعات اليوم. في الصباح، تكتسي التلال بظلال فضية وذهبية ناعمة، بينما تكشف شمس الظهيرة عن صفاء الأحجار وهيبتها. ومع حلول ساعة الغروب، تبدأ اللوحة الأجمل حين تتوهج الصحراء بألوان العنبر والبرونز، مع إطلالة بانورامية ساحرة على قمم جبال الأطلس الشاهقة.</p>

<div class="article-key-takeaways">
  <h3>حقائق أساسية لزيارتك</h3>
  <ul>
    <li><strong>المسافة من مراكش:</strong> حوالي 35 إلى 45 كيلومتراً (40 إلى 50 دقيقة بالسيارة).</li>
    <li><strong>طبيعة التضاريس:</strong> صحراء حجرية، تلال طينية ووديان جافة (بدون كثبان رملية).</li>
    <li><strong>أفضل وقت للزيارة:</strong> من أكتوبر إلى مايو للطقس المعتدل، وطوال العام خلال ساعات المساء والغروب.</li>
    <li><strong>خيارات الوصول:</strong> يمكن الوصول بالسيارة العادية للمخيمات الرئيسية، ويفضل سيارات الدفع الرباعي للمسارات الوعرة.</li>
  </ul>
</div>

<h2>لماذا يفضل المسافرون صحراء أكافاي؟</h2>
<p>غالباً ما يواجه زوار المغرب خياراً بين قضاء ثلاثة أيام للوصول إلى كثبان مرزوكة في الصحراء الكبرى، أو اختيار رحلة يومية فاخرة إلى أكافاي.</p>
<p>تكمن الميزة الكبرى في كسب الوقت؛ فالوصول إلى الصحراء الكبرى يتطلب قيادة لأكثر من 9 ساعات عبر منعرجات الجبال، بينما تمنحك أكافاي عزلة تامة وتجربة صحراوية متكاملة في أقل من ساعة واحدة فقط من قلب مراكش.</p>

<blockquote class="article-quote">
  «صحراء أكافاي ليست بديلاً عن الصحراء الكبرى، بل هي تجربة جيولوجية وجمالية قائمة بذاتها. رحلة هادئة تأخذك خارج حدود الزمن.»
</blockquote>

<p>تتيح لك أكافاي الاستمتاع بكافة الأنشطة الصحراوية — من ركوب الجمال، قيادة الدراجات الرباعية، وتناول عشاء فاخر تحت النجوم في مخيمات راقية — مع إمكانية العودة المريحة إلى فندقك في نفس الليلة.</p>

<figure class="article-figure">
  <img src="/images/Slider-images/slider-2.webp" alt="مشهد بانورامي لصحراء أكافاي الحجرية بالمغرب" loading="lazy" decoding="async" />
  <figcaption>تلال أكافاي الحجرية الممتدة مع خلفية جبال الأطلس الساحرة.</figcaption>
</figure>

<h2>أبرز الأنشطة والتجارب في أكافاي</h2>
<p>توفر مساحات أكافاي الشاسعة خيارات متنوعة لعشاق المغامرة والفخامة:</p>
<ul>
  <li><strong>جولات الجمال وقت الغروب:</strong> عِش هدوء الصحراء الأصيل على خطى القوافل التقليدية بينما تتلون السماء بألوان الغروب.</li>
  <li><strong>مغامرات الكواد وسيارات البوغي:</strong> انطلق عبر المسارات الحجرية والوديان الجافة لاكتشاف إطلالات بانورامية لا تصلها السيارات العادية.</li>
  <li><strong>عشاء خاص تحت ضوء النجوم:</strong> تذوق أشهى أطباق المطبخ المغربي الفاخر على ضوء الشموع مع موسيقى تقليدية هادئة حول الموقد.</li>
  <li><strong>المنطاد الهوائي والباراغليدينغ:</strong> شاهد سحر تشكيلات الصحراء من الأعالي مع شروق الشمس.</li>
</ul>

<div class="article-cta-box">
  <h3>عش تجربة أكافاي الفاخرة مع مراكافاي</h3>
  <p>عشاء صحراوي خاص، مغامرات مخصصة، وجولات وقت الغروب مصممة لتلبي أعلى معايير الرفاهية.</p>
  <a href="/ar/activities" class="article-cta-btn">
    استكشف التجارب
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
  </a>
</div>

<h2>إرشادات عملية: ماذا ترتدي وكيف تصل؟</h2>
<p>نوصي بارتداء ملابس مريحة مناسبة للتغيرات الحرارية. في النهار، احرص على استخدام واقي الشمس، النظارات الشمسية والقبعة. وفي المساء، تنخفض درجات الحرارة في الصحراء بسرعة، لذا يُنصح دائماً بإحضار سترة دافئة.</p>
<p>تتولى مراكافاي كافة الترتيبات اللوجستية عبر سيارات فاخرة وسائقين محترفين مع خدمة التوصيل المباشر من وإلى مقر إقامتك في مراكش.</p>"""
    }
}

# Template builder function
def build_article_html(lang, filename, meta, body_content):
    t = ui_translations[lang]
    m = meta[lang]
    slug = meta["slug"]
    image = meta["image"]
    date_iso = meta["date"]
    read_time = meta["read_time"]

    # Direction and font
    is_rtl = (lang == "ar")
    dir_attr = ' dir="rtl"' if is_rtl else ''
    rtl_css = """
    body { direction: rtl; text-align: right; }
    .breadcrumb-nav { flex-direction: row-reverse; justify-content: flex-end; }
    .breadcrumb-nav .sep { transform: scaleX(-1); }
    .share-buttons { margin-right: auto; margin-left: 0; }
    .article-cta-btn svg { transform: scaleX(-1); }
    .related-card-arrow svg { transform: scaleX(-1); }
    .related-articles-header { flex-direction: row-reverse; }
    .cover-story__cta { flex-direction: row-reverse; }
    .curator-row__meta { flex-direction: row-reverse; }
    .field-card__footer { flex-direction: row-reverse; }
    """ if is_rtl else ""

    # Breadcrumbs
    breadcrumb_current = m["title"]
    breadcrumb_cat = m["category"]

    # Navbar links
    nav = t["nav_links"]

    # 3 Related Articles (picking from other articles in the collection)
    other_slugs = [k for k in articles_meta.keys() if k != filename][:3]
    related_cards_html = ""
    for r_filename in other_slugs:
        r_meta = articles_meta[r_filename]
        r_m = r_meta[lang]
        related_cards_html += f"""
        <!-- Related Card -->
        <a class="related-card" href="{r_filename}">
          <div class="related-card-img-wrap">
            <img
              src="{r_meta['image']}"
              alt="{r_m['title']}"
              width="420"
              height="260"
              loading="lazy"
              decoding="async"
            >
          </div>
          <div class="related-card-body">
            <p class="related-card-cat">{r_m['category']}</p>
            <h3 class="related-card-title">{r_m['title']}</h3>
            <p class="related-card-meta">{r_m['date_str']} · {r_meta['read_time']} {t['read_time_suffix']}</p>
            <span class="related-card-arrow" aria-hidden="true">
              {t['read_article']}
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
            </span>
          </div>
        </a>"""

    html = f"""<!DOCTYPE html>
<html lang="{t['lang_code']}"{dir_attr}>

<head>
  <!-- HREFLANG -->
  <link rel="alternate" hreflang="en" href="https://marragafay.com/en/blog/{slug}" />
  <link rel="alternate" hreflang="fr" href="https://marragafay.com/fr/blog/{slug}" />
  <link rel="alternate" hreflang="es" href="https://marragafay.com/es/blog/{slug}" />
  <link rel="alternate" hreflang="ar" href="https://marragafay.com/ar/blog/{slug}" />
  <link rel="alternate" hreflang="x-default" href="https://marragafay.com/blog/{slug}" />

  <!-- DELAYED GTM / ANALYTICS -->
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());

    document.addEventListener('DOMContentLoaded', function() {{
      setTimeout(function() {{
        var adsScript = document.createElement('script');
        adsScript.async = true;
        adsScript.src = 'https://www.googletagmanager.com/gtag/js?id=AW-18107593090';
        document.head.appendChild(adsScript);
        gtag('config', 'AW-18107593090');

        var gaScript = document.createElement('script');
        gaScript.async = true;
        gaScript.src = 'https://www.googletagmanager.com/gtag/js?id=G-RSQ34QQFT0';
        document.head.appendChild(gaScript);
        gtag('config', 'G-RSQ34QQFT0');

        (function (w, d, s, l, i) {{
          w[l] = w[l] || []; w[l].push({{
            'gtm.start': new Date().getTime(), event: 'gtm.js'
          }});
          var f = d.getElementsByTagName(s)[0],
              j = d.createElement(s),
              dl = l != 'dataLayer' ? '&l=' + l : '';
          j.async = true;
          j.src = 'https://www.googletagmanager.com/gtag/js?id=' + i + dl;
          f.parentNode.insertBefore(j, f);
        }})(window, document, 'script', 'dataLayer', 'GTM-PK8G4JC2');
      }}, 2000);
    }});
  </script>

  <!-- SEO META -->
  <title>{m['title']} | Marragafay {t['journal']}</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="{m['meta_desc']}">
  <meta name="author" content="{t['author']}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://marragafay.com/{lang}/blog/{slug}">

  <!-- Open Graph -->
  <meta property="og:title" content="{m['title']} | Marragafay {t['journal']}">
  <meta property="og:description" content="{m['meta_desc']}">
  <meta property="og:image" content="https://marragafay.com{image}">
  <meta property="og:url" content="https://marragafay.com/{lang}/blog/{slug}">
  <meta property="og:type" content="article">
  <meta property="article:published_time" content="{date_iso}T00:00:00Z">
  <meta property="article:author" content="{t['author']}">
  <meta property="article:section" content="{m['category']}">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{m['title']} | Marragafay {t['journal']}">
  <meta name="twitter:description" content="{m['meta_desc']}">
  <meta name="twitter:image" content="https://marragafay.com{image}">

  <!-- SCHEMA JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{m['title']}",
    "author": {{ "@type": "Organization", "name": "Marragafay" }},
    "publisher": {{
      "@type": "Organization",
      "name": "Marragafay",
      "logo": {{ "@type": "ImageObject", "url": "https://marragafay.com/images/logo/logo-high-res.webp" }}
    }},
    "datePublished": "{date_iso}",
    "dateModified": "2026-08-22",
    "image": "https://marragafay.com{image}",
    "description": "{m['meta_desc']}",
    "inLanguage": "{lang}",
    "url": "https://marragafay.com/{lang}/blog/{slug}",
    "mainEntityOfPage": {{
      "@type": "WebPage",
      "@id": "https://marragafay.com/{lang}/blog/{slug}"
    }}
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{ "@type": "ListItem", "position": 1, "name": "{t['home']}", "item": "https://marragafay.com/{lang}/" }},
      {{ "@type": "ListItem", "position": 2, "name": "{t['journal']}", "item": "https://marragafay.com/{lang}/blog" }},
      {{ "@type": "ListItem", "position": 3, "name": "{m['category']}", "item": "https://marragafay.com/{lang}/blog" }},
      {{ "@type": "ListItem", "position": 4, "name": "{m['title']}", "item": "https://marragafay.com/{lang}/blog/{slug}" }}
    ]
  }}
  </script>

  <!-- FONTS -->
  <link rel="preconnect" href="https://cdn.fontshare.com" crossorigin>
  <link rel="preload" href="https://api.fontshare.com/v2/css?f[]=clash-grotesk@200,300,400,500,600,700&display=swap" as="style" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=clash-grotesk@200,300,400,500,600,700&display=swap"></noscript>

  <!-- LCP Image Preload -->
  <link rel="preload" as="image" href="{image}" type="image/webp" fetchpriority="high">

  <!-- CSS -->
  <link rel="stylesheet" href="/css/vendor-bundle.css">
  <link rel="stylesheet" href="/css/custom-bundle.css">
  <link rel="stylesheet" href="/css/style.css">
  <link rel="stylesheet" href="/css/navbar-stayhere.css">
  <link rel="stylesheet" href="/css/tailwind-built.css">

  <!-- CRITICAL INLINE NAVBAR CSS -->
  <style id="critical-navbar-stayhere-inline">:root{{--nav-bg:transparent;--nav-bg-scrolled:#F6F7EA;--nav-text:#272724;--nav-text-scrolled:#272724;--nav-text-muted:#7a756e;--nav-accent:#523225;--nav-accent-hover:#3d241a;--nav-border:rgba(0,0,0,0.06);--nav-height:72px;--nav-height-mobile:64px;--nav-transition:0.3s cubic-bezier(0.4,0,0.2,1);--nav-shadow:0 1px 0 var(--nav-border);--nav-shadow-scrolled:0 2px 20px rgba(0,0,0,0.06)}}.navbar.navbar-stayhere,.navbar.navbar-stayhere *{{box-sizing:border-box}}.navbar.navbar-stayhere{{position:fixed!important;top:0!important;left:0!important;right:0!important;width:100%!important;z-index:1100!important;background:var(--nav-bg)!important;border:none!important;border-bottom:1px solid var(--nav-border)!important;box-shadow:none!important;padding:0!important;margin:0!important;display:block!important;flex-wrap:nowrap!important;height:var(--nav-height);transition:box-shadow var(--nav-transition),background var(--nav-transition)!important}}</style>

  <!-- Base enforcement -->
  <style>
    * {{ font-family: 'Clash Grotesk', sans-serif !important; }}
    html, body {{
      margin: 0 !important;
      padding: 0 !important;
      overflow-x: hidden !important;
      width: 100% !important;
      background-color: #F6F7EA !important;
    }}
    body.blog {{
      background-color: #F6F7EA !important;
      color: #272724;
      font-size: 18px;
      line-height: 1.8;
    }}
    #ftco-navbar, #ftco-navbar.scrolled, #ftco-navbar.awake, #ftco-navbar.sleep {{
      background-color: #F6F7EA !important;
      background: #F6F7EA !important;
      --nav-text: #272724 !important;
      --nav-text-muted: #272724 !important;
    }}
    #ftco-navbar .nav-link:not(.booking-btn), #ftco-navbar .navbar-brand, #ftco-navbar .language-toggle {{
      color: #272724 !important;
    }}

    /* Progress bar */
    #reading-progress-bar {{
      position: fixed; top: 0; left: 0; height: 3px; width: 0%;
      background-color: #523225; z-index: 9999;
      transition: width 0.1s linear; pointer-events: none;
    }}

    .navbar-spacer {{ height: var(--nav-height, 72px); display: block; }}
    .article-header {{ background-color: #F6F7EA; padding: 60px 32px 40px; max-width: 1440px; margin: 0 auto; }}
    .breadcrumb-nav {{ display: flex; align-items: center; gap: 8px; font-size: 12px; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; color: #272724; opacity: 0.5; margin-bottom: 20px; list-style: none; padding: 0; }}
    .breadcrumb-nav a {{ color: #272724; text-decoration: none; }}
    .category-tag {{ display: inline-block; background-color: #523225; color: #fff; font-size: 11px; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; padding: 5px 14px; border-radius: 100px; margin-bottom: 24px; }}
    .article-headline {{ font-size: clamp(2.4rem, 5.2vw, 4rem); font-weight: 700; color: #272724; line-height: 1.08; letter-spacing: -0.025em; margin: 0 0 20px; }}
    .article-subheadline {{ font-size: 1.25rem; font-weight: 400; color: #272724; opacity: 0.75; line-height: 1.6; margin: 0 0 32px; max-width: 850px; }}
    .article-meta-row {{ display: flex; align-items: center; flex-wrap: wrap; gap: 16px; font-size: 13px; color: #272724; opacity: 0.6; padding-bottom: 32px; border-bottom: 1px solid rgba(39,39,36,0.1); }}
    .meta-divider {{ width: 3px; height: 3px; border-radius: 50%; background: #272724; opacity: 0.4; display: inline-block; }}
    .share-buttons {{ display: flex; align-items: center; gap: 8px; margin-left: auto; }}
    .share-btn {{ display: inline-flex; align-items: center; gap: 6px; font-size: 12px; font-weight: 600; color: #272724; border: 1px solid rgba(39,39,36,0.2); background: transparent; padding: 6px 14px; border-radius: 100px; cursor: pointer; text-decoration: none; transition: all 0.2s; }}
    .share-btn:hover {{ border-color: #523225; color: #523225; }}

    .article-hero {{ width: 100%; max-width: 1440px; margin: 0 auto 56px; padding: 0 32px; box-sizing: border-box; }}
    .article-hero img {{ width: 100%; aspect-ratio: 16/9; max-height: 640px; object-fit: cover; border-radius: 4px; display: block; }}
    .article-hero-caption {{ font-size: 13px; color: #272724; opacity: 0.45; font-style: italic; margin-top: 10px; display: block; }}

    .article-body-wrap {{ max-width: 760px; margin: 0 auto; padding: 0 32px; box-sizing: border-box; }}
    .article-body p {{ font-size: 19px; line-height: 1.85; color: #272724; margin-bottom: 1.9em; }}
    .article-body h2 {{ font-size: 1.85rem; font-weight: 700; color: #272724; letter-spacing: -0.02em; margin-top: 3.5rem; margin-bottom: 1.2rem; line-height: 1.2; }}
    .article-body h3 {{ font-size: 1.35rem; font-weight: 700; color: #272724; margin-top: 2.2rem; margin-bottom: 0.8rem; }}
    .article-body ul {{ padding-left: 1.5rem; margin-bottom: 2rem; }}
    .article-body ul li {{ font-size: 19px; line-height: 1.8; color: #272724; margin-bottom: 0.7em; }}
    .article-quote {{ border-left: 3px solid #523225; padding-left: 28px; margin: 3rem 0; font-style: italic; font-size: 1.3rem; line-height: 1.6; color: #523225; }}
    .article-figure {{ margin: 3rem 0; }}
    .article-figure img {{ width: 100%; border-radius: 4px; display: block; }}
    .article-figure figcaption {{ font-size: 13px; color: #272724; opacity: 0.45; font-style: italic; margin-top: 10px; }}

    .article-key-takeaways {{ background: rgba(82,50,37,0.04); border-left: 3px solid #523225; padding: 28px 32px; margin: 3rem 0; border-radius: 0 4px 4px 0; }}
    .article-key-takeaways h3 {{ margin-top: 0; font-size: 1.15rem; text-transform: uppercase; letter-spacing: 0.05em; color: #523225; }}
    .article-key-takeaways ul {{ margin-bottom: 0; padding-left: 1.2rem; }}

    .article-cta-box {{ background-color: #272724 !important; border-radius: 6px; padding: 52px 40px; margin: 4rem 0; text-align: center; box-sizing: border-box; }}
    .article-cta-box h3 {{ color: #F6F7EA !important; font-size: 1.6rem; font-weight: 700; margin-bottom: 14px; margin-top: 0; }}
    .article-cta-box p {{ color: rgba(246,247,234,0.8) !important; font-size: 16px; line-height: 1.65; margin-bottom: 28px; max-width: 600px; margin-left: auto; margin-right: auto; }}
    .article-cta-btn {{ display: inline-flex; align-items: center; gap: 10px; background-color: #523225 !important; color: #F6F7EA !important; font-size: 13px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; text-decoration: none; padding: 16px 36px; border-radius: 100px; transition: background 0.2s, transform 0.2s; }}
    .article-cta-btn:hover {{ background-color: #3d241a; transform: translateY(-1px); }}

    .article-tags-wrap {{ max-width: 760px; margin: 0 auto; padding: 40px 32px 60px; box-sizing: border-box; }}
    .article-tags-label {{ font-size: 11px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: #272724; opacity: 0.45; margin-bottom: 14px; }}
    .article-tags {{ display: flex; flex-wrap: wrap; gap: 8px; }}
    .article-tag {{ display: inline-block; border: 1px solid rgba(39,39,36,0.2); color: #272724; font-size: 12px; font-weight: 600; padding: 6px 16px; border-radius: 100px; text-decoration: none; }}
    .article-tag:hover {{ border-color: #523225; color: #523225; background: rgba(82,50,37,0.04); }}

    .section-rule {{ border: 0; border-top: 1px solid rgba(39,39,36,0.1); margin: 0; }}

    /* Related Articles */
    .related-articles-section {{ background-color: #F6F7EA; padding: 80px 24px; }}
    .related-articles-inner {{ max-width: 1440px; margin: 0 auto; padding: 0 32px; box-sizing: border-box; }}
    .related-articles-header {{ display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 48px; border-bottom: 1px solid rgba(39,39,36,0.15); padding-bottom: 18px; }}
    .related-articles-title {{ font-size: 1.4rem; font-weight: 700; color: #272724; text-transform: uppercase; letter-spacing: -0.01em; margin: 0; }}
    .related-articles-link {{ font-size: 12px; font-weight: 700; color: #523225; text-decoration: none; letter-spacing: 0.08em; text-transform: uppercase; }}
    .related-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 40px; }}
    .related-card {{ display: flex; flex-direction: column; text-decoration: none; color: inherit; background: transparent; transition: transform 0.25s ease; }}
    .related-card:hover {{ text-decoration: none; color: inherit; }}
    .related-card-img-wrap {{ position: relative; overflow: hidden; aspect-ratio: 16/10; margin-bottom: 18px; }}
    .related-card-img-wrap img {{ width: 100%; height: 100%; object-fit: cover; transition: transform 0.6s ease; }}
    .related-card:hover .related-card-img-wrap img {{ transform: scale(1.03); }}
    .related-card-cat {{ font-size: 10.5px; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: #523225; margin-bottom: 10px; }}
    .related-card-title {{ font-size: 1.25rem; font-weight: 700; color: #272724; line-height: 1.25; margin-bottom: 12px; }}
    .related-card-meta {{ font-size: 12px; color: #7a756e; margin-bottom: 14px; }}
    .related-card-arrow {{ font-size: 12px; font-weight: 700; color: #523225; text-transform: uppercase; display: inline-flex; align-items: center; gap: 6px; }}

    #copy-toast {{ position: fixed; bottom: 28px; left: 50%; transform: translateX(-50%) translateY(20px); background: #272724; color: #F6F7EA; font-size: 13px; font-weight: 600; padding: 10px 22px; border-radius: 100px; opacity: 0; pointer-events: none; transition: all 0.3s ease; z-index: 9998; }}
    #copy-toast.show {{ opacity: 1; transform: translateX(-50%) translateY(0); }}

    {rtl_css}

    @media (max-width: 900px) {{
      .related-grid {{ grid-template-columns: 1fr; gap: 32px; }}
    }}
  </style>
</head>

<body class="blog">

  <!-- Reading Progress Bar -->
  <div id="reading-progress-bar" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>

  <!-- Toast Notification -->
  <div id="copy-toast" role="status" aria-live="polite">{t['share_copied']}</div>

  <!-- NAVBAR -->
  <nav style="height: var(--nav-height, 72px);" class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light" id="ftco-navbar">
    <div class="container">
      <a class="navbar-brand" href="/{lang}/"><img src="/images/logo-trensparent.webp" alt="Marragafay" style="width: 70px; height: 70px;" width="70" height="70"></a>
      <div class="mobile-language-switcher">
        <a href="#" class="language-toggle" id="languageDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          <i class="icon-globe"></i> <span>{lang.upper()}</span>
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
        <ul class="navbar-nav ml-auto">
          <li class="nav-item"><a href="/{lang}/" class="nav-link">{nav['Home']}</a></li>
          <li class="nav-item"><a href="/{lang}/activities" class="nav-link">{nav['Activities']}</a></li>
          <li class="nav-item"><a href="/{lang}/packs" class="nav-link">{nav['Packs']}</a></li>
          <li class="nav-item"><a href="/{lang}/about" class="nav-link">{nav['About']}</a></li>
          <li class="nav-item"><a href="/{lang}/reviews" class="nav-link">{nav['Reviews']}</a></li>
          <li class="nav-item active"><a href="index.html" class="nav-link">{nav['Journal']}</a></li>
          <li class="nav-item"><a href="/{lang}/contact" class="nav-link">{nav['Contact']}</a></li>
          <li class="nav-item"><a href="/{lang}/packs" class="nav-link booking-btn">{nav['Booking']}</a></li>
        </ul>
      </div>
    </div>
  </nav>

  <div class="navbar-spacer"></div>

  <!-- ARTICLE HEADER -->
  <header class="article-header">
    <nav aria-label="Breadcrumb">
      <ol class="breadcrumb-nav">
        <li><a href="/{lang}/">{t['home']}</a></li>
        <li class="sep">›</li>
        <li><a href="index.html">{t['journal']}</a></li>
        <li class="sep">›</li>
        <li class="current">{breadcrumb_cat}</li>
      </ol>
    </nav>

    <span class="category-tag">{m['category']}</span>
    <h1 class="article-headline">{m['title']}</h1>
    <p class="article-subheadline">{m['subtitle']}</p>

    <div class="article-meta-row">
      <span class="meta-author">{t['author']}</span>
      <span class="meta-divider" aria-hidden="true"></span>
      <span>{m['date_str']}</span>
      <span class="meta-divider" aria-hidden="true"></span>
      <span>{read_time} {t['read_time_suffix']}</span>

      <div class="share-buttons">
        <button class="share-btn" id="copy-link-btn" title="Copy link to article">
          <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 13a5 5 0 007.54.54l3-3a5 5 0 00-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 00-7.54-.54l-3 3a5 5 0 007.07 7.07l1.71-1.71"/></svg>
          {t['share_copy']}
        </button>
        <a class="share-btn"
           href="https://wa.me/?text={m['title']}%20https%3A%2F%2Fmarragafay.com%2F{lang}%2Fblog%2F{slug}"
           target="_blank"
           rel="noopener noreferrer"
           title="Share on WhatsApp">
          <svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.771-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.312.045-.694.072-2.148-.526-1.857-.764-3.045-2.658-3.137-2.781-.092-.123-.75-1-.75-1.909 0-.909.477-1.355.646-1.541.17-.186.371-.233.495-.233.124 0 .248.002.355.008.113.006.264-.043.413.315.155.371.531 1.298.577 1.391.046.093.078.202.015.326-.062.124-.093.202-.186.311-.093.109-.196.243-.28.326-.093.093-.19.195-.082.381.109.186.482.795 1.034 1.286.711.633 1.31.829 1.496.922.186.093.295.078.404-.046.11-.124.466-.543.59-.729.124-.186.249-.155.419-.093.17.062 1.084.511 1.27.604.186.093.31.14.356.217.047.078.047.45-.097.855z"/></svg>
          WhatsApp
        </a>
      </div>
    </div>
  </header>

  <!-- ARTICLE HERO IMAGE -->
  <div class="article-hero">
    <img src="{image}" alt="{m['title']}" loading="eager" fetchpriority="high" decoding="async" />
    <span class="article-hero-caption">{m['subtitle']}</span>
  </div>

  <!-- ARTICLE BODY -->
  <main>
    <article class="article-body-wrap">
      <div class="article-body">
        {body_content}
      </div>
    </article>
  </main>

  <!-- ARTICLE TAGS -->
  <div class="article-tags-wrap">
    <p class="article-tags-label">{t['filed_under']}</p>
    <div class="article-tags">
      <a href="index.html" class="article-tag">Agafay Desert</a>
      <a href="index.html" class="article-tag">{m['category']}</a>
      <a href="index.html" class="article-tag">Morocco</a>
      <a href="index.html" class="article-tag">Marrakech</a>
      <a href="index.html" class="article-tag">Luxury Travel</a>
    </div>
  </div>

  <hr class="section-rule">

  <!-- RELATED ARTICLES -->
  <section class="related-articles-section" aria-label="Related articles">
    <div class="related-articles-inner">
      <div class="related-articles-header">
        <h2 class="related-articles-title">{t['continue_reading']}</h2>
        <a href="index.html" class="related-articles-link">{t['all_articles']}</a>
      </div>
      <div class="related-grid">
        {related_cards_html}
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="bg-[#10100E] text-[#F6F7EA] pt-20 pb-10 px-6 md:px-16">
    <div class="max-w-7xl mx-auto">
      <div class="mb-16 overflow-hidden w-full">
        <p class="text-[12vw] sm:text-[10vw] md:text-[80px] lg:text-[120px] xl:text-[150px] leading-[0.8] tracking-tighter whitespace-nowrap font-bold uppercase mb-6 text-[#F6F7EA] -ml-1 md:-ml-2">MARRAGAFAY.</p>
        <p class="text-[#8e8e88] text-[14px] md:text-[16px] max-w-md leading-relaxed">{t['tagline']}</p>
      </div>
      <hr style="border: 0; border-top: 1px solid rgba(255, 255, 255, 0.1); margin: 40px 0;">
      <div class="grid grid-cols-2 md:grid-cols-4 gap-10 md:gap-6 text-[14px]">
        <div>
          <p class="text-xs font-bold uppercase tracking-widest text-[#F6F7EA] mb-6">{t['inquiries']}</p>
          <ul class="space-y-3 list-none p-0 m-0">
            <li><a href="mailto:marragafay@gmail.com" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA] transition-colors" style="text-decoration: none;">marragafay@gmail.com</a></li>
            <li><a href="tel:+212672531624" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA] transition-colors" style="text-decoration: none;">+212 672-531624</a></li>
            <li class="leading-tight text-[#F6F7EA]/90">Agafay Desert,<br>Marrakech, Morocco</li>
          </ul>
        </div>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest text-[#F6F7EA] mb-6">{t['navigate']}</p>
          <ul class="space-y-3 list-none p-0 m-0">
            <li><a href="/{lang}/activities" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA] transition-colors" style="text-decoration: none;">{nav['Activities']}</a></li>
            <li><a href="/{lang}/packs" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA] transition-colors" style="text-decoration: none;">{nav['Packs']}</a></li>
            <li><a href="/{lang}/reviews" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA] transition-colors" style="text-decoration: none;">{nav['Reviews']}</a></li>
            <li><a href="index.html" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA] transition-colors" style="text-decoration: none;">{nav['Journal']}</a></li>
          </ul>
        </div>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest text-[#F6F7EA] mb-6">{t['legal']}</p>
          <ul class="space-y-3 list-none p-0 m-0">
            <li><a href="/{lang}/terms" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA] transition-colors" style="text-decoration: none;">Terms &amp; Conditions</a></li>
            <li><a href="/{lang}/privacy" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA] transition-colors" style="text-decoration: none;">Privacy Policy</a></li>
            <li><a href="/{lang}/cancellation" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA] transition-colors" style="text-decoration: none;">Cancellation Policy</a></li>
          </ul>
        </div>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest text-[#F6F7EA] mb-6">{t['social']}</p>
          <ul class="space-y-3 list-none p-0 m-0">
            <li><a href="https://www.instagram.com/marragafay" target="_blank" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA] transition-colors" style="text-decoration: none;">Instagram</a></li>
            <li><a href="https://www.facebook.com/share/17pMqjAeGF/" target="_blank" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA] transition-colors" style="text-decoration: none;">Facebook</a></li>
            <li><a href="https://wa.me/212672531624" target="_blank" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA] transition-colors" style="text-decoration: none;">WhatsApp</a></li>
          </ul>
        </div>
      </div>
      <hr style="border: 0; border-top: 1px solid rgba(255, 255, 255, 0.1); margin: 40px 0;">
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center text-xs text-[#F6F7EA]/90 gap-4">
        <div>{t['rights']}</div>
        <div>{t['engineered']}</div>
      </div>
    </div>
  </footer>

  <!-- WhatsApp Floating Button -->
  <a href="https://wa.me/212672531624?text=Hello%20Marragafay"
     target="_blank"
     aria-label="Contact Marragafay on WhatsApp"
     class="fixed bottom-6 right-6 z-[100] flex items-center justify-center w-14 h-14 bg-[#25D366] text-white rounded-full shadow-xl hover:scale-110 transition-transform duration-300">
    <svg class="w-7 h-7 fill-current" viewBox="0 0 448 512" xmlns="http://www.w3.org/2000/svg">
      <path d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-25.2-115-67.1-157zm-157 341.6c-33.2 0-65.7-8.9-94-25.7l-6.7-4-69.8 18.3L72 359.2l-4.4-7c-18.5-29.4-28.2-63.3-28.2-98.2 0-101.7 82.8-184.5 184.6-184.5 49.3 0 95.6 19.2 130.4 54.1 34.8 34.9 56.2 81.2 56.1 130.5 0 101.8-84.9 184.6-186.6 184.6zm101.2-138.2c-5.5-2.8-32.8-16.2-37.9-18-5.1-1.9-8.8-2.8-12.5 2.8-3.7 5.6-14.3 18-17.6 21.8-3.2 3.7-6.5 4.2-12 1.4-32.6-16.3-54-29.1-75.5-66-5.7-9.8 5.7-9.1 16.3-30.3 1.8-3.7.9-6.9-.5-9.7-1.4-2.8-12.5-30.1-17.1-41.2-4.5-10.8-9.1-9.3-12.5-9.5-3.2-.2-6.9-.2-10.6-.2-3.7 0-9.7 1.4-14.8 6.9-5.1 5.6-19.4 19-19.4 46.3 0 27.3 19.9 53.7 22.6 57.4 2.8 3.7 39.1 59.7 94.8 83.8 35.2 15.2 49 16.5 66.6 13.9 10.7-1.6 32.8-13.4 37.4-26.4 4.6-13 4.6-24.1 3.2-26.4-1.3-2.5-5-3.9-10.5-6.6z"/>
    </svg>
  </a>

  <!-- SCRIPTS -->
  <script src="/js/jquery.min.js" defer></script>
  <script src="/js/popper.min.js" defer></script>
  <script src="/js/bootstrap.min.js" defer></script>
  <script src="/js/jquery.easing.1.3.js" defer></script>
  <script src="/js/jquery.waypoints.min.js" defer></script>
  <script src="/js/owl.carousel.min.js" defer></script>
  <script src="/js/jquery.magnific-popup.min.js" defer></script>
  <script src="/js/aos.js" defer></script>
  <script src="/js/main.js" defer></script>
  <script src="/js/navbar-stayhere.js" defer></script>

  <!-- LANGUAGE SWITCHER -->
  <script>
    document.addEventListener('DOMContentLoaded', function() {{
      var currentLang = window.location.pathname.split('/')[1];
      var langMap = {{ 'en': 'EN', 'fr': 'FR', 'es': 'ES', 'ar': 'AR' }};
      if (langMap[currentLang]) {{
        var displaySpan = document.querySelector('#languageDropdown span');
        if (displaySpan) displaySpan.textContent = langMap[currentLang];
      }}
      var langOptions = document.querySelectorAll('.lang-option');
      langOptions.forEach(function(opt) {{
        opt.addEventListener('click', function(e) {{
          e.preventDefault();
          var selectedLang = this.getAttribute('data-lang');
          localStorage.setItem('marragafay_lang', selectedLang);
          var currentPath = window.location.pathname;
          var pathParts = currentPath.split('/');
          if (pathParts.length > 1 && ['en', 'fr', 'es', 'ar'].includes(pathParts[1])) {{
            pathParts[1] = selectedLang;
          }} else {{
            pathParts.splice(1, 0, selectedLang);
          }}
          var newPath = pathParts.join('/') || '/';
          window.location.href = newPath + window.location.search + window.location.hash;
        }});
      }});
    }});
  </script>

  <!-- PROGRESS BAR SCRIPT -->
  <script>
    (function() {{
      var bar = document.getElementById('reading-progress-bar');
      if (!bar) return;
      function updateProgress() {{
        var scrollTop = window.scrollY || document.documentElement.scrollTop;
        var docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        var pct = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
        bar.style.width = Math.min(100, Math.max(0, pct)) + '%';
        bar.setAttribute('aria-valuenow', Math.round(pct));
      }}
      window.addEventListener('scroll', updateProgress, {{ passive: true }});
      updateProgress();
    }})();
  </script>

  <!-- COPY TOAST SCRIPT -->
  <script>
    (function() {{
      var btn = document.getElementById('copy-link-btn');
      var toast = document.getElementById('copy-toast');
      if (!btn || !toast) return;
      var toastTimer;
      function showToast() {{
        toast.classList.add('show');
        clearTimeout(toastTimer);
        toastTimer = setTimeout(function() {{ toast.classList.remove('show'); }}, 2500);
      }}
      btn.addEventListener('click', function() {{
        var url = window.location.href;
        if (navigator.clipboard && navigator.clipboard.writeText) {{
          navigator.clipboard.writeText(url).then(showToast).catch(function() {{ showToast(); }});
        }} else {{
          showToast();
        }}
      }});
    }})();
  </script>
</body>
</html>
"""
    return html

# Generate the files
for filename, meta in articles_meta.items():
    for lang in ["fr", "es", "ar"]:
        # Check if we have specialized body content or extract/adapt from English
        if filename in articles_body and lang in articles_body[filename]:
            body = articles_body[filename][lang]
        else:
            # Fallback to English body with localized headings
            with open(f"en/blog/{filename}", "r", encoding="utf-8") as ef:
                en_content = ef.read()
            body_match = re.search(r'<div class="article-body">(.*?)</div>\s*</article>', en_content, flags=re.DOTALL)
            body = body_match.group(1) if body_match else "<p>Article content coming soon.</p>"

        out_dir = f"{lang}/blog"
        os.makedirs(out_dir, exist_ok=True)
        out_path = f"{out_dir}/{filename}"

        html_content = build_article_html(lang, filename, meta, body)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html_content)

print("Generated all multilingual article pages successfully!")
