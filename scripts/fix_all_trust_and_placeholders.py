import re
import glob

html_files = sorted(glob.glob("**/*.html", recursive=True))
print(f"Processing {len(html_files)} HTML files for placeholder and contact fixes...")

for fpath in html_files:
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    orig = content

    # 1. Replace fake phone number +212 612 345 678 with real number +212 672-531624
    content = re.sub(r'\+212\s*612\s*345\s*678', '+212 672-531624', content)
    content = re.sub(r'\+212612345678', '+212672531624', content)

    # 2. Replace hello@marragafay.com with marragafay@gmail.com
    content = content.replace('hello@marragafay.com', 'marragafay@gmail.com')

    # 3. Fix alt="Casablanca" in desert hero images
    content = re.sub(r'alt=["\']Casablanca["\']', 'alt="Agafay Desert Marrakech"', content)

    # 4. Fix alt="Marragafy" typo
    content = re.sub(r'alt=["\']Marragafy["\']', 'alt="Marragafay"', content)

    # 5. Fix MARRAGAFA. French footer typo
    content = re.sub(r'>\s*MARRAGAFA\.\s*<', '>MARRAGAFAY.<', content)

    # 6. Fix placeholder emails
    content = content.replace('your.email@example.com', 'your.email@gmail.com')
    content = content.replace('placeholder="example@email.com"', 'placeholder="your.email@gmail.com"')

    # 7. Fix contradictory review sentence
    content = re.sub(
        r'We do not curate these\.\s*We select the reviews that most accurately describe what we built Marragafay to deliver\.',
        'Verified feedback and authentic testimonials from guests who explored the Agafay Desert with us.',
        content
    )
    content = re.sub(
        r'Nous ne les modifions pas\.\s*Nous sélectionnons les avis.*?\.',
        'Témoignages authentiques et avis vérifiés de voyageurs ayant vécu l\'expérience Agafay avec nous.',
        content
    )
    content = re.sub(
        r'No seleccionamos estos testimonios\.\s*Elegimos las opiniones.*?\.',
        'Opiniones auténticas y verificadas de viajeros que han vivido la experiencia de Agafay con nosotros.',
        content
    )
    content = re.sub(
        r'لا نقوم بتعديل هذه التقييمات\.\s*نختار التقييمات.*?\.',
        'آراء وتجارب حقيقية موثقة من ضيوفنا الذين عاشوا تجربة صحراء أكافاي معنا.',
        content
    )

    if content != orig:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated placeholders/brand/contact in {fpath}")

print("\nPlaceholder, brand, and contact fixes completed successfully!")
