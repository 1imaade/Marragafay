import re
import os
from generate_all_multilingual_articles import ui_translations, articles_meta
from redesign_in_article_cta import new_cta_css, cta_content

languages = ["fr", "es", "ar"]

for filename, meta in articles_meta.items():
    en_filepath = f"en/blog/{filename}"
    with open(en_filepath, "r", encoding="utf-8") as f:
        en_html = f.read()

    # Extract the <article class="article-body"> ... </article>
    body_match = re.search(r'<article class="article-body">(.*?)</article>', en_html, flags=re.DOTALL)
    if not body_match:
        print(f"Error matching body in {en_filepath}")
        continue
    
    en_body = body_match.group(1)

    for lang in languages:
        t = ui_translations[lang]
        m = meta[lang]
        c = cta_content[lang]
        slug = meta["slug"]
        image = meta["image"]
        date_iso = meta["date"]
        read_time = meta["read_time"]

        is_rtl = (lang == "ar")
        dir_attr = ' dir="rtl"' if is_rtl else ''
        rtl_css = """
    body { direction: rtl; text-align: right; }
    .breadcrumb-nav { flex-direction: row-reverse; justify-content: flex-end; }
    .breadcrumb-nav .sep { transform: scaleX(-1); }
    .share-buttons { margin-right: auto; margin-left: 0; }
    .experience-inset__actions { flex-direction: row-reverse; }
    .experience-inset__btn svg { transform: scaleX(-1); }
    .related-card-arrow svg { transform: scaleX(-1); }
    .related-articles-header { flex-direction: row-reverse; }
    .article-experience-inset { text-align: right; }
    """ if is_rtl else ""

        # Replace CTA block in body with localized CTA block
        localized_cta = f"""<div class="article-experience-inset">
        <div class="experience-inset__header">
          <span class="experience-inset__eyebrow">{c['eyebrow']}</span>
          <span class="experience-inset__badge">{c['badge']}</span>
        </div>
        <h3 class="experience-inset__title">{m['title']}</h3>
        <p class="experience-inset__desc">{m['subtitle']}</p>
        
        <div class="experience-inset__perks">
          <span class="inset-perk">
            <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
            {c['perk1']}
          </span>
          <span class="inset-perk">
            <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
            {c['perk2']}
          </span>
          <span class="inset-perk">
            <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
            {c['perk3']}
          </span>
        </div>

        <div class="experience-inset__actions">
          <a href="/{lang}/packs" class="experience-inset__btn">
            <span>{c['btn']}</span>
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
          </a>
          <a href="https://wa.me/212672531624?text={c['wa_text']}" target="_blank" class="experience-inset__whatsapp">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.771-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.312.045-.694.072-2.148-.526-1.857-.764-3.045-2.658-3.137-2.781-.092-.123-.75-1-.75-1.909 0-.909.477-1.355.646-1.541.17-.186.371-.233.495-.233.124 0 .248.002.355.008.113.006.264-.043.413.315.155.371.531 1.298.577 1.391.046.093.078.202.015.326-.062.124-.093.202-.186.311-.093.109-.196.243-.28.326-.093.093-.19.195-.082.381.109.186.482.795 1.034 1.286.711.633 1.31.829 1.496.922.186.093.295.078.404-.046.11-.124.466-.543.59-.729.124-.186.249-.155.419-.093.17.062 1.084.511 1.27.604.186.093.31.14.356.217.047.078.047.45-.097.855z"/></svg>
            <span>{c['whatsapp']}</span>
          </a>
        </div>
      </div>"""

        localized_body = re.sub(
            r'<div class="article-experience-inset">.*?</div>\s*</div>',
            localized_cta,
            en_body,
            flags=re.DOTALL
        )

        # Related Articles
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

        full_html = f"""<!DOCTYPE html>
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
    .article-body blockquote, .article-quote {{ border-left: 3px solid #523225; padding-left: 28px; margin: 3rem 0; font-style: italic; font-size: 1.3rem; line-height: 1.6; color: #523225; }}
    .article-figure {{ margin: 3rem 0; }}
    .article-figure img {{ width: 100%; border-radius: 4px; display: block; }}
    .article-figure figcaption {{ font-size: 13px; color: #272724; opacity: 0.45; font-style: italic; margin-top: 10px; }}

    .article-key-takeaways {{ background: rgba(82,50,37,0.04); border-left: 3px solid #523225; padding: 28px 32px; margin: 3rem 0; border-radius: 0 4px 4px 0; }}
    .article-key-takeaways h3 {{ margin-top: 0; font-size: 1.15rem; text-transform: uppercase; letter-spacing: 0.05em; color: #523225; }}
    .article-key-takeaways ul {{ margin-bottom: 0; padding-left: 1.2rem; }}

{new_cta_css}

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

    /* ═══════════════════════════════════════════════
       RESPONSIVE & MOBILE POLISH (ARTICLE PAGES)
    ═══════════════════════════════════════════════ */
    @media (max-width: 1024px) {{
      .article-header {{ padding: 44px 24px 30px; }}
      .article-hero {{ padding: 0 24px; margin-bottom: 40px; }}
      .article-body-wrap, .article-tags-wrap {{ padding: 0 24px; }}
      .related-articles-section {{ padding: 60px 24px; }}
      .related-grid {{ grid-template-columns: repeat(2, 1fr); gap: 28px; }}
    }}

    @media (max-width: 768px) {{
      .navbar-spacer {{ height: var(--nav-height-mobile, 64px); }}
      .article-header {{ padding: 28px 18px 24px; }}
      .breadcrumb-nav {{ font-size: 10.5px; margin-bottom: 14px; gap: 6px; flex-wrap: wrap; }}
      .category-tag {{ font-size: 9.5px; padding: 4px 12px; margin-bottom: 16px; }}
      .article-headline {{ font-size: clamp(1.75rem, 6.5vw, 2.25rem); line-height: 1.15; margin-bottom: 14px; }}
      .article-subheadline {{ font-size: 1.05rem; line-height: 1.5; margin-bottom: 22px; }}
      .article-meta-row {{ flex-direction: column; align-items: flex-start; gap: 12px; padding-bottom: 20px; font-size: 12px; }}
      .share-buttons {{ width: 100%; margin-left: 0; justify-content: flex-start; padding-top: 6px; gap: 8px; }}
      .share-btn {{ font-size: 11px; padding: 6px 12px; }}

      .article-hero {{ padding: 0 18px; margin-bottom: 28px; }}
      .article-hero img {{ aspect-ratio: 16/10; border-radius: 6px; }}
      .article-hero-caption {{ font-size: 11.5px; margin-top: 8px; }}

      .article-body-wrap {{ padding: 0 18px; margin: 24px auto 0; }}
      .article-body p {{ font-size: 16.5px; line-height: 1.75; margin-bottom: 1.4em; }}
      .article-body h2 {{ font-size: 1.45rem; line-height: 1.25; margin-top: 2.4rem; margin-bottom: 0.9rem; }}
      .article-body h3 {{ font-size: 1.2rem; margin-top: 1.8rem; margin-bottom: 0.6rem; }}
      .article-body ul {{ padding-left: 1.2rem; margin-bottom: 1.5rem; }}
      .article-body ul li {{ font-size: 16.5px; line-height: 1.7; margin-bottom: 0.5em; }}
      .article-body blockquote, .article-quote {{ padding: 6px 0 6px 16px; margin: 2rem 0; font-size: 1.1rem; line-height: 1.55; }}
      .article-figure {{ margin: 2rem 0; }}
      .article-key-takeaways {{ padding: 20px 20px; margin: 2rem 0; }}
      .article-key-takeaways h3 {{ font-size: 1rem; }}

      .article-cta-box, .article-experience-inset {{ padding: 28px 18px; margin: 2.8rem 0; border-radius: 8px; }}
      .experience-inset__actions {{ flex-direction: column; width: 100%; }}
      .experience-inset__btn, .experience-inset__whatsapp {{ width: 100%; justify-content: center; box-sizing: border-box; }}

      .article-tags-wrap {{ padding: 24px 18px 40px; }}
      .article-tag {{ font-size: 11px; padding: 5px 12px; }}

      .related-articles-section {{ padding: 48px 18px; }}
      .related-articles-inner {{ padding: 0; }}
      .related-articles-header {{ margin-bottom: 28px; padding-bottom: 14px; }}
      .related-articles-title {{ font-size: 1.15rem; }}
      .related-articles-link {{ font-size: 11px; }}
      .related-grid {{ grid-template-columns: 1fr; gap: 24px; }}
      .related-card-title {{ font-size: 1.15rem; }}
    }}
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
        {localized_body}
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

        out_path = f"{lang}/blog/{filename}"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(full_html)
        print(f"Generated {out_path}")

print("Successfully built complete multilingual corpus across all 28 articles!")
