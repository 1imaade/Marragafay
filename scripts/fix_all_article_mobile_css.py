import glob
import re

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
      
      /* Article Header */
      .article-header { padding: 28px 18px 24px; }
      .breadcrumb-nav { font-size: 10.5px; margin-bottom: 14px; gap: 6px; flex-wrap: wrap; }
      .category-tag { font-size: 9.5px; padding: 4px 12px; margin-bottom: 16px; }
      .article-headline { font-size: clamp(1.75rem, 6.5vw, 2.25rem); line-height: 1.15; margin-bottom: 14px; }
      .article-subheadline { font-size: 1.05rem; line-height: 1.5; margin-bottom: 22px; }
      .article-meta-row { flex-direction: column; align-items: flex-start; gap: 12px; padding-bottom: 20px; font-size: 12px; }
      .share-buttons { width: 100%; margin-left: 0; justify-content: flex-start; padding-top: 6px; gap: 8px; }
      .share-btn { font-size: 11px; padding: 6px 12px; }

      /* Article Hero */
      .article-hero { padding: 0 18px; margin-bottom: 28px; }
      .article-hero-img-wrap { border-radius: 6px; padding-top: 62.5%; }
      .article-hero img { border-radius: 6px; }
      .article-hero-caption { font-size: 11.5px; margin-top: 8px; }

      /* Article Body Typography & Spacing */
      .article-body-wrap { margin: 24px auto 0; padding: 0 18px; }
      .article-body p { font-size: 16.5px; line-height: 1.75; margin-bottom: 1.4em; }
      .article-body h2 { font-size: 1.45rem; line-height: 1.25; margin-top: 2.4rem; margin-bottom: 0.9rem; }
      .article-body h3 { font-size: 1.2rem; margin-top: 1.8rem; margin-bottom: 0.6rem; }
      .article-body ul { padding-left: 1.2rem; margin-bottom: 1.5rem; }
      .article-body ul li { font-size: 16.5px; line-height: 1.7; margin-bottom: 0.5em; }
      .article-body blockquote, .article-quote { padding: 6px 0 6px 16px; margin: 2rem 0; font-size: 1.1rem; line-height: 1.55; }
      .article-figure { margin: 2rem 0; }
      .article-inline-img { margin: 1.8rem 0 0.5rem; }
      .article-inline-caption { font-size: 11.5px; margin-bottom: 1.5rem; }
      .article-key-takeaways { padding: 20px; margin: 2rem 0; }
      .article-key-takeaways h3 { font-size: 1rem; }

      /* In-Article Booking Box */
      .article-cta-box { padding: 32px 18px; margin: 2.8rem 0; border-radius: 8px; }
      .article-cta-box h3 { font-size: 1.35rem; margin-bottom: 10px; }
      .article-cta-box p { font-size: 14.5px; line-height: 1.6; margin-bottom: 22px; }
      .article-cta-btn { width: 100%; justify-content: center; padding: 14px 24px; font-size: 12px; box-sizing: border-box; }

      /* Article Tags */
      .article-tags-wrap { padding: 24px 18px 40px; }
      .article-tag { font-size: 11px; padding: 5px 12px; }

      /* Related Articles */
      .related-articles-section { padding: 48px 18px; }
      .related-articles-inner { padding: 0; }
      .related-articles-header { margin-bottom: 28px; padding-bottom: 14px; flex-direction: row; justify-content: space-between; align-items: baseline; }
      .related-articles-title { font-size: 1.15rem; }
      .related-articles-link { font-size: 11px; }
      .related-grid { grid-template-columns: 1fr; gap: 24px; }
      .related-card-title { font-size: 1.15rem; }
    }
"""

all_article_files = [f for f in glob.glob("*/blog/*.html") if not f.endswith("index.html")]

for filepath in all_article_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Match whatever responsive block exists before </style>
    if "/* ═══════════════════════════════════════════════\n       RESPONSIVE & MOBILE POLISH" in content:
        content = re.sub(
            r'/\*\s*═══════════════════════════════════════════════\s*RESPONSIVE & MOBILE POLISH.*?(?=</style>)',
            article_mobile_css.strip() + "\n  ",
            content,
            flags=re.DOTALL
        )
    elif "@media (max-width: 1000px)" in content:
        content = re.sub(
            r'/\*\s*──\s*Responsive\s*──\s*\*/.*?(?=</style>)',
            article_mobile_css.strip() + "\n  ",
            content,
            flags=re.DOTALL
        )
    elif "@media (max-width: 640px)" in content:
        content = re.sub(
            r'@media\s*\(max-width:\s*640px\)\s*\{.*?(?=</style>)',
            article_mobile_css.strip() + "\n  ",
            content,
            flags=re.DOTALL
        )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Successfully updated mobile CSS in all {len(all_article_files)} article files!")
