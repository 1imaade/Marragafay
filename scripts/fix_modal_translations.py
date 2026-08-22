import re
import glob

files = glob.glob("**/*.html", recursive=True)

for fpath in files:
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()

    orig = html

    if fpath.startswith("fr/") or fpath.startswith("fr\\"):
        # Fix French modal translations
        html = html.replace('placeholder="Enter your full name"', 'placeholder="Votre nom complet"')
        html = html.replace('placeholder="Enter full name"', 'placeholder="Votre nom complet"')
        html = html.replace('title="Please enter a valid phone number (numbers, spaces, +, - only)"', 'title="Veuillez saisir un numéro valide"')
        html = html.replace('Courriel\n                  Adresse *', 'Adresse e-mail *')
        html = html.replace('Courriel Adresse *', 'Adresse e-mail *')
        html = html.replace('WhatsApp/Téléphone\n                  Numéro *', 'Numéro WhatsApp / Téléphone *')
        html = html.replace('WhatsApp/Téléphone Numéro *', 'Numéro WhatsApp / Téléphone *')
        html = html.replace('Préféré\n                  Date*', 'Date souhaitée *')
        html = html.replace('Préféré Date*', 'Date souhaitée *')
        html = html.replace('Groupe\n                  Taille *', 'Nombre de personnes *')
        html = html.replace('Groupe Taille *', 'Nombre de personnes *')
        html = html.replace('Exigences particulières / Demandes', 'Demandes particulières ou préférences')
        html = html.replace('Parlez-nous de toute restriction alimentaire, d\'occasions spéciales ou d\'exigences d\'accessibilité...', 'Précisez vos éventuelles demandes (régime alimentaire, occasion spéciale, horaire de prise en charge)...')

    elif fpath.startswith("es/") or fpath.startswith("es\\"):
        # Fix Spanish modal translations
        html = html.replace('placeholder="Enter your full name"', 'placeholder="Su nombre completo"')
        html = html.replace('placeholder="Enter full name"', 'placeholder="Su nombre completo"')
        html = html.replace('title="Please enter a valid phone number (numbers, spaces, +, - only)"', 'title="Por favor introduzca un número de teléfono válido"')
        html = html.replace('Correo\n                  Dirección *', 'Correo electrónico *')
        html = html.replace('Correo Dirección *', 'Correo electrónico *')
        html = html.replace('WhatsApp/Teléfono\n                  Número *', 'Número de WhatsApp / Teléfono *')
        html = html.replace('WhatsApp/Teléfono Número *', 'Número de WhatsApp / Teléfono *')
        html = html.replace('Preferido\n                  Fecha*', 'Fecha deseada *')
        html = html.replace('Preferido Fecha*', 'Fecha deseada *')
        html = html.replace('Grupo\n                  Tamaño *', 'Número de personas *')
        html = html.replace('Grupo Tamaño *', 'Número de personas *')
        html = html.replace('Requisitos Especiales / Peticiones', 'Peticiones o requerimientos especiales')
        html = html.replace('Cuéntenos sobre cualquier restricción dietética, ocasiones especiales o requisitos de accesibilidad...', 'Indíquenos cualquier preferencia especial (dieta, celebración, recogida en hotel)...')

    elif fpath.startswith("ar/") or fpath.startswith("ar\\"):
        # Fix Arabic modal translations
        html = html.replace('placeholder="Enter your full name"', 'placeholder="الاسم الكامل"')
        html = html.replace('placeholder="Enter full name"', 'placeholder="الاسم الكامل"')
        html = html.replace('title="Please enter a valid phone number (numbers, spaces, +, - only)"', 'title="يرجى إدخال رقم هاتف صحيح"')
        html = html.replace('البريد\n                  العنوان *', 'البريد الإلكتروني *')
        html = html.replace('البريد العنوان *', 'البريد الإلكتروني *')
        html = html.replace('واتساب/الهاتف\n                  الرقم *', 'رقم الواتساب / الهاتف *')
        html = html.replace('واتساب/الهاتف الرقم *', 'رقم الواتساب / الهاتف *')
        html = html.replace('المفضلة\n                  التاريخ*', 'التاريخ المفضل *')
        html = html.replace('المفضلة التاريخ*', 'التاريخ المفضل *')
        html = html.replace('المجموعة\n                  الحجم *', 'عدد الأشخاص *')
        html = html.replace('المجموعة الحجم *', 'عدد الأشخاص *')

    if html != orig:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Fixed modal translations in {fpath}")

print("Modal translations fixed across all languages!")
