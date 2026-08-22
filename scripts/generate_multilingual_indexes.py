import os

# 1. French Blog Index (fr/blog/index.html)
fr_html = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />

  <title>La Revue &#8212; Récits et Guides du Désert d'Agafay | Marragafay</title>
  <meta name="description" content="Notes de terrain, guides exclusifs et rencontres d'exception dans le désert de pierre d'Agafay, près de Marrakech. Les archives éditoriales de Marragafay." />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="https://marragafay.com/fr/blog" />

  <meta property="og:type" content="website" />
  <meta property="og:title" content="La Revue &#8212; Récits et Guides du Désert d'Agafay | Marragafay" />
  <meta property="og:description" content="Notes de terrain, guides exclusifs et rencontres d'exception dans le désert de pierre d'Agafay." />
  <meta property="og:url" content="https://marragafay.com/fr/blog" />
  <meta property="og:image" content="https://marragafay.com/images/Slider-images/slider-1.webp" />
  <meta property="og:site_name" content="Marragafay" />

  <link rel="alternate" hreflang="en" href="https://marragafay.com/en/blog" />
  <link rel="alternate" hreflang="fr" href="https://marragafay.com/fr/blog" />
  <link rel="alternate" hreflang="es" href="https://marragafay.com/es/blog" />
  <link rel="alternate" hreflang="ar" href="https://marragafay.com/ar/blog" />
  <link rel="alternate" hreflang="x-default" href="https://marragafay.com/blog" />

  <link rel="preconnect" href="https://api.fontshare.com" />
  <link href="https://api.fontshare.com/v2/css?f[]=clash-grotesk@400,500,600,700&display=swap" rel="stylesheet" />

  <link rel="stylesheet" href="/css/vendor-bundle.css" />
  <link rel="stylesheet" href="/css/custom-bundle.css" />
  <link rel="stylesheet" href="/css/style.css" />
  <link rel="stylesheet" href="/css/navbar-stayhere.css" />
  <link rel="stylesheet" href="/css/tailwind-built.css" />

  <style>:root{--nav-bg:transparent;--nav-bg-scrolled:#F6F7EA;--nav-text:#272724;--nav-text-scrolled:#272724;--nav-text-muted:#7a756e;--nav-accent:#523225;--nav-accent-hover:#3d241a;--nav-border:rgba(0,0,0,0.06);--nav-height:72px;--nav-height-mobile:64px;--nav-transition:0.3s cubic-bezier(0.4,0,0.2,1);--nav-shadow:0 1px 0 var(--nav-border);--nav-shadow-scrolled:0 2px 20px rgba(0,0,0,0.06)}.navbar.navbar-stayhere,.navbar.navbar-stayhere *{box-sizing:border-box}.navbar.navbar-stayhere{position:fixed!important;top:0!important;left:0!important;right:0!important;width:100%!important;z-index:1100!important;background:var(--nav-bg)!important;border:none!important;border-bottom:1px solid var(--nav-border)!important;box-shadow:none!important;padding:0!important;margin:0!important;display:block!important;flex-wrap:nowrap!important;height:var(--nav-height);transition:box-shadow var(--nav-transition),background var(--nav-transition)!important}</style>

  <style>
    * { font-family: 'Clash Grotesk', sans-serif !important; }
    #ftco-navbar, #ftco-navbar.scrolled, #ftco-navbar.awake, #ftco-navbar.sleep {
      background-color: #F6F7EA !important;
      background: #F6F7EA !important;
      --nav-text: #272724 !important;
      --nav-text-muted: #272724 !important;
    }
    #ftco-navbar .nav-link:not(.booking-btn),
    #ftco-navbar .navbar-brand,
    #ftco-navbar .language-toggle,
    #ftco-navbar .language-toggle span,
    #ftco-navbar .language-toggle i,
    #ftco-navbar .dropdown-item,
    #ftco-navbar .navbar-toggler,
    #ftco-navbar .icon-menu,
    #ftco-navbar .icon-menu::before,
    #ftco-navbar.scrolled .nav-link:not(.booking-btn),
    #ftco-navbar.scrolled .navbar-brand {
      color: #272724 !important;
      border-color: #272724 !important;
    }
  </style>

  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    document.addEventListener('DOMContentLoaded', function() {
      setTimeout(function() {
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
        (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-PK8G4JC2');
      }, 2000);
    });
  </script>

  <style>
    html, body { background-color: #F6F7EA; color: #272724; margin: 0; padding: 0; }
    body.blog { background-color: #F6F7EA; }
    .sr-only { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; border-width: 0; }
    .journal-page { padding-top: var(--nav-height, 72px); }
    .journal-hero { background-color: #F6F7EA; padding: 80px 0 60px; border-bottom: 1px solid rgba(39,39,36,0.12); }
    .journal-hero__inner { max-width: 1200px; margin: 0 auto; padding: 0 32px; }
    .journal-hero__eyebrow { display: inline-block; font-size: 11px; font-weight: 600; letter-spacing: 0.3em; text-transform: uppercase; color: #523225; margin-bottom: 28px; position: relative; padding-left: 28px; }
    .journal-hero__eyebrow::before { content: ''; position: absolute; left: 0; top: 50%; transform: translateY(-50%); width: 18px; height: 1px; background: #523225; }
    .journal-hero__headline { font-size: clamp(3.2rem, 7vw, 7rem); font-weight: 700; line-height: 0.92; letter-spacing: -0.03em; color: #272724; margin: 0 0 28px; max-width: 900px; }
    .journal-hero__subline { font-size: clamp(0.95rem, 1.5vw, 1.125rem); font-weight: 400; color: #7a756e; max-width: 520px; line-height: 1.65; margin: 0 0 48px; }
    .journal-hero__divider { border: 0; border-top: 1px solid rgba(39,39,36,0.12); margin: 0 0 36px; }
    .category-filter { display: flex; flex-wrap: wrap; gap: 10px; align-items: center; }
    .category-filter__label { font-size: 11px; font-weight: 600; letter-spacing: 0.2em; text-transform: uppercase; color: #7a756e; margin-right: 6px; }
    .category-pill { display: inline-flex; align-items: center; padding: 8px 18px; border-radius: 999px; border: 1px solid rgba(39,39,36,0.2); font-size: 12px; font-weight: 500; letter-spacing: 0.05em; color: #272724; background: transparent; cursor: pointer; transition: all 0.22s ease; text-transform: uppercase; font-family: 'Clash Grotesk', sans-serif !important; }
    .category-pill:hover { border-color: #523225; color: #523225; background: rgba(82,50,37,0.05); }
    .category-pill.active { background: #272724; color: #F6F7EA; border-color: #272724; }
    .journal-section { max-width: 1200px; margin: 0 auto; padding: 0 32px; }
    .journal-section-wrap { padding: 80px 0; }
    .section-label { font-size: 10px; font-weight: 700; letter-spacing: 0.35em; text-transform: uppercase; color: #523225; margin-bottom: 32px; display: flex; align-items: center; gap: 14px; }
    .section-label::after { content: ''; flex: 1; height: 1px; background: rgba(39,39,36,0.1); display: block; }
    .featured-article { display: grid; grid-template-columns: 1fr 1fr; gap: 0; background: #EEF0E2; border-radius: 4px; overflow: hidden; min-height: 520px; }
    .featured-article__image-wrap { position: relative; overflow: hidden; }
    .featured-article__image-wrap img { width: 100%; height: 100%; object-fit: cover; display: block; transition: transform 0.6s cubic-bezier(0.4,0,0.2,1); }
    .featured-article:hover .featured-article__image-wrap img { transform: scale(1.04); }
    .featured-article__image-overlay { position: absolute; inset: 0; background: linear-gradient(135deg,rgba(39,39,36,0.25) 0%,rgba(39,39,36,0.05) 100%); z-index: 1; }
    .featured-article__badge { position: absolute; top: 24px; left: 24px; z-index: 2; background: #F6F7EA; color: #523225; font-size: 9px; font-weight: 700; letter-spacing: 0.25em; text-transform: uppercase; padding: 6px 14px; border-radius: 2px; }
    .featured-article__content { padding: 52px 52px 52px 56px; display: flex; flex-direction: column; justify-content: center; background: #EEF0E2; }
    .featured-article__category { font-size: 10px; font-weight: 700; letter-spacing: 0.3em; text-transform: uppercase; color: #523225; margin-bottom: 20px; }
    .featured-article__title { font-size: clamp(1.5rem,2.8vw,2.25rem); font-weight: 700; line-height: 1.12; letter-spacing: -0.02em; color: #272724; margin: 0 0 20px; }
    .featured-article__excerpt { font-size: 0.975rem; line-height: 1.7; color: #5a5a54; margin: 0 0 32px; max-width: 420px; }
    .featured-article__meta { display: flex; align-items: center; gap: 16px; font-size: 12px; color: #7a756e; font-weight: 500; margin-bottom: 32px; letter-spacing: 0.02em; }
    .featured-article__meta-dot { width: 3px; height: 3px; border-radius: 50%; background: #7a756e; display: inline-block; flex-shrink: 0; }
    .featured-article__author { font-size: 11px; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; color: #272724; }
    .featured-article__cta { display: inline-flex; align-items: center; gap: 10px; font-size: 13px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: #272724; text-decoration: none; border-bottom: 1.5px solid #272724; padding-bottom: 2px; transition: color 0.2s ease,border-color 0.2s ease,gap 0.2s ease; width: fit-content; }
    .featured-article__cta:hover { color: #523225; border-color: #523225; gap: 16px; text-decoration: none; }
    .featured-article__cta-arrow { font-size: 16px; line-height: 1; transition: transform 0.2s ease; }
    .featured-article__cta:hover .featured-article__cta-arrow { transform: translateX(4px); }
    .article-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 28px; }
    .article-card { background: #EEF0E2; border-radius: 4px; overflow: hidden; display: flex; flex-direction: column; text-decoration: none; color: inherit; transition: transform 0.28s cubic-bezier(0.4,0,0.2,1); }
    .article-card:hover { transform: translateY(-4px); text-decoration: none; color: inherit; }
    .article-card__image-wrap { position: relative; overflow: hidden; aspect-ratio: 4/3; }
    .article-card__image-wrap img { width: 100%; height: 100%; object-fit: cover; display: block; transition: transform 0.5s cubic-bezier(0.4,0,0.2,1); }
    .article-card:hover .article-card__image-wrap img { transform: scale(1.05); }
    .article-card__body { padding: 28px 28px 24px; display: flex; flex-direction: column; flex: 1; }
    .article-card__category { font-size: 9px; font-weight: 700; letter-spacing: 0.3em; text-transform: uppercase; color: #523225; margin-bottom: 12px; }
    .article-card__title { font-size: 1.05rem; font-weight: 700; line-height: 1.25; letter-spacing: -0.01em; color: #272724; margin: 0 0 12px; }
    .article-card__excerpt { font-size: 0.875rem; line-height: 1.65; color: #5a5a54; margin: 0 0 20px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
    .article-card__meta { display: flex; align-items: center; gap: 10px; font-size: 11px; color: #7a756e; font-weight: 500; margin-top: auto; padding-top: 16px; border-top: 1px solid rgba(39,39,36,0.08); }
    .article-card__meta-sep { width: 2px; height: 2px; border-radius: 50%; background: #aaa9a0; display: inline-block; flex-shrink: 0; }
    .no-results { grid-column: 1/-1; text-align: center; padding: 60px 20px; color: #7a756e; font-size: 0.95rem; display: none; }
    .newsletter-section { background: #272724; padding: 90px 0; }
    .newsletter-inner { max-width: 600px; margin: 0 auto; padding: 0 32px; text-align: center; }
    .newsletter-eyebrow { font-size: 10px; font-weight: 700; letter-spacing: 0.35em; text-transform: uppercase; color: #523225; margin-bottom: 20px; }
    .newsletter-headline { font-size: clamp(2rem,4vw,3rem); font-weight: 700; line-height: 1.05; letter-spacing: -0.025em; color: #F6F7EA; margin: 0 0 18px; }
    .newsletter-subtext { font-size: 0.95rem; line-height: 1.7; color: rgba(246,247,234,0.65); margin: 0 0 40px; }
    .newsletter-form { display: flex; gap: 0; max-width: 480px; margin: 0 auto; border: 1px solid rgba(246,247,234,0.2); border-radius: 3px; overflow: hidden; }
    .newsletter-form__input { flex: 1; background: transparent; border: none; outline: none; padding: 16px 20px; font-size: 14px; color: #F6F7EA; font-family: 'Clash Grotesk', sans-serif !important; }
    .newsletter-form__input::placeholder { color: rgba(246,247,234,0.4); }
    .newsletter-form__btn { background: #523225; color: #F6F7EA; border: none; padding: 16px 28px; font-size: 12px; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase; cursor: pointer; font-family: 'Clash Grotesk', sans-serif !important; transition: background 0.2s ease; white-space: nowrap; }
    .newsletter-form__btn:hover { background: #3d241a; }
    .newsletter-note { font-size: 11px; color: rgba(246,247,234,0.35); margin-top: 16px; letter-spacing: 0.02em; }
    @media (max-width: 1024px) { .article-grid { grid-template-columns: repeat(2,1fr); } }
    @media (max-width: 768px) {
      .journal-hero { padding: 60px 0 48px; }
      .journal-hero__inner, .journal-section { padding: 0 20px; }
      .journal-section-wrap { padding: 56px 0; }
      .featured-article { grid-template-columns: 1fr; min-height: auto; }
      .featured-article__image-wrap { height: 280px; }
      .featured-article__content { padding: 36px 28px; }
      .article-grid { grid-template-columns: 1fr; gap: 20px; }
      .newsletter-section { padding: 64px 0; }
      .newsletter-form { flex-direction: column; }
      .newsletter-form__input { border-bottom: 1px solid rgba(246,247,234,0.2); }
      .newsletter-form__btn { padding: 14px 20px; }
    }
  </style>
</head>

<body class="blog">
  <nav style="height: var(--nav-height, 72px);" class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light" id="ftco-navbar">
    <div class="container">
      <a class="navbar-brand" href="/fr/"><img src="/images/logo-trensparent.webp" alt="Marragafay" style="width: 70px; height: 70px;" width="70" height="70"></a>
      <div class="mobile-language-switcher">
        <a href="#" class="language-toggle" id="languageDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          <i class="icon-globe"></i> <span>FR</span>
        </a>
        <div class="dropdown-menu dropdown-menu-right" aria-labelledby="languageDropdown">
          <a class="dropdown-item lang-option" href="#" data-lang="en">English</a>
          <a class="dropdown-item lang-option" href="#" data-lang="fr">Français</a>
          <a class="dropdown-item lang-option" href="#" data-lang="es">Español</a>
          <a class="dropdown-item lang-option" href="#" data-lang="ar" dir="rtl">العربية</a>
        </div>
      </div>
      <button class="navbar-toggler" type="button" aria-label="Toggle navigation"><span class="icon-menu"></span></button>
      <div class="collapse navbar-collapse">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item"><a href="/fr/" class="nav-link">Accueil</a></li>
          <li class="nav-item"><a href="/fr/activities" class="nav-link">Activités</a></li>
          <li class="nav-item"><a href="/fr/packs" class="nav-link">Packs</a></li>
          <li class="nav-item"><a href="/fr/about" class="nav-link">À Propos</a></li>
          <li class="nav-item"><a href="/fr/reviews" class="nav-link">Avis</a></li>
          <li class="nav-item active"><a href="/fr/blog" class="nav-link">La Revue</a></li>
          <li class="nav-item"><a href="/fr/contact" class="nav-link">Contact</a></li>
          <li class="nav-item"><a href="/fr/packs" class="nav-link booking-btn">Réservation</a></li>
        </ul>
      </div>
    </div>
  </nav>

  <div class="journal-page">
    <section class="journal-hero">
      <div class="journal-hero__inner">
        <span class="journal-hero__eyebrow">La Revue.</span>
        <h1 class="journal-hero__headline">Récits du<br>désert de pierre.</h1>
        <p class="journal-hero__subline">Notes de terrain, guides exclusifs et rencontres d'exception dans le désert d'Agafay.</p>
        <hr class="journal-hero__divider" />
        <div class="category-filter" role="group" aria-label="Filtrer les articles">
          <span class="category-filter__label">Catégorie:</span>
          <button class="category-pill active" data-filter="all" aria-pressed="true">Tous</button>
          <button class="category-pill" data-filter="desert-guide" aria-pressed="false">Guides Désert</button>
          <button class="category-pill" data-filter="experience" aria-pressed="false">Expériences</button>
          <button class="category-pill" data-filter="culture" aria-pressed="false">Culture</button>
          <button class="category-pill" data-filter="travel-tips" aria-pressed="false">Conseils</button>
        </div>
      </div>
    </section>

    <section class="journal-section-wrap" id="featured-wrap">
      <div class="journal-section">
        <p class="section-label">À la Une</p>
        <article class="featured-article" data-category="desert-guide" id="featured-article">
          <div class="featured-article__image-wrap">
            <img src="/images/Slider-images/slider-1.webp" alt="Désert d'Agafay au coucher du soleil" loading="eager" fetchpriority="high" decoding="async" />
            <div class="featured-article__image-overlay" aria-hidden="true"></div>
            <span class="featured-article__badge">Choix de la Rédaction</span>
          </div>
          <div class="featured-article__content">
            <p class="featured-article__category">Guide Désert</p>
            <h2 class="featured-article__title">Le Guide Complet du Désert d'Agafay &#8212; Le Désert de Pierre Expliqué</h2>
            <p class="featured-article__excerpt">Ce qui distingue Agafay du Sahara et pourquoi les voyageurs privilégient ce plateau à 45 minutes de Marrakech. Un condensé essentiel sur la destination phare du Maroc.</p>
            <div class="featured-article__meta">
              <span class="featured-article__author">Rédaction Marragafay</span>
              <span class="featured-article__meta-dot" aria-hidden="true"></span>
              <span>Août 2026</span>
              <span class="featured-article__meta-dot" aria-hidden="true"></span>
              <span>8 min de lecture</span>
            </div>
            <a href="/en/blog/agafay-desert-guide" class="featured-article__cta">
              Lire l'Article <span class="featured-article__cta-arrow" aria-hidden="true">&#8594;</span>
            </a>
          </div>
        </article>
      </div>
    </section>

    <section class="journal-section-wrap" style="padding-top: 0;" id="grid-wrap">
      <div class="journal-section">
        <p class="section-label">Derniers Récits</p>
        <div class="article-grid" id="article-grid" role="list">

          <a href="/en/blog/agafay-camel-ride" class="article-card" data-category="experience" role="listitem">
            <div class="article-card__image-wrap">
              <img src="/images/Slider-images/slider-3.webp" alt="Balade en dromadaire à Agafay" loading="lazy" decoding="async" width="640" height="480" />
            </div>
            <div class="article-card__body">
              <p class="article-card__category">Expérience</p>
              <h3 class="article-card__title">Balade en Dromadaire au Crépuscule : Ce qu'il Faut Savoir</h3>
              <p class="article-card__excerpt">Le silence d'Agafay à l'heure dorée. Notre guide intime pour une traversée mémorable au rythme du désert.</p>
              <div class="article-card__meta">
                <span>Août 2026</span>
                <span class="article-card__meta-sep" aria-hidden="true"></span>
                <span>5 min de lecture</span>
              </div>
            </div>
          </a>

          <a href="/en/blog/agafay-dinner-experience" class="article-card" data-category="experience" role="listitem">
            <div class="article-card__image-wrap">
              <img src="/images/activites/show.webp" alt="Dîner privé dans le désert d'Agafay" loading="lazy" decoding="async" width="640" height="480" />
            </div>
            <div class="article-card__body">
              <p class="article-card__category">Expérience</p>
              <h3 class="article-card__title">Le Dîner Sous les Étoiles : Une Soirée Privée d'Exception</h3>
              <p class="article-card__excerpt">Lumière des bougies, gastronomie marocaine raffinée et ciel étoilé : les secrets de l'expérience la plus prisée.</p>
              <div class="article-card__meta">
                <span>Juin 2026</span>
                <span class="article-card__meta-sep" aria-hidden="true"></span>
                <span>7 min de lecture</span>
              </div>
            </div>
          </a>

          <a href="/en/blog/agafay-desert-vs-sahara" class="article-card" data-category="desert-guide" role="listitem">
            <div class="article-card__image-wrap">
              <img src="/images/Slider-images/slider-2.webp" alt="Comparaison Désert d'Agafay et Sahara" loading="lazy" decoding="async" width="640" height="480" />
            </div>
            <div class="article-card__body">
              <p class="article-card__category">Guide Désert</p>
              <h3 class="article-card__title">Désert d'Agafay ou Sahara : Quel Désert Choisir ?</h3>
              <p class="article-card__excerpt">Temps de trajet, paysages minéraux contre dunes de sable, budget : le comparatif complet pour votre voyage.</p>
              <div class="article-card__meta">
                <span>Août 2026</span>
                <span class="article-card__meta-sep" aria-hidden="true"></span>
                <span>8 min de lecture</span>
              </div>
            </div>
          </a>

          <a href="/en/blog/agafay-quad-biking-guide" class="article-card" data-category="experience" role="listitem">
            <div class="article-card__image-wrap">
              <img src="/images/activites/quad.webp" alt="Quad dans le désert d'Agafay" loading="lazy" decoding="async" width="640" height="480" />
            </div>
            <div class="article-card__body">
              <p class="article-card__category">Aventure</p>
              <h3 class="article-card__title">Quad à Agafay : Sécurité, Parcours et Meilleures Heures</h3>
              <p class="article-card__excerpt">Tout ce que vous devez savoir pour piloter sur les pistes minérales avec des guides experts et du matériel certifié.</p>
              <div class="article-card__meta">
                <span>Août 2026</span>
                <span class="article-card__meta-sep" aria-hidden="true"></span>
                <span>6 min de lecture</span>
              </div>
            </div>
          </a>

          <a href="/en/blog/marrakech-to-agafay" class="article-card" data-category="travel-tips" role="listitem">
            <div class="article-card__image-wrap">
              <img src="/images/destination-4.jpg" alt="Route de Marrakech vers Agafay" loading="lazy" decoding="async" width="640" height="480" />
            </div>
            <div class="article-card__body">
              <p class="article-card__category">Conseils</p>
              <h3 class="article-card__title">De Marrakech au Désert d'Agafay : Toutes les Options de Trajet</h3>
              <p class="article-card__excerpt">Chauffeur privé, location ou taxi : itinéraire de 45 minutes, état des routes et conseils pratiques.</p>
              <div class="article-card__meta">
                <span>Juillet 2026</span>
                <span class="article-card__meta-sep" aria-hidden="true"></span>
                <span>4 min de lecture</span>
              </div>
            </div>
          </a>

          <a href="/en/blog/berber-culture-agafay" class="article-card" data-category="culture" role="listitem">
            <div class="article-card__image-wrap">
              <img src="/images/Slider-images/slider-4.webp" alt="Culture berbère à Agafay" loading="lazy" decoding="async" width="640" height="480" />
            </div>
            <div class="article-card__body">
              <p class="article-card__category">Culture</p>
              <h3 class="article-card__title">L'Héritage Berbère d'Agafay : Une Culture Millénaire</h3>
              <p class="article-card__excerpt">Bien avant l'essor du tourisme, le plateau abritait des communautés amazighes dont l'hospitalité perdure.</p>
              <div class="article-card__meta">
                <span>Juillet 2026</span>
                <span class="article-card__meta-sep" aria-hidden="true"></span>
                <span>6 min de lecture</span>
              </div>
            </div>
          </a>

          <div class="no-results" id="no-results">Aucun article dans cette catégorie pour le moment.</div>
        </div>
      </div>
    </section>

    <section class="newsletter-section">
      <div class="newsletter-inner">
        <p class="newsletter-eyebrow">La Lettre du Désert</p>
        <h2 class="newsletter-headline">Les nouvelles du désert,<br>dans votre boîte.</h2>
        <p class="newsletter-subtext">Une lettre par mois. Récits, inspirations et offres privées depuis le désert d'Agafay.</p>
        <form class="newsletter-form" action="#" method="post" onsubmit="handleNewsletterSubmit(event);" novalidate>
          <label for="newsletter-email" class="sr-only">Votre adresse e-mail</label>
          <input type="email" id="newsletter-email" name="email" class="newsletter-form__input" placeholder="votre@email.com" required />
          <button type="submit" class="newsletter-form__btn">S'inscrire</button>
        </form>
        <p class="newsletter-note">Un email par mois. Désabonnement simple en un clic.</p>
      </div>
    </section>
  </div>

  <footer class="bg-[#10100E] text-[#F6F7EA] pt-20 pb-10 px-6 md:px-16">
    <div class="max-w-7xl mx-auto">
      <div class="mb-16 overflow-hidden w-full">
        <p class="text-[12vw] sm:text-[10vw] md:text-[80px] lg:text-[120px] xl:text-[150px] leading-[0.8] tracking-tighter whitespace-nowrap font-bold uppercase mb-6 text-[#F6F7EA] -ml-1 md:-ml-2">MARRAGAFAY.</p>
        <p class="text-[#8e8e88] text-[14px] md:text-[16px] max-w-md leading-relaxed">Redéfinir l'expérience du désert de pierre d'Agafay. Luxe sans compromis, flottes exclusives et expertise locale certifiée.</p>
      </div>
      <hr style="border: 0; border-top: 1px solid rgba(255, 255, 255, 0.1); margin: 40px 0;">
      <div class="grid grid-cols-2 md:grid-cols-4 gap-10 md:gap-6 text-[14px]">
        <div>
          <p class="text-xs font-bold uppercase tracking-widest text-[#F6F7EA] mb-6">Contact</p>
          <ul class="space-y-3 list-none p-0 m-0">
            <li><a href="mailto:marragafay@gmail.com" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA] transition-colors" style="text-decoration: none;">marragafay@gmail.com</a></li>
            <li><a href="tel:+212672531624" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA] transition-colors" style="text-decoration: none;">+212 672-531624</a></li>
            <li class="leading-tight text-[#F6F7EA]/90">Désert d'Agafay,<br>Marrakech, Maroc</li>
          </ul>
        </div>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest text-[#F6F7EA] mb-6">Navigation</p>
          <ul class="space-y-3 list-none p-0 m-0">
            <li><a href="/fr/activities" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA] transition-colors" style="text-decoration: none;">Activités</a></li>
            <li><a href="/fr/packs" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA] transition-colors" style="text-decoration: none;">Packs</a></li>
            <li><a href="/fr/reviews" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA] transition-colors" style="text-decoration: none;">Avis</a></li>
            <li><a href="/fr/blog" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA] transition-colors" style="text-decoration: none;">La Revue</a></li>
          </ul>
        </div>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest text-[#F6F7EA] mb-6">Légal</p>
          <ul class="space-y-3 list-none p-0 m-0">
            <li><a href="/fr/terms" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA] transition-colors" style="text-decoration: none;">Conditions Générales</a></li>
            <li><a href="/fr/privacy" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA] transition-colors" style="text-decoration: none;">Confidentialité</a></li>
            <li><a href="/fr/cancellation" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA] transition-colors" style="text-decoration: none;">Annulation</a></li>
          </ul>
        </div>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest text-[#F6F7EA] mb-6">Réseaux</p>
          <ul class="space-y-3 list-none p-0 m-0">
            <li><a href="https://www.instagram.com/marragafay" target="_blank" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA] transition-colors" style="text-decoration: none;">Instagram</a></li>
            <li><a href="https://www.facebook.com/share/17pMqjAeGF/" target="_blank" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA] transition-colors" style="text-decoration: none;">Facebook</a></li>
            <li><a href="https://wa.me/212672531624" target="_blank" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA] transition-colors" style="text-decoration: none;">WhatsApp</a></li>
          </ul>
        </div>
      </div>
      <hr style="border: 0; border-top: 1px solid rgba(255, 255, 255, 0.1); margin: 40px 0;">
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center text-xs text-[#F6F7EA]/90 gap-4">
        <div>&copy; 2026 MARRAGAFAY. TOUS DROITS RÉSERVÉS.</div>
        <div>CONÇU À MARRAKECH.</div>
      </div>
    </div>
  </footer>

  <script src="/js/jquery.min.js" defer></script>
  <script src="/js/popper.min.js" defer></script>
  <script src="/js/bootstrap.min.js" defer></script>
  <script src="/js/navbar-stayhere.js" defer></script>

  <script>
    document.addEventListener('DOMContentLoaded', function() {
      var pills = document.querySelectorAll('.category-pill');
      var cards = document.querySelectorAll('#article-grid .article-card');
      var noResults = document.getElementById('no-results');
      var featuredWrap = document.getElementById('featured-wrap');
      var featured = document.getElementById('featured-article');

      pills.forEach(function(pill) {
        pill.addEventListener('click', function() {
          pills.forEach(function(p) { p.classList.remove('active'); p.setAttribute('aria-pressed', 'false'); });
          this.classList.add('active');
          this.setAttribute('aria-pressed', 'true');
          var cat = this.getAttribute('data-filter');
          var count = 0;
          if (featured) {
            featuredWrap.style.display = (cat === 'all' || featured.getAttribute('data-category') === cat) ? '' : 'none';
          }
          cards.forEach(function(card) {
            var show = (cat === 'all' || card.getAttribute('data-category') === cat);
            card.style.display = show ? '' : 'none';
            if (show) count++;
          });
          if (noResults) noResults.style.display = (count === 0) ? 'block' : 'none';
        });
      });
    });
  </script>
</body>
</html>
"""

with open("fr/blog/index.html", "w", encoding="utf-8") as f:
    f.write(fr_html)
print("Generated: fr/blog/index.html")

# 2. Spanish Blog Index (es/blog/index.html)
es_html = fr_html.replace('lang="fr"', 'lang="es"') \
                 .replace('La Revue &#8212; Récits et Guides du Désert d\'Agafay | Marragafay', 'El Diario &#8212; Historias y Guías del Desierto de Agafay | Marragafay') \
                 .replace('https://marragafay.com/fr/blog', 'https://marragafay.com/es/blog') \
                 .replace('<span>FR</span>', '<span>ES</span>') \
                 .replace('>Accueil<', '>Inicio<') \
                 .replace('>Activités<', '>Actividades<') \
                 .replace('>À Propos<', '>Nosotros<') \
                 .replace('>Avis<', '>Opiniones<') \
                 .replace('>La Revue<', '>El Diario<') \
                 .replace('>Réservation<', '>Reservar<') \
                 .replace('La Revue.', 'El Diario.') \
                 .replace('Récits du<br>désert de pierre.', 'Historias del<br>desierto de piedra.') \
                 .replace('Notes de terrain, guides exclusifs et rencontres d\'exception dans le désert d\'Agafay.', 'Notas de campo, guías exclusivas y encuentros excepcionales en el desierto de Agafay.') \
                 .replace('>Tous<', '>Todos<') \
                 .replace('>Guides Désert<', '>Guías Desierto<') \
                 .replace('>Expériences<', '>Experiencias<') \
                 .replace('>Conseils<', '>Consejos<') \
                 .replace('À la Une', 'Destacado') \
                 .replace('Derniers Récits', 'Del Archivo') \
                 .replace('Choix de la Rédaction', 'Selección Editorial') \
                 .replace('Guide Désert', 'Guía Desierto') \
                 .replace('Lire l\'Article', 'Leer Artículo') \
                 .replace('min de lecture', 'min de lectura') \
                 .replace('La Lettre du Désert', 'La Carta del Desierto') \
                 .replace('Les nouvelles du désert,<br>dans votre boîte.', 'Noticias del desierto,<br>en tu bandeja de entrada.') \
                 .replace('S\'inscrire', 'Suscribirse') \
                 .replace('TOUS DROITS RÉSERVÉS', 'TODOS LOS DERECHOS RESERVADOS') \
                 .replace('CONÇU À MARRAKECH', 'DISEÑADO EN MARRAKECH')

with open("es/blog/index.html", "w", encoding="utf-8") as f:
    f.write(es_html)
print("Generated: es/blog/index.html")

# 3. Arabic Blog Index (ar/blog/index.html with dir="rtl")
ar_html = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />

  <title>المجلة &#8212; قصص وتجارب صحراء أكافاي | ماراكافاي</title>
  <meta name="description" content="مذكرات ميدانية، أدلة حصرية وتجارب فريدة في صحراء أكافاي الحجرية بالقرب من مراكش." />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="https://marragafay.com/ar/blog" />

  <meta property="og:type" content="website" />
  <meta property="og:title" content="المجلة &#8212; قصص وتجارب صحراء أكافاي | ماراكافاي" />
  <meta property="og:description" content="مذكرات ميدانية وتجارب فاخرة في صحراء أكافاي بالقرب من مراكش." />
  <meta property="og:url" content="https://marragafay.com/ar/blog" />
  <meta property="og:image" content="https://marragafay.com/images/Slider-images/slider-1.webp" />

  <link rel="alternate" hreflang="en" href="https://marragafay.com/en/blog" />
  <link rel="alternate" hreflang="fr" href="https://marragafay.com/fr/blog" />
  <link rel="alternate" hreflang="es" href="https://marragafay.com/es/blog" />
  <link rel="alternate" hreflang="ar" href="https://marragafay.com/ar/blog" />
  <link rel="alternate" hreflang="x-default" href="https://marragafay.com/blog" />

  <link rel="preconnect" href="https://api.fontshare.com" />
  <link href="https://api.fontshare.com/v2/css?f[]=clash-grotesk@400,500,600,700&display=swap" rel="stylesheet" />

  <link rel="stylesheet" href="/css/vendor-bundle.css" />
  <link rel="stylesheet" href="/css/custom-bundle.css" />
  <link rel="stylesheet" href="/css/style.css" />
  <link rel="stylesheet" href="/css/navbar-stayhere.css" />
  <link rel="stylesheet" href="/css/tailwind-built.css" />

  <style>
    * { font-family: 'Clash Grotesk', system-ui, -apple-system, sans-serif !important; }
    html, body { background-color: #F6F7EA; color: #272724; margin: 0; padding: 0; }
    body.blog { background-color: #F6F7EA; }
    .journal-page { padding-top: var(--nav-height, 72px); }
    .journal-hero { background-color: #F6F7EA; padding: 80px 0 60px; border-bottom: 1px solid rgba(39,39,36,0.12); }
    .journal-hero__inner { max-width: 1200px; margin: 0 auto; padding: 0 32px; }
    .journal-hero__eyebrow { display: inline-block; font-size: 11px; font-weight: 600; letter-spacing: 0.2em; text-transform: uppercase; color: #523225; margin-bottom: 28px; }
    .journal-hero__headline { font-size: clamp(3rem, 6vw, 6rem); font-weight: 700; line-height: 1.1; color: #272724; margin: 0 0 24px; max-width: 900px; }
    .journal-hero__subline { font-size: clamp(1rem, 1.5vw, 1.2rem); font-weight: 400; color: #7a756e; max-width: 540px; line-height: 1.7; margin: 0 0 48px; }
    .category-filter { display: flex; flex-wrap: wrap; gap: 10px; align-items: center; }
    .category-pill { display: inline-flex; align-items: center; padding: 8px 18px; border-radius: 999px; border: 1px solid rgba(39,39,36,0.2); font-size: 13px; font-weight: 600; color: #272724; background: transparent; cursor: pointer; transition: all 0.22s ease; }
    .category-pill.active { background: #272724; color: #F6F7EA; border-color: #272724; }
    .journal-section { max-width: 1200px; margin: 0 auto; padding: 0 32px; }
    .journal-section-wrap { padding: 80px 0; }
    .section-label { font-size: 12px; font-weight: 700; color: #523225; margin-bottom: 32px; display: flex; align-items: center; gap: 14px; }
    .section-label::after { content: ''; flex: 1; height: 1px; background: rgba(39,39,36,0.1); display: block; }
    .featured-article { display: grid; grid-template-columns: 1fr 1fr; gap: 0; background: #EEF0E2; border-radius: 4px; overflow: hidden; min-height: 520px; }
    .featured-article__image-wrap { position: relative; overflow: hidden; }
    .featured-article__image-wrap img { width: 100%; height: 100%; object-fit: cover; }
    .featured-article__content { padding: 52px 52px 52px 56px; display: flex; flex-direction: column; justify-content: center; background: #EEF0E2; text-align: right; }
    .featured-article__title { font-size: clamp(1.6rem,2.8vw,2.25rem); font-weight: 700; line-height: 1.25; color: #272724; margin: 0 0 20px; }
    .featured-article__excerpt { font-size: 1rem; line-height: 1.7; color: #5a5a54; margin: 0 0 32px; }
    .featured-article__cta { display: inline-flex; align-items: center; gap: 10px; font-size: 14px; font-weight: 700; color: #272724; text-decoration: none; border-bottom: 1.5px solid #272724; padding-bottom: 2px; width: fit-content; }
    .article-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 28px; }
    .article-card { background: #EEF0E2; border-radius: 4px; overflow: hidden; display: flex; flex-direction: column; text-decoration: none; color: inherit; transition: transform 0.28s; text-align: right; }
    .article-card:hover { transform: translateY(-4px); }
    .article-card__image-wrap { position: relative; overflow: hidden; aspect-ratio: 4/3; }
    .article-card__image-wrap img { width: 100%; height: 100%; object-fit: cover; }
    .article-card__body { padding: 28px 28px 24px; display: flex; flex-direction: column; flex: 1; }
    .article-card__title { font-size: 1.1rem; font-weight: 700; line-height: 1.35; color: #272724; margin: 0 0 12px; }
    .article-card__excerpt { font-size: 0.9rem; line-height: 1.65; color: #5a5a54; margin: 0 0 20px; }
    .newsletter-section { background: #272724; padding: 90px 0; text-align: center; }
    .newsletter-headline { font-size: clamp(2rem,4vw,3rem); font-weight: 700; color: #F6F7EA; margin: 0 0 18px; }
    .newsletter-form { display: flex; gap: 0; max-width: 480px; margin: 0 auto; border: 1px solid rgba(246,247,234,0.2); border-radius: 3px; }
    .newsletter-form__input { flex: 1; background: transparent; border: none; outline: none; padding: 16px 20px; font-size: 14px; color: #F6F7EA; text-align: right; }
    .newsletter-form__btn { background: #523225; color: #F6F7EA; border: none; padding: 16px 28px; font-size: 13px; font-weight: 700; cursor: pointer; }
    @media (max-width: 1024px) { .article-grid { grid-template-columns: repeat(2,1fr); } }
    @media (max-width: 768px) {
      .featured-article { grid-template-columns: 1fr; }
      .featured-article__image-wrap { height: 280px; }
      .article-grid { grid-template-columns: 1fr; }
      .newsletter-form { flex-direction: column; }
    }
  </style>
</head>

<body class="blog">
  <nav style="height: var(--nav-height, 72px);" class="navbar navbar-expand-lg navbar-dark ftco_navbar bg-dark ftco-navbar-light" id="ftco-navbar">
    <div class="container">
      <a class="navbar-brand" href="/ar/"><img src="/images/logo-trensparent.webp" alt="Marragafay" style="width: 70px; height: 70px;" width="70" height="70"></a>
      <div class="mobile-language-switcher">
        <a href="#" class="language-toggle" id="languageDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          <i class="icon-globe"></i> <span>AR</span>
        </a>
        <div class="dropdown-menu dropdown-menu-right" aria-labelledby="languageDropdown">
          <a class="dropdown-item lang-option" href="#" data-lang="en">English</a>
          <a class="dropdown-item lang-option" href="#" data-lang="fr">Français</a>
          <a class="dropdown-item lang-option" href="#" data-lang="es">Español</a>
          <a class="dropdown-item lang-option" href="#" data-lang="ar" dir="rtl">العربية</a>
        </div>
      </div>
      <button class="navbar-toggler" type="button" aria-label="Toggle navigation"><span class="icon-menu"></span></button>
      <div class="collapse navbar-collapse">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item"><a href="/ar/" class="nav-link">الرئيسية</a></li>
          <li class="nav-item"><a href="/ar/activities" class="nav-link">الأنشطة</a></li>
          <li class="nav-item"><a href="/ar/packs" class="nav-link">الباقات</a></li>
          <li class="nav-item"><a href="/ar/about" class="nav-link">من نحن</a></li>
          <li class="nav-item"><a href="/ar/reviews" class="nav-link">التقييمات</a></li>
          <li class="nav-item active"><a href="/ar/blog" class="nav-link">المجلة</a></li>
          <li class="nav-item"><a href="/ar/contact" class="nav-link">اتصل بنا</a></li>
          <li class="nav-item"><a href="/ar/packs" class="nav-link booking-btn">الحجز</a></li>
        </ul>
      </div>
    </div>
  </nav>

  <div class="journal-page">
    <section class="journal-hero">
      <div class="journal-hero__inner">
        <span class="journal-hero__eyebrow">المجلة.</span>
        <h1 class="journal-hero__headline">قصص وتجارب من<br>الصحراء الحجرية.</h1>
        <p class="journal-hero__subline">مذكرات ميدانية، أدلة حصرية ولقاءات استثنائية في صحراء أكافاي الساحرة.</p>
        <hr style="border: 0; border-top: 1px solid rgba(39,39,36,0.12); margin: 0 0 36px;" />
        <div class="category-filter">
          <button class="category-pill active">جميع المقالات</button>
          <button class="category-pill">دليل الصحراء</button>
          <button class="category-pill">تجارب فاخرة</button>
          <button class="category-pill">الثقافة والتراث</button>
          <button class="category-pill">نصائح السفر</button>
        </div>
      </div>
    </section>

    <section class="journal-section-wrap">
      <div class="journal-section">
        <p class="section-label">المقال الرئيسي</p>
        <article class="featured-article">
          <div class="featured-article__image-wrap">
            <img src="/images/Slider-images/slider-1.webp" alt="صحراء أكافاي عند الغروب" loading="eager" decoding="async" />
          </div>
          <div class="featured-article__content">
            <p style="font-size: 11px; font-weight: 700; color: #523225; margin-bottom: 12px;">دليل الصحراء</p>
            <h2 class="featured-article__title">الدليل الشامل لصحراء أكافاي &#8212; اكتشف سحر الصحراء الحجرية</h2>
            <p class="featured-article__excerpt">ما يميز أكافاي عن الصحراء الكبرى ولماذا يفضلها الزوار على بعد 45 دقيقة فقط من مراكش. دليلك الكامل لتجربة استثنائية.</p>
            <a href="/en/blog/agafay-desert-guide" class="featured-article__cta">
              اقرأ المقال الكامل &larr;
            </a>
          </div>
        </article>
      </div>
    </section>

    <section class="journal-section-wrap" style="padding-top: 0;">
      <div class="journal-section">
        <p class="section-label">من الأرشيف</p>
        <div class="article-grid">
          <a href="/en/blog/agafay-camel-ride" class="article-card">
            <div class="article-card__image-wrap"><img src="/images/Slider-images/slider-3.webp" alt="ركوب الجمال في أكافاي" /></div>
            <div class="article-card__body">
              <h3 class="article-card__title">جولة الجمال عند الغروب: كل ما تحتاج معرفته</h3>
              <p class="article-card__excerpt">سكينة الصحراء عند المغيب وتجربة ركوب الجمال الخاصة بين تلال أكافاي.</p>
            </div>
          </a>

          <a href="/en/blog/agafay-dinner-experience" class="article-card">
            <div class="article-card__image-wrap"><img src="/images/activites/show.webp" alt="عشاء خاص في صحراء أكافاي" /></div>
            <div class="article-card__body">
              <h3 class="article-card__title">العشاء تحت أضواء النجوم: أمسية مغربية فاخرة</h3>
              <p class="article-card__excerpt">فوانيس الشموع، أشهى المأكولات المغربية وسماء صحراوية تتلألأ بالنجوم.</p>
            </div>
          </a>

          <a href="/en/blog/agafay-desert-vs-sahara" class="article-card">
            <div class="article-card__image-wrap"><img src="/images/Slider-images/slider-2.webp" alt="مقارنة أكافاي والصحراء الكبرى" /></div>
            <div class="article-card__body">
              <h3 class="article-card__title">صحراء أكافاي أم الصحراء الكبرى: أيهما تختار؟</h3>
              <p class="article-card__excerpt">مقارنة شاملة في المسافة، التكاليف، وطبيعة التضاريس لتنظيم رحلتك المثالية.</p>
            </div>
          </a>
        </div>
      </div>
    </section>
  </div>

  <footer class="bg-[#10100E] text-[#F6F7EA] pt-20 pb-10 px-6 md:px-16" style="text-align: right;">
    <div class="max-w-7xl mx-auto">
      <div class="mb-16 overflow-hidden w-full">
        <p class="text-[12vw] sm:text-[10vw] md:text-[80px] lg:text-[120px] xl:text-[150px] leading-[0.8] tracking-tighter whitespace-nowrap font-bold uppercase mb-6 text-[#F6F7EA]">MARRAGAFAY.</p>
        <p class="text-[#8e8e88] text-[14px] md:text-[16px] max-w-md leading-relaxed">إعادة تعريف تجربة صحراء أكافاي الحجرية. فخامة بلا تنازل، أساطيل حصرية وخبرة محلية معتمدة.</p>
      </div>
      <hr style="border: 0; border-top: 1px solid rgba(255, 255, 255, 0.1); margin: 40px 0;">
      <div class="grid grid-cols-2 md:grid-cols-4 gap-10 md:gap-6 text-[14px]">
        <div>
          <p class="text-xs font-bold uppercase tracking-widest text-[#F6F7EA] mb-6">تواصل معنا</p>
          <ul class="space-y-3 list-none p-0 m-0">
            <li><a href="mailto:marragafay@gmail.com" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA]">marragafay@gmail.com</a></li>
            <li><a href="tel:+212672531624" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA]">+212 672-531624</a></li>
            <li class="text-[#F6F7EA]/90">صحراء أكافاي، مراكش، المغرب</li>
          </ul>
        </div>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest text-[#F6F7EA] mb-6">روابط سريعة</p>
          <ul class="space-y-3 list-none p-0 m-0">
            <li><a href="/ar/activities" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA]">الأنشطة</a></li>
            <li><a href="/ar/packs" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA]">الباقات</a></li>
            <li><a href="/ar/reviews" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA]">التقييمات</a></li>
            <li><a href="/ar/blog" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA]">المجلة</a></li>
          </ul>
        </div>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest text-[#F6F7EA] mb-6">قانوني</p>
          <ul class="space-y-3 list-none p-0 m-0">
            <li><a href="/ar/terms" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA]">الشروط والأحكام</a></li>
            <li><a href="/ar/privacy" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA]">سياسة الخصوصية</a></li>
            <li><a href="/ar/cancellation" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA]">سياسة الإلغاء</a></li>
          </ul>
        </div>
        <div>
          <p class="text-xs font-bold uppercase tracking-widest text-[#F6F7EA] mb-6">تابعنا</p>
          <ul class="space-y-3 list-none p-0 m-0">
            <li><a href="https://www.instagram.com/marragafay" target="_blank" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA]">Instagram</a></li>
            <li><a href="https://wa.me/212672531624" target="_blank" class="text-[#F6F7EA]/90 hover:text-[#F6F7EA]">WhatsApp</a></li>
          </ul>
        </div>
      </div>
      <hr style="border: 0; border-top: 1px solid rgba(255, 255, 255, 0.1); margin: 40px 0;">
      <div class="flex justify-between items-center text-xs text-[#F6F7EA]/90">
        <div>&copy; 2026 ماراكافاي. جميع الحقوق محفوظة.</div>
        <div>صُمم في مراكش.</div>
      </div>
    </div>
  </footer>
</body>
</html>
"""

with open("ar/blog/index.html", "w", encoding="utf-8") as f:
    f.write(ar_html)
print("Generated: ar/blog/index.html")

print("All multilingual indexes generated successfully.")
