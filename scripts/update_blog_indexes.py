import re

# EN Index
with open("en/blog/index.html", "r", encoding="utf-8") as f:
    en_content = f.read()

# Fix CSS for newsletter-section and ensure background is dark with !important
old_newsletter_css = """.newsletter-section { background: #272724; padding: 90px 0; }
    .newsletter-inner { max-width: 600px; margin: 0 auto; padding: 0 32px; text-align: center; }
    .newsletter-eyebrow { font-size: 10px; font-weight: 700; letter-spacing: 0.35em; text-transform: uppercase; color: #523225; margin-bottom: 20px; }
    .newsletter-headline { font-size: clamp(2rem,4vw,3rem); font-weight: 700; line-height: 1.05; letter-spacing: -0.025em; color: #F6F7EA; margin: 0 0 18px; }
    .newsletter-subtext { font-size: 0.95rem; line-height: 1.7; color: rgba(246,247,234,0.65); margin: 0 0 40px; }
    .newsletter-form { display: flex; gap: 0; max-width: 480px; margin: 0 auto; border: 1px solid rgba(246,247,234,0.2); border-radius: 3px; overflow: hidden; }
    .newsletter-form__input { flex: 1; background: transparent; border: none; outline: none; padding: 16px 20px; font-size: 14px; color: #F6F7EA; font-family: 'Clash Grotesk', sans-serif !important; }
    .newsletter-form__input::placeholder { color: rgba(246,247,234,0.4); }
    .newsletter-form__btn { background: #523225; color: #F6F7EA; border: none; padding: 16px 28px; font-size: 12px; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase; cursor: pointer; font-family: 'Clash Grotesk', sans-serif !important; transition: background 0.2s ease; white-space: nowrap; }
    .newsletter-form__btn:hover { background: #3d241a; }
    .newsletter-note { font-size: 11px; color: rgba(246,247,234,0.35); margin-top: 16px; letter-spacing: 0.02em; }"""

new_newsletter_css = """.newsletter-section { background-color: #272724 !important; color: #F6F7EA !important; padding: 90px 0; }
    .newsletter-inner { max-width: 600px; margin: 0 auto; padding: 0 32px; text-align: center; }
    .newsletter-eyebrow { font-size: 11px; font-weight: 700; letter-spacing: 0.3em; text-transform: uppercase; color: #d4af37 !important; margin-bottom: 20px; }
    .newsletter-headline { font-size: clamp(2rem,4vw,3.2rem); font-weight: 700; line-height: 1.08; letter-spacing: -0.025em; color: #F6F7EA !important; margin: 0 0 18px; }
    .newsletter-subtext { font-size: 1rem; line-height: 1.7; color: rgba(246,247,234,0.8) !important; margin: 0 0 36px; }
    .newsletter-form { display: flex; gap: 0; max-width: 480px; margin: 0 auto; border: 1px solid rgba(246,247,234,0.3) !important; border-radius: 4px; overflow: hidden; background: rgba(255, 255, 255, 0.05) !important; }
    .newsletter-form__input { flex: 1; background: transparent !important; border: none !important; outline: none !important; padding: 16px 20px; font-size: 14px; color: #F6F7EA !important; font-family: 'Clash Grotesk', sans-serif !important; }
    .newsletter-form__input::placeholder { color: rgba(246,247,234,0.45) !important; }
    .newsletter-form__btn { background-color: #523225 !important; color: #F6F7EA !important; border: none !important; padding: 16px 28px; font-size: 12px; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase; cursor: pointer; font-family: 'Clash Grotesk', sans-serif !important; transition: background 0.2s ease; white-space: nowrap; }
    .newsletter-form__btn:hover { background-color: #3d241a !important; }
    .newsletter-note { font-size: 12px; color: rgba(246,247,234,0.45) !important; margin-top: 16px; letter-spacing: 0.02em; }"""

if old_newsletter_css in en_content:
    en_content = en_content.replace(old_newsletter_css, new_newsletter_css)

# Update the grid markup to replace broken image and add the 6th and 7th cards
grid_start = '<div class="article-grid" id="article-grid" role="list">'
grid_end = '<!-- NEWSLETTER -->'

new_grid_html = """<div class="article-grid" id="article-grid" role="list">

          <a href="/en/blog/agafay-desert-guide" class="article-card" data-category="desert-guide" role="listitem" aria-label="Desert Guide: The Complete Guide to Agafay Desert">
            <div class="article-card__image-wrap">
              <img src="/images/Slider-images/slider-2.webp" alt="The Agafay stone desert plateau" loading="lazy" decoding="async" width="640" height="480" />
            </div>
            <div class="article-card__body">
              <p class="article-card__category">Desert Guide</p>
              <h3 class="article-card__title">The Complete Guide to Agafay Desert &#8212; Morocco&#x2019;s Stone Desert Explained</h3>
              <p class="article-card__excerpt">What makes Agafay different from the Sahara, and why travelers are increasingly choosing this 45-minute drive from Marrakech over a 10-hour journey south.</p>
              <div class="article-card__meta">
                <span>August 2026</span>
                <span class="article-card__meta-sep" aria-hidden="true"></span>
                <span>8 min read</span>
              </div>
            </div>
          </a>

          <a href="/en/blog/agafay-camel-ride" class="article-card" data-category="experience" role="listitem" aria-label="Experience: Sunset Camel Ride in Agafay">
            <div class="article-card__image-wrap">
              <img src="/images/Slider-images/slider-3.webp" alt="Camel ride at sunset in the Agafay desert" loading="lazy" decoding="async" width="640" height="480" />
            </div>
            <div class="article-card__body">
              <p class="article-card__category">Experience</p>
              <h3 class="article-card__title">Sunset Camel Ride in Agafay: What to Expect (An Honest Account)</h3>
              <p class="article-card__excerpt">The silence before sunset in the desert is not empty &#8212; it is full. Our guide on what every first-time visitor should know before mounting the camel.</p>
              <div class="article-card__meta">
                <span>August 2026</span>
                <span class="article-card__meta-sep" aria-hidden="true"></span>
                <span>5 min read</span>
              </div>
            </div>
          </a>

          <a href="/en/blog/berber-culture-agafay" class="article-card" data-category="culture" role="listitem" aria-label="Culture: Berber Heritage and the Agafay">
            <div class="article-card__image-wrap">
              <img src="/images/Slider-images/slider-4.webp" alt="Berber landscape and culture in the Agafay region" loading="lazy" decoding="async" width="640" height="480" />
            </div>
            <div class="article-card__body">
              <p class="article-card__category">Culture</p>
              <h3 class="article-card__title">Berber Heritage and the Agafay: A Culture That Predates Tourism</h3>
              <p class="article-card__excerpt">Long before quad bikes and glamping tents arrived, the Agafay stone plateau was home to Berber communities whose traditions survive intact.</p>
              <div class="article-card__meta">
                <span>July 2026</span>
                <span class="article-card__meta-sep" aria-hidden="true"></span>
                <span>6 min read</span>
              </div>
            </div>
          </a>

          <a href="/en/blog/marrakech-to-agafay" class="article-card" data-category="travel-tips" role="listitem" aria-label="Travel Tips: Marrakech to Agafay Desert">
            <div class="article-card__image-wrap">
              <img src="/images/Slider-images/slider-1.webp" alt="The road from Marrakech to the Agafay desert" loading="lazy" decoding="async" width="640" height="480" />
            </div>
            <div class="article-card__body">
              <p class="article-card__category">Travel Tips</p>
              <h3 class="article-card__title">Marrakech to Agafay Desert: Every Way to Get There</h3>
              <p class="article-card__excerpt">From private transfer to shared taxi, the 45-kilometer journey separates the medina from the silence. A complete breakdown of every option, with costs.</p>
              <div class="article-card__meta">
                <span>July 2026</span>
                <span class="article-card__meta-sep" aria-hidden="true"></span>
                <span>4 min read</span>
              </div>
            </div>
          </a>

          <a href="/en/blog/agafay-dinner-experience" class="article-card" data-category="experience" role="listitem" aria-label="Experience: The Agafay Dinner Experience">
            <div class="article-card__image-wrap">
              <img src="/images/activites/show.webp" alt="Private luxury dinner under the stars in the Agafay desert" loading="lazy" decoding="async" width="640" height="480" />
            </div>
            <div class="article-card__body">
              <p class="article-card__category">Experience</p>
              <h3 class="article-card__title">The Agafay Dinner Experience: Luxury Under a Moroccan Sky</h3>
              <p class="article-card__excerpt">How a private desert dinner became the most requested experience in Marragafay&#x2019;s catalogue &#8212; and what separates a good dinner from an unforgettable one.</p>
              <div class="article-card__meta">
                <span>June 2026</span>
                <span class="article-card__meta-sep" aria-hidden="true"></span>
                <span>7 min read</span>
              </div>
            </div>
          </a>

          <a href="/en/blog/agafay-quad-biking-guide" class="article-card" data-category="experience" role="listitem" aria-label="Adventure: Quad Biking in Agafay Desert">
            <div class="article-card__image-wrap">
              <img src="/images/activites/quad.webp" alt="Quad biking across the Agafay stone plateau" loading="lazy" decoding="async" width="640" height="480" />
            </div>
            <div class="article-card__body">
              <p class="article-card__category">Adventure</p>
              <h3 class="article-card__title">Quad Biking in Agafay Desert: Safety, Tips & What You'll See</h3>
              <p class="article-card__excerpt">Everything you need to know about piloting powerful 4x4 quad bikes across Morocco's most thrilling mineral terrain.</p>
              <div class="article-card__meta">
                <span>August 2026</span>
                <span class="article-card__meta-sep" aria-hidden="true"></span>
                <span>6 min read</span>
              </div>
            </div>
          </a>

          <div class="no-results" id="no-results" aria-live="polite">
            No articles found in this category yet. More stories are on their way.
          </div>

        </div>
      </div>
    </section>

    <!-- NEWSLETTER -->
    <section class="newsletter-section" style="background-color: #272724 !important; color: #F6F7EA !important;">
      <div class="newsletter-inner">
        <p class="newsletter-eyebrow">The Desert Letter</p>
        <h2 class="newsletter-headline">Desert dispatches,<br>delivered.</h2>
        <p class="newsletter-subtext">One monthly letter. No noise. Stories, guides, and seasonal offers from the stone desert.</p>
        <form class="newsletter-form" action="#" method="post" onsubmit="handleNewsletterSubmit(event);" novalidate aria-label="Newsletter signup">
          <label for="newsletter-email" class="sr-only">Your email address</label>
          <input type="email" id="newsletter-email" name="email" class="newsletter-form__input" placeholder="your@email.com" autocomplete="email" required aria-required="true" />
          <button type="submit" class="newsletter-form__btn" aria-label="Subscribe to the desert letter">Subscribe</button>
        </form>
        <p class="newsletter-note">One email per month. Unsubscribe at any time.</p>
      </div>
    </section>
"""

# Replace the section in en_content
pattern = re.compile(r'<div class="article-grid" id="article-grid" role="list">.*?<!-- NEWSLETTER -->\s*<section class="newsletter-section">.*?</section>', re.DOTALL)
if pattern.search(en_content):
    en_content = pattern.sub(new_grid_html, en_content)

with open("en/blog/index.html", "w", encoding="utf-8") as f:
    f.write(en_content)

print("Updated en/blog/index.html successfully.")
