/**
 * whatsapp-prefill.js
 * ─────────────────────────────────────────────────────────────────────────────
 * Dynamic WhatsApp pre-filled message generator for Marragafay.
 *
 * Works on EVERY page that includes this script:
 *   • Pack / Activity pages rendered by TourPageTemplate (via its internal call)
 *   • index.html modals (#whatsapp-btn, #whatsapp-btn-activity)
 *
 * Strategy
 * ─────────────────────────────────────────────────────────────────────────────
 *  1. Pack name: read `data-pack-name` attribute on the <a> tag first,
 *     then fall back to the nearest `data-pack-name` on a parent form/modal,
 *     then fall back to the page <h1>, then to a safe default string.
 *  2. Language: read `<html lang="xx">`.  Supports EN / FR / ES / PT / DE.
 *     Any unrecognised code falls back to English.
 *  3. URL encoding: uses the native `encodeURIComponent` — line-breaks → %0A,
 *     spaces → %20, special chars properly escaped.
 *  4. GTM continuity: ONLY `href` is ever mutated.
 *     `id` and `class` attributes are NEVER changed.
 *
 * Usage
 * ─────────────────────────────────────────────────────────────────────────────
 *  Include the script after the DOM-generating code on any page:
 *
 *    <script src="../js/whatsapp-prefill.js"></script>
 *
 *  The script self-invokes via DOMContentLoaded (or immediately if the DOM is
 *  already ready at load time), so order relative to other scripts is safe.
 *
 *  To override the language on a specific button without changing <html lang>,
 *  add a `data-lang` attribute to the <a> tag:
 *    <a id="whatsapp-btn" data-lang="fr" …>
 *
 *  To override the pack name on a button, add `data-pack-name`:
 *    <a id="whatsapp-btn" data-pack-name="Luxe Pack" …>
 * ─────────────────────────────────────────────────────────────────────────────
 */

(function (window, document) {
  'use strict';

  // ── Configuration ──────────────────────────────────────────────────────────
  var PHONE = '212672531624';

  /**
   * Localised message templates.
   * Each function receives the resolved pack name and returns a plain string
   * (NOT yet encoded).  Line-breaks are represented as \n.
   */
  var TEMPLATES = {
    ar: function (pack, ref) {
      return (
        'مرحباً Marragafay!\n' +
        'أود التحقق من توفر ' + pack + '.\n' +
        'التفاصيل:\n' +
        '- التاريخ:\n' +
        '- عدد الأفراد:' +
        (ref ? '\nRef: ' + ref : '')
      );
    },
    fr: function (pack, ref) {
      return (
        'Bonjour Marragafay !\n' +
        'Je souhaite vérifier la disponibilité pour ' + pack + '.\n' +
        'Mes détails :\n' +
        '- Date :\n' +
        '- Personnes :' +
        (ref ? '\nRef: ' + ref : '')
      );
    },
    es: function (pack, ref) {
      return (
        '¡Hola Marragafay! Quiero consultar disponibilidad para ' + pack + '.\n' +
        'Mis datos:\n' +
        '- Fecha:\n' +
        '- Personas:' +
        (ref ? '\nRef: ' + ref : '')
      );
    },
    pt: function (pack, ref) {
      return (
        'Olá Marragafay! Quero verificar disponibilidade para ' + pack + '.\n' +
        'Meus detalhes:\n' +
        '- Data:\n' +
        '- Pessoas:' +
        (ref ? '\nRef: ' + ref : '')
      );
    },
    de: function (pack, ref) {
      return (
        'Hallo Marragafay! Ich möchte die Verfügbarkeit für ' + pack + ' prüfen.\n' +
        'Meine Details:\n' +
        '- Datum:\n' +
        '- Gäste:' +
        (ref ? '\nRef: ' + ref : '')
      );
    },
    en: function (pack, ref) {
      return (
        'Hello Marragafay!\n' +
        'I would like to check availability for ' + pack + '.\n' +
        'My details:\n' +
        '- Date:\n' +
        '- Guests:' +
        (ref ? '\nRef: ' + ref : '')
      );
    }
  };

  // ── Helpers ────────────────────────────────────────────────────────────────

  /**
   * Normalise a BCP-47 tag to a bare two-letter code.
   * "fr-FR" → "fr",  "EN" → "en",  "zh-Hans" → "zh" (falls back to "en")
   */
  function normaliseLang(raw) {
    if (!raw) return 'en';
    var code = raw.toLowerCase().split(/[-_]/)[0];
    return TEMPLATES[code] ? code : 'en';
  }

  /**
   * Try to read the pack name for a given WhatsApp button element.
   * Priority:
   *   1. data-pack-name on the <a> itself
   *   2. data-pack-name on the closest ancestor with that attribute
   *   3. First <h1 class="pack-title"> in the document
   *   4. The document <title> minus the site suffix (best-effort)
   *   5. Hardcoded fallback
   */
  function resolvePackName(btn) {
    // 1. Explicit attribute on the button
    var name = btn.getAttribute('data-pack-name');
    if (name && name.trim()) return name.trim();

    // 2. Ancestor with data-pack-name (e.g. a modal wrapper)
    var ancestor = btn.closest ? btn.closest('[data-pack-name]') : null;
    if (!ancestor) {
      // Manual closest for older engines
      var el = btn.parentElement;
      while (el) {
        if (el.hasAttribute && el.hasAttribute('data-pack-name')) {
          ancestor = el;
          break;
        }
        el = el.parentElement;
      }
    }
    if (ancestor) {
      name = ancestor.getAttribute('data-pack-name');
      if (name && name.trim()) return name.trim();
    }

    // 3. Page h1.pack-title (tour pages)
    var h1 = document.querySelector('h1.pack-title');
    if (h1 && h1.textContent.trim()) return h1.textContent.trim();

    // 4. Parse <title>  e.g. "Luxe Pack - Agafay Desert | Marragafay"
    var titleEl = document.title || '';
    var titlePart = titleEl.split(/[-|]/)[0].trim();
    if (titlePart) return titlePart;

    // 5. Fallback
    return 'this Pack';
  }

  /**
   * Build the WhatsApp `href` for a given button, lang override, and pack name.
   */
  function buildHref(btn) {
    // Language: button-level override > html[lang]
    var rawLang = btn.getAttribute('data-lang') ||
                  document.documentElement.getAttribute('lang') ||
                  'en';
    var lang = normaliseLang(rawLang);

    var packName = resolvePackName(btn);
    var inquiryId = btn.getAttribute('data-inquiry-id');
    if (!inquiryId && window.MarragafayAttribution && typeof window.MarragafayAttribution.generateInquiryId === 'function') {
      inquiryId = window.MarragafayAttribution.generateInquiryId();
      btn.setAttribute('data-inquiry-id', inquiryId);
      window.MarragafayAttribution.recordInquiry({
        inquiry_id: inquiryId,
        source_category: 'whatsapp_handoff',
        pack_presented: packName,
        final_requested_pack: packName,
        cta_location: btn.id || btn.className || 'whatsapp_button',
        language: lang
      });
    }

    var message  = TEMPLATES[lang](packName, inquiryId);
    var encoded  = encodeURIComponent(message);

    return 'https://wa.me/' + PHONE + '?text=' + encoded;
  }

  // ── Main Logic ─────────────────────────────────────────────────────────────

  /**
   * Wire up all WhatsApp CTA buttons on the page.
   * Targets:
   *   #whatsapp-btn           – pack / activity booking card
   *   #whatsapp-btn-activity  – index.html activity modal
   *   .whatsapp-cta-btn       – any future buttons using the shared class
   *
   * ONLY href is mutated.  id and class are left untouched.
   */
  function wireButtons() {
    var selectors = [
      '#whatsapp-btn',
      '#whatsapp-btn-activity',
      '.whatsapp-cta-btn'
    ];

    selectors.forEach(function (sel) {
      var elements = document.querySelectorAll(sel);
      elements.forEach(function (btn) {
        if (!btn) return;
        btn.href = buildHref(btn);
      });
    });
  }

  // ── Initialise ─────────────────────────────────────────────────────────────
  // Run immediately if DOM is ready, otherwise wait for DOMContentLoaded.
  // This makes the script safe whether it's in <head> or end of <body>.
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', wireButtons);
  } else {
    wireButtons();
  }

  // Also expose a public API so TourPageTemplate (and future code) can
  // re-trigger wiring after dynamic content is injected.
  window.MarragafayWA = {
    wire: wireButtons,
    buildHref: buildHref
  };

}(window, document));
