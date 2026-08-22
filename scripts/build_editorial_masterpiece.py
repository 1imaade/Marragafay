import re

# 1. Read en/blog/index.html
with open("en/blog/index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the middle section styles and HTML completely
new_middle_css = """    /* ═══════════════════════════════════════════════
       LUXURY EDITORIAL MAGAZINE SECTIONS
    ═══════════════════════════════════════════════ */
    .journal-section { max-width: 1440px; margin: 0 auto; padding: 0 32px; box-sizing: border-box; }
    .journal-section-wrap { padding: 64px 0; }

    /* Editorial Section Header */
    .editorial-header {
      display: flex;
      align-items: flex-end;
      justify-content: space-between;
      margin-bottom: 36px;
      padding-bottom: 18px;
      border-bottom: 1.5px solid rgba(39, 39, 36, 0.12);
    }
    .editorial-header__left { display: flex; align-items: baseline; gap: 16px; }
    .editorial-header__num {
      font-size: 13px;
      font-weight: 700;
      color: #523225;
      letter-spacing: 0.15em;
    }
    .editorial-header__title {
      font-size: 1.4rem;
      font-weight: 700;
      color: #272724;
      letter-spacing: -0.015em;
      margin: 0;
      text-transform: uppercase;
    }
    .editorial-header__sub {
      font-size: 12px;
      font-weight: 500;
      color: #7a756e;
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }

    /* ─── 1. COVER STORY (Full-Width Cinematic Lead) ─── */
    .cover-story {
      display: grid;
      grid-template-columns: 1.25fr 1fr;
      background: #EEF0E2;
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid rgba(39, 39, 36, 0.08);
      box-shadow: 0 12px 36px rgba(39, 39, 36, 0.05);
      transition: box-shadow 0.3s ease, transform 0.3s ease;
      text-decoration: none;
      color: inherit;
    }
    .cover-story:hover {
      box-shadow: 0 20px 48px rgba(39, 39, 36, 0.09);
      text-decoration: none;
      color: inherit;
    }
    .cover-story__media {
      position: relative;
      overflow: hidden;
      min-height: 480px;
    }
    .cover-story__media img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.8s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .cover-story:hover .cover-story__media img {
      transform: scale(1.04);
    }
    .cover-story__badge {
      position: absolute;
      top: 24px;
      left: 24px;
      background: rgba(246, 247, 234, 0.95);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      color: #523225;
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.25em;
      text-transform: uppercase;
      padding: 7px 18px;
      border-radius: 100px;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.12);
      border: 1px solid rgba(82, 50, 37, 0.15);
      z-index: 2;
    }
    .cover-story__body {
      padding: 64px 56px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      background: #EEF0E2;
      box-sizing: border-box;
    }
    .cover-story__tag-row {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 22px;
    }
    .cover-story__tag {
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: #523225;
      background: rgba(82, 50, 37, 0.08);
      padding: 5px 14px;
      border-radius: 100px;
    }
    .cover-story__read-time {
      font-size: 12px;
      font-weight: 500;
      color: #7a756e;
    }
    .cover-story__title {
      font-size: clamp(2rem, 3.4vw, 2.9rem);
      font-weight: 700;
      line-height: 1.1;
      letter-spacing: -0.025em;
      color: #272724;
      margin: 0 0 20px;
    }
    .cover-story__standfirst {
      font-size: 1.08rem;
      line-height: 1.75;
      color: #4e4e48;
      margin: 0 0 36px;
      max-width: 540px;
    }
    .cover-story__footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-top: 24px;
      border-top: 1px solid rgba(39, 39, 36, 0.1);
      margin-top: auto;
    }
    .cover-story__author {
      font-size: 11.5px;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: #272724;
    }
    .cover-story__cta {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: #523225;
      transition: gap 0.25s ease;
    }
    .cover-story:hover .cover-story__cta {
      gap: 16px;
    }

    /* ─── 2. ASYMMETRIC STORY DUO ─── */
    .story-duo {
      display: grid;
      grid-template-columns: 1.3fr 1fr;
      gap: 36px;
      margin-top: 20px;
    }
    .story-card-tall {
      background: #EEF0E2;
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid rgba(39, 39, 36, 0.08);
      display: flex;
      flex-direction: column;
      text-decoration: none;
      color: inherit;
      transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.3s ease;
    }
    .story-card-tall:hover {
      transform: translateY(-6px);
      box-shadow: 0 18px 40px rgba(39, 39, 36, 0.08);
      text-decoration: none;
      color: inherit;
    }
    .story-card-tall__media {
      position: relative;
      aspect-ratio: 16/10;
      overflow: hidden;
    }
    .story-card-tall__media img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .story-card-tall:hover .story-card-tall__media img { transform: scale(1.05); }
    .story-card-tall__body {
      padding: 36px 36px 32px;
      display: flex;
      flex-direction: column;
      flex: 1;
    }
    .story-card-tall__tag {
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: #523225;
      margin-bottom: 14px;
    }
    .story-card-tall__title {
      font-size: 1.55rem;
      font-weight: 700;
      line-height: 1.22;
      letter-spacing: -0.02em;
      color: #272724;
      margin: 0 0 16px;
    }
    .story-card-tall__excerpt {
      font-size: 1rem;
      line-height: 1.7;
      color: #5a5a54;
      margin: 0 0 28px;
    }
    .story-card-tall__footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-top: auto;
      padding-top: 20px;
      border-top: 1px solid rgba(39, 39, 36, 0.08);
      font-size: 12px;
      color: #7a756e;
    }

    /* Right side stacked card */
    .story-card-stacked {
      background: #EEF0E2;
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid rgba(39, 39, 36, 0.08);
      display: flex;
      flex-direction: column;
      text-decoration: none;
      color: inherit;
      transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.3s ease;
    }
    .story-card-stacked:hover {
      transform: translateY(-6px);
      box-shadow: 0 18px 40px rgba(39, 39, 36, 0.08);
      text-decoration: none;
      color: inherit;
    }
    .story-card-stacked__media {
      position: relative;
      aspect-ratio: 16/10;
      overflow: hidden;
    }
    .story-card-stacked__media img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .story-card-stacked:hover .story-card-stacked__media img { transform: scale(1.05); }
    .story-card-stacked__body {
      padding: 32px 32px 28px;
      display: flex;
      flex-direction: column;
      flex: 1;
    }
    .story-card-stacked__tag {
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: #523225;
      margin-bottom: 12px;
    }
    .story-card-stacked__title {
      font-size: 1.35rem;
      font-weight: 700;
      line-height: 1.25;
      letter-spacing: -0.015em;
      color: #272724;
      margin: 0 0 14px;
    }
    .story-card-stacked__excerpt {
      font-size: 0.95rem;
      line-height: 1.65;
      color: #5a5a54;
      margin: 0 0 24px;
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }
    .story-card-stacked__footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-top: auto;
      padding-top: 18px;
      border-top: 1px solid rgba(39, 39, 36, 0.08);
      font-size: 12px;
      color: #7a756e;
    }

    /* ─── 3. EDITORIAL ATMOSPHERIC QUOTE STRIP ─── */
    .quote-interlude {
      margin: 72px 0;
      background: #272724;
      color: #F6F7EA;
      border-radius: 8px;
      padding: 70px 56px;
      position: relative;
      overflow: hidden;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.15);
    }
    .quote-interlude::before {
      content: '“';
      position: absolute;
      top: -30px;
      left: 36px;
      font-size: 180px;
      font-family: serif;
      color: rgba(246, 247, 234, 0.06);
      line-height: 1;
      pointer-events: none;
    }
    .quote-interlude__inner {
      max-width: 860px;
      margin: 0 auto;
      text-align: center;
      position: relative;
      z-index: 1;
    }
    .quote-interlude__eyebrow {
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.3em;
      text-transform: uppercase;
      color: #d4af37;
      margin-bottom: 24px;
      display: block;
    }
    .quote-interlude__text {
      font-size: clamp(1.4rem, 2.8vw, 2.2rem);
      font-weight: 600;
      line-height: 1.35;
      letter-spacing: -0.015em;
      color: #F6F7EA;
      margin: 0 0 28px;
      font-style: italic;
    }
    .quote-interlude__author {
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: rgba(246, 247, 234, 0.6);
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
    }
    .quote-interlude__author::before,
    .quote-interlude__author::after {
      content: '';
      width: 24px;
      height: 1px;
      background: rgba(246, 247, 234, 0.2);
    }

    /* ─── 4. FIELD DISPATCHES (3-Column Editorial Grid) ─── */
    .field-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 32px;
    }
    .field-card {
      background: #EEF0E2;
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid rgba(39, 39, 36, 0.08);
      display: flex;
      flex-direction: column;
      text-decoration: none;
      color: inherit;
      transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.3s ease;
    }
    .field-card:hover {
      transform: translateY(-6px);
      box-shadow: 0 18px 40px rgba(39, 39, 36, 0.08);
      text-decoration: none;
      color: inherit;
    }
    .field-card__media {
      position: relative;
      aspect-ratio: 16/10;
      overflow: hidden;
    }
    .field-card__media img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .field-card:hover .field-card__media img { transform: scale(1.05); }
    .field-card__body {
      padding: 30px 28px 26px;
      display: flex;
      flex-direction: column;
      flex: 1;
    }
    .field-card__tag-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
    }
    .field-card__tag {
      font-size: 10.5px;
      font-weight: 700;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: #523225;
    }
    .field-card__num {
      font-size: 11px;
      font-weight: 700;
      color: #8e8e88;
      letter-spacing: 0.1em;
    }
    .field-card__title {
      font-size: 1.22rem;
      font-weight: 700;
      line-height: 1.28;
      letter-spacing: -0.015em;
      color: #272724;
      margin: 0 0 14px;
    }
    .field-card__excerpt {
      font-size: 0.95rem;
      line-height: 1.7;
      color: #5a5a54;
      margin: 0 0 24px;
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }
    .field-card__footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-top: auto;
      padding-top: 18px;
      border-top: 1px solid rgba(39, 39, 36, 0.08);
      font-size: 12px;
      color: #7a756e;
    }
    .field-card__arrow {
      font-size: 13px;
      font-weight: 700;
      color: #523225;
      transition: transform 0.2s ease;
    }
    .field-card:hover .field-card__arrow {
      transform: translateX(4px);
    }

    /* Responsive */
    @media (max-width: 1024px) {
      .cover-story { grid-template-columns: 1fr; }
      .cover-story__media { min-height: 340px; }
      .cover-story__body { padding: 44px 36px; }
      .story-duo { grid-template-columns: 1fr; }
      .field-grid { grid-template-columns: repeat(2, 1fr); }
    }
    @media (max-width: 768px) {
      .journal-section { padding: 0 20px; }
      .journal-section-wrap { padding: 44px 0; }
      .quote-interlude { padding: 48px 24px; margin: 48px 0; }
      .field-grid { grid-template-columns: 1fr; }
    }"""

# 2. Build the new HTML structure for the middle section
new_middle_html = """    <!-- ═══════════════════════════════════════════════
         EDITORIAL MASTERPIECE — THE JOURNAL
    ═══════════════════════════════════════════════ -->

    <!-- 1. COVER STORY -->
    <section class="journal-section-wrap" style="padding-bottom: 30px;">
      <div class="journal-section">
        <div class="editorial-header">
          <div class="editorial-header__left">
            <span class="editorial-header__num">01 /</span>
            <h2 class="editorial-header__title">The Lead Story</h2>
          </div>
          <span class="editorial-header__sub">Flagship Field Note</span>
        </div>

        <a href="agafay-desert-guide.html" class="cover-story" data-category="desert-guide">
          <div class="cover-story__media">
            <img src="/images/Slider-images/slider-1.webp" alt="The Agafay stone desert plateau" loading="eager" fetchpriority="high" decoding="async" />
            <span class="cover-story__badge">Editor’s Pick</span>
          </div>
          <div class="cover-story__body">
            <div class="cover-story__tag-row">
              <span class="cover-story__tag">Desert Guide</span>
              <span class="cover-story__read-time">8 min read</span>
            </div>
            <h3 class="cover-story__title">The Complete Guide to Agafay Desert — Morocco’s Stone Desert Explained</h3>
            <p class="cover-story__standfirst">What makes Agafay different from the Sahara, and why travelers are increasingly choosing this 45-minute drive from Marrakech over a 10-hour journey south. A comprehensive primer on the mineral plateau redefining Moroccan desert travel.</p>
            <div class="cover-story__footer">
              <span class="cover-story__author">Marragafay Editorial · August 2026</span>
              <span class="cover-story__cta">Read Full Story →</span>
            </div>
          </div>
        </a>
      </div>
    </section>

    <!-- 2. ASYMMETRIC STORY DUO -->
    <section class="journal-section-wrap" style="padding-top: 30px; padding-bottom: 30px;">
      <div class="journal-section">
        <div class="editorial-header">
          <div class="editorial-header__left">
            <span class="editorial-header__num">02 /</span>
            <h2 class="editorial-header__title">Curator’s Selection</h2>
          </div>
          <span class="editorial-header__sub">Encounters & Traditions</span>
        </div>

        <div class="story-duo">
          <!-- Story 1 (Tall / Dominant) -->
          <a href="agafay-camel-ride.html" class="story-card-tall" data-category="experience">
            <div class="story-card-tall__media">
              <img src="/images/Slider-images/slider-3.webp" alt="Sunset Camel Ride in Agafay" loading="lazy" decoding="async" />
            </div>
            <div class="story-card-tall__body">
              <span class="story-card-tall__tag">Experience</span>
              <h3 class="story-card-tall__title">Sunset Camel Ride in Agafay: What to Expect (An Honest Account)</h3>
              <p class="story-card-tall__excerpt">The silence before sunset in the desert is not empty — it is full. Our field guide on what every traveler should understand before mounting the camel for an authentic sunset crossing.</p>
              <div class="story-card-tall__footer">
                <span>August 2026 · 5 min read</span>
                <span style="font-weight: 700; color: #523225;">Read Story →</span>
              </div>
            </div>
          </a>

          <!-- Story 2 (Stacked / Cultural Depth) -->
          <a href="berber-culture-agafay.html" class="story-card-stacked" data-category="culture">
            <div class="story-card-stacked__media">
              <img src="/images/Slider-images/slider-4.webp" alt="Berber heritage and culture in Agafay" loading="lazy" decoding="async" />
            </div>
            <div class="story-card-stacked__body">
              <span class="story-card-stacked__tag">Culture & Heritage</span>
              <h3 class="story-card-stacked__title">Berber Heritage and the Agafay: A Culture That Predates Tourism</h3>
              <p class="story-card-stacked__excerpt">Long before modern desert camps arrived, the stone hills of Agafay sustained Berber communities whose dry-stone architecture and hospitality rituals survive intact.</p>
              <div class="story-card-stacked__footer">
                <span>July 2026 · 6 min read</span>
                <span style="font-weight: 700; color: #523225;">Read Story →</span>
              </div>
            </div>
          </a>
        </div>
      </div>
    </section>

    <!-- 3. ATMOSPHERIC EDITORIAL INTERLUDE -->
    <section class="journal-section-wrap" style="padding-top: 20px; padding-bottom: 20px;">
      <div class="journal-section">
        <div class="quote-interlude">
          <div class="quote-interlude__inner">
            <span class="quote-interlude__eyebrow">Agafay Field Philosophy</span>
            <p class="quote-interlude__text">“The stone desert is not empty — it is vast, silent, and ancient. A forty-five minute drive that feels like a quiet departure from time itself.”</p>
            <span class="quote-interlude__author">Marragafay Field Notes · Marrakech</span>
          </div>
        </div>
      </div>
    </section>

    <!-- 4. FIELD DISPATCHES GRID -->
    <section class="journal-section-wrap" style="padding-top: 30px;">
      <div class="journal-section">
        <div class="editorial-header">
          <div class="editorial-header__left">
            <span class="editorial-header__num">03 /</span>
            <h2 class="editorial-header__title">Field Dispatches</h2>
          </div>
          <span class="editorial-header__sub">Guides, Routes & Gastronomy</span>
        </div>

        <div class="field-grid" id="article-grid">
          <!-- Card 1 -->
          <a href="marrakech-to-agafay.html" class="field-card" data-category="travel-tips">
            <div class="field-card__media">
              <img src="/images/gallery/gal1.webp" alt="Route from Marrakech to Agafay Desert" loading="lazy" decoding="async" />
            </div>
            <div class="field-card__body">
              <div class="field-card__tag-row">
                <span class="field-card__tag">Travel Logistics</span>
                <span class="field-card__num">01</span>
              </div>
              <h3 class="field-card__title">Marrakech to Agafay Desert: Every Way to Get There</h3>
              <p class="field-card__excerpt">From private transfers to scenic backcountry roads, the 45-kilometer journey separates the bustling medina from absolute stillness. Full cost and timing breakdown.</p>
              <div class="field-card__footer">
                <span>July 2026 · 4 min read</span>
                <span class="field-card__arrow">Read →</span>
              </div>
            </div>
          </a>

          <!-- Card 2 -->
          <a href="agafay-dinner-experience.html" class="field-card" data-category="experience">
            <div class="field-card__media">
              <img src="/images/activites/show.webp" alt="Agafay dinner under the stars" loading="lazy" decoding="async" />
            </div>
            <div class="field-card__body">
              <div class="field-card__tag-row">
                <span class="field-card__tag">Night Experiences</span>
                <span class="field-card__num">02</span>
              </div>
              <h3 class="field-card__title">The Agafay Dinner Experience: Luxury Under a Moroccan Sky</h3>
              <p class="field-card__excerpt">How a candlelit desert dinner became Marragafay’s most coveted evening ritual — and the subtle gastronomic details that make it unforgettable.</p>
              <div class="field-card__footer">
                <span>June 2026 · 7 min read</span>
                <span class="field-card__arrow">Read →</span>
              </div>
            </div>
          </a>

          <!-- Card 3 -->
          <a href="agafay-quad-biking-guide.html" class="field-card" data-category="experience">
            <div class="field-card__media">
              <img src="/images/activites/quad.webp" alt="Quad biking in Agafay Desert" loading="lazy" decoding="async" />
            </div>
            <div class="field-card__body">
              <div class="field-card__tag-row">
                <span class="field-card__tag">Adventure Trails</span>
                <span class="field-card__num">03</span>
              </div>
              <h3 class="field-card__title">Quad Biking in Agafay Desert: Safety, Tips & What You'll See</h3>
              <p class="field-card__excerpt">Everything you need to know about navigating high-performance 4x4 machines across Morocco’s most exhilarating stone canyons and panoramic ridges.</p>
              <div class="field-card__footer">
                <span>August 2026 · 6 min read</span>
                <span class="field-card__arrow">Read →</span>
              </div>
            </div>
          </a>
        </div>

        <div class="no-results" id="no-results" style="text-align: center; padding: 60px 20px; color: #7a756e; display: none;">
          No articles found in this category. More stories coming soon.
        </div>
      </div>
    </section>"""

# Replace in content:
# 1. Replace CSS from /* Sections */ down to .newsletter-wrap
css_cut_pattern = re.compile(r'/\*\s*Sections\s*\*/.*?/\*\s*Newsletter Section', re.DOTALL)
content = css_cut_pattern.sub(new_middle_css + "\n\n    /* Newsletter Section", content)

# 2. Replace HTML from <!-- FEATURED ARTICLE --> down to <!-- NEWSLETTER -->
html_cut_pattern = re.compile(r'<!-- FEATURED ARTICLE -->.*?<!-- NEWSLETTER -->', re.DOTALL)
content = html_cut_pattern.sub(new_middle_html + "\n\n    <!-- NEWSLETTER -->", content)

# 3. Update Category Filter JS so it filters across all cards gracefully
js_filter_code = """  // Category Filter Functionality
  document.addEventListener('DOMContentLoaded', function() {
    var pills = document.querySelectorAll('.category-pill');
    var items = document.querySelectorAll('[data-category]');
    var noResults = document.getElementById('no-results');

    pills.forEach(function(pill) {
      pill.addEventListener('click', function() {
        pills.forEach(function(p) { p.classList.remove('active'); p.setAttribute('aria-pressed', 'false'); });
        this.classList.add('active');
        this.setAttribute('aria-pressed', 'true');
        var filter = this.getAttribute('data-filter');

        var visibleCount = 0;
        items.forEach(function(item) {
          if (filter === 'all' || item.getAttribute('data-category') === filter) {
            item.style.display = '';
            visibleCount++;
          } else {
            item.style.display = 'none';
          }
        });

        if (noResults) {
          noResults.style.display = (visibleCount === 0) ? 'block' : 'none';
        }
      });
    });
  });"""

content = re.sub(r'// Category Filter Functionality.*?</script>', js_filter_code + '\n</script>', content, flags=re.DOTALL)

with open("en/blog/index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Built editorial masterpiece for en/blog/index.html!")
