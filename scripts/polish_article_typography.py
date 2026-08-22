import glob
import re

files = glob.glob("en/blog/*.html")

for filepath in files:
    if filepath.endswith("index.html"):
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Typography in CSS
    content = re.sub(
        r'\.article-body p\s*\{[^}]*\}',
        """.article-body p {
      font-size: 19px;
      line-height: 1.85;
      color: #272724;
      margin-bottom: 1.9em;
    }""",
        content
    )

    content = re.sub(
        r'\.article-body h2\s*\{[^}]*\}',
        """.article-body h2 {
      font-size: clamp(1.75rem, 3.2vw, 2.25rem);
      font-weight: 700;
      color: #272724;
      margin-top: 3.5rem;
      margin-bottom: 1.2rem;
      line-height: 1.2;
      letter-spacing: -0.02em;
    }""",
        content
    )

    content = re.sub(
        r'\.article-body h3\s*\{[^}]*\}',
        """.article-body h3 {
      font-size: 1.35rem;
      font-weight: 700;
      color: #523225;
      margin-top: 2.2rem;
      margin-bottom: 0.8rem;
      letter-spacing: -0.01em;
    }""",
        content
    )

    content = re.sub(
        r'\.article-body blockquote\s*\{[^}]*\}',
        """.article-body blockquote {
      border-left: 3.5px solid #523225;
      padding: 8px 0 8px 1.8rem;
      margin: 3rem 0;
      font-style: italic;
      font-size: 1.35rem;
      color: #523225;
      line-height: 1.6;
    }""",
        content
    )

    content = re.sub(
        r'\.article-body ul li\s*\{[^}]*\}',
        """.article-body ul li {
      font-size: 19px;
      line-height: 1.8;
      color: #272724;
      margin-bottom: 0.7em;
    }""",
        content
    )

    # 2. In-Article CTA box
    content = re.sub(
        r'\.article-cta-box\s*\{[^}]*\}',
        """.article-cta-box {
      background-color: #272724 !important;
      border-radius: 6px;
      padding: 52px 40px;
      margin: 3.5rem 0;
      text-align: center;
      box-sizing: border-box;
    }""",
        content
    )

    content = re.sub(
        r'\.article-cta-box h3\s*\{[^}]*\}',
        """.article-cta-box h3 {
      color: #F6F7EA !important;
      font-size: 1.6rem;
      font-weight: 700;
      margin-bottom: 14px;
      margin-top: 0;
      letter-spacing: -0.01em;
    }""",
        content
    )

    content = re.sub(
        r'\.article-cta-box p\s*\{[^}]*\}',
        """.article-cta-box p {
      color: rgba(246,247,234,0.8) !important;
      font-size: 16px;
      line-height: 1.65;
      margin-bottom: 28px;
      max-width: 600px;
      margin-left: auto;
      margin-right: auto;
    }""",
        content
    )

    content = re.sub(
        r'\.article-cta-btn\s*\{[^}]*\}',
        """.article-cta-btn {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background-color: #523225 !important;
      color: #F6F7EA !important;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      text-decoration: none;
      padding: 16px 36px;
      border-radius: 100px;
      transition: background 0.2s, transform 0.2s;
    }""",
        content
    )

    # 3. Related Cards styling
    content = re.sub(
        r'\.related-card\s*\{[^}]*\}',
        """.related-card {
      display: flex;
      flex-direction: column;
      text-decoration: none;
      color: inherit;
      border-radius: 4px;
      overflow: hidden;
      background: #EEF0E2;
      transition: transform 0.25s cubic-bezier(0.4,0,0.2,1);
    }""",
        content
    )

    # Replace any leftover destination-4.jpg
    content = content.replace("/images/destination-4.jpg", "/images/Slider-images/slider-4.webp")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Polished typography in: {filepath}")

print("All article pages polished.")
