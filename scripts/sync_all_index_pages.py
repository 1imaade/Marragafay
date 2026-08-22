import re

for lang in ['fr', 'es', 'ar']:
    filepath = f"{lang}/blog/index.html"
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace duplicate image with gal1.webp
    content = content.replace('/images/destination-4.jpg', '/images/gallery/gal1.webp')
    content = content.replace('/images/Slider-images/slider-1.webp" alt="Route', '/images/gallery/gal1.webp" alt="Route')

    # Ensure pill form styling
    content = content.replace(
        '.newsletter-form { display: flex; gap: 0; max-width: 480px;',
        '.newsletter-form { display: flex; max-width: 520px; border-radius: 100px; padding: 4px 4px 4px 20px; align-items: center;'
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Synced: {filepath}")

print("All language index pages synchronized.")
