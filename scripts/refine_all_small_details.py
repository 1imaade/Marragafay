import re

with open("en/blog/index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Refine CSS in en/blog/index.html
style_block_replacement = """    /* Hero */
    .journal-hero { background-color: #F6F7EA; padding: 72px 0 54px; border-bottom: 1px solid rgba(39,39,36,0.1); }
    .journal-hero__inner { max-width: 1440px; margin: 0 auto; padding: 0 32px; box-sizing: border-box; }
    .journal-hero__eyebrow { display: inline-flex; align-items: center; gap: 10px; font-size: 11px; font-weight: 700; letter-spacing: 0.3em; text-transform: uppercase; color: #523225; margin-bottom: 24px; }
    .journal-hero__eyebrow::before { content: ''; width: 24px; height: 1.5px; background: #523225; display: inline-block; }
    .journal-hero__headline { font-size: clamp(3rem, 6.5vw, 6.5rem); font-weight: 700; line-height: 0.94; letter-spacing: -0.035em; color: #272724; margin: 0 0 24px; max-width: 960px; }
    .journal-hero__subline { font-size: clamp(1rem, 1.4vw, 1.15rem); font-weight: 400; color: #6e6a64; max-width: 540px; line-height: 1.65; margin: 0 0 42px; }
    .journal-hero__divider { border: 0; border-top: 1px solid rgba(39,39,36,0.1); margin: 0 0 32px; }

    /* Filter Pills */
    .category-filter { display: flex; flex-wrap: wrap; gap: 10px; align-items: center; }
    .category-filter__label { font-size: 11px; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase; color: #7a756e; margin-right: 8px; }
    .category-pill { display: inline-flex; align-items: center; padding: 9px 22px; border-radius: 100px; border: 1px solid rgba(39,39,36,0.2); font-size: 12px; font-weight: 600; letter-spacing: 0.06em; color: #272724; background: transparent; cursor: pointer; transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1); text-transform: uppercase; font-family: 'Clash Grotesk', sans-serif !important; }
    .category-pill:hover { border-color: #523225; color: #523225; background: rgba(82,50,37,0.06); transform: translateY(-1px); }
    .category-pill.active { background: #272724; color: #F6F7EA; border-color: #272724; box-shadow: 0 4px 14px rgba(39,39,36,0.15); }

    /* Sections */
    .journal-section { max-width: 1440px; margin: 0 auto; padding: 0 32px; box-sizing: border-box; }
    .journal-section-wrap { padding: 72px 0; }
    .section-label { font-size: 11px; font-weight: 700; letter-spacing: 0.28em; text-transform: uppercase; color: #523225; margin-bottom: 32px; display: flex; align-items: center; gap: 16px; }
    .section-label::after { content: ''; flex: 1; height: 1px; background: rgba(39,39,36,0.12); display: block; }

    /* Featured Article Card — Refined */
    .featured-article {
      display: grid;
      grid-template-columns: 1.15fr 1fr;
      gap: 0;
      background: #EEF0E2;
      border-radius: 8px;
      overflow: hidden;
      min-height: 520px;
      border: 1px solid rgba(39,39,36,0.08);
      box-shadow: 0 10px 30px rgba(39,39,36,0.04);
      transition: box-shadow 0.3s ease, transform 0.3s ease;
    }
    .featured-article:hover {
      box-shadow: 0 18px 42px rgba(39,39,36,0.08);
    }
    .featured-article__image-wrap { position: relative; overflow: hidden; }
    .featured-article__image-wrap img { width: 100%; height: 100%; object-fit: cover; display: block; transition: transform 0.7s cubic-bezier(0.4,0,0.2,1); }
    .featured-article:hover .featured-article__image-wrap img { transform: scale(1.04); }
    .featured-article__image-overlay { position: absolute; inset: 0; background: linear-gradient(135deg,rgba(39,39,36,0.18) 0%,rgba(39,39,36,0.02) 100%); z-index: 1; }
    .featured-article__badge {
      position: absolute;
      top: 24px;
      left: 24px;
      z-index: 2;
      background: rgba(246,247,234,0.96);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      color: #523225;
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.25em;
      text-transform: uppercase;
      padding: 7px 18px;
      border-radius: 100px;
      box-shadow: 0 4px 14px rgba(0,0,0,0.12);
      border: 1px solid rgba(82,50,37,0.15);
    }
    .featured-article__content {
      padding: 60px 60px 60px 64px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      background: #EEF0E2;
      box-sizing: border-box;
    }
    .featured-article__category {
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: #523225;
      margin-bottom: 20px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .featured-article__category::before {
      content: '';
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #523225;
      display: inline-block;
    }
    .featured-article__title {
      font-size: clamp(1.85rem, 3.2vw, 2.75rem);
      font-weight: 700;
      line-height: 1.1;
      letter-spacing: -0.025em;
      color: #272724;
      margin: 0 0 20px;
    }
    .featured-article__excerpt {
      font-size: 1.05rem;
      line-height: 1.75;
      color: #4e4e48;
      margin: 0 0 32px;
      max-width: 540px;
    }
    .featured-article__meta {
      display: flex;
      align-items: center;
      gap: 16px;
      font-size: 12.5px;
      color: #7a756e;
      font-weight: 500;
      margin-bottom: 34px;
      letter-spacing: 0.02em;
    }
    .featured-article__meta-dot { width: 3px; height: 3px; border-radius: 50%; background: #7a756e; display: inline-block; flex-shrink: 0; }
    .featured-article__author { font-size: 11px; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: #272724; }
    .featured-article__cta {
      display: inline-flex;
      align-items: center;
      gap: 12px;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: #272724;
      text-decoration: none;
      border-bottom: 1.5px solid #272724;
      padding-bottom: 3px;
      transition: color 0.25s ease, border-color 0.25s ease, gap 0.25s ease;
      width: fit-content;
    }
    .featured-article__cta:hover { color: #523225; border-color: #523225; gap: 18px; text-decoration: none; }
    .featured-article__cta-arrow { font-size: 16px; line-height: 1; transition: transform 0.25s ease; }
    .featured-article__cta:hover .featured-article__cta-arrow { transform: translateX(4px); }

    /* Article Grid */
    .article-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; }

    /* Article Card — Luxury Editorial */
    .article-card {
      background: #EEF0E2;
      border-radius: 8px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      text-decoration: none;
      color: inherit;
      border: 1px solid rgba(39, 39, 36, 0.07);
      transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      box-sizing: border-box;
    }
    .article-card:hover {
      transform: translateY(-6px);
      box-shadow: 0 18px 40px rgba(39, 39, 36, 0.08);
      text-decoration: none;
      color: inherit;
    }
    .article-card__image-wrap {
      position: relative;
      overflow: hidden;
      aspect-ratio: 16/10;
    }
    .article-card__image-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .article-card:hover .article-card__image-wrap img {
      transform: scale(1.05);
    }
    .article-card__body {
      padding: 32px 30px 28px;
      display: flex;
      flex-direction: column;
      flex: 1;
      box-sizing: border-box;
    }
    .article-card__category {
      font-size: 10.5px;
      font-weight: 700;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: #523225;
      margin-bottom: 14px;
      display: inline-block;
    }
    .article-card__title {
      font-size: 1.22rem;
      font-weight: 700;
      line-height: 1.26;
      letter-spacing: -0.015em;
      color: #272724;
      margin: 0 0 14px;
    }
    .article-card__excerpt {
      font-size: 0.95rem;
      line-height: 1.7;
      color: #5a5a54;
      margin: 0 0 24px;
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }
    .article-card__meta {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 12px;
      color: #7a756e;
      font-weight: 500;
      margin-top: auto;
      padding-top: 18px;
      border-top: 1px solid rgba(39, 39, 36, 0.08);
      letter-spacing: 0.02em;
    }
    .article-card__meta-left { display: flex; align-items: center; gap: 10px; }
    .article-card__meta-sep {
      width: 3px;
      height: 3px;
      border-radius: 50%;
      background: #aaa9a0;
      display: inline-block;
      flex-shrink: 0;
    }
    .article-card__meta-arrow {
      font-size: 13px;
      color: #523225;
      font-weight: 700;
      transition: transform 0.2s ease;
    }
    .article-card:hover .article-card__meta-arrow {
      transform: translateX(4px);
    }
    .no-results { grid-column: 1/-1; text-align: center; padding: 60px 20px; color: #7a756e; font-size: 0.95rem; display: none; }"""

# Replace in content
pattern = re.compile(r'/\*\s*Hero\s*\*/.*?\.no-results\s*\{[^}]*\}', re.DOTALL)
if pattern.search(content):
    content = pattern.sub(style_block_replacement, content)

with open("en/blog/index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Refined all small details in en/blog/index.html.")
