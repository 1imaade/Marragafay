/**
 * Global Google Ads conversion tracking for WhatsApp links.
 *
 * This file is intentionally delegated from document-level click handling so
 * it also covers links created or updated after initial page load (including
 * whatsapp-prefill.js). The initialization guard prevents duplicate listeners
 * if the script is accidentally included more than once.
 */
(function (window, document) {
  'use strict';

  var INIT_FLAG = '__marragafayWhatsAppConversionTrackingInitialized';
  var CONVERSION_DESTINATION = 'AW-18107593090/l7wZCI7twukcEILjr7pD';
  var EVENT_TIMEOUT = 800;

  if (window[INIT_FLAG]) return;
  window[INIT_FLAG] = true;

  function isWhatsAppUrl(value) {
    var url;

    try {
      url = new URL(value, document.baseURI);
    } catch (error) {
      return false;
    }

    if (url.protocol !== 'http:' && url.protocol !== 'https:') return false;

    var hostname = url.hostname.toLowerCase();
    return hostname === 'wa.me' ||
      hostname === 'whatsapp.com' ||
      hostname.slice(-'.whatsapp.com'.length) === '.whatsapp.com';
  }

  function once(callback) {
    var called = false;

    return function () {
      if (called) return;
      called = true;
      callback();
    };
  }

  /**
   * Send the conversion and call onComplete when navigation may continue.
   * Missing/failed gtag must never block the original WhatsApp action.
   */
  function reportConversion(onComplete) {
    var complete = once(onComplete || function () {});
    var timeoutId = window.setTimeout(complete, EVENT_TIMEOUT);

    try {
      if (typeof window.gtag !== 'function') {
        window.clearTimeout(timeoutId);
        complete();
        return;
      }

      window.gtag('event', 'conversion', {
        'send_to': CONVERSION_DESTINATION,
        'event_callback': function () {
          window.clearTimeout(timeoutId);
          complete();
        },
        'event_timeout': EVENT_TIMEOUT
      });
    } catch (error) {
      window.clearTimeout(timeoutId);
      complete();
    }
  }

  /**
   * Public helper for any future explicit CTA wiring.
   * It follows Google's callback pattern for same-tab navigation.
   */
  window.gtag_report_conversion = function (url) {
    reportConversion(function () {
      if (typeof url !== 'undefined' && url !== null) {
        window.location.href = url;
      }
    });

    return false;
  };

  function getAnchor(target) {
    var element = target;

    while (element && element !== document) {
      if (element.tagName && element.tagName.toLowerCase() === 'a') {
        return element;
      }
      element = element.parentElement;
    }

    return null;
  }

  document.addEventListener('click', function (event) {
    if (event.defaultPrevented) return;

    var link = getAnchor(event.target);
    if (!link || !link.href || !isWhatsAppUrl(link.href)) return;

    // Mark this event so a re-dispatched/bubbled copy cannot count twice.
    if (event.__marragafayWhatsAppConversionHandled) return;
    event.__marragafayWhatsAppConversionHandled = true;

    var target = (link.getAttribute('target') || '').toLowerCase();
    var preservesNativeNavigation = target === '_blank' ||
      event.button !== 0 || event.metaKey || event.ctrlKey ||
      event.shiftKey || event.altKey;

    if (preservesNativeNavigation) {
      // Do not interfere with new-tab or modified-click behavior.
      reportConversion();
      return;
    }

    event.preventDefault();
    reportConversion(function () {
      window.location.href = link.href;
    });
  }, true);

  // Small public surface for diagnostics and explicit integrations.
  window.MarragafayWhatsAppConversion = {
    destination: CONVERSION_DESTINATION,
    isWhatsAppUrl: isWhatsAppUrl,
    report: reportConversion
  };
}(window, document));
