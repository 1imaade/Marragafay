import re
import glob

# 1. UI Translations
ui_translations = {
    "en": {
        "lang_code": "en",
        "home": "Home",
        "journal": "The Journal",
        "author": "Marragafay Editorial",
        "read_time_suffix": "min read",
        "share_copy": "Copy Link",
        "share_copied": "Link copied to clipboard!",
        "filed_under": "Filed Under",
        "continue_reading": "Continue Reading",
        "all_articles": "All Articles →",
        "read_article": "Read Article",
        "tagline": "Redefining the Agafay stone desert experience. Uncompromising luxury, exclusive fleets, and certified local expertise.",
        "inquiries": "Inquiries",
        "navigate": "Navigate",
        "legal": "Legal",
        "social": "Social",
        "rights": "© 2026 MARRAGAFAY. ALL RIGHTS RESERVED.",
        "engineered": "ENGINEERED IN MARRAKECH.",
        "cta_title": "Experience Agafay with Marragafay",
        "cta_desc": "Private desert dinners, quad adventures, and sunset camel rides — curated for those who seek extraordinary experiences.",
        "cta_btn": "Explore Experiences →",
        "cta_url": "/en/activities",
        "nav_links": {
            "Home": "Home",
            "Activities": "Activities",
            "Packs": "Packs",
            "About": "About",
            "Reviews": "Reviews",
            "Journal": "Journal",
            "Contact": "Contact",
            "Booking": "Booking"
        }
    },
    "fr": {
        "lang_code": "fr",
        "home": "Accueil",
        "journal": "La Revue",
        "author": "Rédaction Marragafay",
        "read_time_suffix": "min de lecture",
        "share_copy": "Copier le lien",
        "share_copied": "Lien copié dans le presse-papiers !",
        "filed_under": "Classé dans",
        "continue_reading": "Poursuivre la lecture",
        "all_articles": "Tous les Articles →",
        "read_article": "Lire l'Article",
        "tagline": "Redéfinir l'expérience du désert de pierre d'Agafay. Un luxe sans compromis, des flottes exclusives et une expertise locale certifiée.",
        "inquiries": "Renseignements",
        "navigate": "Navigation",
        "legal": "Mentions Légales",
        "social": "Réseaux Sociaux",
        "rights": "© 2026 MARRAGAFAY. TOUS DROITS RÉSERVÉS.",
        "engineered": "CONÇU À MARRAKECH.",
        "cta_title": "Vivez l'Expérience Agafay avec Marragafay",
        "cta_desc": "Dîners privés dans le désert, aventures en quad et balades à dos de chameau au coucher du soleil — créés pour ceux qui recherchent des moments extraordinaires.",
        "cta_btn": "Explorer les Expériences →",
        "cta_url": "/fr/activities",
        "nav_links": {
            "Home": "Accueil",
            "Activities": "Activités",
            "Packs": "Packs",
            "About": "À Propos",
            "Reviews": "Avis",
            "Journal": "La Revue",
            "Contact": "Contact",
            "Booking": "Réservation"
        }
    },
    "es": {
        "lang_code": "es",
        "home": "Inicio",
        "journal": "El Diario",
        "author": "Equipo Editorial Marragafay",
        "read_time_suffix": "min de lectura",
        "share_copy": "Copiar enlace",
        "share_copied": "¡Enlace copiado al portapapeles!",
        "filed_under": "Archivado en",
        "continue_reading": "Continuar Leyendo",
        "all_articles": "Todos los Artículos →",
        "read_article": "Leer Artículo",
        "tagline": "Redefiniendo la experiencia en el desierto de piedra de Agafay. Lujo sin concesiones, flotas exclusivas y experiencia local certificada.",
        "inquiries": "Consultas",
        "navigate": "Navegación",
        "legal": "Legal",
        "social": "Social",
        "rights": "© 2026 MARRAGAFAY. TODOS LOS DERECHOS RESERVADOS.",
        "engineered": "DISEÑADO EN MARRAKECH.",
        "cta_title": "Vive la Experiencia Agafay con Marragafay",
        "cta_desc": "Cenas privadas en el desierto, aventuras en quad y paseos en camello al atardecer, diseñados para quienes buscan experiencias extraordinarias.",
        "cta_btn": "Explorar Experiencias →",
        "cta_url": "/es/activities",
        "nav_links": {
            "Home": "Inicio",
            "Activities": "Actividades",
            "Packs": "Paquetes",
            "About": "Sobre Nosotros",
            "Reviews": "Reseñas",
            "Journal": "El Diario",
            "Contact": "Contacto",
            "Booking": "Reservar"
        }
    },
    "ar": {
        "lang_code": "ar",
        "home": "الرئيسية",
        "journal": "المجلة",
        "author": "فريق تحرير مراكافاي",
        "read_time_suffix": "دقائق قراءة",
        "share_copy": "نسخ الرابط",
        "share_copied": "!تم نسخ الرابط بنجاح",
        "filed_under": "تصنيف المقال",
        "continue_reading": "متابعة القراءة",
        "all_articles": "← جميع المقالات",
        "read_article": "اقرأ المقال",
        "tagline": "إعادة صياغة تجربة صحراء أكافاي الحجرية. فخامة مطلقة، أسطول حصري، وخبرة محلية معتمدة.",
        "inquiries": "الاستفسارات",
        "navigate": "تصفح الموقع",
        "legal": "الشروط والأحكام",
        "social": "التواصل الاجتماعي",
        "rights": "© 2026 MARRAGAFAY. جميع الحقوق محفوظة.",
        "engineered": "صُمم في مراكش.",
        "cta_title": "عش تجربة أكافاي الفاخرة مع مراكافاي",
        "cta_desc": "عشاء صحراوي خاص، مغامرات بالدراجات الرباعية، وجولات على الجمال وقت الغروب — مصممة خصيصاً للباحثين عن التميز.",
        "cta_btn": "← استكشف التجارب",
        "cta_url": "/ar/activities",
        "nav_links": {
            "Home": "الرئيسية",
            "Activities": "الأنشطة",
            "Packs": "الباقات",
            "About": "من نحن",
            "Reviews": "التقييمات",
            "Journal": "المجلة",
            "Contact": "اتصل بنا",
            "Booking": "الحجز"
        }
    }
}

# 2. Articles Meta
articles_meta = {
    "agafay-desert-guide.html": {
        "slug": "agafay-desert-guide",
        "date": "2026-08-01",
        "read_time": "8",
        "image": "/images/Slider-images/slider-1.webp",
        "en": {
            "title": "The Complete Guide to Agafay Desert — Morocco's Stone Desert Explained",
            "subtitle": "Everything first-time visitors need to know about the stone plateau 45 minutes from Marrakech.",
            "category": "Desert Guide",
            "date_str": "August 2026",
            "meta_desc": "Everything first-time visitors need to know about Morocco's Agafay stone desert — activities, best time to visit, how to get there, and what makes it unique."
        },
        "fr": {
            "title": "Le Guide Complet du Désert d'Agafay — Le Désert de Pierre Marocain Expliqué",
            "subtitle": "Tout ce que les visiteurs doivent savoir sur le plateau minéral à 45 minutes de Marrakech.",
            "category": "Guide du Désert",
            "date_str": "Août 2026",
            "meta_desc": "Tout ce que vous devez savoir sur le désert de pierre d'Agafay au Maroc : activités, meilleure période, comment y accéder et ce qui le rend unique."
        },
        "es": {
            "title": "La Guía Completa del Desierto de Agafay — El Desierto de Piedra de Marruecos",
            "subtitle": "Todo lo que los viajeros deben saber sobre la meseta mineral a 45 minutos de Marrakech.",
            "category": "Guía del Desierto",
            "date_str": "Agosto 2026",
            "meta_desc": "Todo lo que necesitas saber sobre el desierto de piedra de Agafay: actividades, mejor época para visitar, cómo llegar y qué lo hace único."
        },
        "ar": {
            "title": "الدليل الشامل لصحراء أكافاي — استكشف الصحراء الصخرية الساحرة بالمغرب",
            "subtitle": "كل ما يحتاج الزوار لمعرفته عن هضبة أكافاي الواقعة على بعد 45 دقيقة فقط من مراكش.",
            "category": "دليل الصحراء",
            "date_str": "أغسطس 2026",
            "meta_desc": "كل ما تحتاج معرفته عن صحراء أكافاي الحجرية بالمغرب: الأنشطة، أفضل أوقات الزيارة، كيفية الوصول، وما يجعلها تجربة فريدة."
        }
    },
    "agafay-camel-ride.html": {
        "slug": "agafay-camel-ride",
        "date": "2026-08-10",
        "read_time": "5",
        "image": "/images/Slider-images/slider-3.webp",
        "en": {
            "title": "Sunset Camel Ride in Agafay: What to Expect (An Honest Account)",
            "subtitle": "The silence before sunset in the desert is not empty — it is full. Our guide on what every first-time visitor should know.",
            "category": "Experience",
            "date_str": "August 2026",
            "meta_desc": "What to expect on a sunset camel ride in Agafay Desert: timing, what to wear, photography tips, and honest expectations."
        },
        "fr": {
            "title": "Balade en Chameau au Coucher du Soleil à Agafay : À Quoi s'Attendre",
            "subtitle": "Le silence avant le coucher du soleil dans le désert de pierre : conseils, horaires et sensations.",
            "category": "Expérience",
            "date_str": "Août 2026",
            "meta_desc": "À quoi s'attendre lors d'une balade exclusive en chameau au coucher du soleil dans le désert d'Agafay : horaires, tenue recommandée et conseils photo."
        },
        "es": {
            "title": "Paseo en Camello al Atardecer en Agafay: Qué Esperar (Relato Honesto)",
            "subtitle": "El silencio antes del atardecer en el desierto mineral: horarios, vestimenta y fotografía.",
            "category": "Experiencia",
            "date_str": "Agosto 2026",
            "meta_desc": "Qué esperar de un exclusivo paseo en camello al atardecer en el desierto de Agafay: tiempos, vestimenta recomendada y consejos fotográficos."
        },
        "ar": {
            "title": "جولة على الجمال وقت الغروب في أكافاي: ماذا تتوقع (دليل مفصل)",
            "subtitle": "الهدوء الساحر قبل غروب الشمس في الصحراء الصخرية: التوقيت، الزي المناسب، وأسرار التصوير.",
            "category": "تجربة",
            "date_str": "أغسطس 2026",
            "meta_desc": "ماذا تتوقع من جولة ركوب الجمال الفاخرة وقت الغروب في صحراء أكافاي: التوقيت المثالي، الملابس المناسبة، ونصائح التصوير."
        }
    },
    "berber-culture-agafay.html": {
        "slug": "berber-culture-agafay",
        "date": "2026-07-20",
        "read_time": "6",
        "image": "/images/gallery/gal4.webp",
        "en": {
            "title": "Berber Heritage and the Agafay: A Culture That Predates Tourism",
            "subtitle": "Long before desert tourism arrived, the Agafay plateau was home to Berber communities whose traditions survive intact.",
            "category": "Culture",
            "date_str": "July 2026",
            "meta_desc": "Explore the deep Berber heritage, architecture, and timeless hospitality traditions of the Agafay stone desert communities."
        },
        "fr": {
            "title": "L'Héritage Berbère et Agafay : Une Culture Antérieure au Tourisme",
            "subtitle": "Histoire vivante, architecture de pierre et rituels d'hospitalité au cœur du plateau d'Agafay.",
            "category": "Culture & Patrimoine",
            "date_str": "Juillet 2026",
            "meta_desc": "Découvrez l'histoire et les traditions des communautés berbères qui habitent le désert de pierre d'Agafay depuis des siècles."
        },
        "es": {
            "title": "El Patrimonio Bereber y Agafay: Una Cultura Anterior al Turismo",
            "subtitle": "Historia viva, arquitectura de piedra y rituales de hospitalidad en el corazón de Agafay.",
            "category": "Cultura y Patrimonio",
            "date_str": "Julio 2026",
            "meta_desc": "Descubre la historia y las tradiciones de las comunidades bereberes que han habitado el desierto de piedra de Agafay durante siglos."
        },
        "ar": {
            "title": "التراث الأمازيغي وأكافاي: ثقافة أصيلة تسبق السياحة",
            "subtitle": "تاريخ عريق، هندسة حجرية فريدة، وتقاليد كرم وضيافة تمتد لقرون في صحراء أكافاي.",
            "category": "ثقافة وتراث",
            "date_str": "يوليو 2026",
            "meta_desc": "استكشف تاريخ وتقاليد المجتمعات الأمازيغية العريقة في صحراء أكافاي الحجرية وطقوس الضيافة الأصيلة."
        }
    },
    "marrakech-to-agafay.html": {
        "slug": "marrakech-to-agafay",
        "date": "2026-07-15",
        "read_time": "4",
        "image": "/images/destination-4.jpg",
        "en": {
            "title": "Marrakech to Agafay Desert: Every Way to Get There",
            "subtitle": "From private transfers to rental cars, the 45-kilometer journey separates the medina from the silence.",
            "category": "Travel Tips",
            "date_str": "July 2026",
            "meta_desc": "Complete guide on how to get from Marrakech to the Agafay Desert — private transfers, taxis, car rentals, and practical tips."
        },
        "fr": {
            "title": "De Marrakech au Désert d'Agafay : Tous les Moyens de Transport",
            "subtitle": "Transferts privés, taxis et itinéraires pour parcourir les 45 kilomètres séparant la médina du silence.",
            "category": "Conseils Pratiques",
            "date_str": "Juillet 2026",
            "meta_desc": "Comment se rendre de Marrakech au désert d'Agafay : comparatif des transports, durée du trajet, prix et conseils pratiques."
        },
        "es": {
            "title": "De Marrakech al Desierto de Agafay: Todas las Formas de Llegar",
            "subtitle": "Traslados privados, taxis y consejos para recorrer los 45 kilómetros desde la medina hasta el desierto.",
            "category": "Consejos de Viaje",
            "date_str": "Julio 2026",
            "meta_desc": "Cómo ir de Marrakech al desierto de Agafay: opciones de transporte, duración del trayecto, costes y recomendaciones."
        },
        "ar": {
            "title": "من مراكش إلى صحراء أكافاي: دليلك الشامل لكافة وسائل النقل",
            "subtitle": "من النقل الخاص إلى سيارات الأجرة، 45 كيلومتراً تفصل بين صخب المدينة القديمة وهدوء الصحراء.",
            "category": "نصائح السفر",
            "date_str": "يوليو 2026",
            "meta_desc": "دليلك للوصول من مراكش إلى صحراء أكافاي: مقارنة وسائل النقل، المدة الزمنية، التكاليف، وأهم النصائح العملية."
        }
    },
    "agafay-dinner-experience.html": {
        "slug": "agafay-dinner-experience",
        "date": "2026-06-28",
        "read_time": "7",
        "image": "/images/activites/show.webp",
        "en": {
            "title": "The Agafay Desert Dinner — A Private Evening Under the Stars",
            "subtitle": "How a private desert dinner became the most requested experience in Marragafay's catalogue.",
            "category": "Dining",
            "date_str": "June 2026",
            "meta_desc": "Experience a private candlelit dinner under the desert sky in Agafay — gourmet Moroccan gastronomy, live fire spectacle, and stargazing."
        },
        "fr": {
            "title": "Le Dîner dans le Désert d'Agafay — Une Soirée Privée Sous les Étoiles",
            "subtitle": "Gastronomie marocaine raffinée, spectacle de feu et observation des étoiles au milieu des collines.",
            "category": "Gastronomie",
            "date_str": "Juin 2026",
            "meta_desc": "Découvrez l'expérience exclusive d'un dîner sous les étoiles dans le désert d'Agafay : menu gastronomique, feu de camp et ambiance magique."
        },
        "es": {
            "title": "Cena en el Desierto de Agafay — Una Velada Privada Bajo las Estrellas",
            "subtitle": "Gastronomía marroquí gourmet, espectáculo de fuego y observación astronómica en el desierto.",
            "category": "Gastronomía",
            "date_str": "Junio 2026",
            "meta_desc": "Disfruta de una cena privada bajo las estrellas en el desierto de Agafay: alta cocina marroquí, espectáculo de fuego y cielo estrellado."
        },
        "ar": {
            "title": "عشاء صحراوي ساحر في أكافاي — أمسية خاصة تحت قبة النجوم",
            "subtitle": "أطباق مغربية أصيلة، عروض نار حية، وسحر السهر تحت سماء الصحراء المتلألئة بالنجوم.",
            "category": "تجربة طعام",
            "date_str": "يونيو 2026",
            "meta_desc": "عش تجربة عشاء رومانسي فاخر تحت نجوم صحراء أكافاي: مأكولات مغربية فاخرة، عروض فنية حية، وأجواء ساحرة."
        }
    },
    "agafay-quad-biking-guide.html": {
        "slug": "agafay-quad-biking-guide",
        "date": "2026-08-15",
        "read_time": "6",
        "image": "/images/activites/quad.webp",
        "en": {
            "title": "Quad Biking in Agafay Desert: Safety, Tips & What You'll See",
            "subtitle": "An exhilarating ride across barren hills and ancient trails with the High Atlas mountains as your backdrop.",
            "category": "Adventure",
            "date_str": "August 2026",
            "meta_desc": "Everything you need to know about quad biking in Agafay Desert: safety gear, terrain guide, difficulty levels, and photo spots."
        },
        "fr": {
            "title": "Quad dans le Désert d'Agafay : Sécurité, Parcours et Conseils",
            "subtitle": "Sensations fortes sur les pistes minérales avec la chaîne de l'Atlas en toile de fond panoramique.",
            "category": "Aventure",
            "date_str": "Août 2026",
            "meta_desc": "Guide complet du quad dans le désert d'Agafay : équipement de sécurité, niveaux de difficulté, meilleurs spots photo et conseils."
        },
        "es": {
            "title": "Quad en el Desierto de Agafay: Seguridad, Rutas y Consejos",
            "subtitle": "Adrenalina y aventura sobre colinas áridas con la cordillera del Atlas como telón de fondo.",
            "category": "Aventura",
            "date_str": "Agosto 2026",
            "meta_desc": "Guía completa para hacer quad en el desierto de Agafay: equipamiento, dificultad, paradas fotográficas y normas de seguridad."
        },
        "ar": {
            "title": "مغامرة الكواد في صحراء أكافاي: الأمان، المسارات، وأهم النصائح",
            "subtitle": "إثارة وتشويق عبر التلال الصخرية والمسارات الوعرة مع إطلالة بانورامية على جبال الأطلس الكبير.",
            "category": "مغامرة",
            "date_str": "أغسطس 2026",
            "meta_desc": "كل ما تريد معرفته عن جولات الكواد في صحراء أكافاي: معايير السلامة، مستويات الصعوبة، وأجمل نقاط التصوير."
        }
    },
    "agafay-desert-vs-sahara.html": {
        "slug": "agafay-desert-vs-sahara",
        "date": "2026-07-28",
        "read_time": "7",
        "image": "/images/gallery/gal2.webp",
        "en": {
            "title": "Agafay Desert vs Sahara: Which Desert Experience Is Right for You?",
            "subtitle": "Comparing drive times, landscape differences, costs, and atmosphere to help you make the right choice.",
            "category": "Comparison",
            "date_str": "July 2026",
            "meta_desc": "Detailed comparison between Agafay Stone Desert and the Sahara Desert (Merzouga & Zagora) to choose the best experience for your trip."
        },
        "fr": {
            "title": "Désert d'Agafay ou Sahara : Quel Désert Choisir pour Votre Voyage ?",
            "subtitle": "Temps de trajet, paysages, budget et ambiance : notre comparatif complet pour bien choisir.",
            "category": "Comparatif",
            "date_str": "Juillet 2026",
            "meta_desc": "Agafay ou Sahara (Merzouga/Zagora) ? Découvrez les différences clés de temps de route, de paysage et d'expérience pour faire le bon choix."
        },
        "es": {
            "title": "Desierto de Agafay vs Sahara: ¿Cuál Elegir para tu Viaje?",
            "subtitle": "Comparativa de tiempos de viaje, paisajes, presupuesto y ambiente para elegir la mejor opción.",
            "category": "Comparativa",
            "date_str": "Julio 2026",
            "meta_desc": "Agafay o el Sahara (Merzouga/Zagora): comparamos distancias, paisajes, costes y experiencias para ayudarte a decidir."
        },
        "ar": {
            "title": "صحراء أكافاي أم الصحراء الكبرى: أيهما أفضل لرحلتك القادمة بالمغرب؟",
            "subtitle": "مقارنة شاملة للمسافات، طبيعة التضاريس، التكاليف، والأجواء لمساعدتك في اختيار التجربة المثالية.",
            "category": "مقارنة",
            "date_str": "يوليو 2026",
            "meta_desc": "مقارنة تفصيلية بين صحراء أكافاي القريبة من مراكش وكثبان الصحراء الكبرى في مرزوكة وزاكورة لمساعدتك في اتخاذ القرار."
        }
    }
}

# 3. Master CSS
master_css = """
    * { font-family: 'Clash Grotesk', sans-serif !important; box-sizing: border-box; }
    html, body {
      margin: 0 !important;
      padding: 0 !important;
      overflow-x: hidden !important;
      max-width: 100vw !important;
      width: 100% !important;
      background-color: #F6F7EA !important;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }
    body.blog {
      background-color: #F6F7EA !important;
      color: #272724;
      font-size: 18px;
      line-height: 1.8;
    }
    #ftco-navbar, #ftco-navbar.scrolled, #ftco-navbar.awake, #ftco-navbar.sleep {
      background-color: #F6F7EA !important;
      background: #F6F7EA !important;
      --nav-text: #272724 !important;
      --nav-text-muted: #272724 !important;
    }
    #ftco-navbar .nav-link:not(.booking-btn), #ftco-navbar .navbar-brand, #ftco-navbar .language-toggle {
      color: #272724 !important;
    }

    /* Reading Progress Bar */
    #reading-progress-bar {
      position: fixed; top: 0; left: 0; height: 3px; width: 0%;
      background-color: #523225; z-index: 9999;
      transition: width 0.1s linear; pointer-events: none;
    }

    .navbar-spacer { height: var(--nav-height, 72px); display: block; }
    
    /* Article Header */
    .article-header {
      background-color: #F6F7EA;
      padding: 56px 32px 36px;
      max-width: 1200px;
      margin: 0 auto;
      box-sizing: border-box;
    }
    .breadcrumb-nav {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 12px;
      font-weight: 600;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: #272724;
      opacity: 0.55;
      margin-bottom: 20px;
      list-style: none;
      padding: 0;
    }
    .breadcrumb-nav a { color: #272724; text-decoration: none; }
    .breadcrumb-nav a:hover { opacity: 0.8; }
    .category-tag {
      display: inline-block;
      background-color: #523225;
      color: #fff;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      padding: 5px 14px;
      border-radius: 100px;
      margin-bottom: 20px;
    }
    .article-headline {
      font-size: clamp(2.3rem, 5vw, 3.8rem);
      font-weight: 700;
      color: #272724;
      line-height: 1.08;
      letter-spacing: -0.025em;
      margin: 0 0 18px;
      word-wrap: break-word;
    }
    .article-subheadline {
      font-size: 1.25rem;
      font-weight: 400;
      color: #272724;
      opacity: 0.8;
      line-height: 1.6;
      margin: 0 0 28px;
      max-width: 840px;
    }
    .article-meta-row {
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 14px;
      font-size: 13px;
      color: #272724;
      opacity: 0.65;
      padding-bottom: 28px;
      border-bottom: 1px solid rgba(39,39,36,0.12);
    }
    .meta-divider {
      width: 3px;
      height: 3px;
      border-radius: 50%;
      background: #272724;
      opacity: 0.4;
      display: inline-block;
    }
    .share-buttons {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-left: auto;
    }
    .share-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 12px;
      font-weight: 600;
      color: #272724;
      border: 1px solid rgba(39,39,36,0.22);
      background: transparent;
      padding: 6px 14px;
      border-radius: 100px;
      cursor: pointer;
      text-decoration: none;
      transition: all 0.2s;
    }
    .share-btn:hover { border-color: #523225; color: #523225; }

    /* Article Hero Image */
    .article-hero {
      width: 100%;
      max-width: 1200px;
      margin: 0 auto 48px;
      padding: 0 32px;
      box-sizing: border-box;
    }
    .article-hero img {
      width: 100%;
      aspect-ratio: 16/9;
      max-height: 600px;
      object-fit: cover;
      border-radius: 8px;
      display: block;
    }
    .article-hero-caption {
      font-size: 13px;
      color: #272724;
      opacity: 0.5;
      font-style: italic;
      margin-top: 10px;
      display: block;
      line-height: 1.45;
    }

    /* Article Body Typography */
    .article-body-wrap {
      max-width: 740px;
      margin: 0 auto;
      padding: 0 32px;
      box-sizing: border-box;
    }
    .article-body p {
      font-size: 18.5px;
      line-height: 1.85;
      color: #272724;
      margin-bottom: 1.8em;
    }
    .article-body h2 {
      font-size: 1.8rem;
      font-weight: 700;
      color: #272724;
      letter-spacing: -0.02em;
      margin-top: 3.2rem;
      margin-bottom: 1.1rem;
      line-height: 1.22;
    }
    .article-body h3 {
      font-size: 1.35rem;
      font-weight: 700;
      color: #272724;
      margin-top: 2.2rem;
      margin-bottom: 0.75rem;
      line-height: 1.3;
    }
    .article-body ul {
      padding-left: 1.5rem;
      margin-bottom: 2rem;
    }
    .article-body ul li {
      font-size: 18.5px;
      line-height: 1.8;
      color: #272724;
      margin-bottom: 0.65em;
    }
    .article-body blockquote, .article-quote {
      border-left: 3px solid #523225;
      padding-left: 24px;
      margin: 2.8rem 0;
      font-style: italic;
      font-size: 1.25rem;
      line-height: 1.6;
      color: #523225;
    }
    .article-inline-img {
      width: 100% !important;
      max-width: 100% !important;
      height: auto !important;
      border-radius: 8px !important;
      margin: 2.8rem 0 0.8rem !important;
      display: block !important;
      object-fit: cover !important;
    }
    .article-inline-caption {
      font-size: 13px !important;
      color: #272724 !important;
      opacity: 0.5 !important;
      font-style: italic !important;
      display: block !important;
      margin-bottom: 2.8rem !important;
      line-height: 1.45 !important;
    }

    /* In-Article Booking CTA */
    .article-cta-box {
      background-color: #272724 !important;
      color: #F6F7EA !important;
      padding: 44px 36px;
      border-radius: 10px;
      margin: 3.5rem 0;
      text-align: center;
      box-sizing: border-box;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
    }
    .article-cta-box h3 {
      color: #F6F7EA !important;
      font-size: clamp(1.4rem, 2.5vw, 1.85rem) !important;
      font-weight: 700 !important;
      margin-top: 0 !important;
      margin-bottom: 12px !important;
      line-height: 1.25 !important;
      letter-spacing: -0.015em !important;
    }
    .article-cta-box p {
      color: rgba(246, 247, 234, 0.82) !important;
      font-size: 16px !important;
      line-height: 1.65 !important;
      max-width: 540px !important;
      margin: 0 auto 24px !important;
    }
    .article-cta-btn {
      display: inline-flex !important;
      align-items: center !important;
      justify-content: center !important;
      gap: 8px !important;
      background-color: #523225 !important;
      color: #F6F7EA !important;
      padding: 13px 30px !important;
      border-radius: 100px !important;
      font-weight: 700 !important;
      text-decoration: none !important;
      font-size: 13px !important;
      letter-spacing: 0.08em !important;
      text-transform: uppercase !important;
      transition: all 0.25s ease !important;
    }
    .article-cta-btn:hover {
      background-color: #3d241a !important;
      color: #F6F7EA !important;
      transform: translateY(-1px) !important;
      box-shadow: 0 4px 14px rgba(82, 50, 37, 0.4) !important;
    }

    /* Tags Wrap */
    .article-tags-wrap {
      max-width: 740px;
      margin: 0 auto;
      padding: 36px 32px 56px;
      box-sizing: border-box;
    }
    .article-tags-label {
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: #272724;
      opacity: 0.45;
      margin-bottom: 14px;
    }
    .article-tags {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }
    .article-tag {
      display: inline-block;
      border: 1px solid rgba(39,39,36,0.2);
      color: #272724;
      font-size: 12px;
      font-weight: 600;
      padding: 6px 16px;
      border-radius: 100px;
      text-decoration: none;
      transition: all 0.2s;
    }
    .article-tag:hover {
      border-color: #523225;
      color: #523225;
      background: rgba(82,50,37,0.05);
    }

    .section-rule {
      border: 0;
      border-top: 1px solid rgba(39,39,36,0.1);
      margin: 0;
    }

    /* Related Articles */
    .related-articles-section {
      background-color: #F6F7EA;
      padding: 72px 24px;
    }
    .related-articles-inner {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 32px;
      box-sizing: border-box;
    }
    .related-articles-header {
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      margin-bottom: 40px;
      border-bottom: 1px solid rgba(39,39,36,0.15);
      padding-bottom: 16px;
    }
    .related-articles-title {
      font-size: 1.35rem;
      font-weight: 700;
      color: #272724;
      text-transform: uppercase;
      letter-spacing: -0.01em;
      margin: 0;
    }
    .related-articles-link {
      font-size: 12px;
      font-weight: 700;
      color: #523225;
      text-decoration: none;
      letter-spacing: 0.08em;
      text-transform: uppercase;
    }
    .related-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 36px;
    }
    .related-card {
      display: flex;
      flex-direction: column;
      text-decoration: none;
      color: inherit;
      background: transparent;
      transition: transform 0.25s ease;
    }
    .related-card:hover { text-decoration: none; color: inherit; }
    .related-card-img-wrap {
      position: relative;
      overflow: hidden;
      aspect-ratio: 16/10;
      border-radius: 6px;
      margin-bottom: 16px;
    }
    .related-card-img-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.6s ease;
    }
    .related-card:hover .related-card-img-wrap img {
      transform: scale(1.03);
    }
    .related-card-cat {
      font-size: 10.5px;
      font-weight: 700;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: #523225;
      margin-bottom: 8px;
    }
    .related-card-title {
      font-size: 1.2rem;
      font-weight: 700;
      color: #272724;
      line-height: 1.25;
      margin-bottom: 10px;
    }
    .related-card-meta {
      font-size: 12px;
      color: #7a756e;
      margin-bottom: 12px;
    }
    .related-card-arrow {
      font-size: 12px;
      font-weight: 700;
      color: #523225;
      text-transform: uppercase;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    #copy-toast {
      position: fixed;
      bottom: 28px;
      left: 50%;
      transform: translateX(-50%) translateY(20px);
      background: #272724;
      color: #F6F7EA;
      font-size: 13px;
      font-weight: 600;
      padding: 10px 22px;
      border-radius: 100px;
      opacity: 0;
      pointer-events: none;
      transition: all 0.3s ease;
      z-index: 9998;
    }
    #copy-toast.show { opacity: 1; transform: translateX(-50%) translateY(0); }

    /* ═══════════════════════════════════════════════
       MOBILE RESPONSIVE PERFECTION (ARTICLE PAGES)
    ═══════════════════════════════════════════════ */
    @media (max-width: 1024px) {
      .article-header { padding: 40px 24px 28px; }
      .article-hero { padding: 0 24px; margin-bottom: 36px; }
      .article-body-wrap, .article-tags-wrap { padding: 0 24px; }
      .related-articles-section { padding: 56px 24px; }
      .related-grid { grid-template-columns: repeat(2, 1fr); gap: 28px; }
    }

    @media (max-width: 768px) {
      .navbar-spacer { height: var(--nav-height-mobile, 64px) !important; }
      
      .article-header {
        padding: 24px 18px 18px !important;
        max-width: 100% !important;
      }
      .breadcrumb-nav {
        font-size: 11px !important;
        margin-bottom: 12px !important;
        gap: 6px !important;
        flex-wrap: wrap !important;
      }
      .category-tag {
        font-size: 10px !important;
        padding: 4px 12px !important;
        margin-bottom: 14px !important;
      }
      .article-headline {
        font-size: clamp(1.85rem, 7vw, 2.35rem) !important;
        line-height: 1.15 !important;
        margin: 0 0 14px !important;
        letter-spacing: -0.02em !important;
        word-break: break-word !important;
      }
      .article-subheadline {
        font-size: 16px !important;
        line-height: 1.55 !important;
        margin: 0 0 18px !important;
        opacity: 0.8 !important;
      }
      .article-meta-row {
        flex-direction: row !important;
        flex-wrap: wrap !important;
        align-items: center !important;
        gap: 8px 12px !important;
        font-size: 12px !important;
        padding-bottom: 16px !important;
      }
      .share-buttons {
        width: 100% !important;
        margin-left: 0 !important;
        margin-top: 6px !important;
        justify-content: flex-start !important;
        gap: 8px !important;
      }
      .share-btn {
        font-size: 11.5px !important;
        padding: 6px 14px !important;
      }

      .article-hero {
        padding: 0 18px !important;
        margin-bottom: 24px !important;
        max-width: 100% !important;
      }
      .article-hero img {
        aspect-ratio: 16/10 !important;
        max-height: 300px !important;
        border-radius: 6px !important;
      }
      .article-hero-caption {
        font-size: 11.5px !important;
        margin-top: 6px !important;
      }

      .article-body-wrap {
        padding: 0 18px !important;
        margin: 0 auto !important;
        max-width: 100% !important;
      }
      .article-body p {
        font-size: 16.5px !important;
        line-height: 1.75 !important;
        margin-bottom: 1.35em !important;
      }
      .article-body h2 {
        font-size: 1.45rem !important;
        line-height: 1.25 !important;
        margin-top: 2.2rem !important;
        margin-bottom: 0.8rem !important;
        letter-spacing: -0.015em !important;
      }
      .article-body h3 {
        font-size: 1.2rem !important;
        line-height: 1.3 !important;
        margin-top: 1.6rem !important;
        margin-bottom: 0.5rem !important;
      }
      .article-body ul {
        padding-left: 1.25rem !important;
        margin-bottom: 1.4rem !important;
      }
      .article-body ul li {
        font-size: 16.5px !important;
        line-height: 1.65 !important;
        margin-bottom: 0.5em !important;
      }
      .article-body blockquote, .article-quote {
        border-left: 3px solid #523225 !important;
        padding: 6px 0 6px 14px !important;
        margin: 1.8rem 0 !important;
        font-size: 1.1rem !important;
        line-height: 1.55 !important;
      }
      .article-inline-img {
        margin: 1.8rem 0 0.6rem !important;
        border-radius: 6px !important;
      }
      .article-inline-caption {
        font-size: 11.5px !important;
        margin-bottom: 1.8rem !important;
      }

      .article-cta-box {
        padding: 28px 18px !important;
        margin: 2.4rem 0 !important;
        border-radius: 8px !important;
        width: 100% !important;
      }
      .article-cta-box h3 {
        font-size: 1.35rem !important;
        line-height: 1.25 !important;
        margin-bottom: 10px !important;
      }
      .article-cta-box p {
        font-size: 14.5px !important;
        line-height: 1.6 !important;
        margin-bottom: 18px !important;
        max-width: 100% !important;
      }
      .article-cta-btn {
        width: 100% !important;
        padding: 13px 20px !important;
        font-size: 12.5px !important;
        justify-content: center !important;
        text-align: center !important;
      }

      .article-tags-wrap {
        padding: 20px 18px 36px !important;
        max-width: 100% !important;
      }
      .article-tags-label {
        font-size: 10.5px !important;
        margin-bottom: 10px !important;
      }
      .article-tags {
        gap: 7px !important;
      }
      .article-tag {
        font-size: 11px !important;
        padding: 5px 12px !important;
      }

      .related-articles-section {
        padding: 40px 18px !important;
      }
      .related-articles-inner {
        padding: 0 !important;
        max-width: 100% !important;
      }
      .related-articles-header {
        margin-bottom: 24px !important;
        padding-bottom: 12px !important;
      }
      .related-articles-title {
        font-size: 1.15rem !important;
      }
      .related-articles-link {
        font-size: 11px !important;
      }
      .related-grid {
        grid-template-columns: 1fr !important;
        gap: 24px !important;
      }
      .related-card-img-wrap {
        aspect-ratio: 16/10 !important;
        margin-bottom: 12px !important;
        border-radius: 6px !important;
      }
      .related-card-cat {
        font-size: 10px !important;
        margin-bottom: 6px !important;
      }
      .related-card-title {
        font-size: 1.15rem !important;
        line-height: 1.28 !important;
        margin-bottom: 6px !important;
      }
      .related-card-meta {
        font-size: 11.5px !important;
        margin-bottom: 10px !important;
      }
    }
"""

rtl_style = """
    body[dir="rtl"] { direction: rtl; text-align: right; }
    body[dir="rtl"] .breadcrumb-nav { flex-direction: row-reverse; justify-content: flex-end; }
    body[dir="rtl"] .breadcrumb-nav .sep { transform: scaleX(-1); }
    body[dir="rtl"] .share-buttons { margin-right: auto; margin-left: 0; justify-content: flex-start; }
    body[dir="rtl"] .related-articles-header { flex-direction: row-reverse; }
    body[dir="rtl"] .related-card-arrow svg { transform: scaleX(-1); }
    body[dir="rtl"] .article-body blockquote, body[dir="rtl"] .article-quote {
      border-left: none !important;
      border-right: 3px solid #523225 !important;
      padding-left: 0 !important;
      padding-right: 24px !important;
    }
    @media (max-width: 768px) {
      body[dir="rtl"] .article-body blockquote, body[dir="rtl"] .article-quote {
        padding-right: 14px !important;
      }
    }
"""

clean_articles_content = {}

for filename in articles_meta.keys():
    en_path = f"en/blog/{filename}"
    with open(en_path, "r", encoding="utf-8") as f:
        html = f.read()

    m = re.search(r'<article class="article-body-wrap">\s*<div class="article-body">(.*?)(</div>\s*</article>|</article>)', html, flags=re.DOTALL)
    if not m:
        m = re.search(r'<article[^>]*>(.*?)</article>', html, flags=re.DOTALL)
    
    if m:
        raw_body = m.group(1).strip()
        raw_body = re.sub(r'<div class="(article-experience-inset|article-cta-box)">.*?</div>\s*(</div>)?', '', raw_body, flags=re.DOTALL)
        raw_body = re.sub(r'<div class="related-grid">.*', '', raw_body, flags=re.DOTALL)
        raw_body = re.sub(r'<div class="article-tags-wrap">.*', '', raw_body, flags=re.DOTALL)
        raw_body = re.sub(r'<section class="related-articles-section".*', '', raw_body, flags=re.DOTALL)
        clean_articles_content[filename] = raw_body.strip()
        print(f"Extracted {filename}: {len(clean_articles_content[filename])} chars")
    else:
        print(f"Error extracting {filename}")

def generate_article_page(filename, lang):
    t = ui_translations[lang]
    meta = articles_meta[filename]
    m = meta[lang]
    slug = meta["slug"]
    image = meta["image"]
    date_iso = meta["date"]
    read_time = meta["read_time"]

    is_rtl = (lang == "ar")
    dir_attr = ' dir="rtl"' if is_rtl else ''
    
    cta_html = f"""<div class="article-cta-box">
        <h3>{t['cta_title']}</h3>
        <p>{t['cta_desc']}</p>
        <a href="{t['cta_url']}" class="article-cta-btn">{t['cta_btn']}</a>
      </div>"""

    body_content = f"{clean_articles_content[filename]}\n\n      {cta_html}"

    other_slugs = [k for k in articles_meta.keys() if k != filename][:3]
    related_cards_html = ""
    for r_filename in other_slugs:
        r_meta = articles_meta[r_filename]
        r_m = r_meta[lang]
        related_cards_html += f"""
        <a class="related-card" href="{r_filename}">
          <div class="related-card-img-wrap">
            <img src="{r_meta['image']}" alt="{r_m['title']}" width="420" height="260" loading="lazy" decoding="async">
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

    nav = t["nav_links"]
    css_block = master_css + (rtl_style if is_rtl else "")

    return f"""<!DOCTYPE html>
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
{css_block}
  </style>
</head>

<body class="blog">
  <div id="reading-progress-bar" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
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
        <li class="current">{m['category']}</li>
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
</html>"""

# Generate ALL 28 articles with clean single CSS block & flawless responsive markup
for filename in articles_meta.keys():
    for lang in ["en", "fr", "es", "ar"]:
        html_out = generate_article_page(filename, lang)
        target_path = f"{lang}/blog/{filename}"
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(html_out)
        print(f"Clean rebuilt {target_path}")

print("\nAll 28 articles clean rebuilt with 100% responsive perfection!")
