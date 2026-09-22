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
            standard: ['Standard', 'Agafay Evening Experience', 'View Standard Pack ►'],
            private: ['Private', 'Private Agafay Evening', 'View Private Pack ►'],
            'private-plus': ['Private+', 'Agafay & Atlas — Full-Day Quad', 'View Private+ Pack ►'],
            buggy: ['Buggy', 'Private Agafay Buggy Experience', 'Discover Buggy Experience ►']
        },
        fr: {
            standard: ['Standard', 'Expérience Soirée Agafay', 'Découvrir le forfait ►'],
            private: ['Privé', 'Soirée Privée à Agafay', 'Découvrir le forfait ►'],
            'private-plus': ['Privé+', 'Agafay & Atlas — Journée Complète Quad', 'Découvrir le forfait ►'],
            buggy: ['Buggy', 'Expérience Privée en Buggy à Agafay', 'Découvrir l\'expérience buggy ►']
        },
        es: {
            standard: ['Estándar', 'Experiencia Nocturna en Agafay', 'Descubrir el paquete ►'],
            private: ['Privado', 'Velada Privada en Agafay', 'Descubrir el paquete ►'],
            'private-plus': ['Privado+', 'Agafay y Atlas — Día Completo en Quad', 'Descubrir el paquete ►'],
            buggy: ['Buggy', 'Experiencia Privada en Buggy por Agafay', 'Descubrir experiencia en buggy ►']
        },
        ar: {
            standard: ['القياسية', 'تجربة أمسية أكافاي', 'استكشف الباقة ◄'],
            private: ['الخاصة', 'أمسية أكافاي الخاصة', 'استكشف الباقة ◄'],
            'private-plus': ['خاصة+', 'أكافاي والأطلس — يوم كامل كواد', 'استكشف الباقة ◄'],
            buggy: ['بوغي', 'تجربة البوغي الخاصة بأكافاي', 'استكشف تجربة البوغي ◄']
        }
    };

    // Language-only sentence frames. Numeric and operational values are injected from ProductData.
    var WORDS = {
        en: {
            shared: 'Shared hotel / riad pickup & return', private: 'Private hotel / riad transfer',
            quad: '{d} quad ride across Agafay', quadPrivate: '{d} private quad session',
            quadPlus: '{d} private quad exploration across Agafay & the Atlas', buggy: '{d} private buggy ride',
            camel: '{d} camel ride', pool: 'Pool access & Moroccan mint tea', sunset: 'Sunset photo pause',
            dinner: 'Traditional Moroccan dinner', show: 'Live fire & music show', guide: 'Dedicated guide',
            fullGuide: 'Dedicated full-day guide', scarf: 'Desert scarf to wear & keep',
            water: 'Bottled water included', softDrink: 'Bottled water + soft drink', sweets: 'Moroccan sweets',
            safety: 'Safety gear & briefing', lunch: 'Traditional Moroccan lunch',
            transferShared: 'Shared Transfer', transferPrivate: 'Private Transfer',
            quadLabel: 'Quad', camelLabel: 'Camel', buggyLabel: 'Buggy', guideLabel: 'Guide',
            lunchDinner: 'Lunch & Dinner', dinnerShow: 'Dinner & Show', twoGuests: '2 guests/buggy'
        },
        fr: {
            shared: 'Prise en charge et retour partagés depuis votre hôtel ou riad', private: 'Transfert privé aller-retour depuis votre hôtel ou riad',
            quad: 'Sortie de quad de {d} à travers le désert d\'Agafay', quadPrivate: 'Session privée en quad de {d}',
            quadPlus: 'Exploration privée en quad de {d} à travers Agafay et l\'Atlas', buggy: 'Balade privée en buggy de {d}',
            camel: 'Balade à dos de dromadaire de {d}', pool: 'Accès piscine & thé à la menthe marocain', sunset: 'Pause photo au coucher du soleil',
            dinner: 'Dîner marocain traditionnel', show: 'Spectacle vivant de feu et musique', guide: 'Guide dédié',
            fullGuide: 'Guide dédié pour la journée complète', scarf: 'Chèche du désert offert à porter et garder',
            water: 'Eau minérale en bouteille', softDrink: 'Eau en bouteille + boisson sans alcool', sweets: 'Pâtisseries marocaines',
            safety: 'Équipement de sécurité & briefing', lunch: 'Déjeuner marocain traditionnel',
            transferShared: 'Transfert Partagé', transferPrivate: 'Transfert Privé',
            quadLabel: 'Quad', camelLabel: 'Dromadaire', buggyLabel: 'Buggy', guideLabel: 'Guide',
            lunchDinner: 'Déjeuner & Dîner', dinnerShow: 'Dîner & Spectacle', twoGuests: '2 pers/buggy'
        },
        es: {
            shared: 'Recogida y regreso compartidos desde su hotel o riad', private: 'Traslado privado de ida y vuelta desde su hotel o riad',
            quad: 'Paseo en quad de {d} por Agafay', quadPrivate: 'Sesión privada de quad de {d}',
            quadPlus: 'Exploración privada en quad de {d} por Agafay y el Atlas', buggy: 'Paseo privado en buggy de {d}',
            camel: 'Paseo en camello de {d}', pool: 'Acceso a la piscina y té de menta marroquí', sunset: 'Pausa fotográfica al atardecer',
            dinner: 'Cena tradicional marroquí', show: 'Espectáculo en vivo de fuego y música', guide: 'Guía exclusivo dedicado',
            fullGuide: 'Guía dedicado de jornada completa', scarf: 'Pañuelo del desierto de regalo',
            water: 'Agua mineral embotellada', softDrink: 'Agua embotellada + refresco', sweets: 'Dulces tradicionales marroquíes',
            safety: 'Equipo de seguridad e instrucciones', lunch: 'Almuerzo tradicional marroquí',
            transferShared: 'Traslado Compartido', transferPrivate: 'Traslado Privado',
            quadLabel: 'Quad', camelLabel: 'Camello', buggyLabel: 'Buggy', guideLabel: 'Guía',
            lunchDinner: 'Almuerzo y Cena', dinnerShow: 'Cena y Espectáculo', twoGuests: '2 pers/buggy'
        },
        ar: {
            shared: 'نقل مشترك ذهاباً وإياباً من الفندق أو الرياض', private: 'نقل خاص ذهاباً وإياباً من الفندق أو الرياض',
            quad: 'قيادة كواد لمدة {d} عبر صحراء أكافاي', quadPrivate: 'جلسة كواد خاصة لمدة {d}',
            quadPlus: 'استكشاف خاص بالكواد لمدة {d} عبر أكافاي وجبال الأطلس', buggy: 'جولة بوغي خاصة لمدة {d}',
            camel: 'جولة ركوب الجمال لمدة {d}', pool: 'دخول المسبح وشاي مغربي تقليدي بالنعناع', sunset: 'استراحة تصوير لمشهد غروب الشمس',
            dinner: 'عشاء مغربي تقليدي فاخر', show: 'عرض حي للنار والموسيقى', guide: 'مرشد سياحي خاص ومخصص',
            fullGuide: 'مرشد سياحي مخصص طوال اليوم', scarf: 'وشاح صحراوي أصيل هدية لارتدائه والاحتفاظ به',
            water: 'مياه معدنية معبأة', softDrink: 'مياه معبأة ومشروب غازي', sweets: 'حلويات مغربية تقليدية فاخرة',
            safety: 'معدات السلامة وإرشادات الأمان الكاملة', lunch: 'وجبة غداء مغربية تقليدية كاملة',
            transferShared: 'نقل مشترك', transferPrivate: 'نقل خاص',
            quadLabel: 'كواد', camelLabel: 'جمل', buggyLabel: 'بوغي', guideLabel: 'مرشد',
            lunchDinner: 'غداء وعشاء', dinnerShow: 'عشاء وعرض', twoGuests: 'مركبة لضيفين'
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
            includes = [transport, format(words.quadPrivate, values), format(words.camel, { d: facts.camelDuration }), words.pool, words.sunset, words.dinner, words.show, words.guide, words.scarf, words.softDrink, words.sweets, words.safety];
        } else if (canonicalKey === 'private-plus') {
            includes = [transport, format(words.quadPlus, values), words.lunch, words.pool, format(words.camel, { d: facts.camelDuration }), words.sunset, words.dinner, words.show, words.fullGuide, words.scarf, words.softDrink, words.sweets, words.safety];
        } else {
            includes = [transport, format(words.buggy, values), words.twoGuests, format(words.camel, { d: facts.camelDuration }), words.pool, words.sunset, words.dinner, words.show, words.guide, words.water, words.safety];
        }

        var ui = UI_STRINGS[loc] || UI_STRINGS.en;
        var price = product && product.priceEUR;
        var duration = product && product.duration || '';
        var cardSummary;
        if (canonicalKey === 'standard') {
            cardSummary = duration + ' · ' + (facts.transportMode === 'shared' ? words.transferShared : words.transferPrivate) + ' · ' + facts.quadDuration + ' ' + words.quadLabel + ' · ' + facts.camelDuration + ' ' + words.camelLabel + ' · ' + words.dinnerShow;
        } else if (canonicalKey === 'private') {
            cardSummary = duration + ' · ' + words.transferPrivate + ' · ' + facts.quadDuration + ' ' + words.quadLabel + ' · ' + facts.camelDuration + ' ' + words.camelLabel + ' · ' + words.guideLabel + ' · ' + words.dinnerShow;
        } else if (canonicalKey === 'private-plus') {
            cardSummary = duration + ' · ' + words.transferPrivate + ' · ' + facts.quadDuration + ' ' + words.quadLabel + ' · ' + words.lunchDinner + ' · ' + facts.camelDuration + ' ' + words.camelLabel + ' · ' + words.guideLabel;
        } else {
            cardSummary = duration + ' · ' + words.transferPrivate + ' · ' + facts.quadDuration + ' ' + words.buggyLabel + ' (' + words.twoGuests + ') · ' + facts.camelDuration + ' ' + words.camelLabel + ' · ' + words.dinnerShow;
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
