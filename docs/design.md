---
version: alpha
name: Marragafay Modern
description: A warm, hospitality-forward system with bold orange accents, soft cream surfaces, and oversized editorial typography.
colors:
  primary: "#523225"
  secondary: "#272724"
  tertiary: "#f6f7ea"
  neutral: "#ffffff"
  surface: "#f6f7ea"
  on-surface: "#272724"
  muted: "#b8b5a6"
  overlay: "#00000099"
  border: "#d9d7ca"
  success: "#1f8a5b"
  error: "#d64545"
typography:
  headline-display:
    fontFamily: "Clash Display" #
    fontSize: "88px"
    fontWeight: 600
    lineHeight: "92px"
    letterSpacing: "-1.76px"
  headline-lg:
    fontFamily: "Lay Grotesk"
    fontSize: "48px"
    fontWeight: 600
    lineHeight: "48px"
    letterSpacing: "-0.96px"
  headline-md:
    fontFamily: "Lay Grotesk"
    fontSize: "30px"
    fontWeight: 600
    lineHeight: "36px"
    letterSpacing: "-0.6px"
  headline-sm:
    fontFamily: "Lay Grotesk"
    fontSize: "18px"
    fontWeight: 600
    lineHeight: "22px"
    letterSpacing: "0px"
  body-lg:
    fontFamily: "Lay Grotesk"
    fontSize: "18px"
    fontWeight: 400
    lineHeight: "28px"
    letterSpacing: "0px"
  body-md:
    fontFamily: "Lay Grotesk"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: "24px"
    letterSpacing: "0px"
  body-sm:
    fontFamily: "Lay Grotesk"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: "20px"
    letterSpacing: "0px"
  label-lg:
    fontFamily: "Lay Grotesk"
    fontSize: "16px"
    fontWeight: 600
    lineHeight: "20px"
    letterSpacing: "0px"
  label-md:
    fontFamily: "Lay Grotesk"
    fontSize: "14px"
    fontWeight: 600
    lineHeight: "18px"
    letterSpacing: "0px"
  label-sm:
    fontFamily: "Lay Grotesk"
    fontSize: "12px"
    fontWeight: 500
    lineHeight: "16px"
    letterSpacing: "0px"
  nav-md:
    fontFamily: "Lay Grotesk"
    fontSize: "14px"
    fontWeight: 600
    lineHeight: "18px"
    letterSpacing: "0px"
  caption-sm:
    fontFamily: "Lay Grotesk"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: "16px"
    letterSpacing: "0px"
rounded:
  none: 0px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 28px
  full: 9999px
spacing:
  xs: 8px
  sm: 16px
  md: 28px
  lg: 40px
  xl: 64px
  gutter: 24px
  section: 96px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.tertiary}"
    typography: "{typography.label-lg}"
    rounded: "{rounded.full}"
    padding: "16px 40px"
    height: "56px"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.label-lg}"
    rounded: "{rounded.full}"
    padding: "16px 40px"
    height: "56px"
  button-link:
    backgroundColor: "transparent"
    textColor: "{colors.tertiary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "0px"
  card:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: "28px"
  input:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "16px 20px"
    height: "56px"
  chip:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: "8px 12px"
---

# StayHere Modern

## Overview
StayHere feels like a contemporary hospitality brand: welcoming, premium, and easy to trust. The visual tone is warm rather than stark, with a creamy base, bright citrus-orange actions, and large editorial headlines that give the interface a confident, destination-led personality. The layout is spacious and image-forward, with a strong sense of motion and discovery rather than dense information display.

## Colors
- **Primary (#523225):** A deep, rich desert brown (leather/earth tone) used for the brand mark, key calls to action, and the strongest moments of emphasis. It anchors the interface in the natural Agafay environment, providing a premium, organic contrast against the soft cream background without feeling loud or cheap.
- **Secondary (#272724):** A deep charcoal used for navigation, body copy, and readable UI text where the design needs structure and clarity.
- **Tertiary (#f6f7ea):** A warm cream that acts as the dominant surface color and gives the site its relaxed, sunlit hospitality feel.
- **Neutral (#ffffff):** Clean white for inputs, elevated panels, and small UI surfaces that need crisp separation.
- **Surface (#f6f7ea):** The main page and card surface tone, reinforcing the brand’s soft, natural atmosphere.
- **On-surface (#272724):** Primary text and icon color on light surfaces; use it for contrast-critical content.
- **Muted (#b8b5a6):** A subdued beige-gray for helper text, metadata, and secondary interface details.
- **Overlay (#00000099):** A translucent dark layer used over photography to preserve text legibility without hiding the hero image.
- **Border (#d9d7ca):** A gentle line color for dividing form fields and supporting UI without introducing a harsh frame.
- **Success (#1f8a5b):** A restrained green for positive states and confirmations when needed.
- **Error (#d64545):** A clear red for validation and error messaging.

## Typography
The system is anchored by **Lay Grotesk**, a modern grotesk with a polished but friendly character. Headlines use strong weights and tight negative letter spacing, creating the large editorial feel seen in the hero; body text stays lighter and highly readable. Inter can be used as a fallback when necessary, but the primary voice should remain consistent with Lay Grotesk.

- **Headline display and large headlines:** Use for hero statements and major section titles. These sizes are intentionally oversized and compact, with the display style carrying the strongest brand personality.
- **Headline medium and small:** Use for card titles, page subsections, and compact editorial moments. These should remain semibold and visually crisp.
- **Body text:** Keep copy calm, readable, and minimally decorated. The source uses a modest line height and avoids dense blocks of text.
- **Labels and navigation:** Use semibold labels for buttons, form triggers, and nav items. The interface favors clear, direct wording over decorative styling.
- **Letter spacing:** Headlines use slight negative tracking for a tight, premium feel; labels and body copy stay at normal spacing.
- **Uppercase conventions:** The screenshot does not rely on aggressive all-caps styling; clarity and legibility matter more than shouting.

## Layout & Spacing
The layout is built around a wide, fluid hero with content aligned to the left and anchored by a prominent booking bar. Spacing feels generous, with a rhythm that steps through 8px, 16px, 28px, 40px, and 64px increments. Sections and overlays should preserve breathing room, while dense UI areas like the booking form use compact, carefully aligned spacing for efficiency.

Containers should favor broad desktop widths and edge-to-edge imagery, with content inset enough to keep the composition balanced. Cards and utility panels use a consistent internal padding of around 28px, while buttons rely on substantial horizontal padding to feel substantial and touch-friendly.

## Elevation & Depth
The system is mostly flat and tonal rather than shadow-heavy. Depth comes from contrast between cream, white, and dark overlays, plus the layered photography in the hero. When elevation is needed, use subtle shadows sparingly, as in the booking panel and cookie notice, to separate utility elements without breaking the calm aesthetic.

Borders are light and unobtrusive; many components depend on spacing and color separation instead of strong outlines. Inset detail can be used to create quiet refinement on cards and panels.

## Shapes
The shape language is soft and approachable. Large buttons are fully pill-shaped, while cards and fields use moderate radii to keep the interface friendly and modern. Rounded corners should feel deliberate and smooth, not playful or bubbly.

- **Full radius:** Reserved for primary and secondary buttons, chips, and high-emphasis interactive controls.
- **Medium radius:** Best for inputs, booking fields, and smaller UI containers.
- **Large radius:** Use for cards and major panels where the surface should feel relaxed and premium.

## Components
### Buttons
- **Primary buttons** should use `button-primary`: orange background, cream text, semibold label, full-pill radius, and a 56px height. These are reserved for the main action, such as booking or checking availability.
- **Secondary buttons** should use `button-secondary`: transparent background with orange text and border, keeping the same pill shape and sizing as the primary button.
- **Link buttons** should use `button-link` for low-emphasis actions such as legal links or inline utility actions. They should stay text-like and unboxed.
- Button sizing should remain generous; the source favors 16px vertical rhythm, 40px horizontal padding, and clear hit targets.

### Cards
- Cards should use `card`: cream background, dark text, 28px padding, and a 16px radius.
- Keep cards visually quiet; they should support content rather than compete with the hero or CTAs.
- Use subtle inset treatment or very light borders instead of heavy drop shadows.

### Inputs
- Inputs should feel like part of a cohesive booking system: white or cream surfaces, dark text, medium radius, and 56px height.
- Labels and helper text should remain small and restrained, with enough contrast to stay legible over light backgrounds.
- Grouped form fields should align tightly and read as one combined control, as seen in the booking bar.

### Chips and small utilities
- Use `chip` for compact contextual tags, filters, or metadata pills.
- Chips should be low-contrast, rounded, and lightweight, with small type and modest padding.
- Icons and caret indicators should stay minimal and functional.

### Navigation and supporting UI
- Navigation should be simple and text-led, with medium-weight labels and minimal chrome.
- Cookie notices, language selectors, and helper panels should use dark surfaces with light text when they need to sit over photography.
- Keep icons small and understated; the brand voice is driven more by typography and color than by ornament.

## Do's and Don'ts
- Do use the orange primary color sparingly for decisive actions and brand accents.
- Don't flood the interface with multiple bright accent colors; keep the palette tightly controlled.
- Do preserve the generous, editorial scale of headlines.
- Don't compress hero typography into small, conventional web copy sizing.
- Do keep surfaces warm and soft, especially on landing pages and utility panels.
- Don't replace the cream background with stark pure white across the system.
- Do favor pill-shaped CTAs and softly rounded containers.
- Don't introduce sharp, angular corners for primary interactive elements.
- Do rely on spacing and contrast for hierarchy before adding heavy shadows.
- Don't overuse elevation or glossy effects; the design should stay calm and modern.