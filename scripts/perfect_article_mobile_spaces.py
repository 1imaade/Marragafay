import glob
import re

perfect_article_css = """
    * { font-family: 'Clash Grotesk', sans-serif !important; box-sizing: border-box; }
    html, body {
      margin: 0 !important;
      padding: 0 !important;
      overflow-x: hidden !important;
      max-width: 100vw !important;
      width: 100% !important;
      background-color: #F6F7EA !important;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }
    body.blog {
      background-color: #F6F7EA !important;
      color: #272724;
      font-size: 18px;
      line-height: 1.8;
    }
    #ftco-navbar, #ftco-navbar.scrolled, #ftco-navbar.awake, #ftco-navbar.sleep {
      background-color: #F6F7EA !important;
      background: #F6F7EA !important;
      --nav-text: #272724 !important;
      --nav-text-muted: #272724 !important;
    }
    #ftco-navbar .nav-link:not(.booking-btn), #ftco-navbar .navbar-brand, #ftco-navbar .language-toggle {
      color: #272724 !important;
    }

    /* Reading Progress Bar */
    #reading-progress-bar {
      position: fixed; top: 0; left: 0; height: 3px; width: 0%;
      background-color: #523225; z-index: 9999;
      transition: width 0.1s linear; pointer-events: none;
    }

    .navbar-spacer { height: var(--nav-height, 72px); display: block; }
    
    /* Article Header */
    .article-header {
      background-color: #F6F7EA;
      padding: 56px 32px 36px;
      max-width: 1200px;
      margin: 0 auto;
      box-sizing: border-box;
    }
    .breadcrumb-nav {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 12px;
      font-weight: 600;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: #272724;
      opacity: 0.55;
      margin-bottom: 20px;
      list-style: none;
      padding: 0;
    }
    .breadcrumb-nav a { color: #272724; text-decoration: none; }
    .breadcrumb-nav a:hover { opacity: 0.8; }
    .category-tag {
      display: inline-block;
      background-color: #523225;
      color: #fff;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      padding: 5px 14px;
      border-radius: 100px;
      margin-bottom: 20px;
    }
    .article-headline {
      font-size: clamp(2.3rem, 5vw, 3.8rem);
      font-weight: 700;
      color: #272724;
      line-height: 1.08;
      letter-spacing: -0.025em;
      margin: 0 0 18px;
      word-wrap: break-word;
    }
    .article-subheadline {
      font-size: 1.25rem;
      font-weight: 400;
      color: #272724;
      opacity: 0.8;
      line-height: 1.6;
      margin: 0 0 28px;
      max-width: 840px;
    }
    .article-meta-row {
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 14px;
      font-size: 13px;
      color: #272724;
      opacity: 0.65;
      padding-bottom: 28px;
      border-bottom: 1px solid rgba(39,39,36,0.12);
    }
    .meta-divider {
      width: 3px;
      height: 3px;
      border-radius: 50%;
      background: #272724;
      opacity: 0.4;
      display: inline-block;
    }
    .share-buttons {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-left: auto;
    }
    .share-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 12px;
      font-weight: 600;
      color: #272724;
      border: 1px solid rgba(39,39,36,0.22);
      background: transparent;
      padding: 6px 14px;
      border-radius: 100px;
      cursor: pointer;
      text-decoration: none;
      transition: all 0.2s;
    }
    .share-btn:hover { border-color: #523225; color: #523225; }

    /* Article Hero Image */
    .article-hero {
      width: 100%;
      max-width: 1200px;
      margin: 0 auto 48px;
      padding: 0 32px;
      box-sizing: border-box;
    }
    .article-hero img {
      width: 100%;
      aspect-ratio: 16/9;
      max-height: 600px;
      object-fit: cover;
      border-radius: 8px;
      display: block;
    }
    .article-hero-caption {
      font-size: 13px;
      color: #272724;
      opacity: 0.5;
      font-style: italic;
      margin-top: 10px;
      display: block;
      line-height: 1.45;
    }

    /* Article Body Typography */
    .article-body-wrap {
      max-width: 740px;
      margin: 0 auto;
      padding: 0 32px;
      box-sizing: border-box;
    }
    .article-body p {
      font-size: 18.5px;
      line-height: 1.85;
      color: #272724;
      margin-bottom: 1.8em;
    }
    .article-body h2 {
      font-size: 1.8rem;
      font-weight: 700;
      color: #272724;
      letter-spacing: -0.02em;
      margin-top: 3.2rem;
      margin-bottom: 1.1rem;
      line-height: 1.22;
    }
    .article-body h3 {
      font-size: 1.35rem;
      font-weight: 700;
      color: #272724;
      margin-top: 2.2rem;
      margin-bottom: 0.75rem;
      line-height: 1.3;
    }
    .article-body ul {
      padding-left: 1.5rem;
      margin-bottom: 2rem;
    }
    .article-body ul li {
      font-size: 18.5px;
      line-height: 1.8;
      color: #272724;
      margin-bottom: 0.65em;
    }
    .article-body blockquote, .article-quote {
      border-left: 3px solid #523225;
      padding-left: 24px;
      margin: 2.8rem 0;
      font-style: italic;
      font-size: 1.25rem;
      line-height: 1.6;
      color: #523225;
    }
    .article-inline-img {
      width: 100% !important;
      max-width: 100% !important;
      height: auto !important;
      border-radius: 8px !important;
      margin: 2.8rem 0 0.8rem !important;
      display: block !important;
      object-fit: cover !important;
    }
    .article-inline-caption {
      font-size: 13px !important;
      color: #272724 !important;
      opacity: 0.5 !important;
      font-style: italic !important;
      display: block !important;
      margin-bottom: 2.8rem !important;
      line-height: 1.45 !important;
    }

    /* In-Article Booking CTA */
    .article-cta-box {
      background-color: #272724 !important;
      color: #F6F7EA !important;
      padding: 44px 36px;
      border-radius: 10px;
      margin: 3.5rem 0;
      text-align: center;
      box-sizing: border-box;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
    }
    .article-cta-box h3 {
      color: #F6F7EA !important;
      font-size: clamp(1.4rem, 2.5vw, 1.85rem) !important;
      font-weight: 700 !important;
      margin-top: 0 !important;
      margin-bottom: 12px !important;
      line-height: 1.25 !important;
      letter-spacing: -0.015em !important;
    }
    .article-cta-box p {
      color: rgba(246, 247, 234, 0.82) !important;
      font-size: 16px !important;
      line-height: 1.65 !important;
      max-width: 540px !important;
      margin: 0 auto 24px !important;
    }
    .article-cta-btn {
      display: inline-flex !important;
      align-items: center !important;
      justify-content: center !important;
      gap: 8px !important;
      background-color: #523225 !important;
      color: #F6F7EA !important;
      padding: 13px 30px !important;
      border-radius: 100px !important;
      font-weight: 700 !important;
      text-decoration: none !important;
      font-size: 13px !important;
      letter-spacing: 0.08em !important;
      text-transform: uppercase !important;
      transition: all 0.25s ease !important;
    }
    .article-cta-btn:hover {
      background-color: #3d241a !important;
      color: #F6F7EA !important;
      transform: translateY(-1px) !important;
      box-shadow: 0 4px 14px rgba(82, 50, 37, 0.4) !important;
    }

    /* Tags Wrap */
    .article-tags-wrap {
      max-width: 740px;
      margin: 0 auto;
      padding: 36px 32px 56px;
      box-sizing: border-box;
    }
    .article-tags-label {
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: #272724;
      opacity: 0.45;
      margin-bottom: 14px;
    }
    .article-tags {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }
    .article-tag {
      display: inline-block;
      border: 1px solid rgba(39,39,36,0.2);
      color: #272724;
      font-size: 12px;
      font-weight: 600;
      padding: 6px 16px;
      border-radius: 100px;
      text-decoration: none;
      transition: all 0.2s;
    }
    .article-tag:hover {
      border-color: #523225;
      color: #523225;
      background: rgba(82,50,37,0.05);
    }

    .section-rule {
      border: 0;
      border-top: 1px solid rgba(39,39,36,0.1);
      margin: 0;
    }

    /* Related Articles */
    .related-articles-section {
      background-color: #F6F7EA;
      padding: 72px 24px;
    }
    .related-articles-inner {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 32px;
      box-sizing: border-box;
    }
    .related-articles-header {
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      margin-bottom: 40px;
      border-bottom: 1px solid rgba(39,39,36,0.15);
      padding-bottom: 16px;
    }
    .related-articles-title {
      font-size: 1.35rem;
      font-weight: 700;
      color: #272724;
      text-transform: uppercase;
      letter-spacing: -0.01em;
      margin: 0;
    }
    .related-articles-link {
      font-size: 12px;
      font-weight: 700;
      color: #523225;
      text-decoration: none;
      letter-spacing: 0.08em;
      text-transform: uppercase;
    }
    .related-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 36px;
    }
    .related-card {
      display: flex;
      flex-direction: column;
      text-decoration: none;
      color: inherit;
      background: transparent;
      transition: transform 0.25s ease;
    }
    .related-card:hover { text-decoration: none; color: inherit; }
    .related-card-img-wrap {
      position: relative;
      overflow: hidden;
      aspect-ratio: 16/10;
      border-radius: 6px;
      margin-bottom: 16px;
    }
    .related-card-img-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.6s ease;
    }
    .related-card:hover .related-card-img-wrap img {
      transform: scale(1.03);
    }
    .related-card-cat {
      font-size: 10.5px;
      font-weight: 700;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: #523225;
      margin-bottom: 8px;
    }
    .related-card-title {
      font-size: 1.2rem;
      font-weight: 700;
      color: #272724;
      line-height: 1.25;
      margin-bottom: 10px;
    }
    .related-card-meta {
      font-size: 12px;
      color: #7a756e;
      margin-bottom: 12px;
    }
    .related-card-arrow {
      font-size: 12px;
      font-weight: 700;
      color: #523225;
      text-transform: uppercase;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    #copy-toast {
      position: fixed;
      bottom: 28px;
      left: 50%;
      transform: translateX(-50%) translateY(20px);
      background: #272724;
      color: #F6F7EA;
      font-size: 13px;
      font-weight: 600;
      padding: 10px 22px;
      border-radius: 100px;
      opacity: 0;
      pointer-events: none;
      transition: all 0.3s ease;
      z-index: 9998;
    }
    #copy-toast.show { opacity: 1; transform: translateX(-50%) translateY(0); }

    /* ═══════════════════════════════════════════════
       MOBILE RESPONSIVE PERFECTION (ARTICLE PAGES)
    ═══════════════════════════════════════════════ */
    @media (max-width: 1024px) {
      .article-header { padding: 40px 24px 28px; }
      .article-hero { padding: 0 24px; margin-bottom: 36px; }
      .article-body-wrap, .article-tags-wrap { padding: 0 24px; }
      .related-articles-section { padding: 56px 24px; }
      .related-grid { grid-template-columns: repeat(2, 1fr); gap: 28px; }
    }

    @media (max-width: 768px) {
      .navbar-spacer { height: var(--nav-height-mobile, 64px) !important; }
      
      .article-header {
        padding: 24px 18px 18px !important;
        max-width: 100% !important;
      }
      .breadcrumb-nav {
        font-size: 11px !important;
        margin-bottom: 12px !important;
        gap: 6px !important;
        flex-wrap: wrap !important;
      }
      .category-tag {
        font-size: 10px !important;
        padding: 4px 12px !important;
        margin-bottom: 14px !important;
      }
      .article-headline {
        font-size: clamp(1.85rem, 7vw, 2.35rem) !important;
        line-height: 1.15 !important;
        margin: 0 0 14px !important;
        letter-spacing: -0.02em !important;
        word-break: break-word !important;
      }
      .article-subheadline {
        font-size: 16px !important;
        line-height: 1.55 !important;
        margin: 0 0 18px !important;
        opacity: 0.8 !important;
      }
      .article-meta-row {
        flex-direction: row !important;
        flex-wrap: wrap !important;
        align-items: center !important;
        gap: 8px 12px !important;
        font-size: 12px !important;
        padding-bottom: 16px !important;
      }
      .share-buttons {
        width: 100% !important;
        margin-left: 0 !important;
        margin-top: 6px !important;
        justify-content: flex-start !important;
        gap: 8px !important;
      }
      .share-btn {
        font-size: 11.5px !important;
        padding: 6px 14px !important;
      }

      .article-hero {
        padding: 0 18px !important;
        margin-bottom: 24px !important;
        max-width: 100% !important;
      }
      .article-hero img {
        aspect-ratio: 16/10 !important;
        max-height: 300px !important;
        border-radius: 6px !important;
      }
      .article-hero-caption {
        font-size: 11.5px !important;
        margin-top: 6px !important;
      }

      .article-body-wrap {
        padding: 0 18px !important;
        margin: 0 auto !important;
        max-width: 100% !important;
      }
      .article-body p {
        font-size: 16.5px !important;
        line-height: 1.75 !important;
        margin-bottom: 1.35em !important;
      }
      .article-body h2 {
        font-size: 1.45rem !important;
        line-height: 1.25 !important;
        margin-top: 2.2rem !important;
        margin-bottom: 0.8rem !important;
        letter-spacing: -0.015em !important;
      }
      .article-body h3 {
        font-size: 1.2rem !important;
        line-height: 1.3 !important;
        margin-top: 1.6rem !important;
        margin-bottom: 0.5rem !important;
      }
      .article-body ul {
        padding-left: 1.25rem !important;
        margin-bottom: 1.4rem !important;
      }
      .article-body ul li {
        font-size: 16.5px !important;
        line-height: 1.65 !important;
        margin-bottom: 0.5em !important;
      }
      .article-body blockquote, .article-quote {
        border-left: 3px solid #523225 !important;
        padding: 6px 0 6px 14px !important;
        margin: 1.8rem 0 !important;
        font-size: 1.1rem !important;
        line-height: 1.55 !important;
      }
      .article-inline-img {
        margin: 1.8rem 0 0.6rem !important;
        border-radius: 6px !important;
      }
      .article-inline-caption {
        font-size: 11.5px !important;
        margin-bottom: 1.8rem !important;
      }

      .article-cta-box {
        padding: 28px 18px !important;
        margin: 2.4rem 0 !important;
        border-radius: 8px !important;
        width: 100% !important;
      }
      .article-cta-box h3 {
        font-size: 1.35rem !important;
        line-height: 1.25 !important;
        margin-bottom: 10px !important;
      }
      .article-cta-box p {
        font-size: 14.5px !important;
        line-height: 1.6 !important;
        margin-bottom: 18px !important;
        max-width: 100% !important;
      }
      .article-cta-btn {
        width: 100% !important;
        padding: 13px 20px !important;
        font-size: 12.5px !important;
        justify-content: center !important;
        text-align: center !important;
      }

      .article-tags-wrap {
        padding: 20px 18px 36px !important;
        max-width: 100% !important;
      }
      .article-tags-label {
        font-size: 10.5px !important;
        margin-bottom: 10px !important;
      }
      .article-tags {
        gap: 7px !important;
      }
      .article-tag {
        font-size: 11px !important;
        padding: 5px 12px !important;
      }

      .related-articles-section {
        padding: 40px 18px !important;
      }
      .related-articles-inner {
        padding: 0 !important;
        max-width: 100% !important;
      }
      .related-articles-header {
        margin-bottom: 24px !important;
        padding-bottom: 12px !important;
      }
      .related-articles-title {
        font-size: 1.15rem !important;
      }
      .related-articles-link {
        font-size: 11px !important;
      }
      .related-grid {
        grid-template-columns: 1fr !important;
        gap: 24px !important;
      }
      .related-card-img-wrap {
        aspect-ratio: 16/10 !important;
        margin-bottom: 12px !important;
        border-radius: 6px !important;
      }
      .related-card-cat {
        font-size: 10px !important;
        margin-bottom: 6px !important;
      }
      .related-card-title {
        font-size: 1.15rem !important;
        line-height: 1.28 !important;
        margin-bottom: 6px !important;
      }
      .related-card-meta {
        font-size: 11.5px !important;
        margin-bottom: 10px !important;
      }
    }
"""

rtl_style = """
    body[dir="rtl"] { direction: rtl; text-align: right; }
    body[dir="rtl"] .breadcrumb-nav { flex-direction: row-reverse; justify-content: flex-end; }
    body[dir="rtl"] .breadcrumb-nav .sep { transform: scaleX(-1); }
    body[dir="rtl"] .share-buttons { margin-right: auto; margin-left: 0; justify-content: flex-start; }
    body[dir="rtl"] .related-articles-header { flex-direction: row-reverse; }
    body[dir="rtl"] .related-card-arrow svg { transform: scaleX(-1); }
    body[dir="rtl"] .article-body blockquote, body[dir="rtl"] .article-quote {
      border-left: none !important;
      border-right: 3px solid #523225 !important;
      padding-left: 0 !important;
      padding-right: 24px !important;
    }
    @media (max-width: 768px) {
      body[dir="rtl"] .article-body blockquote, body[dir="rtl"] .article-quote {
        padding-right: 14px !important;
      }
    }
"""

files = glob.glob("*/blog/*.html")
articles = [f for f in files if not f.endswith("index.html")]

for fpath in articles:
    lang = fpath.split("/")[0]
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    # Replace the <style>...</style> block with our perfect responsive CSS
    # We find the style tag after critical inline navbar style
    css_to_insert = perfect_article_css
    if lang == "ar":
        css_to_insert += rtl_style

    # Replace between `<style>` and `</style>` that comes after `<style id="critical-navbar-stayhere-inline">`
    parts = html.split('<!-- Base enforcement -->')
    if len(parts) == 2:
        before = parts[0]
        # in parts[1], replace from `<style>` to `</style>`
        after_style = re.sub(r'<style>.*?</style>', f'<style>\n{css_to_insert}\n  </style>', parts[1], flags=re.DOTALL, count=1)
        html = before + '<!-- Base enforcement -->\n  ' + after_style

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Applied perfect mobile styling to {fpath}")

print("Applied perfect mobile responsive widths, sizes, and spaces across all 28 articles!")
