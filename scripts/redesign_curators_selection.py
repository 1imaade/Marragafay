import re
import glob

css_to_replace_regex = r'/\*\s*─── FRAMELESS DUO ───\s*\*/.*?(?=\/\*\s*─── FRAMELESS QUOTE ───\s*\*/)'

new_css = """/* ─── FRAMELESS DUO (REFINED) ─── */
    .story-duo { 
      display: grid; 
      grid-template-columns: 1.15fr 0.85fr; /* Elegant asymmetry */
      gap: 80px; 
      align-items: start; /* Prevents stretching and awkward gaps! */
      margin-top: 24px;
    }

    .story-card {
      display: flex;
      flex-direction: column;
      text-decoration: none;
      color: inherit;
    }
    .story-card:hover { text-decoration: none; color: inherit; }

    /* The left card (larger) */
    .story-card--primary .story-card__media {
      aspect-ratio: 4/5;
      margin-bottom: 32px;
    }
    .story-card--primary .story-card__title {
      font-size: clamp(2rem, 3vw, 2.4rem);
      line-height: 1.1;
    }

    /* The right card (smaller, pushed down for staggered editorial look) */
    .story-card--secondary {
      margin-top: 160px; /* Stagger effect */
    }
    .story-card--secondary .story-card__media {
      aspect-ratio: 4/3;
      margin-bottom: 28px;
    }
    .story-card--secondary .story-card__title {
      font-size: clamp(1.6rem, 2vw, 1.8rem);
      line-height: 1.15;
    }

    .story-card__media {
      overflow: hidden;
      position: relative;
    }
    .story-card__media img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.8s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .story-card:hover .story-card__media img {
      transform: scale(1.03);
    }

    .story-card__tag {
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: #523225;
      margin-bottom: 16px;
      display: block;
    }

    .story-card__title {
      font-weight: 700;
      letter-spacing: -0.02em;
      color: #272724;
      margin: 0 0 16px;
      font-family: 'Clash Grotesk', sans-serif;
    }

    .story-card__excerpt {
      font-size: 1.1rem;
      line-height: 1.65;
      color: #4e4e48;
      margin: 0 0 32px;
    }

    .story-card__footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-top: 18px;
      border-top: 1px solid rgba(39, 39, 36, 0.15);
      font-size: 12.5px;
      font-weight: 500;
      color: #7a756e;
    }
    .story-card__read {
      font-weight: 700;
      color: #272724;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      transition: color 0.2s;
    }
    .story-card:hover .story-card__read {
      color: #523225;
    }

    @media (max-width: 1024px) {
      .story-duo { grid-template-columns: 1fr; gap: 60px; }
      .story-card--secondary { margin-top: 0; }
      .story-card--primary .story-card__media { aspect-ratio: 16/10; }
    }
    
    """

# We also need to rewrite the HTML for the story-duo block.
# We will match the entire <div class="story-duo"> ... </div> block and replace it.

for filepath in glob.glob("*/blog/index.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace CSS
    content = re.sub(css_to_replace_regex, new_css, content, flags=re.DOTALL)

    # Replace HTML
    # Note: We need to parse out the translated text so we don't lose it!
    # Let's extract the translated text from the existing HTML.
    
    # Left card extraction
    left_match = re.search(r'<a href="agafay-camel-ride.html".*?</a>', content, flags=re.DOTALL)
    right_match = re.search(r'<a href="berber-culture-agafay.html".*?</a>', content, flags=re.DOTALL)
    
    if left_match and right_match:
        left_html = left_match.group(0)
        right_html = right_match.group(0)
        
        l_tag = re.search(r'<span class="story-card-tall__tag">(.*?)</span>', left_html).group(1)
        l_title = re.search(r'<h3 class="story-card-tall__title">(.*?)</h3>', left_html).group(1)
        l_excerpt = re.search(r'<p class="story-card-tall__excerpt">(.*?)</p>', left_html).group(1)
        l_meta_date = re.search(r'<span>(.*?·.*?read|.*?·.*?min|.*?·.*?)</span>', left_html)
        if l_meta_date: l_meta_date = l_meta_date.group(1)
        else: l_meta_date = "August 2026 · 5 min read" # fallback
        l_meta_read = re.search(r'<span style=".*?">(.*?)</span>', left_html).group(1)
        
        r_tag = re.search(r'<span class="story-card-stacked__tag">(.*?)</span>', right_html).group(1)
        r_title = re.search(r'<h3 class="story-card-stacked__title">(.*?)</h3>', right_html).group(1)
        r_excerpt = re.search(r'<p class="story-card-stacked__excerpt">(.*?)</p>', right_html).group(1)
        r_meta_date = re.search(r'<span>(.*?·.*?read|.*?·.*?min|.*?·.*?)</span>', right_html)
        if r_meta_date: r_meta_date = r_meta_date.group(1)
        else: r_meta_date = "July 2026 · 6 min read" # fallback
        r_meta_read = re.search(r'<span style=".*?">(.*?)</span>', right_html).group(1)

        new_duo_html = f"""<div class="story-duo">
          <a href="agafay-camel-ride.html" class="story-card story-card--primary" data-category="experience">
            <div class="story-card__media">
              <img src="/images/Slider-images/slider-3.webp" alt="Sunset Camel Ride in Agafay" loading="lazy" decoding="async" />
            </div>
            <span class="story-card__tag">{l_tag}</span>
            <h3 class="story-card__title">{l_title}</h3>
            <p class="story-card__excerpt">{l_excerpt}</p>
            <div class="story-card__footer">
              <span>{l_meta_date}</span>
              <span class="story-card__read">{l_meta_read}</span>
            </div>
          </a>

          <a href="berber-culture-agafay.html" class="story-card story-card--secondary" data-category="culture">
            <div class="story-card__media">
              <img src="/images/Slider-images/slider-4.webp" alt="Berber heritage and culture in Agafay" loading="lazy" decoding="async" />
            </div>
            <span class="story-card__tag">{r_tag}</span>
            <h3 class="story-card__title">{r_title}</h3>
            <p class="story-card__excerpt">{r_excerpt}</p>
            <div class="story-card__footer">
              <span>{r_meta_date}</span>
              <span class="story-card__read">{r_meta_read}</span>
            </div>
          </a>
        </div>"""

        content = re.sub(r'<div class="story-duo">.*?</div>\s*</section>', new_duo_html + '\n      </div>\n    </section>', content, flags=re.DOTALL)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully redesigned Curator's Selection in {filepath}")
    else:
        print(f"Could not parse HTML in {filepath}")

