import glob
import re

# 1. Mobile CSS for Index Pages
index_mobile_css = """
    /* ═══════════════════════════════════════════════
       RESPONSIVE & MOBILE POLISH (TABLET & MOBILE)
    ═══════════════════════════════════════════════ */
    @media (max-width: 1024px) {
      .journal-hero { padding: 54px 0 40px; }
      .journal-section, .journal-hero__inner { padding: 0 24px; }
      .cover-story { grid-template-columns: 1fr; gap: 32px; }
      .editorial-band { padding: 48px 0; }
      .curator-diptych { grid-template-columns: 1fr; }
      .diptych-card { padding: 28px 0 !important; border-left: none !important; border-bottom: 1px solid rgba(39, 39, 36, 0.15); }
      .diptych-card:last-child { border-bottom: none; }
      .field-grid { grid-template-columns: repeat(2, 1fr); gap: 32px; }
      .quote-interlude { padding: 56px 0; }
    }

    @media (max-width: 768px) {
      /* Mobile Hero */
      .journal-page { padding-top: var(--nav-height-mobile, 64px); }
      .journal-hero { padding: 36px 0 30px; }
      .journal-section, .journal-hero__inner { padding: 0 18px; }
      .journal-hero__eyebrow { font-size: 10px; margin-bottom: 16px; gap: 8px; }
      .journal-hero__headline { font-size: clamp(2.3rem, 9.5vw, 3.2rem); line-height: 1.0; margin-bottom: 16px; }
      .journal-hero__subline { font-size: 1rem; line-height: 1.55; margin-bottom: 28px; }
      .journal-hero__divider { margin-bottom: 22px; }

      /* Mobile Horizontal Scrolling Filter Bar */
      .category-filter {
        display: flex;
        flex-wrap: nowrap;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
        padding-bottom: 8px;
        margin: 0 -18px;
        padding-left: 18px;
        padding-right: 18px;
        scrollbar-width: none;
      }
      .category-filter::-webkit-scrollbar { display: none; }
      .category-filter__label { display: none; }
      .category-pill { padding: 7px 16px; font-size: 11px; flex-shrink: 0; }

      /* Section Headers */
      .editorial-band { padding: 36px 0; }
      .editorial-header { margin-bottom: 24px; padding-bottom: 14px; }
      .editorial-header__num { font-size: 11px; }
      .editorial-header__title { font-size: 1.15rem; }
      .editorial-header__sub { font-size: 10.5px; }

      /* 01 / The Lead Story */
      .cover-story { gap: 20px; }
      .cover-story__badge { top: 12px; left: 12px; font-size: 9px; padding: 5px 12px; }
      .cover-story__tag-row { margin-bottom: 14px; gap: 8px; }
      .cover-story__tag { font-size: 10px; }
      .cover-story__read-time { font-size: 11px; }
      .cover-story__title { font-size: clamp(1.45rem, 5.5vw, 1.85rem); line-height: 1.15; margin-bottom: 14px; }
      .cover-story__standfirst { font-size: 0.95rem; line-height: 1.55; margin-bottom: 20px; }
      .cover-story__footer { padding-top: 16px; font-size: 11px; }
      .cover-story__author { font-size: 10.5px; }
      .cover-story__cta { font-size: 11.5px; }

      /* 02 / Curator's Diptych */
      .diptych-card__media { margin-bottom: 18px; aspect-ratio: 16/10; }
      .diptych-card__tag { font-size: 10px; margin-bottom: 8px; }
      .diptych-card__title { font-size: 1.35rem; line-height: 1.2; margin-bottom: 10px; }
      .diptych-card__excerpt { font-size: 0.95rem; line-height: 1.55; margin-bottom: 18px; }
      .diptych-card__footer { padding-top: 14px; font-size: 11px; }

      /* 03 / Philosophy Quote */
      .quote-interlude { padding: 40px 10px; }
      .quote-interlude::before { margin-bottom: 24px; }
      .quote-interlude::after { margin-top: 24px; }
      .quote-interlude__eyebrow { font-size: 9.5px; margin-bottom: 16px; }
      .quote-interlude__text { font-size: clamp(1.3rem, 5vw, 1.65rem); line-height: 1.4; margin-bottom: 20px; }
      .quote-interlude__author { font-size: 10.5px; }

      /* 03 / Field Dispatches Grid */
      .field-grid { grid-template-columns: 1fr; gap: 28px; }
      .field-card__media { margin-bottom: 14px; aspect-ratio: 16/10; }
      .field-card__tag { font-size: 10px; }
      .field-card__title { font-size: 1.2rem; line-height: 1.25; margin-bottom: 8px; }
      .field-card__excerpt { font-size: 0.92rem; line-height: 1.5; margin-bottom: 14px; -webkit-line-clamp: 2; }
      .field-card__footer { padding-top: 12px; font-size: 11px; }

      /* Newsletter */
      .band-newsletter { padding: 44px 0 52px; }
      .newsletter-eyebrow { font-size: 10px; margin-bottom: 14px; }
      .newsletter-headline { font-size: clamp(1.65rem, 6.5vw, 2.2rem); line-height: 1.15; margin-bottom: 10px; }
      .newsletter-subtext { font-size: 0.95rem; line-height: 1.55; margin-bottom: 22px; }
      .newsletter-form { flex-direction: column; border-radius: 12px; padding: 6px; background: #F6F7EA; gap: 6px; }
      .newsletter-form__input { width: 100%; padding: 12px 14px; font-size: 14px; text-align: center; }
      .newsletter-form__btn { width: 100%; border-radius: 8px; padding: 13px 20px; font-size: 12px; }
      .newsletter-note { font-size: 11px; margin-top: 14px; }
    }
"""

# Update all 4 index files
for index_file in glob.glob("*/blog/index.html"):
    with open(index_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace old responsive blocks
    content = re.sub(
        r'/\*\s*Responsive\s*\*/.*?(?=</style>)',
        index_mobile_css + "\n  ",
        content,
        flags=re.DOTALL
    )
    content = re.sub(
        r'/\*\s*═══════════════════════════════════════════════\s*RESPONSIVE & MOBILE POLISH.*?/\*\s*───\s*FRAMELESS QUOTE',
        "/* ─── FRAMELESS QUOTE",
        content,
        flags=re.DOTALL
    )
    # Remove any duplicate @media (max-width: 900px) that was added earlier inside diptych
    content = re.sub(
        r'@media\s*\(max-width:\s*900px\)\s*\{\s*\.curator-diptych\s*\{.*?\}\s*\}\s*\}',
        "",
        content,
        flags=re.DOTALL
    )

    with open(index_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Polished mobile styling in {index_file}")

# 2. Mobile CSS for Article Pages
article_mobile_css = """
    /* ═══════════════════════════════════════════════
       RESPONSIVE & MOBILE POLISH (ARTICLE PAGES)
    ═══════════════════════════════════════════════ */
    @media (max-width: 1024px) {
      .article-header { padding: 44px 24px 30px; }
      .article-hero { padding: 0 24px; margin-bottom: 40px; }
      .article-body-wrap, .article-tags-wrap { padding: 0 24px; }
      .related-articles-section { padding: 60px 24px; }
      .related-grid { grid-template-columns: repeat(2, 1fr); gap: 28px; }
    }

    @media (max-width: 768px) {
      .navbar-spacer { height: var(--nav-height-mobile, 64px); }
      .article-header { padding: 28px 18px 24px; }
      .breadcrumb-nav { font-size: 10px; margin-bottom: 14px; gap: 6px; }
      .category-tag { font-size: 9.5px; padding: 4px 12px; margin-bottom: 16px; }
      .article-headline { font-size: clamp(1.75rem, 6.5vw, 2.25rem); line-height: 1.15; margin-bottom: 14px; }
      .article-subheadline { font-size: 1.05rem; line-height: 1.5; margin-bottom: 22px; }
      .article-meta-row { flex-direction: column; align-items: flex-start; gap: 12px; padding-bottom: 20px; font-size: 12px; }
      .share-buttons { width: 100%; margin-left: 0; justify-content: flex-start; padding-top: 6px; gap: 8px; }
      .share-btn { font-size: 11px; padding: 6px 12px; }

      .article-hero { padding: 0 18px; margin-bottom: 28px; }
      .article-hero img { aspect-ratio: 16/10; border-radius: 6px; }
      .article-hero-caption { font-size: 11.5px; margin-top: 8px; }

      .article-body-wrap { padding: 0 18px; }
      .article-body p { font-size: 16.5px; line-height: 1.75; margin-bottom: 1.4em; }
      .article-body h2 { font-size: 1.45rem; line-height: 1.25; margin-top: 2.4rem; margin-bottom: 0.9rem; }
      .article-body h3 { font-size: 1.2rem; margin-top: 1.8rem; margin-bottom: 0.6rem; }
      .article-body ul { padding-left: 1.2rem; margin-bottom: 1.5rem; }
      .article-body ul li { font-size: 16.5px; line-height: 1.7; margin-bottom: 0.5em; }
      .article-quote { padding-left: 18px; margin: 2rem 0; font-size: 1.1rem; line-height: 1.55; }
      .article-figure { margin: 2rem 0; }
      .article-key-takeaways { padding: 20px 20px; margin: 2rem 0; }
      .article-key-takeaways h3 { font-size: 1rem; }

      .article-cta-box { padding: 36px 20px; margin: 2.8rem 0; border-radius: 8px; }
      .article-cta-box h3 { font-size: 1.35rem; margin-bottom: 10px; }
      .article-cta-box p { font-size: 14.5px; line-height: 1.6; margin-bottom: 22px; }
      .article-cta-btn { width: 100%; justify-content: center; padding: 14px 24px; font-size: 12px; box-sizing: border-box; }

      .article-tags-wrap { padding: 24px 18px 40px; }
      .article-tag { font-size: 11px; padding: 5px 12px; }

      .related-articles-section { padding: 48px 18px; }
      .related-articles-inner { padding: 0; }
      .related-articles-header { margin-bottom: 28px; padding-bottom: 14px; }
      .related-articles-title { font-size: 1.15rem; }
      .related-articles-link { font-size: 11px; }
      .related-grid { grid-template-columns: 1fr; gap: 24px; }
      .related-card-title { font-size: 1.15rem; }
    }
"""

all_article_files = [f for f in glob.glob("*/blog/*.html") if not f.endswith("index.html")]

for article_file in all_article_files:
    with open(article_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace old responsive block in articles
    if "@media (max-width: 900px)" in content:
        content = re.sub(
            r'@media\s*\(max-width:\s*900px\)\s*\{.*?\}\s*(?=</style>)',
            article_mobile_css + "\n  ",
            content,
            flags=re.DOTALL
        )
    elif "@media (max-width: 1000px)" in content:
        content = re.sub(
            r'/\*\s*──\s*Responsive\s*──\s*\*/.*?(?=</style>)',
            article_mobile_css + "\n  ",
            content,
            flags=re.DOTALL
        )
    elif "@media (max-width: 640px)" in content:
        content = re.sub(
            r'@media\s*\(max-width:\s*640px\)\s*\{.*?(?=</style>)',
            article_mobile_css + "\n  ",
            content,
            flags=re.DOTALL
        )

    with open(article_file, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Polished mobile responsiveness across all {len(all_article_files)} article files!")
