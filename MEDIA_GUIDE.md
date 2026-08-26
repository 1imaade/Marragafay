# Marragafay media guide

This guide defines the additive media foundation. Existing image files, URLs, HTML references, CSS, and page behavior remain unchanged until a migration is explicitly verified.

## Canonical deployed namespace

New web-ready assets belong under `public/media/`, which is served as `/media/`:

```text
media/
├── activities/{quad,buggy,camel,paragliding,hot-air-balloon,dinner-show}/{hero,gallery,thumbs}/
├── packs/{basic,comfort,luxe}/{hero,gallery,thumbs}/
├── shared/{camp,pool,transport,dining,show}/
├── brand/
├── blog/
└── seo/
```

The directory names and asset names use lowercase kebab-case. Do not use spaces, underscores, camelCase, mixed case, or spelling variants such as `activites` or `hot-air-ballone` in new canonical paths.

## Naming and variants

- Activity hero: `activities/quad/hero/quad-hero.webp`
- Activity gallery item: `activities/quad/gallery/quad-01.webp`
- Pack hero: `packs/basic/hero/basic-hero.webp`
- Shared asset: `shared/pool/pool-01.webp`
- Responsive delivery variant: add a width suffix, for example `quad-01-w640.webp` and `quad-01-w1280.webp`.
- Thumbnail delivery belongs in `thumbs/` and follows the same stable stem, for example `quad-01-w320.webp`.
- Keep one stable asset id in the manifest even when the asset has multiple format or width variants.
- Use `candidate` as a provisional role for verified imported media whose final hero/gallery order has not been selected yet; it does not change website behavior.
- Use WebP as the default delivery format. Add AVIF only when it is generated and checked as part of a later migration. Keep original camera/source files outside the deployed project tree.

The manifest records the verified dimensions of each file, its owner, roles/usages, shared status, alt text, canonical path, and responsive variants. Do not add guessed entries: a file is added only after its actual type, dimensions, ownership, and alt text are known.

## Responsive image policy

Generate only the widths needed by the component and never upscale a source. A normal starting set is 320px for thumbs, 640px for cards/gallery previews, 960px or 1280px for content, and up to 1600px for heroes. The final widths depend on the source dimensions and layout.

When a page is migrated, use explicit `width`/`height`, `loading="lazy"` for below-the-fold images, and `srcset`/`sizes` for responsive variants. Keep the current references untouched until the migrated page has been checked on desktop and mobile.

## Source originals and contact sheets

Raw originals, unedited batch files, and future contact sheets must stay outside both `public/media/` and the deployed project. Use this sibling workspace when a batch arrives:

```text
/home/imaade/Projects/Marragafay/Marragafay-media-source/
├── inbox/<batch-id>/raw/
├── inbox/<batch-id>/contact-sheets/
└── archive/<batch-id>/
```

Only verified web-ready derivatives are copied into `public/media/`. The source workspace is an intake/archive location, not a URL namespace.

## Staged migration workflow

1. Place one batch in the external `inbox/<batch-id>/raw/` folder; do not copy it into `public/media/` yet.
2. Run the media inventory, duplicate, actual-type, and reference checks against the batch and the project.
3. Select one owner at a time (for example `activities/quad`), generate lowercase kebab-case derivatives, and copy only verified web-ready files into its canonical folders.
4. Add manifest entries with measured dimensions, real alt text, owner, roles, and variants; run manifest/path validation.
5. Migrate one page/language set at a time. Verify the rendered page, responsive loading, and old URL behavior before changing any live reference.
6. Keep the legacy files and URLs during the migration window. Deprecation or cleanup is a separate, explicitly approved step after all references are proven safe.

The foundation deliberately does not migrate activities, refactor HTML/media references, change CSS, or delete/rename existing images.
