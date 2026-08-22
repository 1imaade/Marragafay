import re
import os

seo_data = {
    # 1. Packages
    "packages/comfort.html": {
        "en": {
            "title": "Agafay Desert Tour from Marrakech | Quad, Camel & Dinner | Marragafay",
            "meta_desc": "Book the ultimate Agafay Desert tour from Marrakech with 1h quad biking, sunset camel ride, swimming pool access, and Moroccan dinner show. Pay on-site with Marragafay.",
            "h1": "Agafay Desert Tour with Quad, Camel Ride & Dinner",
            "intro": "Experience the definitive half-day Agafay Desert tour from Marrakech. Includes hotel pickup, quad biking across stone desert trails, a sunset camel trek, and an unforgettable Moroccan dinner show under the stars."
        },
        "fr": {
            "title": "Excursion Désert d'Agafay depuis Marrakech | Quad, Dromadaire & Dîner | Marragafay",
            "meta_desc": "Réservez l'excursion complète dans le désert d'Agafay depuis Marrakech : quad, balade en dromadaire au coucher du soleil, piscine et dîner spectacle. Paiement sur place.",
            "h1": "Excursion Désert d'Agafay avec Quad, Dromadaire & Dîner",
            "intro": "Vivez l'expérience incontournable du désert d'Agafay au départ de Marrakech. Transfert inclus, 1h de quad sur les pistes minérales, balade en dromadaire au coucher du soleil et dîner spectacle féerique sous les étoiles."
        },
        "es": {
            "title": "Excursión al Desierto de Agafay desde Marrakech | Quad, Camello y Cena | Marragafay",
            "meta_desc": "Reserve la mejor excursión al desierto de Agafay desde Marrakech: quad, paseo en camello al atardecer, piscina y cena espectáculo marroquí. Pago en el lugar.",
            "h1": "Excursión al Desierto de Agafay con Quad, Camello y Cena",
            "intro": "Disfrute de la excursión más completa al desierto de Agafay desde Marrakech. Incluye recogida en su hotel, quad por las colinas áridas, paseo en camello al atardecer y cena tradicional con espectáculo de fuego."
        },
        "ar": {
            "title": "رحلة صحراء أكافاي من مراكش | كواد، ركوب الجمال وعشاء مغربي | مراكافاي",
            "meta_desc": "احجز أفضل رحلة إلى صحراء أكافاي من مراكش: جولة كواد لمدة ساعة، ركوب الجمال وقت الغروب، مسبح وعشاء مع عرض ناري ساحر. الدفع في الموقع.",
            "h1": "رحلة صحراء أكافاي مع كواد، ركوب الجمال وعشاء بدوي",
            "intro": "عش تجربة صحراوية لا تُنسى في صحراء أكافاي انطلاقاً من مراكش. تشمل النقل من فندقك، قيادة الكواد عبر المسارات الحجرية، جولة على الجمال وقت الغروب، وعشاءً مغربياً أصيلاً تحت قبة النجوم."
        }
    },
    "packages/luxe.html": {
        "en": {
            "title": "Private Agafay Desert Tour from Marrakech | VIP Experience | Marragafay",
            "meta_desc": "Book an exclusive private VIP tour to Agafay Desert from Marrakech. Dedicated luxury 4x4 transport, private quad biking, sunset camel ride, and VIP fireside dinner.",
            "h1": "Private VIP Agafay Desert Experience",
            "intro": "The pinnacle of desert luxury. Travel by private air-conditioned 4x4 with your personal chauffeur, enjoy dedicated private quad guides, and relax at an exclusive desert camp with gourmet gastronomy."
        },
        "fr": {
            "title": "Excursion Privée VIP Désert d'Agafay depuis Marrakech | Marragafay",
            "meta_desc": "Réservez votre excursion privée VIP dans le désert d'Agafay. Transport 4x4 haut de gamme avec chauffeur privé, quad exclusif, dromadaire et dîner VIP sous les étoiles.",
            "h1": "Expérience Privée VIP dans le Désert d'Agafay",
            "intro": "Le summum du luxe dans le désert. Transfert privé en 4x4 climatisé avec chauffeur dédié, guide de quad particulier et dîner gastronomique exclusif au coin du feu sous les étoiles."
        },
        "es": {
            "title": "Tour Privado VIP al Desierto de Agafay desde Marrakech | Marragafay",
            "meta_desc": "Reserve un tour privado VIP exclusivo al desierto de Agafay. Transporte privado en 4x4 de lujo, quad privado, paseo en camello y cena gourmet junto al fuego.",
            "h1": "Experiencia Privada VIP en el Desierto de Agafay",
            "intro": "La máxima exclusividad en el desierto. Viaje en 4x4 privado con chofer dedicado, disfrute de guías de quad exclusivos y relájese en un campamento privado con cena gourmet."
        },
        "ar": {
            "title": "رحلة خاصة VIP إلى صحراء أكافاي من مراكش | تجربة فاخرة | مراكافاي",
            "meta_desc": "احجز رحلتك الخاصة VIP إلى صحراء أكافاي من مراكش. نقل خاص بسيارة 4x4 فاخرة مع سائق خاص، كواد خاص، ركوب الجمال وعشاء رومانسي فاخر.",
            "h1": "تجربة خاصة VIP في صحراء أكافاي",
            "intro": "قمة الفخامة والخصوصية في الصحراء. تنقل بسيارة 4x4 مكيفة وخاصة مع سائقك المخصص، واستمتع بجولة كواد خاصة وعشاء مغربي راقٍ على ضوء الشموع والنجوم."
        }
    },
    "packages/basic.html": {
        "en": {
            "title": "Agafay Desert Discovery Day Trip from Marrakech | Marragafay",
            "meta_desc": "Explore the stone desert with the Agafay Discovery Day Trip. Includes Marrakech transfers, quad biking, camel trekking, and tea at a traditional desert camp.",
            "h1": "Agafay Desert Discovery Tour",
            "intro": "An accessible and thrilling half-day introduction to Morocco's stone desert. Ride high-performance quads across barren hills and experience a peaceful camel trek with mountain views."
        },
        "fr": {
            "title": "Journée Découverte du Désert d'Agafay depuis Marrakech | Marragafay",
            "meta_desc": "Découvrez le désert de pierre avec l'excursion Agafay Découverte. Transfert depuis Marrakech, quad, dromadaire et pause thé dans un camp traditionnel.",
            "h1": "Excursion Découverte du Désert d'Agafay",
            "intro": "Une formule idéale pour découvrir la beauté minérale d'Agafay en demi-journée. Quad sur les crêtes rocheuses, balade en dromadaire et thé traditionnel face aux montagnes de l'Atlas."
        },
        "es": {
            "title": "Excursión de un Día al Desierto de Agafay desde Marrakech | Marragafay",
            "meta_desc": "Descubra el desierto mineral con el tour Agafay Discovery. Incluye traslados desde Marrakech, quad, paseo en camello y té en campamento tradicional.",
            "h1": "Tour Descubrimiento del Desierto de Agafay",
            "intro": "Una emocionante introducción de medio día al desierto de piedra de Marruecos. Recorra senderos en quad y disfrute de un tranquilo paseo en camello con vistas panorámicas."
        },
        "ar": {
            "title": "جولة استكشاف صحراء أكافاي من مراكش | نصف يوم | مراكافاي",
            "meta_desc": "استكشف الصحراء الصخرية مع جولة أكافاي ديسكفري. تشمل النقل من مراكش، قيادة الكواد، ركوب الجمال وجلسة شاي مغربي في مخيم صحراوي.",
            "h1": "جولة استكشاف صحراء أكافاي",
            "intro": "المدخل المثالي لاكتشاف سحر صحراء أكافاي في نصف يوم. مغامرة كواد ممتعة عبر التلال وجولة على الجمال مع إطلالة خلابة على جبال الأطلس الكبير."
        }
    },
    "packs.html": {
        "en": {
            "title": "Agafay Desert Tour Packages & Experiences from Marrakech | Marragafay",
            "meta_desc": "Browse all-inclusive Agafay Desert tour packages from Marrakech. Compare Signature, Luxury VIP, and Discovery bundles with quad biking, camel rides, and dinners.",
            "h1": "Agafay Desert Tour Packages",
            "intro": "Curated multi-experience bundles combining high-adrenaline quad adventures with authentic fireside dining."
        },
        "fr": {
            "title": "Packs & Forfaits Excursions Désert d'Agafay Marrakech | Marragafay",
            "meta_desc": "Découvrez nos forfaits tout compris dans le désert d'Agafay : Pack Signature, VIP Privé et Découverte avec quad, dromadaire, piscine et dîner spectacle.",
            "h1": "Forfaits & Packs Désert d'Agafay",
            "intro": "Des formules combinées complètes alliant le frisson du quad tout-terrain et la magie d'un dîner sous les étoiles."
        },
        "es": {
            "title": "Paquetes y Excursiones al Desierto de Agafay Marrakech | Marragafay",
            "meta_desc": "Compare nuestros paquetes todo incluido para el desierto de Agafay: Pack Signature, VIP Privado y Discovery con quad, camello, piscina y cena espectáculo.",
            "h1": "Paquetes de Excursión en Agafay",
            "intro": "Paquetes completos que combinan emocionantes aventuras en quad con auténticas cenas bajo las estrellas."
        },
        "ar": {
            "title": "باقات وعروض رحلات صحراء أكافاي من مراكش | مراكافاي",
            "meta_desc": "تصفح باقات الرحلات الشاملة في صحراء أكافاي من مراكش: باقة سيغنتشر، باقة VIP الخاصة، وباقة الاستكشاف مع الكواد والجمال والعشاء الفاخر.",
            "h1": "باقات رحلات صحراء أكافاي",
            "intro": "باقات متكاملة تجمع بين إثارة مغامرات الكواد وسحر العشاء البدوي الفاخر تحت سماء الصحراء."
        }
    },

    # 2. Activities
    "activities/quad-biking.html": {
        "en": {
            "title": "Quad Biking in Agafay Desert from Marrakech | Marragafay",
            "meta_desc": "Book an exhilarating quad biking tour in the Agafay Desert near Marrakech. Yamaha & Can-Am ATVs, certified guides, safety gear, and hotel pickup included.",
            "h1": "Agafay Desert Quad Biking Tour",
            "intro": "Conquer the rugged limestone plateaus and dry riverbeds of Agafay on high-powered ATVs. Guided by native certified instructors with full safety briefing and hotel transfers."
        },
        "fr": {
            "title": "Quad dans le Désert d'Agafay depuis Marrakech | Marragafay",
            "meta_desc": "Réservez votre randonnée en quad dans le désert d'Agafay. Véhicules récents, guides certifiés, équipement de sécurité et transferts hôtel inclus.",
            "h1": "Randonnée Quad dans le Désert d'Agafay",
            "intro": "Domptez les pistes minérales et les collines rocheuses d'Agafay au guidon de quads puissants et récents, encadré par des guides locaux certifiés."
        },
        "es": {
            "title": "Quad en el Desierto de Agafay desde Marrakech | Marragafay",
            "meta_desc": "Reserve su tour en quad por el desierto de Agafay. ATVs de alta gama, guías certificados, equipo de seguridad y transporte desde su hotel en Marrakech.",
            "h1": "Tour en Quad por el Desierto de Agafay",
            "intro": "Sienta la adrenalina recorriendo los cañones y colinas del desierto de piedra con quads de última generación y guías profesionales locales."
        },
        "ar": {
            "title": "جولة الكواد في صحراء أكافاي من مراكش | دراجات رباعية | مراكافاي",
            "meta_desc": "احجز جولة قيادة الدراجات الرباعية (كواد) في صحراء أكافاي قرب مراكش. آليات حديثة، مرشدون معتمدون، خوذات واقية ونقل من الفندق.",
            "h1": "جولة الكواد في صحراء أكافاي",
            "intro": "عش قمة الإثارة والمغامرة عبر تلال وهضاب صحراء أكافاي الصخرية على متن أحدث الدراجات الرباعية وتحت إشراف مرشدين محليين محترفين."
        }
    },
    "activities/camel-ride.html": {
        "en": {
            "title": "Sunset Camel Ride in Agafay Desert Marrakech | Marragafay",
            "meta_desc": "Experience a magical sunset camel ride in the Agafay Desert near Marrakech. Authentic Berber nomadic attire, tea ceremony, and hotel transfers included.",
            "h1": "Sunset Camel Ride in Agafay Desert",
            "intro": "Traverse the undulating stone desert at a tranquil, ancient rhythm. Dressed in traditional nomadic cheich scarves, ride across golden ridges as the sun sets over the Atlas."
        },
        "fr": {
            "title": "Balade en Dromadaire au Coucher du Soleil à Agafay | Marragafay",
            "meta_desc": "Vivez une balade authentique en dromadaire au coucher du soleil dans le désert d'Agafay. Tenue traditionnelle nomade, cérémonie du thé et transferts inclus.",
            "h1": "Balade en Dromadaire au Coucher du Soleil",
            "intro": "Traversez le plateau minéral au rythme apaisant des caravanes traditionnelles. Chèche saharien inclus, pause thé et coucher de soleil inoubliable."
        },
        "es": {
            "title": "Paseo en Camello al Atardecer en Agafay Marrakech | Marragafay",
            "meta_desc": "Disfrute de un mágico paseo en camello al atardecer en el desierto de Agafay. Atuendo bereber tradicional, té marroquí y traslados incluidos.",
            "h1": "Paseo en Camello al Atardecer en Agafay",
            "intro": "Recorra las colinas doradas al ritmo tranquilo de los nómadas del desierto, vestido con el tradicional cheich y disfrutando del atardecer sobre el Atlas."
        },
        "ar": {
            "title": "ركوب الجمال وقت الغروب في صحراء أكافاي مراكش | مراكافاي",
            "meta_desc": "استمتع بجولة ساحرة لركوب الجمال وقت غروب الشمس في صحراء أكافاي قرب مراكش. زي صحراوي تقليدي، جلسة شاي ونقل مريح من فندقك.",
            "h1": "جولة ركوب الجمال وقت الغروب في أكافاي",
            "intro": "استمتع بالهدوء الساحر وأنت تعبر تلال الصحراء الذهبية على ظهور الجمال بالزي الصحراوي الأصيل، واختم الجولة بكوب شاي مغربي مع غروب الشمس."
        }
    },
    "activities/dinner-show.html": {
        "en": {
            "title": "Agafay Desert Dinner & Show from Marrakech | Marragafay",
            "meta_desc": "Book an unforgettable desert dinner under the stars in Agafay. Gourmet Moroccan tagines, live fire spectacle, Gnawa music, and private campfire.",
            "h1": "Agafay Desert Dinner & Live Show",
            "intro": "Indulge in authentic Moroccan cuisine under the desert sky. Enjoy live fire breathers, traditional Berber musicians, and candlelit ambiance in the stone desert."
        },
        "fr": {
            "title": "Dîner Spectacle dans le Désert d'Agafay depuis Marrakech | Marragafay",
            "meta_desc": "Soirée d'exception sous les étoiles d'Agafay : gastronomie marocaine raffinée, spectacle de feu spectaculaire, musique gnaoua et feu de camp.",
            "h1": "Dîner Spectacle dans le Désert d'Agafay",
            "intro": "Savourez un dîner marocain d'exception sous les étoiles d'Agafay. Spectacle de cracheurs de feu, musiciens traditionnels et ambiance féerique au coin du feu."
        },
        "es": {
            "title": "Cena y Espectáculo en el Desierto de Agafay Marrakech | Marragafay",
            "meta_desc": "Cena inolvidable bajo las estrellas de Agafay: alta cocina marroquí, espectáculo de fuego en vivo, música tradicional y hoguera privada.",
            "h1": "Cena con Espectáculo en el Desierto de Agafay",
            "intro": "Disfrute de la auténtica gastronomía marroquí bajo el cielo estrellado del desierto, acompañada de espectáculos de fuego, música en vivo y ambiente mágico."
        },
        "ar": {
            "title": "عشاء وسهرة فنية في صحراء أكافاي من مراكش | مراكافاي",
            "meta_desc": "احجز عشاءً صحراوياً رومانسياً تحت نجوم أكافاي: أشهى الطواجن المغربية، عروض نار حية، موسيقى كناوة وسهرة حول نار المخيم.",
            "h1": "عشاء وعرض فني في صحراء أكافاي",
            "intro": "تذوق أشهى المأكولات المغربية الأصيلة تحت سماء أكافاي الصافية، واستمتع بعروض النار الحية والموسيقى الفلكلورية حول موقد النار الدافئ."
        }
    },
    "activities/buggy.html": {
        "en": {
            "title": "Dune Buggy Adventure in Agafay Desert Marrakech | Marragafay",
            "meta_desc": "Drive high-performance dune buggies in the Agafay Desert. Polaris & Can-Am buggies, extreme off-road trails, licensed instructors, and hotel transfers.",
            "h1": "Agafay Desert Dune Buggy Tour",
            "intro": "Experience raw off-road power in an open-cockpit dune buggy. Traverse dry canyons and challenging rocky terrain with certified professional desert instructors."
        },
        "fr": {
            "title": "Aventure Buggy dans le Désert d'Agafay Marrakech | Marragafay",
            "meta_desc": "Pilotage de buggys performants dans le désert d'Agafay : pistes tout-terrain, matériel de sécurité, instructeurs diplômés et transferts hôtel.",
            "h1": "Aventure en Buggy dans le Désert d'Agafay",
            "intro": "Sensations fortes et puissance tout-terrain au volant de buggys récents. Franchissez les canyons et collines d'Agafay en toute sécurité."
        },
        "es": {
            "title": "Aventura en Buggy por el Desierto de Agafay Marrakech | Marragafay",
            "meta_desc": "Conduzca buggies de alta potencia por el desierto de Agafay: rutas off-road, equipamiento completo de seguridad y traslados incluidos.",
            "h1": "Tour en Buggy por el Desierto de Agafay",
            "intro": "Adrenalina pura pilotando buggies de alto rendimiento por senderos escarpados y cañones del desierto con instructores profesionales."
        },
        "ar": {
            "title": "مغامرة البوغي في صحراء أكافاي مراكش | مركبات الدفع الرباعي | مراكافاي",
            "meta_desc": "قد أحدث مركبات البوغي القوية في صحراء أكافاي: مسارات وعرة مثيرة، معدات أمان متكاملة، ونقل مريح من الفندق.",
            "h1": "مغامرة البوغي في صحراء أكافاي",
            "intro": "انطلق في مغامرة شيقة لقيادة مركبات البوغي القوية عبر التضاريس والوديان الصخرية لصحراء أكافاي برفقة طاقم تدريب محترف."
        }
    },
    "activities/hot-air-balloon.html": {
        "en": {
            "title": "Hot Air Balloon Flight Marrakech & Agafay Desert | Marragafay",
            "meta_desc": "Experience a sunrise hot air balloon flight over Marrakech and the Agafay Desert with panoramic views of the Atlas Mountains. Berber breakfast included.",
            "h1": "Marrakech & Agafay Hot Air Balloon Flight",
            "intro": "Float peacefully at dawn over the desert plateau as the morning sun illuminates the snow-capped High Atlas Mountains. Includes fresh Berber breakfast and flight certificate."
        },
        "fr": {
            "title": "Vol en Montgolfière à Marrakech & Désert d'Agafay | Marragafay",
            "meta_desc": "Envolez-vous en montgolfière au lever du soleil au-dessus du désert et de l'Atlas. Vue panoramique spectaculaire et petit-déjeuner berbère inclus.",
            "h1": "Vol en Montgolfière au Lever du Soleil",
            "intro": "Volez au-dessus des paysages lunaires d'Agafay au lever du jour avec une vue panoramique grandiose sur la chaîne de l'Atlas. Petit-déjeuner berbère inclus."
        },
        "es": {
            "title": "Vuelo en Globo Aerostático Marrakech y Desierto de Agafay | Marragafay",
            "meta_desc": "Disfrute de un vuelo en globo al amanecer sobre Marrakech y el desierto de Agafay con vistas a la cordillera del Atlas. Desayuno bereber incluido.",
            "h1": "Vuelo en Globo Aerostático al Amanecer",
            "intro": "Sobrevuele el desierto de piedra al amanecer con vistas panorámicas únicas a las cumbres del Atlas. Incluye desayuno tradicional bereber."
        },
        "ar": {
            "title": "رحلة المنطاد الهوائي في مراكش وصحراء أكافاي | مراكافاي",
            "meta_desc": "حلق مع شروق الشمس في رحلة منطاد هوائي ساحرة فوق مراكش وصحراء أكافاي مع إطلالة بانورامية على جبال الأطلس وفطور مغربي أصيل.",
            "h1": "رحلة المنطاد الهوائي مع شروق الشمس",
            "intro": "حلق في سكون الصباح الباكر فوق هضبة أكافاي واستمتع بمشاهد بانورامية خيالية لجبال الأطلس، متبوعة بفطور بلدي شهي في خيمة تقليدية."
        }
    },
    "activities/paragliding.html": {
        "en": {
            "title": "Paragliding Tandem Flight over Agafay Desert Marrakech | Marragafay",
            "meta_desc": "Soar high above the Agafay stone desert on a tandem paragliding flight with certified pilots. High Atlas mountain backdrops and GoPro video options.",
            "h1": "Agafay Desert Paragliding Adventure",
            "intro": "Experience the ultimate freedom of flight with certified tandem paragliding pilots over the dramatic expanses of Agafay and the Kik Plateau."
        },
        "fr": {
            "title": "Parapente en Tandem au-dessus du Désert d'Agafay | Marragafay",
            "meta_desc": "Volez en parapente biplace au-dessus du désert d'Agafay avec des pilotes certifiés. Vues aériennes uniques sur l'Atlas et transferts inclus.",
            "h1": "Vol en Parapente dans le Désert d'Agafay",
            "intro": "Prenez de la hauteur et découvrez les reliefs d'Agafay vus du ciel lors d'un vol biplace encadré par des moniteurs professionnels certifiés."
        },
        "es": {
            "title": "Vuelo en Parapente Biplaza sobre el Desierto de Agafay | Marragafay",
            "meta_desc": "Vuele en parapente biplaza sobre la meseta de Agafay con pilotos certificados. Vistas aéreas inigualables del Atlas y transporte incluido.",
            "h1": "Aventura de Parapente en el Desierto de Agafay",
            "intro": "Sienta la emoción de volar en parapente biplaza con pilotos titulados, contemplando el contraste entre el desierto y las montañas del Atlas."
        },
        "ar": {
            "title": "الطيران الشراعي في سماء صحراء أكافاي مراكش | مراكافاي",
            "meta_desc": "حلق كالطير في رحلة طيران شراعي ثنائي فوق صحراء أكافاي مع طيارين محترفين معتمدين وإطلالة ساحرة على جبال الأطلس.",
            "h1": "مغامرة الطيران الشراعي في صحراء أكافاي",
            "intro": "عش إحساس التحليق الحر في السماء رفقة طيارين معتمدين دولياً، وشاهد تضاريس صحراء أكافاي الخلابة من منظور جوي لا مثيل له."
        }
    },
    "activities.html": {
        "en": {
            "title": "Agafay Desert Activities & Adventure Tours from Marrakech | Marragafay",
            "meta_desc": "Discover top outdoor activities in Agafay Desert: quad biking, dune buggy safaris, sunset camel rides, hot air balloon flights, and desert dinners.",
            "h1": "Agafay Desert Activities & Adventures",
            "intro": "A curated selection of high-adrenaline and authentic cultural escapes in the Agafay stone desert."
        },
        "fr": {
            "title": "Activités & Excursions dans le Désert d'Agafay Marrakech | Marragafay",
            "meta_desc": "Toutes les activités incontournables dans le désert d'Agafay : quad, buggy, balade en dromadaire, montgolfière, parapente et dîners sous les étoiles.",
            "h1": "Activités & Aventures dans le Désert d'Agafay",
            "intro": "Une sélection rigoureuse d'aventures et d'expériences culturelles authentiques dans le désert de pierre d'Agafay."
        },
        "es": {
            "title": "Actividades y Excursiones en el Desierto de Agafay Marrakech | Marragafay",
            "meta_desc": "Descubra las mejores actividades en el desierto de Agafay: rutas en quad y buggy, paseos en camello al atardecer, vuelos en globo y cenas bajo las estrellas.",
            "h1": "Actividades y Aventuras en Agafay",
            "intro": "Una cuidada selección de aventuras de adrenalina y experiencias culturales auténticas en el desierto de Agafay."
        },
        "ar": {
            "title": "أنشطة ومغامرات صحراء أكافاي من مراكش | مراكافاي",
            "meta_desc": "اكتشف أفضل الأنشطة والتجارب في صحراء أكافاي: دراجات الكواد، رحلات البوغي، ركوب الجمال، رحلات المنطاد الهوائي، وسهرات العشاء الفاخرة.",
            "h1": "أنشطة ومغامرات صحراء أكافاي",
            "intro": "مجموعة مختارة من أفضل الأنشطة الحماسية والتجارب الثقافية الأصيلة في قلب صحراء أكافاي."
        }
    }
}

for rel_path, lang_dict in seo_data.items():
    for lang in ["en", "fr", "es", "ar"]:
        fpath = f"{lang}/{rel_path}"
        if not os.path.exists(fpath):
            print(f"Skipping missing {fpath}")
            continue

        d = lang_dict[lang]

        with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
            html = f.read()

        # 1. Update <title>
        html = re.sub(r'<title>.*?</title>', f'<title>{d["title"]}</title>', html, count=1, flags=re.DOTALL)

        # 2. Update <meta name="description">
        html = re.sub(r'<meta\s+name=["\']description["\']\s+content=["\'].*?["\']\s*>', f'<meta name="description" content="{d["meta_desc"]}">', html, count=1, flags=re.DOTALL)

        # 3. Update og:title and twitter:title
        html = re.sub(r'<meta\s+property=["\']og:title["\']\s+content=["\'].*?["\']\s*>', f'<meta property="og:title" content="{d["title"]}">', html, count=1, flags=re.DOTALL)
        html = re.sub(r'<meta\s+name=["\']twitter:title["\']\s+content=["\'].*?["\']\s*>', f'<meta name="twitter:title" content="{d["title"]}">', html, count=1, flags=re.DOTALL)

        # 4. Update og:description and twitter:description
        html = re.sub(r'<meta\s+property=["\']og:description["\']\s+content=["\'].*?["\']\s*>', f'<meta property="og:description" content="{d["meta_desc"]}">', html, count=1, flags=re.DOTALL)
        html = re.sub(r'<meta\s+name=["\']twitter:description["\']\s+content=["\'].*?["\']\s*>', f'<meta name="twitter:description" content="{d["meta_desc"]}">', html, count=1, flags=re.DOTALL)

        # 5. Update main H1
        # Match H1 in hero
        html = re.sub(r'<h1[^>]*>.*?</h1>', f'<h1 class="text-[42px] md:text-[64px] font-medium text-[#F6F7EA] tracking-tight leading-[1.05] mb-3">{d["h1"]}</h1>', html, count=1, flags=re.DOTALL)

        # 6. Update hero subtitle/intro paragraph if present
        if "intro" in d:
            html = re.sub(
                r'<p class="text-\[14px\] md:text-\[15px\] text-white/75 leading-relaxed font-normal mb-2 max-w-2xl drop-shadow-md">.*?</p>',
                f'<p class="text-[14px] md:text-[15px] text-white/75 leading-relaxed font-normal mb-2 max-w-2xl drop-shadow-md">{d["intro"]}</p>',
                html,
                count=1,
                flags=re.DOTALL
            )

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Optimized On-Page SEO for {fpath}")

print("\nAll Money Pages successfully optimized for search intent and conversion!")
