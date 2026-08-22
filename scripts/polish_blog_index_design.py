import re

# Update en/blog/index.html with unique imagery, polished card typography, and pill newsletter
with open("en/blog/index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Card CSS for better typography, category badge, and smooth shadow
card_css_pattern = re.compile(r'/\*\s*Article Card\s*\*/.*?\.no-results\s*\{[^}]*\}', re.DOTALL)
new_card_css = """/* Article Card — Luxury Editorial */
    .article-card {
      background: #EEF0E2;
      border-radius: 6px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      text-decoration: none;
      color: inherit;
      transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      box-sizing: border-box;
    }
    .article-card:hover {
      transform: translateY(-6px);
      box-shadow: 0 16px 36px rgba(39, 39, 36, 0.08);
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
      font-size: 1.2rem;
      font-weight: 700;
      line-height: 1.28;
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
      gap: 12px;
      font-size: 12px;
      color: #7a756e;
      font-weight: 500;
      margin-top: auto;
      padding-top: 18px;
      border-top: 1px solid rgba(39, 39, 36, 0.08);
      letter-spacing: 0.02em;
    }
    .article-card__meta-sep {
      width: 3px;
      height: 3px;
      border-radius: 50%;
      background: #aaa9a0;
      display: inline-block;
      flex-shrink: 0;
    }
    .no-results { grid-column: 1/-1; text-align: center; padding: 60px 20px; color: #7a756e; font-size: 0.95rem; display: none; }"""

if card_css_pattern.search(content):
    content = card_css_pattern.sub(new_card_css, content)

# 2. Update Newsletter form styling to modern pill layout
newsletter_css_pattern = re.compile(r'/\*\s*Newsletter Section\s*—\s*Contained Luxury Card\s*\*/.*?\.newsletter-note\s*\{[^}]*\}', re.DOTALL)
new_newsletter_css = """/* Newsletter Section — Contained Luxury Card */
    .newsletter-wrap { padding: 40px 0 100px; }
    .newsletter-card {
      background: #EEF0E2;
      border-radius: 8px;
      padding: 80px 48px;
      text-align: center;
      box-sizing: border-box;
      border: 1px solid rgba(39, 39, 36, 0.08);
    }
    .newsletter-eyebrow {
      display: inline-block;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.3em;
      text-transform: uppercase;
      color: #523225;
      margin-bottom: 20px;
    }
    .newsletter-headline {
      font-size: clamp(2.2rem, 4.2vw, 3.4rem);
      font-weight: 700;
      line-height: 1.08;
      letter-spacing: -0.025em;
      color: #272724;
      margin: 0 0 18px;
    }
    .newsletter-subtext {
      font-size: 1.05rem;
      line-height: 1.7;
      color: #5a5a54;
      max-width: 540px;
      margin: 0 auto 40px;
    }
    .newsletter-form {
      display: flex;
      max-width: 520px;
      margin: 0 auto;
      border: 1px solid rgba(39, 39, 36, 0.18);
      border-radius: 100px;
      overflow: hidden;
      background: #F6F7EA;
      box-shadow: 0 4px 16px rgba(39, 39, 36, 0.04);
      padding: 4px 4px 4px 20px;
      align-items: center;
    }
    .newsletter-form__input {
      flex: 1;
      background: transparent !important;
      border: none !important;
      outline: none !important;
      padding: 12px 14px;
      font-size: 15px;
      color: #272724 !important;
      font-family: 'Clash Grotesk', sans-serif !important;
    }
    .newsletter-form__input::placeholder {
      color: #8e8e88;
    }
    .newsletter-form__btn {
      background-color: #272724 !important;
      color: #F6F7EA !important;
      border: none !important;
      padding: 14px 32px;
      border-radius: 100px;
      font-size: 12.5px;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      cursor: pointer;
      font-family: 'Clash Grotesk', sans-serif !important;
      transition: background 0.2s ease, transform 0.2s ease;
      white-space: nowrap;
    }
    .newsletter-form__btn:hover {
      background-color: #523225 !important;
      transform: translateY(-1px);
    }
    .newsletter-note {
      font-size: 12.5px;
      color: #7a756e;
      margin-top: 18px;
      letter-spacing: 0.02em;
    }
    @media (max-width: 640px) {
      .newsletter-form { flex-direction: column; border-radius: 8px; padding: 0; }
      .newsletter-form__input { width: 100%; padding: 14px 16px; border-bottom: 1px solid rgba(39,39,36,0.1) !important; }
      .newsletter-form__btn { width: 100%; border-radius: 0; padding: 14px 20px; }
      .newsletter-card { padding: 48px 24px; }
    }"""

if newsletter_css_pattern.search(content):
    content = newsletter_css_pattern.sub(new_newsletter_css, content)

# 3. Update Unique Images in Grid:
# Card 4 (Marrakech to Agafay): use /images/gallery/gal1.webp instead of duplicate camel
content = content.replace(
    '<a href="marrakech-to-agafay.html" class="article-card" data-category="travel-tips" role="listitem" aria-label="Travel Tips: Marrakech to Agafay Desert">\n            <div class="article-card__image-wrap">\n              <img src="/images/Slider-images/slider-1.webp"',
    '<a href="marrakech-to-agafay.html" class="article-card" data-category="travel-tips" role="listitem" aria-label="Travel Tips: Marrakech to Agafay Desert">\n            <div class="article-card__image-wrap">\n              <img src="/images/gallery/gal1.webp"'
)

with open("en/blog/index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated en/blog/index.html with design polish.")
