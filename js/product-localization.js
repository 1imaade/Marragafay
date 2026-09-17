/**
 * Marragafay Multilingual Product Presentation Layer
 *
 * Provides natural localized presentation strings for English, French, Spanish, and Arabic.
 * Factual data (prices, durations, transport type, inclusions count, rules) remains strictly
 * canonical in ProductData; this module only handles natural localized presentation.
 */

(function (root, factory) {
    if (typeof define === 'function' && define.amd) {
        define([], factory);
    } else if (typeof module === 'object' && module.exports) {
        module.exports = factory();
    } else {
        root.ProductLocalization = factory();
    }
}(typeof self !== 'undefined' ? self : this, function () {
    'use strict';

    var LOCALIZED_DATA = {
        en: {
            standard: {
                name: 'Standard',
                title: 'Agafay Evening Experience',
                transport: 'Shared hotel / riad pickup & return',
                duration: '15:30–22:00',
                cardSummary: '15:30 — 22:00 · Shared Transfer · 1h Quad · 20min Camel · Dinner & Show',
                tag: 'STANDARD · 45€ / guest',
                fromPrice: 'From 45€ / person',
                cta: 'View Standard Pack ►',
                includes: [
                    'Shared hotel / riad pickup & return',
                    '1h quad ride across Agafay',
                    '20min camel ride',
                    'Pool access & Moroccan mint tea',
                    'Sunset photo pause',
                    'Traditional Moroccan dinner',
                    'Live fire & music show',
                    'Bottled water included',
                    'Safety gear & briefing'
                ]
            },
            private: {
                name: 'Private',
                title: 'Private Agafay Evening',
                transport: 'Private hotel / riad transfer',
                duration: '15:30–22:00',
                cardSummary: '15:30 — 22:00 · Private Transfer · 1h30 Quad · 20min Camel · Guide · Dinner & Show',
                tag: 'PRIVATE · 75€ / guest',
                fromPrice: 'From 75€ / person',
                cta: 'View Private Pack ►',
                includes: [
                    'Private hotel / riad transfer',
                    '1h30 private quad session',
                    '20min camel ride',
                    'Pool access & Moroccan mint tea',
                    'Sunset photo pause',
                    'Traditional Moroccan dinner',
                    'Live fire & music show',
                    'Dedicated guide',
                    'Desert scarf to wear & keep',
                    'Bottled water + soft drink',
                    'Moroccan sweets',
                    'Safety gear & briefing'
                ]
            },
            'private-plus': {
                name: 'Private+',
                title: 'Agafay & Atlas — Full-Day Quad',
                transport: 'Private hotel / riad transfer',
                duration: '09:00–22:00',
                cardSummary: '09:00 — 22:00 · Private Transfer · 3h Quad · Lunch & Dinner · 45min Camel · Guide',
                tag: 'PRIVATE+ · 119€ / guest',
                fromPrice: 'From 119€ / person',
                cta: 'View Private+ Pack ►',
                includes: [
                    'Private hotel / riad transfer',
                    '3h private quad exploration across Agafay & the Atlas',
                    'Traditional Moroccan lunch',
                    'Pool access & Moroccan mint tea',
                    '45min camel ride',
                    'Sunset pause',
                    'Traditional Moroccan dinner',
                    'Live fire & music show',
                    'Dedicated full-day guide',
                    'Desert scarf to wear & keep',
                    'Bottled water + soft drink',
                    'Moroccan sweets',
                    'Safety gear & briefing'
                ]
            },
            buggy: {
                name: 'Buggy',
                title: 'Private Agafay Buggy Experience',
                transport: 'Private hotel / riad transfer',
                duration: 'Flexible',
                cardSummary: 'Flexible Departure · Private Transfer · 1h Buggy (2 guests/buggy) · 20min Camel · Dinner & Show',
                tag: 'BUGGY · 129€ / guest',
                fromPrice: 'From 129€ / person',
                cta: 'Discover Buggy Experience ►',
                includes: [
                    'Private hotel / riad transfer',
                    '1h private buggy ride',
                    'One buggy for two guests',
                    '20min camel ride',
                    'Pool access & Moroccan mint tea',
                    'Sunset photo pause',
                    'Traditional Moroccan dinner',
                    'Live fire & music show',
                    'Dedicated guide',
                    'Bottled water included',
                    'Safety gear & briefing'
                ]
            }
        },

        fr: {
            standard: {
                name: 'Standard',
                title: 'Expérience Soirée Agafay',
                transport: 'Prise en charge et retour partagés depuis votre hôtel ou riad',
                duration: '15:30–22:00',
                cardSummary: '15:30 — 22:00 · Transfert Partagé · 1h Quad · 20min Dromadaire · Dîner & Spectacle',
                tag: 'STANDARD · 45€ / pers',
                fromPrice: 'À partir de 45€ / personne',
                cta: 'Découvrir le forfait ►',
                includes: [
                    'Prise en charge et retour partagés depuis votre hôtel ou riad',
                    '1h de quad à travers le désert d\'Agafay',
                    '20 min de balade à dos de dromadaire',
                    'Accès piscine & thé à la menthe marocain',
                    'Pause photo au coucher du soleil',
                    'Dîner marocain traditionnel',
                    'Spectacle vivant de feu et musique',
                    'Eau minérale en bouteille',
                    'Équipement de sécurité & briefing'
                ]
            },
            private: {
                name: 'Privé',
                title: 'Soirée Privée à Agafay',
                transport: 'Transfert privé aller-retour depuis votre hôtel ou riad',
                duration: '15:30–22:00',
                cardSummary: '15:30 — 22:00 · Transfert Privé · 1h30 Quad · 20min Dromadaire · Guide · Dîner & Spectacle',
                tag: 'PRIVÉ · 75€ / pers',
                fromPrice: 'À partir de 75€ / personne',
                cta: 'Découvrir le forfait ►',
                includes: [
                    'Transfert privé aller-retour depuis votre hôtel ou riad',
                    '1h30 de session privée en quad',
                    '20 min de balade à dos de dromadaire',
                    'Accès piscine & thé à la menthe marocain',
                    'Pause photo au coucher du soleil',
                    'Dîner marocain traditionnel',
                    'Spectacle vivant de feu et musique',
                    'Guide dédié',
                    'Chèche du désert offert à porter et garder',
                    'Eau en bouteille + boisson sans alcool',
                    'Pâtisseries marocaines',
                    'Équipement de sécurité & briefing'
                ]
            },
            'private-plus': {
                name: 'Privé+',
                title: 'Agafay & Atlas — Journée Complète Quad',
                transport: 'Transfert privé aller-retour depuis votre hôtel ou riad',
                duration: '09:00–22:00',
                cardSummary: '09:00 — 22:00 · Transfert Privé · 3h Quad · Déjeuner & Dîner · 45min Dromadaire · Guide',
                tag: 'PRIVÉ+ · 119€ / pers',
                fromPrice: 'À partir de 119€ / personne',
                cta: 'Découvrir le forfait ►',
                includes: [
                    'Transfert privé aller-retour depuis votre hôtel ou riad',
                    '3h d\'exploration privée en quad à travers Agafay et l\'Atlas',
                    'Déjeuner marocain traditionnel',
                    'Accès piscine & thé à la menthe marocain',
                    '45 min de balade à dos de dromadaire',
                    'Pause coucher de soleil',
                    'Dîner marocain traditionnel',
                    'Spectacle vivant de feu et musique',
                    'Guide dédié pour la journée complète',
                    'Chèche du désert offert à porter et garder',
                    'Eau en bouteille + boisson sans alcool',
                    'Pâtisseries marocaines',
                    'Équipement de sécurité & briefing'
                ]
            },
            buggy: {
                name: 'Buggy',
                title: 'Expérience Privée en Buggy à Agafay',
                transport: 'Transfert privé aller-retour depuis votre hôtel ou riad',
                duration: 'Flexible',
                cardSummary: 'Horaires Flexibles · Transfert Privé · 1h Buggy (2 pers/buggy) · 20min Dromadaire · Dîner & Spectacle',
                tag: 'BUGGY · 129€ / pers',
                fromPrice: 'À partir de 129€ / personne',
                cta: 'Découvrir l\'expérience buggy ►',
                includes: [
                    'Transfert privé aller-retour depuis votre hôtel ou riad',
                    '1h de balade privée en buggy',
                    'Un buggy pour deux personnes',
                    '20 min de balade à dos de dromadaire',
                    'Accès piscine & thé à la menthe marocain',
                    'Pause photo au coucher du soleil',
                    'Dîner marocain traditionnel',
                    'Spectacle vivant de feu et musique',
                    'Guide dédié',
                    'Eau minérale en bouteille',
                    'Équipement de sécurité & briefing'
                ]
            }
        },

        es: {
            standard: {
                name: 'Estándar',
                title: 'Experiencia Nocturna en Agafay',
                transport: 'Recogida y regreso compartidos desde su hotel o riad',
                duration: '15:30–22:00',
                cardSummary: '15:30 — 22:00 · Traslado Compartido · 1h Quad · 20min Camello · Cena y Espectáculo',
                tag: 'ESTÁNDAR · 45€ / pers',
                fromPrice: 'Desde 45€ / persona',
                cta: 'Descubrir el paquete ►',
                includes: [
                    'Recogida y regreso compartidos desde su hotel o riad',
                    '1h de paseo en quad por Agafay',
                    '20 min de paseo en camello',
                    'Acceso a la piscina y té de menta marroquí',
                    'Pausa fotográfica al atardecer',
                    'Cena tradicional marroquí',
                    'Espectáculo en vivo de fuego y música',
                    'Agua mineral embotellada',
                    'Equipo de seguridad e instrucciones'
                ]
            },
            private: {
                name: 'Privado',
                title: 'Velada Privada en Agafay',
                transport: 'Traslado privado de ida y vuelta desde su hotel o riad',
                duration: '15:30–22:00',
                cardSummary: '15:30 — 22:00 · Traslado Privado · 1h30 Quad · 20min Camello · Guía · Cena y Espectáculo',
                tag: 'PRIVADO · 75€ / pers',
                fromPrice: 'Desde 75€ / persona',
                cta: 'Descubrir el paquete ►',
                includes: [
                    'Traslado privado de ida y vuelta desde su hotel o riad',
                    '1h30 de sesión privada en quad',
                    '20 min de paseo en camello',
                    'Acceso a la piscina y té de menta marroquí',
                    'Pausa fotográfica al atardecer',
                    'Cena tradicional marroquí',
                    'Espectáculo en vivo de fuego y música',
                    'Guía exclusivo dedicado',
                    'Pañuelo del desierto de regalo',
                    'Agua embotellada + refresco',
                    'Dulces tradicionales marroquíes',
                    'Equipo de seguridad e instrucciones'
                ]
            },
            'private-plus': {
                name: 'Privado+',
                title: 'Agafay y Atlas — Día Completo en Quad',
                transport: 'Traslado privado de ida y vuelta desde su hotel o riad',
                duration: '09:00–22:00',
                cardSummary: '09:00 — 22:00 · Traslado Privado · 3h Quad · Almuerzo y Cena · 45min Camello · Guía',
                tag: 'PRIVADO+ · 119€ / pers',
                fromPrice: 'Desde 119€ / persona',
                cta: 'Descubrir el paquete ►',
                includes: [
                    'Traslado privado de ida y vuelta desde su hotel o riad',
                    '3h de exploración privada en quad por Agafay y el Atlas',
                    'Almuerzo tradicional marroquí',
                    'Acceso a la piscina y té de menta marroquí',
                    '45 min de paseo en camello',
                    'Pausa al atardecer',
                    'Cena tradicional marroquí',
                    'Espectáculo en vivo de fuego y música',
                    'Guía dedicado de jornada completa',
                    'Pañuelo del desierto de regalo',
                    'Agua embotellada + refresco',
                    'Dulces tradicionales marroquíes',
                    'Equipo de seguridad e instrucciones'
                ]
            },
            buggy: {
                name: 'Buggy',
                title: 'Experiencia Privada en Buggy por Agafay',
                transport: 'Traslado privado de ida y vuelta desde su hotel o riad',
                duration: 'Flexible',
                cardSummary: 'Salida Flexible · Traslado Privado · 1h Buggy (2 pers/buggy) · 20min Camello · Cena y Espectáculo',
                tag: 'BUGGY · 129€ / pers',
                fromPrice: 'Desde 129€ / persona',
                cta: 'Descubrir experiencia en buggy ►',
                includes: [
                    'Traslado privado de ida y vuelta desde su hotel o riad',
                    '1h de paseo privado en buggy',
                    'Un buggy para dos personas',
                    '20 min de paseo en camello',
                    'Acceso a la piscina y té de menta marroquí',
                    'Pausa fotográfica al atardecer',
                    'Cena tradicional marroquí',
                    'Espectáculo en vivo de fuego y música',
                    'Guía dedicado',
                    'Agua mineral embotellada',
                    'Equipo de seguridad e instrucciones'
                ]
            }
        },

        ar: {
            standard: {
                name: 'القياسية',
                title: 'تجربة أمسية أكافاي',
                transport: 'نقل مشترك ذهاباً وإياباً من الفندق أو الرياض',
                duration: '15:30–22:00',
                cardSummary: '15:30 — 22:00 · نقل مشترك · ساعة كواد · 20 دقيقة جمل · عشاء وعرض',
                tag: 'القياسية · 45€ / للضيف',
                fromPrice: 'ابتداءً من 45€ / للشخص',
                cta: 'استكشف الباقة ◄',
                includes: [
                    'نقل مشترك ذهاباً وإياباً من الفندق أو الرياض',
                    'ساعة كاملة من قيادة الكواد عبر صحراء أكافاي',
                    'جولة ركوب الجمال لمدة 20 دقيقة',
                    'دخول المسبح وشاي مغربي تقليدي بالنعناع',
                    'استراحة تصوير لمشهد غروب الشمس',
                    'عشاء مغربي تقليدي فاخر',
                    'عرض حي للشهب النارية والموسيقى',
                    'مياه معدنية معبأة',
                    'معدات السلامة وإرشادات الأمان الكاملة'
                ]
            },
            private: {
                name: 'الخاصة',
                title: 'أمسية أكافاي الخاصة',
                transport: 'نقل خاص ذهاباً وإياباً من الفندق أو الرياض',
                duration: '15:30–22:00',
                cardSummary: '15:30 — 22:00 · نقل خاص · 1h30 كواد · 20 دقيقة جمل · مرشد خاص · عشاء وعرض',
                tag: 'الخاصة · 75€ / للضيف',
                fromPrice: 'ابتداءً من 75€ / للشخص',
                cta: 'استكشف الباقة ◄',
                includes: [
                    'نقل خاص ذهاباً وإياباً من الفندق أو الرياض',
                    'ساعة ونصف قيادة خاصة ومستقلة للكواد',
                    'جولة ركوب الجمال لمدة 20 دقيقة',
                    'دخول المسبح وشاي مغربي تقليدي بالنعناع',
                    'استراحة تصوير لمشهد غروب الشمس',
                    'عشاء مغربي تقليدي فاخر',
                    'عرض حي للشهب النارية والموسيقى',
                    'مرشد سياحي خاص ومخصص لمجموعتكم',
                    'وشاح صحراوي أصيل هدية لارتدائه والاحتفاظ به',
                    'مياه معبأة ومشروبات غازية منعشة',
                    'حلويات مغربية تقليدية فاخرة',
                    'معدات السلامة وإرشادات الأمان الكاملة'
                ]
            },
            'private-plus': {
                name: 'خاصة+',
                title: 'أكافاي والأطلس — يوم كامل كواد',
                transport: 'نقل خاص ذهاباً وإياباً من الفندق أو الرياض',
                duration: '09:00–22:00',
                cardSummary: '09:00 — 22:00 · نقل خاص · 3 ساعات كواد · غداء وعشاء · 45 دقيقة جمل · مرشد',
                tag: 'خاصة+ · 119€ / للضيف',
                fromPrice: 'ابتداءً من 119€ / للشخص',
                cta: 'استكشف الباقة ◄',
                includes: [
                    'نقل خاص ذهاباً وإياباً من الفندق أو الرياض',
                    '3 ساعات استكشاف خاص بالكواد عبر أكافاي وجبال الأطلس',
                    'وجبة غداء مغربية تقليدية كاملة',
                    'دخول المسبح وشاي مغربي تقليدي بالنعناع',
                    'جولة ركوب الجمال لمدة 45 دقيقة',
                    'استراحة غروب الشمس في موقع مميز',
                    'عشاء مغربي تقليدي فاخر',
                    'عرض حي للشهب النارية والموسيقى',
                    'مرشد سياحي مخصص طوال اليوم',
                    'وشاح صحراوي أصيل هدية لارتدائه والاحتفاظ به',
                    'مياه معبأة ومشروبات غازية منعشة',
                    'حلويات مغربية تقليدية فاخرة',
                    'معدات السلامة وإرشادات الأمان الكاملة'
                ]
            },
            buggy: {
                name: 'بوغي',
                title: 'تجربة البوغي الخاصة بأكافاي',
                transport: 'نقل خاص ذهاباً وإياباً من الفندق أو الرياض',
                duration: 'توقيت مرن',
                cardSummary: 'انطلاق مرن · نقل خاص · ساعة بوغي (مركبة لضيفين) · 20 دقيقة جمل · عشاء وعرض',
                tag: 'بوغي · 129€ / للضيف',
                fromPrice: 'ابتداءً من 129€ / للشخص',
                cta: 'استكشف تجربة البوغي ◄',
                includes: [
                    'نقل خاص ذهاباً وإياباً من الفندق أو الرياض',
                    'ساعة كاملة جولة بوغي خاصة ومستقلة',
                    'مركبة بوغي واحدة لكل ضيفين',
                    'جولة ركوب الجمال لمدة 20 دقيقة',
                    'دخول المسبح وشاي مغربي تقليدي بالنعناع',
                    'استراحة تصوير لمشهد غروب الشمس',
                    'عشاء مغربي تقليدي فاخر',
                    'عرض حي للشهب النارية والموسيقى',
                    'مرشد سياحي خاص ومخصص',
                    'مياه معدنية معبأة',
                    'معدات السلامة وإرشادات الأمان الكاملة'
                ]
            }
        }
    };

    var UI_STRINGS = {
        en: {
            allPackages: 'All packages ►',
            currencyMad: 'MAD',
            perGuest: '/ guest',
            perPerson: '/ person',
            from: 'From'
        },
        fr: {
            allPackages: 'Tous les forfaits ►',
            currencyMad: 'MAD',
            perGuest: '/ pers',
            perPerson: '/ personne',
            from: 'À partir de'
        },
        es: {
            allPackages: 'Todos los paquetes ►',
            currencyMad: 'MAD',
            perGuest: '/ pers',
            perPerson: '/ persona',
            from: 'Desde'
        },
        ar: {
            allPackages: 'جميع الباقات ◄',
            currencyMad: 'درهم',
            perGuest: '/ للضيف',
            perPerson: '/ للشخص',
            from: 'ابتداءً من'
        }
    };

    function normalizeLocale(rawLocale) {
        if (!rawLocale || typeof rawLocale !== 'string') return 'en';
        var norm = rawLocale.trim().toLowerCase().slice(0, 2);
        if (norm === 'fr' || norm === 'es' || norm === 'ar') return norm;
        return 'en';
    }

    function getLocalizedFields(canonicalKey, locale) {
        var loc = normalizeLocale(locale);
        var table = LOCALIZED_DATA[loc] || LOCALIZED_DATA.en;
        return table[canonicalKey] || null;
    }

    function getUiString(key, locale) {
        var loc = normalizeLocale(locale);
        var table = UI_STRINGS[loc] || UI_STRINGS.en;
        return table[key] || '';
    }

    return Object.freeze({
        normalizeLocale: normalizeLocale,
        getLocalizedFields: getLocalizedFields,
        getUiString: getUiString,
        LOCALIZED_DATA: LOCALIZED_DATA,
        UI_STRINGS: UI_STRINGS
    });
}));
