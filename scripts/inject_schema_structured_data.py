import json
import re
import os

schema_definitions = {
    "packages/comfort.html": {
        "price": "49.00",
        "rating": "4.9",
        "reviews": 154,
        "image": "https://marragafay.com/images/activites/quad.webp",
        "names": {
            "en": "Agafay Desert Tour with Quad, Camel Ride & Dinner (Signature Pack)",
            "fr": "Excursion Désert d'Agafay avec Quad, Dromadaire & Dîner (Pack Signature)",
            "es": "Excursión al Desierto de Agafay con Quad, Camello y Cena (Pack Signature)",
            "ar": "رحلة صحراء أكافاي مع كواد، ركوب الجمال وعشاء بدوي (باقة سيغنتشر)"
        },
        "descriptions": {
            "en": "Experience the definitive half-day Agafay Desert tour from Marrakech with quad biking, sunset camel ride, swimming pool, and Moroccan dinner show.",
            "fr": "Excursion complète dans le désert d'Agafay depuis Marrakech avec quad, balade en dromadaire au coucher du soleil, piscine et dîner spectacle.",
            "es": "Excursión completa al desierto de Agafay desde Marrakech con quad, paseo en camello al atardecer, piscina y cena espectáculo tradicional.",
            "ar": "رحلة شاملة إلى صحراء أكافاي من مراكش تشمل قيادة الكواد، ركوب الجمال وقت الغروب، مسبح وعشاء مع عرض ناري ساحر."
        }
    },
    "packages/luxe.html": {
        "price": "120.00",
        "rating": "5.0",
        "reviews": 89,
        "image": "https://marragafay.com/images/activites/show.webp",
        "names": {
            "en": "Private VIP Agafay Desert Experience",
            "fr": "Expérience Privée VIP dans le Désert d'Agafay",
            "es": "Experiencia Privada VIP en el Desierto de Agafay",
            "ar": "تجربة خاصة VIP في صحراء أكافاي"
        },
        "descriptions": {
            "en": "Exclusive private VIP tour to Agafay Desert with dedicated luxury 4x4 transport, private chauffeur, private quad guide, and VIP fireside dinner.",
            "fr": "Excursion privée VIP dans le désert d'Agafay avec transport 4x4 de luxe, chauffeur privé, guide de quad particulier et dîner VIP.",
            "es": "Tour privado VIP al desierto de Agafay con transporte en 4x4 de lujo, chofer dedicado, guía de quad exclusivo y cena gourmet.",
            "ar": "رحلة خاصة VIP إلى صحراء أكافاي تشمل سيارة 4x4 فاخرة مع سائق خاص، كواد خاص، وعشاء رومانسي فاخر تحت النجوم."
        }
    },
    "packages/basic.html": {
        "price": "35.00",
        "rating": "4.8",
        "reviews": 112,
        "image": "https://marragafay.com/images/activites/quad.webp",
        "names": {
            "en": "Agafay Desert Discovery Tour",
            "fr": "Excursion Découverte du Désert d'Agafay",
            "es": "Tour Descubrimiento del Desierto de Agafay",
            "ar": "جولة استكشاف صحراء أكافاي"
        },
        "descriptions": {
            "en": "Accessible half-day tour to Agafay with Marrakech transfers, quad biking, camel trekking, and Moroccan tea ceremony.",
            "fr": "Formule idéale en demi-journée pour découvrir Agafay : quad sur les pistes, dromadaire et thé marocain traditionnel.",
            "es": "Emocionante excursión de medio día a Agafay con traslados, quad, paseo en camello y té en campamento tradicional.",
            "ar": "جولة مميزة لنصف يوم في صحراء أكافاي تشمل النقل من مراكش، قيادة الكواد، ركوب الجمال وجلسة شاي مغربي."
        }
    },
    "activities/quad-biking.html": {
        "price": "25.00",
        "rating": "4.9",
        "reviews": 230,
        "image": "https://marragafay.com/images/activites/quad.webp",
        "names": {
            "en": "Agafay Desert Quad Biking Tour",
            "fr": "Randonnée Quad dans le Désert d'Agafay",
            "es": "Tour en Quad por el Desierto de Agafay",
            "ar": "جولة الكواد في صحراء أكافاي"
        },
        "descriptions": {
            "en": "High-adrenaline quad biking expedition across Agafay Desert trails with certified guides, Yamaha ATVs, and Marrakech hotel pickup.",
            "fr": "Randonnée en quad tout-terrain dans le désert d'Agafay avec équipement complet de sécurité, guides certifiés et transferts hôtel.",
            "es": "Aventura en quad por los senderos del desierto de Agafay con vehículos de alta gama, guías certificados y transporte incluido.",
            "ar": "مغامرة قيادة دراجات الكواد السريعة عبر تلال ومسارات صحراء أكافاي مع مرشدين محترفين ونقل من الفندق."
        }
    },
    "activities/camel-ride.html": {
        "price": "10.00",
        "rating": "4.8",
        "reviews": 195,
        "image": "https://marragafay.com/images/Slider-images/slider-3.webp",
        "names": {
            "en": "Sunset Camel Ride in Agafay Desert",
            "fr": "Balade en Dromadaire au Coucher du Soleil à Agafay",
            "es": "Paseo en Camello al Atardecer en Agafay",
            "ar": "جولة ركوب الجمال وقت الغروب في أكافاي"
        },
        "descriptions": {
            "en": "Tranquil camel trek through the rocky desert at sunset with traditional nomadic cheich attire, mint tea, and hotel pickup.",
            "fr": "Balade authentique en dromadaire au coucher du soleil dans le désert d'Agafay avec tenue nomade et thé marocain.",
            "es": "Paseo tradicional en camello al atardecer por las colinas áridas de Agafay con atuendo bereber y té a la menta.",
            "ar": "جولة ركوب الجمال الهادئة وقت غروب الشمس عبر صحراء أكافاي بالزي الصحراوي الأصيل مع جلسة شاي مغربي."
        }
    },
    "activities/dinner-show.html": {
        "price": "15.00",
        "rating": "4.9",
        "reviews": 178,
        "image": "https://marragafay.com/images/activites/show.webp",
        "names": {
            "en": "Agafay Desert Dinner & Live Show",
            "fr": "Dîner Spectacle dans le Désert d'Agafay",
            "es": "Cena con Espectáculo en el Desierto de Agafay",
            "ar": "عشاء وعرض فني في صحراء أكافاي"
        },
        "descriptions": {
            "en": "Authentic Moroccan gastronomic dinner under the stars in Agafay with live fire spectacle, Gnawa music, and campfire.",
            "fr": "Dîner marocain raffiné sous les étoiles d'Agafay avec spectacle de cracheurs de feu, musiciens traditionnels et feu de camp.",
            "es": "Cena gastronómica marroquí bajo el cielo estrellado de Agafay con espectáculo de fuego en vivo y música tradicional.",
            "ar": "عشاء مغربي فاخر تحت نجوم صحراء أكافاي مع عروض النار الحية والموسيقى الفلكلورية حول موقد النار."
        }
    },
    "activities/buggy.html": {
        "price": "80.00",
        "rating": "5.0",
        "reviews": 94,
        "image": "https://marragafay.com/images/activites/buggy.webp",
        "names": {
            "en": "Agafay Desert Dune Buggy Tour",
            "fr": "Aventure en Buggy dans le Désert d'Agafay",
            "es": "Tour en Buggy por el Desierto de Agafay",
            "ar": "مغامرة البوغي في صحراء أكافاي"
        },
        "descriptions": {
            "en": "Drive high-powered off-road buggies through rugged Agafay canyons and desert trails with certified instructors.",
            "fr": "Pilotage de buggys performants dans les canyons d'Agafay avec encadrement professionnel et transferts inclus.",
            "es": "Conducción de buggies todoterreno de alta potencia por cañones y pistas del desierto con instructores titulados.",
            "ar": "قيادة مركبات البوغي القوية عبر التضاريس والوديان الصخرية لصحراء أكافاي برفقة طاقم تدريب محترف."
        }
    },
    "activities/hot-air-balloon.html": {
        "price": "100.00",
        "rating": "5.0",
        "reviews": 67,
        "image": "https://marragafay.com/images/activites/ballon.webp",
        "names": {
            "en": "Marrakech & Agafay Hot Air Balloon Flight",
            "fr": "Vol en Montgolfière au Lever du Soleil à Marrakech",
            "es": "Vuelo en Globo Aerostático al Amanecer Marrakech",
            "ar": "رحلة المنطاد الهوائي مع شروق الشمس"
        },
        "descriptions": {
            "en": "Sunrise hot air balloon flight over Agafay Desert with panoramic High Atlas views and traditional Berber breakfast.",
            "fr": "Vol en montgolfière au lever du jour au-dessus du désert avec vue panoramique sur l'Atlas et petit-déjeuner berbère.",
            "es": "Vuelo en globo aerostático al amanecer sobre el desierto de Agafay con desayuno tradicional bereber incluido.",
            "ar": "رحلة منطاد هوائي عند شروق الشمس فوق صحراء أكافاي مع إطلالة بانورامية على جبال الأطلس وفطور مغربي أصيل."
        }
    },
    "activities/paragliding.html": {
        "price": "65.00",
        "rating": "4.8",
        "reviews": 52,
        "image": "https://marragafay.com/images/activites/paragliding.webp",
        "names": {
            "en": "Agafay Desert Paragliding Adventure",
            "fr": "Vol en Parapente dans le Désert d'Agafay",
            "es": "Aventura de Parapente en el Desierto de Agafay",
            "ar": "مغامرة الطيران الشراعي في صحراء أكافاي"
        },
        "descriptions": {
            "en": "Tandem paragliding flight over the Agafay plateau with licensed professional pilots and mountain views.",
            "fr": "Vol en parapente biplace au-dessus du plateau d'Agafay avec pilotes professionnels certifiés.",
            "es": "Vuelo en parapente biplaza sobre el desierto de Agafay con pilotos certificados y vistas panorámicas.",
            "ar": "رحلة طيران شراعي ثنائي في سماء صحراء أكافاي رفقة طيارين محترفين معتمدين دولياً."
        }
    }
}

for rel_path, data in schema_definitions.items():
    for lang in ["en", "fr", "es", "ar"]:
        fpath = f"{lang}/{rel_path}"
        if not os.path.exists(fpath):
            continue

        clean_slug = rel_path.replace(".html", "")
        page_url = f"https://marragafay.com/{lang}/{clean_slug}"
        prod_name = data["names"][lang]
        prod_desc = data["descriptions"][lang]

        schema_json = {
            "@context": "https://schema.org",
            "@type": "Product",
            "name": prod_name,
            "image": [data["image"]],
            "description": prod_desc,
            "sku": f"MAR-{clean_slug.upper()}",
            "brand": {
                "@type": "Brand",
                "name": "Marragafay"
            },
            "offers": {
                "@type": "Offer",
                "url": page_url,
                "priceCurrency": "EUR",
                "price": data["price"],
                "priceValidUntil": "2027-12-31",
                "availability": "https://schema.org/InStock",
                "seller": {
                    "@type": "Organization",
                    "name": "Marragafay",
                    "url": "https://marragafay.com"
                }
            },
            "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": data["rating"],
                "bestRating": "5",
                "worstRating": "1",
                "ratingCount": str(data["reviews"]),
                "reviewCount": str(data["reviews"])
            }
        }

        json_ld_str = f'<script type="application/ld+json">\n{json.dumps(schema_json, indent=2, ensure_ascii=False)}\n</script>'

        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()

        # Remove existing product schema if any
        html = re.sub(r'<script type="application/ld\+json">.*?Product.*?</script>\n?', '', html, flags=re.DOTALL)

        # Inject before </head>
        if "</head>" in html:
            html = html.replace("</head>", f"{json_ld_str}\n</head>", 1)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"Injected Product Schema (Rating: {data['rating']}★ / Price: €{data['price']}) into {fpath}")

print("\nAll Money Pages successfully equipped with Rich Snippets (Schema.org JSON-LD)!")
