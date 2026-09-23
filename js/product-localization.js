/**
 * Marragafay multilingual product presentation.
 * ProductData owns all product facts; this module only supplies language.
 */
(function (root, factory) {
    if (typeof define === 'function' && define.amd) define([], factory);
    else if (typeof module === 'object' && module.exports) module.exports = factory();
    else root.ProductLocalization = factory();
}(typeof self !== 'undefined' ? self : this, function () {
    'use strict';

    // No prices, durations, transport rules, or inclusion facts live here.
    var COPY = {
        en: {
            standard: ['Standard', 'Standard Agafay Evening', 'View Standard ►'],
            private: ['Private', 'Private Agafay Evening', 'View Private ►'],
            'private-plus': ['Private+', 'Private+ Full-Day Agafay Experience', 'View Private+ ►'],
            buggy: ['Buggy', 'Private Buggy Experience from Marrakech', 'View Buggy ►']
        },
        fr: {
            standard: ['Standard', 'Soirée Standard à Agafay', 'Découvrir Standard ►'],
            private: ['Private', 'Soirée Private à Agafay', 'Découvrir Private ►'],
            'private-plus': ['Private+', 'Private+ — Journée complète à Agafay', 'Découvrir Private+ ►'],
            buggy: ['Buggy', 'Expérience Buggy privée depuis Marrakech', 'Découvrir Buggy ►']
        },
        es: {
            standard: ['Standard', 'Experiencia Standard en Agafay', 'Ver Standard ►'],
            private: ['Private', 'Experiencia Private en Agafay', 'Ver Private ►'],
            'private-plus': ['Private+', 'Private+ — Experiencia de día completo en Agafay', 'Ver Private+ ►'],
            buggy: ['Buggy', 'Experiencia privada en buggy desde Marrakech', 'Ver Buggy ►']
        },
        ar: {
            standard: ['Standard', 'أمسية Standard في أكافاي', 'اكتشف Standard ◄'],
            private: ['Private', 'أمسية Private في أكافاي', 'اكتشف Private ◄'],
            'private-plus': ['Private+', 'تجربة Private+ ليوم كامل في أكافاي', 'اكتشف Private+ ◄'],
            buggy: ['Buggy', 'تجربة بوغي خاصة انطلاقاً من مراكش', 'اكتشف Buggy ◄']
        }
    };

    // Language-only sentence frames. Numeric and operational values are injected from ProductData.
    var WORDS = {
        en: {
            shared: 'Shared round-trip pickup from your hotel, riad, or another address in Marrakech', private: 'Private round-trip pickup from your hotel, riad, or another address in Marrakech',
            quad: '{d} quad ride across Agafay', quadPrivate: '{d} private quad session',
            quadPlus: '{d} private quad exploration in Agafay', buggy: '{d} private buggy ride',
            camel: '{d} camel ride', pool: 'Pool access & Moroccan mint tea', sunset: 'Sunset photo pause',
            dinner: 'Traditional Moroccan dinner', show: 'Live fire & music show', guide: 'Dedicated guide',
            fullGuide: 'Dedicated full-day guide', scarf: 'Cheche scarf gift to keep',
            water: 'Cold bottled water', softDrink: 'One soft drink', sweets: 'Moroccan pastry gift',
            safety: 'Safety gear & briefing', lunch: 'Traditional Moroccan lunch',
            groupLunch: 'Lunch reserved for your group', groupDinner: 'Dinner reserved for your group',
            gifts: 'Water, gifts & sweets', fullDay: 'Full day',
            durationQuad: '{d} quad', durationPrivateQuad: '{d} private quad', durationCamel: '{d} camel', durationBuggy: '{d} buggy',
            transferShared: 'Shared Marrakech pickup', transferPrivate: 'Private Transfer',
            quadLabel: 'Quad', camelLabel: 'Camel', buggyLabel: 'Buggy', guideLabel: 'Guide',
            lunchDinner: 'Lunch & Dinner for your group', dinnerShow: 'Dinner & Show', twoGuests: '2 guests/buggy'
        },
        fr: {
            shared: 'Prise en charge partagée aller-retour depuis votre hôtel, riad ou une autre adresse à Marrakech', private: 'Prise en charge privée aller-retour depuis votre hôtel, riad ou une autre adresse à Marrakech',
            quad: 'Sortie de quad de {d} à travers le désert d\'Agafay', quadPrivate: 'Session privée en quad de {d}',
            quadPlus: 'Exploration privée en quad de {d} à Agafay', buggy: 'Balade privée en buggy de {d}',
            camel: 'Balade à dos de dromadaire de {d}', pool: 'Accès piscine & thé à la menthe marocain', sunset: 'Pause photo au coucher du soleil',
            dinner: 'Dîner marocain traditionnel', show: 'Spectacle vivant de feu et musique', guide: 'Guide dédié',
            fullGuide: 'Guide dédié pour la journée complète', scarf: 'Chèche offert à garder',
            water: 'Eau fraîche en bouteille', softDrink: 'Une boisson sans alcool', sweets: 'Coffret de pâtisseries marocaines offert',
            safety: 'Équipement de sécurité & briefing', lunch: 'Déjeuner marocain traditionnel',
            groupLunch: 'Déjeuner réservé à votre groupe', groupDinner: 'Dîner réservé à votre groupe',
            gifts: 'Eau, cadeaux et pâtisseries', fullDay: 'Journée complète',
            durationQuad: '{d} de quad', durationPrivateQuad: '{d} de quad privé', durationCamel: '{d} à dos de dromadaire', durationBuggy: '{d} de buggy',
            transferShared: 'Prise en charge partagée à Marrakech', transferPrivate: 'Transfert privé',
            quadLabel: 'Quad', camelLabel: 'Dromadaire', buggyLabel: 'Buggy', guideLabel: 'Guide',
            lunchDinner: 'Déjeuner & dîner pour votre groupe', dinnerShow: 'Dîner & Spectacle', twoGuests: '2 pers/buggy'
        },
        es: {
            shared: 'Recogida compartida de ida y vuelta desde su hotel, riad u otra dirección de Marrakech', private: 'Recogida privada de ida y vuelta desde su hotel, riad u otra dirección de Marrakech',
            quad: 'Paseo en quad de {d} por Agafay', quadPrivate: 'Sesión privada de quad de {d}',
            quadPlus: 'Exploración privada en quad de {d} por Agafay', buggy: 'Paseo privado en buggy de {d}',
            camel: 'Paseo en camello de {d}', pool: 'Acceso a la piscina y té de menta marroquí', sunset: 'Pausa fotográfica al atardecer',
            dinner: 'Cena tradicional marroquí', show: 'Espectáculo en vivo de fuego y música', guide: 'Guía exclusivo dedicado',
            fullGuide: 'Guía dedicado de jornada completa', scarf: 'Cheche de regalo para conservar',
            water: 'Agua fría embotellada', softDrink: 'Un refresco', sweets: 'Regalo de pastelería marroquí',
            safety: 'Equipo de seguridad e instrucciones', lunch: 'Almuerzo tradicional marroquí',
            groupLunch: 'Almuerzo reservado para su grupo', groupDinner: 'Cena reservada para su grupo',
            gifts: 'Agua, regalos y dulces', fullDay: 'Día completo',
            durationQuad: '{d} en quad', durationPrivateQuad: '{d} en quad privado', durationCamel: '{d} en camello', durationBuggy: '{d} en buggy',
            transferShared: 'Recogida compartida en Marrakech', transferPrivate: 'Traslado privado',
            quadLabel: 'Quad', camelLabel: 'Camello', buggyLabel: 'Buggy', guideLabel: 'Guía',
            lunchDinner: 'Almuerzo y cena para su grupo', dinnerShow: 'Cena y Espectáculo', twoGuests: '2 pers/buggy'
        },
        ar: {
            shared: 'نقل مشترك ذهاباً وإياباً من الفندق أو الرياض أو عنوان آخر داخل مراكش', private: 'نقل خاص ذهاباً وإياباً من الفندق أو الرياض أو أي عنوان آخر داخل مراكش',
            quad: 'قيادة كواد لمدة {d} عبر صحراء أكافاي', quadPrivate: 'جلسة كواد خاصة لمدة {d}',
            quadPlus: 'استكشاف خاص بالكواد لمدة {d} في أكافاي', buggy: 'جولة بوغي خاصة لمدة {d}',
            camel: 'جولة ركوب الجمال لمدة {d}', pool: 'دخول المسبح وشاي مغربي تقليدي بالنعناع', sunset: 'استراحة تصوير لمشهد غروب الشمس',
            dinner: 'عشاء مغربي تقليدي فاخر', show: 'عرض حي للنار والموسيقى', guide: 'مرشد سياحي خاص ومخصص',
            fullGuide: 'مرشد سياحي مخصص طوال اليوم', scarf: 'وشاح شيش هدية للاحتفاظ به',
            water: 'مياه باردة معبأة', softDrink: 'مشروب غازي واحد', sweets: 'علبة حلويات مغربية كهدية',
            safety: 'معدات السلامة وإرشادات الأمان الكاملة', lunch: 'وجبة غداء مغربية تقليدية كاملة',
            groupLunch: 'غداء مخصص لمجموعتكم', groupDinner: 'عشاء مخصص لمجموعتكم',
            gifts: 'ماء وهدايا وحلويات', fullDay: 'يوم كامل',
            durationQuad: 'كواد لمدة {d}', durationPrivateQuad: 'كواد خاص لمدة {d}', durationCamel: 'ركوب الجمال لمدة {d}', durationBuggy: 'بوغي لمدة {d}',
            transferShared: 'نقل مشترك داخل مراكش', transferPrivate: 'نقل خاص',
            quadLabel: 'كواد', camelLabel: 'جمل', buggyLabel: 'بوغي', guideLabel: 'مرشد',
            lunchDinner: 'غداء وعشاء لمجموعتكم', dinnerShow: 'عشاء وعرض', twoGuests: 'مركبة لضيفين'
        }
    };

    var UI_STRINGS = {
        en: { allPackages: 'All packages ►', currencyMad: 'MAD', perGuest: '/ guest', perPerson: '/ person', from: 'From' },
        fr: { allPackages: 'Tous les forfaits ►', currencyMad: 'MAD', perGuest: '/ pers', perPerson: '/ personne', from: 'À partir de' },
        es: { allPackages: 'Todos los paquetes ►', currencyMad: 'MAD', perGuest: '/ pers', perPerson: '/ persona', from: 'Desde' },
        ar: { allPackages: 'جميع الباقات ◄', currencyMad: 'درهم', perGuest: '/ للضيف', perPerson: '/ للشخص', from: 'ابتداءً من' }
    };

    function normalizeLocale(rawLocale) {
        if (!rawLocale || typeof rawLocale !== 'string') return 'en';
        var locale = rawLocale.trim().toLowerCase().slice(0, 2);
        return ['fr', 'es', 'ar'].indexOf(locale) !== -1 ? locale : 'en';
    }

    function format(template, values) {
        return String(template).replace(/\{(\w+)\}/g, function (_, key) {
            return values[key] == null ? '' : values[key];
        });
    }

    function getLocalizedFields(canonicalKey, locale, product) {
        var loc = normalizeLocale(locale);
        var copy = COPY[loc][canonicalKey] || COPY.en[canonicalKey];
        var words = WORDS[loc] || WORDS.en;
        var facts = (product && product.facts) || {};
        var values = { d: facts.quadDuration || '' };
        var transport = facts.transportMode === 'shared' ? words.shared : words.private;
        var includes;

        if (canonicalKey === 'standard') {
            includes = [transport, format(words.quad, values), format(words.camel, { d: facts.camelDuration }), words.pool, words.sunset, words.dinner, words.show, words.water, words.safety];
        } else if (canonicalKey === 'private') {
            includes = [transport, format(words.quadPrivate, values), format(words.camel, { d: facts.camelDuration }), words.pool, words.sunset, words.dinner, words.show, words.guide, words.scarf, words.water, words.softDrink, words.sweets, words.safety];
        } else if (canonicalKey === 'private-plus') {
            includes = [transport, format(words.quadPlus, values), words.groupLunch, words.pool, format(words.camel, { d: facts.camelDuration }), words.sunset, words.groupDinner, words.show, words.fullGuide, words.scarf, words.water, words.softDrink, words.sweets, words.safety];
        } else {
            includes = [transport, format(words.buggy, values), words.twoGuests, format(words.camel, { d: facts.camelDuration }), words.pool, words.sunset, words.dinner, words.show, words.guide, words.water, words.safety];
        }

        var ui = UI_STRINGS[loc] || UI_STRINGS.en;
        var price = product && product.priceEUR;
        var duration = product && product.duration || '';
        if (canonicalKey === 'standard') {
            duration = format(words.durationQuad, { d: facts.quadDuration }) + ' · ' + format(words.durationCamel, { d: facts.camelDuration });
        } else if (canonicalKey === 'private') {
            duration = format(words.durationPrivateQuad, { d: facts.quadDuration }) + ' · ' + format(words.durationCamel, { d: facts.camelDuration });
        } else if (canonicalKey === 'private-plus') {
            duration = words.fullDay + ' · ' + format(words.durationPrivateQuad, { d: facts.quadDuration }) + ' · ' + format(words.durationCamel, { d: facts.camelDuration });
        } else if (canonicalKey === 'buggy') {
            duration = format(words.durationBuggy, { d: facts.quadDuration }) + ' · ' + format(words.durationCamel, { d: facts.camelDuration });
        }
        var cardSummary;
        if (canonicalKey === 'standard') {
            cardSummary = facts.quadDuration + ' ' + words.quadLabel + ' · ' + facts.camelDuration + ' ' + words.camelLabel + ' · ' + words.transferShared + ' · ' + words.dinnerShow;
        } else if (canonicalKey === 'private') {
            cardSummary = facts.quadDuration + ' ' + words.quadLabel + ' · ' + facts.camelDuration + ' ' + words.camelLabel + ' · ' + words.transferPrivate + ' · ' + words.gifts;
        } else if (canonicalKey === 'private-plus') {
            cardSummary = words.fullDay + ' · ' + facts.quadDuration + ' ' + words.quadLabel + ' · ' + facts.camelDuration + ' ' + words.camelLabel + ' · ' + words.lunchDinner;
        } else {
            cardSummary = facts.quadDuration + ' ' + words.buggyLabel + ' · ' + facts.camelDuration + ' ' + words.camelLabel + ' · ' + words.transferPrivate + ' · ' + words.dinnerShow;
        }

        return {
            name: copy[0], title: copy[1], cta: copy[2],
            transport: transport, duration: duration, cardSummary: cardSummary,
            tag: copy[0].toUpperCase() + ' · ' + (price == null ? '' : price + '€') + ' ' + ui.perGuest,
            fromPrice: ui.from + ' ' + (price == null ? '' : price + '€') + ' ' + ui.perPerson,
            includes: includes
        };
    }

    function getUiString(key, locale) {
        var table = UI_STRINGS[normalizeLocale(locale)] || UI_STRINGS.en;
        return table[key] || '';
    }

    return Object.freeze({
        normalizeLocale: normalizeLocale,
        getLocalizedFields: getLocalizedFields,
        getUiString: getUiString,
        LOCALIZED_DATA: COPY,
        UI_STRINGS: UI_STRINGS
    });
}));
