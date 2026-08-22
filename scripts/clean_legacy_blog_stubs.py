for lang in ["en", "fr", "es", "ar"]:
    # Update lang/blog.html to redirect to /lang/blog/
    with open(f"{lang}/blog.html", "w", encoding="utf-8") as f:
        f.write(f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Marragafay The Journal</title>
  <meta http-equiv="refresh" content="0; url=/{lang}/blog/">
  <link rel="canonical" href="https://marragafay.com/{lang}/blog">
</head>
<body>
  <p>Redirecting to <a href="/{lang}/blog/">The Journal</a>...</p>
</body>
</html>""")

    # Update lang/blog-single.html to redirect to /lang/blog/
    with open(f"{lang}/blog-single.html", "w", encoding="utf-8") as f:
        f.write(f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Marragafay The Journal</title>
  <meta http-equiv="refresh" content="0; url=/{lang}/blog/">
  <link rel="canonical" href="https://marragafay.com/{lang}/blog">
</head>
<body>
  <p>Redirecting to <a href="/{lang}/blog/">The Journal</a>...</p>
</body>
</html>""")

# Root blog-single.html
with open("blog-single.html", "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Marragafay The Journal</title>
  <meta http-equiv="refresh" content="0; url=/en/blog/">
  <link rel="canonical" href="https://marragafay.com/en/blog">
</head>
<body>
  <p>Redirecting to <a href="/en/blog/">The Journal</a>...</p>
</body>
</html>""")

print("Cleaned legacy blog stubs and set clean redirects.")
