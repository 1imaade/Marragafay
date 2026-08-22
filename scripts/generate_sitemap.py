import os
from generate_all_multilingual_articles import articles_meta

languages = ["en", "fr", "es", "ar"]
article_slugs = list(articles_meta.keys())

sitemap_entries = []

# Header
sitemap_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">

  <!-- Core Pages -->
  <url>
    <loc>https://marragafay.com/</loc>
    <lastmod>2026-08-22</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://marragafay.com/activities</loc>
    <lastmod>2026-08-22</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://marragafay.com/packs</loc>
    <lastmod>2026-08-22</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://marragafay.com/about</loc>
    <lastmod>2026-08-22</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://marragafay.com/reviews</loc>
    <lastmod>2026-08-22</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://marragafay.com/contact</loc>
    <lastmod>2026-08-22</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>

  <!-- Journal Index Pages (Multilingual Cluster) -->
'''

for lang in languages:
    sitemap_xml += f'''  <url>
    <loc>https://marragafay.com/{lang}/blog</loc>
    <lastmod>2026-08-22</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.85</priority>
    <xhtml:link rel="alternate" hreflang="en" href="https://marragafay.com/en/blog" />
    <xhtml:link rel="alternate" hreflang="fr" href="https://marragafay.com/fr/blog" />
    <xhtml:link rel="alternate" hreflang="es" href="https://marragafay.com/es/blog" />
    <xhtml:link rel="alternate" hreflang="ar" href="https://marragafay.com/ar/blog" />
    <xhtml:link rel="alternate" hreflang="x-default" href="https://marragafay.com/en/blog" />
  </url>
'''

sitemap_xml += '\n  <!-- Individual Journal Articles (Multilingual Cluster) -->\n'

for filename, meta in articles_meta.items():
    slug = meta["slug"]
    for lang in languages:
        sitemap_xml += f'''  <url>
    <loc>https://marragafay.com/{lang}/blog/{slug}</loc>
    <lastmod>2026-08-22</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.75</priority>
    <xhtml:link rel="alternate" hreflang="en" href="https://marragafay.com/en/blog/{slug}" />
    <xhtml:link rel="alternate" hreflang="fr" href="https://marragafay.com/fr/blog/{slug}" />
    <xhtml:link rel="alternate" hreflang="es" href="https://marragafay.com/es/blog/{slug}" />
    <xhtml:link rel="alternate" hreflang="ar" href="https://marragafay.com/ar/blog/{slug}" />
    <xhtml:link rel="alternate" hreflang="x-default" href="https://marragafay.com/en/blog/{slug}" />
  </url>
'''

sitemap_xml += '</urlset>\n'

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_xml)

print("Generated comprehensive multilingual sitemap.xml with 32 blog URLs!")
