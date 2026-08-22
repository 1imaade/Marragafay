import os
import re
import glob

# Master translations dictionary for common layout strings
ui_translations = {
    "fr": {
        "lang_code": "fr",
        "dir": "ltr",
        "home": "Accueil",
        "journal": "La Revue",
        "booking": "Réservation",
        "read_time_suffix": "min de lecture",
        "filed_under": "Classé dans",
        "continue_reading": "Poursuivre la lecture",
        "all_articles": "Tous les Articles →",
        "read_article": "Lire l'Article",
        "share_copy": "Copier le lien",
        "share_copied": "Lien copié dans le presse-papiers !",
        "author": "Rédaction Marragafay",
        "tagline": "Redéfinir l'expérience du désert de pierre d'Agafay. Un luxe sans compromis, des flottes exclusives et une expertise locale certifiée.",
        "inquiries": "Renseignements",
        "navigate": "Navigation",
        "legal": "Mentions Légales",
        "social": "Réseaux Sociaux",
        "rights": "© 2026 MARRAGAFAY. TOUS DROITS RÉSERVÉS.",
        "engineered": "CONÇU À MARRAKECH.",
        "cta_title": "Vivez l'Expérience Agafay avec Marragafay",
        "cta_text": "Dîners privés dans le désert, aventures en quad et balades à dos de chameau au coucher du soleil — créés pour ceux qui recherchent des moments extraordinaires.",
        "cta_btn": "Explorer les Expériences",
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
        "dir": "ltr",
        "home": "Inicio",
        "journal": "El Diario",
        "booking": "Reservar",
        "read_time_suffix": "min de lectura",
        "filed_under": "Archivado en",
        "continue_reading": "Continuar Leyendo",
        "all_articles": "Todos los Artículos →",
        "read_article": "Leer Artículo",
        "share_copy": "Copiar enlace",
        "share_copied": "¡Enlace copiado al portapapeles!",
        "author": "Equipo Editorial Marragafay",
        "tagline": "Redefiniendo la experiencia en el desierto de piedra de Agafay. Lujo sin concesiones, flotas exclusivas y experiencia local certificada.",
        "inquiries": "Consultas",
        "navigate": "Navegación",
        "legal": "Legal",
        "social": "Social",
        "rights": "© 2026 MARRAGAFAY. TODOS LOS DERECHOS RESERVADOS.",
        "engineered": "DISEÑADO EN MARRAKECH.",
        "cta_title": "Vive la Experiencia Agafay con Marragafay",
        "cta_text": "Cenas privadas en el desierto, aventuras en quad y paseos en camello al atardecer: seleccionados para quienes buscan experiencias extraordinarias.",
        "cta_btn": "Explorar Experiencias",
        "nav_links": {
            "Home": "Inicio",
            "Activities": "Actividades",
            "Packs": "Packs",
            "About": "Nosotros",
            "Reviews": "Reseñas",
            "Journal": "El Diario",
            "Contact": "Contacto",
            "Booking": "Reservar"
        }
    },
    "ar": {
        "lang_code": "ar",
        "dir": "rtl",
        "home": "الرئيسية",
        "journal": "المجلة",
        "booking": "الحجز",
        "read_time_suffix": "دقائق قراءة",
        "filed_under": "تصنيف المقال",
        "continue_reading": "متابعة القراءة",
        "all_articles": "← جميع المقالات",
        "read_article": "اقرأ المقال",
        "share_copy": "نسخ الرابط",
        "share_copied": "!تم نسخ الرابط بنجاح",
        "author": "فريق تحرير مراكافاي",
        "tagline": "إعادة صياغة تجربة صحراء أكافاي الحجرية. فخامة مطلقة، أسطول حصري، وخبرة محلية معتمدة.",
        "inquiries": "الاستفسارات",
        "navigate": "تصفح الموقع",
        "legal": "الشروط والأحكام",
        "social": "التواصل الاجتماعي",
        "rights": "© 2026 MARRAGAFAY. جميع الحقوق محفوظة.",
        "engineered": "صُمم في مراكش.",
        "cta_title": "عش تجربة أكافاي الفاخرة مع مراكافاي",
        "cta_text": "عشاء صحراوي خاص، مغامرات بالدراجات الرباعية، وجولات على الجمال وقت الغروب — مصممة خصيصاً للباحثين عن التميز.",
        "cta_btn": "استكشف التجارب",
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

# Metadata translations for all 7 articles
articles_meta = {
    "agafay-desert-guide.html": {
        "slug": "agafay-desert-guide",
        "date": "2026-08-01",
        "date_str_en": "August 2026",
        "read_time": "8",
        "category_en": "Desert Guide",
        "image": "/images/Slider-images/slider-1.webp",
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
        "date_str_en": "August 2026",
        "read_time": "5",
        "category_en": "Experience",
        "image": "/images/Slider-images/slider-3.webp",
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
        "date_str_en": "July 2026",
        "read_time": "6",
        "category_en": "Culture",
        "image": "/images/gallery/gal4.webp",
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
        "date_str_en": "July 2026",
        "read_time": "4",
        "category_en": "Travel Tips",
        "image": "/images/gallery/gal1.webp",
        "fr": {
            "title": "De Marrakech au Désert d'Agafay : Tous les Moyens de Transport",
            "subtitle": "Transfert privé, location ou taxi : itinéraire détaillé pour parcourir les 45 km séparant la ville du désert.",
            "category": "Conseils Voyage",
            "date_str": "Juillet 2026",
            "meta_desc": "Comment se rendre au désert d'Agafay depuis Marrakech : prix, durées, options de transport privé et conseils d'itinéraire."
        },
        "es": {
            "title": "De Marrakech al Desierto de Agafay: Todas las Formas de Llegar",
            "subtitle": "Traslados privados, alquiler de coches o taxi: guía completa para recorrer los 45 km hasta el desierto.",
            "category": "Logística de Viaje",
            "date_str": "Julio 2026",
            "meta_desc": "Cómo llegar al desierto de Agafay desde Marrakech: precios, tiempos de viaje, opciones privadas y consejos de ruta."
        },
        "ar": {
            "title": "من مراكش إلى صحراء أكافاي: كافة خيارات التنقل والمواصلات",
            "subtitle": "نقل خاص، سيارة أجرة أو قيادة ذاتية: تفاصيل رحلة الـ 45 كيلومتراً الفاصلة بين المدينة والهدوء.",
            "category": "نصائح السفر",
            "date_str": "يوليو 2026",
            "meta_desc": "كيفية الوصول إلى صحراء أكافاي من مراكش: التكاليف، أوقات الرحلة، خيارات النقل الخاص الفاخر، وأفضل المسارات."
        }
    },
    "agafay-dinner-experience.html": {
        "slug": "agafay-dinner-experience",
        "date": "2026-06-28",
        "date_str_en": "June 2026",
        "read_time": "7",
        "category_en": "Experience",
        "image": "/images/activites/show.webp",
        "fr": {
            "title": "L'Expérience Dîner à Agafay : Gastronomie et Luxe sous le Ciel Étoilé",
            "subtitle": "Pourquoi un dîner privé aux chandelles dans le désert est devenu le rituel le plus prisé de Marrakech.",
            "category": "Expérience Nocturne",
            "date_str": "Juin 2026",
            "meta_desc": "Découvrez l'expérience exclusive d'un dîner gastronomique privé dans le désert d'Agafay sous le ciel étoilé du Maroc."
        },
        "es": {
            "title": "Cena en el Desierto de Agafay: Lujo Gastronómico bajo el Cielo Marroquí",
            "subtitle": "Por qué una cena privada a la luz de las velas es la experiencia nocturna más solicitada.",
            "category": "Experiencias Nocturnas",
            "date_str": "Junio 2026",
            "meta_desc": "Descubre la experiencia exclusiva de una cena privada gourmet en el desierto de Agafay bajo el cielo estrellado."
        },
        "ar": {
            "title": "تجربة العشاء في أكافاي: فخامة استثنائية تحت سماء المغرب المتلألئة",
            "subtitle": "كيف أصبح العشاء الخاص على ضوء الشموع في قلب الصحراء التجربة المسائية الأكثر تميزاً في مراكش.",
            "category": "تجارب مسائية",
            "date_str": "يونيو 2026",
            "meta_desc": "اكتشف تجربة العشاء الفاخر والخاص في صحراء أكافاي: أجواء استثنائية على ضوء الشموع ومأكولات مغربية راقية."
        }
    },
    "agafay-quad-biking-guide.html": {
        "slug": "agafay-quad-biking-guide",
        "date": "2026-08-15",
        "date_str_en": "August 2026",
        "read_time": "6",
        "category_en": "Experience",
        "image": "/images/activites/quad.webp",
        "fr": {
            "title": "Quad dans le Désert d'Agafay : Sécurité, Conseils et Itinéraires Panoramiques",
            "subtitle": "Tout pour piloter en toute sérénité à travers les crêtes et canyons minéraux du plateau.",
            "category": "Aventure & Pistes",
            "date_str": "Août 2026",
            "meta_desc": "Guide complet du quad dans le désert d'Agafay : conseils de sécurité, équipement fourni, circuits panoramiques et machines 4x4."
        },
        "es": {
            "title": "Rutas en Quad por el Desierto de Agafay: Guía de Seguridad y Recorridos",
            "subtitle": "Todo lo necesario para pilotar con seguridad a través de los cañones y colinas de piedra.",
            "category": "Rutas de Aventura",
            "date_str": "Agosto 2026",
            "meta_desc": "Guía completa para pilotar quads en el desierto de Agafay: seguridad, equipo necesario, circuitos panorámicos y consejos."
        },
        "ar": {
            "title": "قيادة الكواد في صحراء أكافاي: إرشادات السلامة وأفضل المسارات البانورامية",
            "subtitle": "كل ما تحتاج معرفته لخوض مغامرة الدراجات الرباعية 4x4 عبر تلال ووديان أكافاي الحجرية.",
            "category": "مغامرات الدراجات",
            "date_str": "أغسطس 2026",
            "meta_desc": "دليل شامل لقيادة دراجات الكواد في صحراء أكافاي: تدابير السلامة، المعدات، وأفضل المسارات الصحراوية المشوقة."
        }
    },
    "agafay-desert-vs-sahara.html": {
        "slug": "agafay-desert-vs-sahara",
        "date": "2026-08-05",
        "date_str_en": "August 2026",
        "read_time": "7",
        "category_en": "Desert Guide",
        "image": "/images/Slider-images/slider-2.webp",
        "fr": {
            "title": "Désert d'Agafay ou Sahara : Quel Désert Choisir lors de Votre Séjour ?",
            "subtitle": "Comparatif détaillé : temps de trajet, paysages, confort et activités pour faire le bon choix.",
            "category": "Guide du Désert",
            "date_str": "Août 2026",
            "meta_desc": "Agafay contre le Sahara : comparatif complet du temps de trajet, du coût, des paysages et du niveau de confort pour votre voyage au Maroc."
        },
        "es": {
            "title": "¿Desierto de Agafay o el Sahara? Cuál Elegir para tu Viaje a Marruecos",
            "subtitle": "Comparativa completa: tiempos de viaje, paisajes, comodidades y experiencias.",
            "category": "Guía del Desierto",
            "date_str": "Agosto 2026",
            "meta_desc": "Agafay vs Sáhara: comparativa detallada de tiempo de viaje, costes, paisajes y confort para elegir la mejor opción en Marruecos."
        },
        "ar": {
            "title": "صحراء أكافاي أم الصحراء الكبرى؟ أيهما تختار لرحلتك في المغرب؟",
            "subtitle": "مقارنة شاملة: مدة الرحلة، طبيعة التضاريس، مستوى الراحة الفاخرة، والأنشطة المتاحة.",
            "category": "دليل الصحراء",
            "date_str": "أغسطس 2026",
            "meta_desc": "مقارنة دقيقة بين صحراء أكافاي الحجرية والصحراء الكبرى: الفروقات في المسافة، التكاليف، الراحة والأنشطة لتختار الأنسب لرحلتك."
        }
    }
}

print(f"Loaded {len(articles_meta)} articles configuration.")
