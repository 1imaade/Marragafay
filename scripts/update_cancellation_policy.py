import re

cancellation_data = {
    "en": {
        "badge": "Booking & Cancellation Terms",
        "title": "cancellation policy.",
        "subtitle": "No upfront payment required. 100% pay on-site after your experience, with flexible courtesy cancellation.",
        "overview_label": "Overview",
        "overview_title": "zero deposit. total trust.",
        "overview_desc": "At Marragafay, we never charge advance deposits or require credit card prepayments online. You pay on-site only after you have fully enjoyed your desert experience. All we ask in return is simple courtesy: if your plans change or you decide not to proceed with an activity, please notify us as early as possible so we can release our private drivers, guides, and desert camps.",
        "concierge_title": "Concierge Desk",
        "concierge_desc": "Need to cancel, change your pickup time, or switch activities? Send us a quick WhatsApp message.",
        "concierge_btn": "Chat on WhatsApp ↗",
        "points": [
            {
                "num": "01 · Pay On-Site After the Experience",
                "title": "No Advance Payment or Deposit",
                "desc": "Your reservation is fully confirmed without any credit card prepayment or advance deposit. Payment is made directly on-site (in cash or by card) after your desert activity, dinner, or tour has concluded."
            },
            {
                "num": "02 · Changing Your Mind or Cancelling",
                "title": "Simple Courtesy Notification",
                "desc": "If you change your mind, want to cancel, or decide not to participate in an activity, there are never any fees or penalties. We simply ask that you message or call our concierge team as soon as possible so we can adjust our schedule and cancel your private vehicle dispatch."
            },
            {
                "num": "03 · Date & Time Adjustments",
                "title": "Free Flexible Rescheduling",
                "desc": "Feel free to adjust your departure time, add or remove guests, or switch to another day. Just message us on WhatsApp (+212 672-531624), and we will update your booking instantly with zero hassle."
            },
            {
                "num": "04 · Weather & Safety Guarantee",
                "title": "Weather Protection Policy",
                "desc": "Desert experiences depend on outdoor conditions. If severe wind, rain, or heat makes an activity uncomfortable or unsafe, we will happily reschedule to another date or cancel your booking with zero obligation."
            }
        ]
    },
    "fr": {
        "badge": "Conditions de Réservation & Annulation",
        "title": "politique d'annulation.",
        "subtitle": "Aucun paiement à l'avance. Paiement sur place à la fin de votre expérience et annulation flexible sur simple préavis.",
        "overview_label": "Aperçu",
        "overview_title": "zéro acompte. confiance totale.",
        "overview_desc": "Chez Marragafay, nous ne demandons aucun paiement anticipé ni caution par carte bancaire. Vous réglez directement sur place, uniquement après avoir pleinement profité de votre expérience. Tout ce que nous vous demandons en retour est une simple courtoisie : si vos projets changent ou si vous décidez de ne pas faire une activité, merci de nous prévenir au plus tôt afin de libérer nos chauffeurs privés, guides et campements.",
        "concierge_title": "Conciergerie Dédiée",
        "concierge_desc": "Vous souhaitez annuler, décaler votre heure ou changer d'activité ? Envoyez-nous un simple message WhatsApp.",
        "concierge_btn": "Discuter sur WhatsApp ↗",
        "points": [
            {
                "num": "01 · Paiement sur Place après l'Expérience",
                "title": "Aucun Prépaiement ni Caution",
                "desc": "Votre réservation est confirmée sans aucun paiement préalable par carte bancaire. Le règlement s'effectue directement sur place (en espèces ou par carte) une fois votre activité, dîner ou excursion terminé."
            },
            {
                "num": "02 · Changement d'Avis ou Annulation",
                "title": "Simple Notification de Courtoisie",
                "desc": "Si vous changez d'avis, souhaitez annuler ou ne plus participer à une activité, aucun frais ni pénalité ne vous sera facturé. Nous vous demandons simplement de contacter notre conciergerie dès que possible afin d'annuler le départ du véhicule privé."
            },
            {
                "num": "03 · Ajustement de Date et d'Horaire",
                "title": "Modification Gratuite et Souple",
                "desc": "Vous pouvez facilement ajuster votre heure de prise en charge, ajouter des participants ou changer de date. Écrivez-nous sur WhatsApp (+212 672-531624), nous mettrons à jour votre planning instantanément."
            },
            {
                "num": "04 · Météo et Sécurité",
                "title": "Garantie Conditions Météo",
                "desc": "Les expériences dans le désert dépendent du climat. En cas de vent violent, pluie ou chaleur excessive rendant l'activité inconfortable, nous reportons ou annulons votre réservation sans aucun engagement de votre part."
            }
        ]
    },
    "es": {
        "badge": "Términos de Reserva y Cancelación",
        "title": "política de cancelación.",
        "subtitle": "Sin pagos por adelantado. Pago 100% en el lugar tras finalizar la experiencia y cancelación flexible con solo avisarnos.",
        "overview_label": "Resumen",
        "overview_title": "cero anticipos. total confianza.",
        "overview_desc": "En Marragafay nunca solicitamos depósitos por adelantado ni cobros previos con tarjeta de crédito. El pago se realiza directamente en el lugar una vez concluida su experiencia en el desierto. Todo lo que pedimos a cambio es simple cortesía: si sus planes cambian o decide no realizar la actividad, por favor infórmenos con la mayor antelación posible para liberar a nuestros conductores privados, guías y campamentos.",
        "concierge_title": "Mesa de Conserjería",
        "concierge_desc": "¿Necesita cancelar, cambiar la hora de recogida o elegir otra actividad? Escríbanos rápidamente por WhatsApp.",
        "concierge_btn": "Escribir por WhatsApp ↗",
        "points": [
            {
                "num": "01 · Pago en el Lugar al Finalizar",
                "title": "Sin Depósitos ni Pagos Previos",
                "desc": "Su reserva queda totalmente confirmada sin necesidad de pagar por anticipado. El pago se efectúa directamente en el lugar (en efectivo o con tarjeta) después de haber disfrutado de su actividad, cena o recorrido."
            },
            {
                "num": "02 · Cambio de Planes o Cancelación",
                "title": "Aviso de Cortesía sin Penalización",
                "desc": "Si cambia de opinión, desea cancelar o decide no realizar alguna actividad, no aplicamos ningún cargo ni penalización. Tan solo le pedimos que nos avise por WhatsApp o teléfono cuanto antes para cancelar el vehículo privado asignado."
            },
            {
                "num": "03 · Cambio de Horarios y Fechas",
                "title": "Reprogramación Fácil y Gratuita",
                "desc": "Puede cambiar su hora de salida, añadir invitados o posponer la actividad a otro día sin complicaciones. Solo envíenos un mensaje al +212 672-531624 y actualizaremos su reserva al instante."
            },
            {
                "num": "04 · Clima y Seguridad",
                "title": "Garantía por Condiciones Climáticas",
                "desc": "Las actividades en el desierto dependen del clima. Si el viento fuerte, la lluvia o condiciones adversas impiden disfrutar la experiencia con comodidad, reprogramamos o cancelamos su reserva sin ningún compromiso."
            }
        ]
    },
    "ar": {
        "badge": "شروط الحجز والإلغاء",
        "title": "سياسة الإلغاء.",
        "subtitle": "بدون أي دفع مسبق. الدفع يتم في الموقع بعد نهاية تجربتكم، مع مرونة تامة في الإلغاء بمجرد إشعارنا.",
        "overview_label": "نظرة عامة",
        "overview_title": "بدون عربون. ثقة تامة ومتبادلة.",
        "overview_desc": "في مراكافاي، لا نطلب أي دفع مسبق أو اقتطاع بنكي عبر الإنترنت. يتم الدفع مباشرة في عين المكان بعد انتهاء تجربتكم الصحراوية واستمتاعكم الكامل بها. كل ما نرجوه منكم هو مجرد إشعارنا في حال تغيّرت خططكم أو قررتم عدم القيام بالنشاط، حتى نتمكن من تحرير السائق الخاص والمرشدين والمخيمات المخصصة لكم.",
        "concierge_title": "خدمة الكونسيرج الخاصة",
        "concierge_desc": "هل ترغب في الإلغاء، تعديل موعد الانطلاق، أو تغيير نوع النشاط؟ أرسل لنا رسالة سريعة عبر واتساب.",
        "concierge_btn": "تواصل عبر واتساب ↗",
        "points": [
            {
                "num": "٠١ · الدفع في الموقع بعد نهاية التجربة",
                "title": "بدون دفع مسبق أو عربون",
                "desc": "حجزكم مؤكد بالكامل دون الحاجة لأي دفع مسبق عبر البطاقة البنكية. يتم سداد المبلغ مباشرة في الموقع (نقداً أو بالبطاقة) بعد اكتمال نشاطكم الصحراوي أو وجبة العشاء."
            },
            {
                "num": "٠٢ · تغيير الخطط أو الإلغاء",
                "title": "إشعار بسيط بدون أي رسوم",
                "desc": "إذا قررتم إلغاء الحجز أو عدم القيام بالنشاط لأي سبب، فلا توجد أي غرامات أو رسوم إلغاء على الإطلاق. نرجو فقط إعلام فريقنا عبر واتساب أو الهاتف في أقرب وقت لإلغاء السيارة الخاصة الموجهة إليكم."
            },
            {
                "num": "٠٣ · مرونة تعديل المواعيد والتواريخ",
                "title": "تغيير الموعد بكل سهولة ومجاناً",
                "desc": "يمكنكم تعديل ساعة الانطلاق، إضافة أو تقليل عدد الضيوف، أو تأجيل التجربة ليوم آخر. تواصلوا معنا عبر واتساب (+212 672-531624) وسنقوم بتحديث الحجز فوراً."
            },
            {
                "num": "٠٤ · الأحوال الجوية والسلامة",
                "title": "ضمان الحماية والتقلبات الجوية",
                "desc": "تعتمد الأنشطة الخارجية على حالة الطقس. في حال وجود رياح قوية أو أمطار قد تؤثر على راحتكم، سنقوم بتأجيل النشاط أو إلغائه بكل سرور دون أي التزام من طرفكم."
            }
        ]
    }
}

for lang in ["en", "fr", "es", "ar"]:
    fpath = f"{lang}/cancellation.html"
    d = cancellation_data[lang]
    is_rtl = (lang == "ar")
    
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update Hero section
    # Replace badge, title, subtitle
    hero_pattern = r'(<!-- HERO SECTION -->.*?<!-- Badges -->\s*<div class="flex items-center gap-2 mb-6">\s*<span[^>]*>).*?(</span>\s*</div>\s*<!-- Title -->\s*<h1[^>]*>).*?(</h1>\s*<!-- Subtitle -->\s*<p[^>]*>).*?(</p>\s*</div>\s*</section>)'
    
    hero_replace = rf'\g<1>{d["badge"]}\g<2>{d["title"]}\g<3>{d["subtitle"]}\g<4>'
    html = re.sub(hero_pattern, hero_replace, html, flags=re.DOTALL)

    # 2. Build points HTML
    points_html = ""
    for pt in d["points"]:
        points_html += f"""
            <div class="border-b border-[#10100E]/10 pb-10 last:border-b-0">
              <span class="text-xs font-bold uppercase tracking-widest text-[#10100E]/50 mb-2 block">{pt['num']}</span>
              <h2 class="text-xl md:text-2xl font-semibold text-[#10100E] mb-3 tracking-tight lowercase" style="font-family: 'Clash Grotesk', sans-serif;">
                {pt['title']}
              </h2>
              <p class="text-[#10100E]/80 text-[15px] md:text-[16px] leading-[28px] font-normal m-0">
                {pt['desc']}
              </p>
            </div>"""

    # 3. Replace Policy Section Content
    policy_section_pattern = r'<!-- POLICY 2-COLUMN SECTION -->\s*<section class="w-full bg-\[#F6F7EA\] border-t border-\[#e2e0d3\] py-20 px-6 md:px-16"[^>]*>.*?</section>'
    
    new_policy_section = f"""<!-- POLICY 2-COLUMN SECTION -->
      <section class="w-full bg-[#F6F7EA] border-t border-[#e2e0d3] py-20 px-6 md:px-16" style="background-color: #F6F7EA !important;">
        <div class="max-w-7xl mx-auto">
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-16 lg:gap-24">

            <!-- LEFT COLUMN: Overview & Concierge Card (4 cols) -->
            <div class="lg:col-span-4 lg:sticky lg:top-32 self-start">
              <span class="text-xs font-bold uppercase tracking-widest text-[#10100E]/60 mb-2 block">{d['overview_label']}</span>
              <h2 class="text-[28px] md:text-[34px] font-semibold text-[#10100E] tracking-tight lowercase mb-4" style="font-family: 'Clash Grotesk', sans-serif;">
                {d['overview_title']}
              </h2>
              <p class="text-[#10100E]/70 text-[15px] leading-[26px] mb-8 font-normal">
                {d['overview_desc']}
              </p>

              <!-- Concierge Box -->
              <div class="p-6 bg-white border border-[#10100E]/10 rounded-2xl shadow-sm">
                <p class="text-xs font-bold uppercase tracking-widest text-[#10100E]/70 mb-2">{d['concierge_title']}</p>
                <p class="text-sm text-[#10100E]/80 mb-4">{d['concierge_desc']}</p>
                <a href="https://wa.me/212672531624" target="_blank" class="inline-block w-full text-center bg-[#523225] text-white px-5 py-3 text-xs font-semibold uppercase tracking-wider hover:bg-[#3d251b] transition-colors rounded-xl" style="text-decoration: none;">
                  {d['concierge_btn']}
                </a>
              </div>
            </div>

            <!-- RIGHT COLUMN: Detailed Policy Points (8 cols) -->
            <div class="lg:col-span-8 space-y-10">
              {points_html}
            </div>

          </div>
        </div>
      </section>"""

    html = re.sub(policy_section_pattern, new_policy_section, html, flags=re.DOTALL)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Updated cancellation policy for {fpath}")

print("\nCancellation policy pages successfully updated across all languages!")
