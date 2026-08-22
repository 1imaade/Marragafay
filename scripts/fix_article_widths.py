import glob
import re

files = glob.glob("en/blog/*.html")

for filepath in files:
    if filepath.endswith("index.html"):
        continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace width constraints in CSS
    # 1. Article Header: 1440px max-width, 32px padding
    content = re.sub(
        r'\.article-header\s*\{[^}]*\}',
        """.article-header {
      background-color: #F6F7EA;
      padding: 60px 32px 40px;
      max-width: 1440px;
      margin: 0 auto;
    }""",
        content
    )

    # 2. Article Header Rule
    content = re.sub(
        r'\.article-header-rule\s*\{[^}]*\}',
        """.article-header-rule {
      border: 0;
      border-top: 1px solid rgba(39,39,36,0.12);
      margin: 32px auto 0;
      max-width: 1440px;
      padding: 0 32px;
      box-sizing: border-box;
    }""",
        content
    )

    # 3. Article Headline & Subheadline
    content = re.sub(
        r'\.article-headline\s*\{[^}]*\}',
        """.article-headline {
      font-size: clamp(2.4rem, 5.2vw, 4rem);
      font-weight: 700;
      color: #272724;
      line-height: 1.08;
      letter-spacing: -0.025em;
      margin-bottom: 20px;
      margin-top: 0;
      max-width: 1100px;
    }""",
        content
    )

    content = re.sub(
        r'\.article-subheadline\s*\{[^}]*\}',
        """.article-subheadline {
      font-size: 1.25rem;
      font-weight: 400;
      color: #272724;
      opacity: 0.75;
      line-height: 1.6;
      margin-bottom: 32px;
      max-width: 850px;
    }""",
        content
    )

    # 4. Article Hero Image Container: 1440px max-width, 32px padding
    content = re.sub(
        r'\.article-hero\s*\{[^}]*\}',
        """.article-hero {
      width: 100%;
      max-width: 1440px;
      margin: 0 auto;
      padding: 40px 32px 0;
      box-sizing: border-box;
    }""",
        content
    )

    # 5. Article Body Wrap: 920px max-width, 32px padding
    content = re.sub(
        r'\.article-body-wrap\s*\{[^}]*\}',
        """.article-body-wrap {
      max-width: 920px;
      margin: 60px auto 0;
      padding: 0 32px;
      box-sizing: border-box;
    }""",
        content
    )

    # 6. Article Tags Wrap: 920px max-width, 32px padding
    content = re.sub(
        r'\.article-tags-wrap\s*\{[^}]*\}',
        """.article-tags-wrap {
      max-width: 920px;
      margin: 0 auto;
      padding: 40px 32px 60px;
      box-sizing: border-box;
    }""",
        content
    )

    # 7. Related Articles Section: 1440px max-width, 32px padding
    content = re.sub(
        r'\.related-articles-inner\s*\{[^}]*\}',
        """.related-articles-inner {
      max-width: 1440px;
      margin: 0 auto;
      padding: 0 32px;
      box-sizing: border-box;
    }""",
        content
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated container width in: {filepath}")

print("All article pages adjusted to match header 1440px alignment and 32px padding.")
