import re
import glob
import os

files = glob.glob("**/*.html", recursive=True)
print(f"Auditing {len(files)} HTML files against configured integrity rules...")

issues = []

banned_patterns = [
    (r"4\.9\s*/\s*5", "Found unsupported aggregate rating"),
    (r"(?:500\+|more than 500|más de 500|أكثر من 500)\s*(?:reviews|avis|reseñas|تعليق|تقييم)", "Found unsupported review count"),
    (r"\b10k\+", "Found unsupported audience counter"),
    (r"(?:limited daily capacity|capacité journalière limitée|aforo diario limitado|القدرة اليومية محدودة)", "Found unverified scarcity claim"),
    (r"(?:best rate guaranteed|meilleur tarif garanti|mejor tarifa garantizada|أفضل سعر مضمون)", "Found unverified best-rate guarantee"),
    (r"\b48\s*(?:hours|heures|horas|ساعة)", "Found cancellation window conflicting with the 24-hour policy"),
    (r"every camel experience is strictly private", "Found unconditional private-camel claim"),
    (r"all transfers are (?:fully )?private", "Found unconditional private-transfer claim"),
    (r"const\s+baseReviews\s*=", "Found seeded review data"),
    (r"verified feedback and authentic testimonials", "Found unsupported verification claim"),
    (r"(?:unfiltered words from real guests|mots non filtrés de vrais invités|palabras sin filtrar de invitados reales|كلمات لم تتم تصفيتها من ضيوف حقيقيين)", "Found unsupported review-authenticity claim"),
    (r"(?:Signature and Luxury packages are never shared|forfaits Signature et Luxe ne sont jamais partagés|paquetes Signature y Luxury nunca se comparten|الباقات المميزة والرفاهية أبدًا)", "Found Signature privacy claim conflicting with the shared offer"),
    (r"<!-- Reviews Section -->", "Found hard-coded review section without source provenance"),
    (r"\b(?:Book Now|Book now|Réservez maintenant|Reserva ahora|احجز الآن)\b", "Found immediate-booking CTA on an availability-request flow"),
    (r"\b(?:Discovery Pack|Signature Pack|Luxury Pack)\b", "Found legacy package branding name"),
]

for fpath in files:
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Check fake numbers
    if "612 345 678" in content or "612345678" in content:
        issues.append((fpath, "Found fake phone number"))

    # Check wrong city alt
    if 'alt="Casablanca"' in content:
        issues.append((fpath, "Found alt='Casablanca'"))

    # Check brand typos
    if 'alt="Marragafy"' in content:
        issues.append((fpath, "Found alt='Marragafy'"))
    if '>MARRAGAFA.<' in content:
        issues.append((fpath, "Found >MARRAGAFA.<"))

    # Check placeholder example emails
    if "example.com" in content:
        issues.append((fpath, "Found example.com email"))

    # Check dead links in footer
    if 'href="#fleet"' in content or 'href="#events"' in content or 'href="#standard"' in content:
        issues.append((fpath, "Found dead # anchor in footer"))

    # Check contradictory review sentence
    if "We do not curate these" in content or "Nous ne les modifions pas" in content:
        issues.append((fpath, "Found contradictory review sentence"))

    for pattern, message in banned_patterns:
        if re.search(pattern, content, flags=re.IGNORECASE):
            issues.append((fpath, message))

    if re.search(r"</button>\s*(?:Check availability|Vérifier la disponibilité|Ver disponibilidad|تحقق من التوفر)\s*</button>", content):
        issues.append((fpath, "Found malformed duplicate booking button"))



if not issues:
    print("\nIntegrity audit passed: no configured violations found.")
else:
    print(f"\nFound {len(issues)} remaining issues:")
    for f, msg in issues:
        print(f"  {f}: {msg}")
