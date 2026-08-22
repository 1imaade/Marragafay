import os
import glob

files = glob.glob("en/blog/*.html") + glob.glob("fr/blog/*.html") + glob.glob("es/blog/*.html") + glob.glob("ar/blog/*.html")

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace destination-4.jpg with slider-4.webp or slider-1.webp
    if "/images/destination-4.jpg" in content:
        content = content.replace("/images/destination-4.jpg", "/images/Slider-images/slider-4.webp")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed images in: {filepath}")

print("All blog image references updated to valid webp assets.")
