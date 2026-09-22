import assert from 'node:assert/strict';
import test from 'node:test';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.resolve(__dirname, '..');

// Initialize localization engine for Node tests
import ProductLocalization from '../js/product-localization.js';
globalThis.ProductLocalization = ProductLocalization;
import ProductData from '../js/product-data.js';

const LOCALES = ['en', 'fr', 'es', 'ar'];

test('1. Core localized pages include product scripts in correct execution order', () => {
    const pageTypes = [
        'packs.html',
        'packages/basic.html',
        'packages/comfort.html',
        'packages/luxe.html',
        'activities/buggy.html',
        'index.html'
    ];

    LOCALES.forEach(loc => {
        pageTypes.forEach(relPath => {
            const filePath = path.join(ROOT, loc, relPath);
            assert.ok(fs.existsSync(filePath), `File must exist: ${loc}/${relPath}`);
            const html = fs.readFileSync(filePath, 'utf-8');

            const hasLocScript = html.includes('product-localization.js');
            const hasDataScript = html.includes('product-data.js');
            const hasPricingScript = html.includes('dynamic-pricing.js');

            assert.ok(hasDataScript, `${loc}/${relPath} must include product-data.js`);
            assert.ok(hasPricingScript, `${loc}/${relPath} must include dynamic-pricing.js`);

            // Non-EN pages should include product-localization.js
            if (loc !== 'en') {
                assert.ok(hasLocScript, `${loc}/${relPath} must include product-localization.js`);
                const locIndex = html.indexOf('product-localization.js');
                const dataIndex = html.indexOf('product-data.js');
                const pricingIndex = html.indexOf('dynamic-pricing.js');

                assert.ok(locIndex < dataIndex, `product-localization.js must precede product-data.js in ${loc}/${relPath}`);
                assert.ok(dataIndex < pricingIndex, `product-data.js must precede dynamic-pricing.js in ${loc}/${relPath}`);
            }
        });
    });
});

test('2. packs.html in all 4 locales binds the 4 canonical products', () => {
    const expectedKeys = ['standard', 'private', 'private-plus', 'buggy'];

    LOCALES.forEach(loc => {
        const filePath = path.join(ROOT, loc, 'packs.html');
        const html = fs.readFileSync(filePath, 'utf-8');

        expectedKeys.forEach(k => {
            assert.ok(
                html.includes(`data-product="${k}"`),
                `packs.html in ${loc} must contain data-product="${k}"`
            );
        });

        // Ensure badge is updated (4 packages, not 10)
        assert.ok(!html.includes('10 packs'), `packs.html in ${loc} must not claim 10 packs`);
        assert.ok(!html.includes('10 paquets'), `packs.html in ${loc} must not claim 10 paquets`);
        assert.ok(!html.includes('10 paquetes'), `packs.html in ${loc} must not claim 10 paquetes`);
        assert.ok(!html.includes('10 عبوات'), `packs.html in ${loc} must not claim 10 عبوات`);
    });
});

test('3. Package detail pages bind to their canonical product keys', () => {
    const mapping = {
        'packages/basic.html': 'standard',
        'packages/comfort.html': 'private',
        'packages/luxe.html': 'private-plus',
        'activities/buggy.html': 'buggy'
    };

    LOCALES.forEach(loc => {
        Object.entries(mapping).forEach(([relPath, key]) => {
            const filePath = path.join(ROOT, loc, relPath);
            const html = fs.readFileSync(filePath, 'utf-8');

            assert.ok(
                html.includes(`data-product="${key}"`),
                `${loc}/${relPath} must bind data-product="${key}"`
            );
            assert.ok(
                html.includes('data-field="price-eur"'),
                `${loc}/${relPath} must bind data-field="price-eur"`
            );
        });
    });
});

test('4. Canonical product facts (EUR/MAD/timing) align identically across all 4 locales', () => {
    const expectations = {
        standard: { eur: 45, mad: 450, duration: '15:30–22:00' },
        private: { eur: 75, mad: 750, duration: '15:30–22:00' },
        'private-plus': { eur: 119, mad: 1190, duration: '09:00–22:00' },
        buggy: { eur: 129, mad: 1290 }
    };

    LOCALES.forEach(loc => {
        Object.entries(expectations).forEach(([k, exp]) => {
            const prod = ProductData.getLocalizedProduct(k, loc);
            assert.ok(prod, `Product ${k} must exist for locale ${loc}`);
            assert.equal(prod.priceEUR, exp.eur, `Price EUR for ${k} in ${loc} must be ${exp.eur}`);
            assert.equal(prod.priceMAD, exp.mad, `Price MAD for ${k} in ${loc} must be ${exp.mad}`);
            if (exp.duration) {
                assert.equal(prod.duration, exp.duration, `Duration for ${k} in ${loc} must be ${exp.duration}`);
            }
            assert.ok(prod.transport, `Transport must be localized for ${k} in ${loc}`);
            assert.ok(Array.isArray(prod.includes) && prod.includes.length >= 9, `Inclusions for ${k} in ${loc} must be complete`);
            assert.ok(prod.cardSummary.includes(prod.facts.quadDuration), `Quad duration for ${k} in ${loc} must come from canonical facts`);
            assert.ok(prod.cardSummary.includes(prod.facts.camelDuration), `Camel duration for ${k} in ${loc} must come from canonical facts`);
        });
    });
});

test('5. Zero forbidden legacy strings across all locales', () => {
    const forbiddenChecks = [
        { pattern: /10\s*(?:packs|paquets|paquetes|عبوات)/i, desc: 'legacy 10-packs count' },
        { pattern: /800\s*(?:MAD|درهم)/i, desc: 'legacy 800 MAD buggy price' },
        { pattern: /1199\s*(?:MAD|درهم)/i, desc: 'legacy 1199 MAD buggy surcharge' },
        { pattern: /1600\s*(?:MAD|درهم)|1\s*600\s*MAD|1\.600\s*MAD/i, desc: 'legacy 1600 MAD buggy solo price' },
        { pattern: /2398/i, desc: 'legacy 2398 MAD buggy price' },
        { pattern: /(?:central meeting point|point de rencontre central|punto de encuentro central|نقطة اللقاء المركزية|نقطة انطلاق مركزية)/i, desc: 'central meeting point claim' },
        { pattern: /(?:30min camel|30 min camel|30 minutes camel|30 min de dromadaire|30 minutos de camello|30 دقيقة جمل)/i, desc: '30min camel on private pack' }
    ];

    const packageFiles = [
        'packs.html',
        'packages/basic.html',
        'packages/comfort.html',
        'packages/luxe.html',
        'activities/buggy.html'
    ];

    LOCALES.forEach(loc => {
        packageFiles.forEach(relPath => {
            const filePath = path.join(ROOT, loc, relPath);
            const html = fs.readFileSync(filePath, 'utf-8');

            forbiddenChecks.forEach(({ pattern, desc }) => {
                const match = html.match(pattern);
                assert.ok(!match, `Found forbidden ${desc} in ${loc}/${relPath}: "${match ? match[0] : ''}"`);
            });
        });
    });

    // Verify "All packages" is not untranslated in non-EN files
    ['fr', 'es', 'ar'].forEach(loc => {
        ['packs.html', 'index.html'].forEach(relPath => {
            const filePath = path.join(ROOT, loc, relPath);
            const html = fs.readFileSync(filePath, 'utf-8');
            assert.ok(!html.includes('All packages'), `Unlocalized "All packages" found in ${loc}/${relPath}`);
        });
    });
});

test('6. Dynamic price change simulation updates all 4 locales simultaneously without drift', () => {
    // Simulate price change: 45 EUR -> 46 EUR / 460 MAD
    ProductData.setProductOverride('standard', { priceEUR: 46, priceMAD: 460 });

    LOCALES.forEach(loc => {
        const prod = ProductData.getLocalizedProduct('standard', loc);
        assert.equal(prod.priceEUR, 46, `Simulated EUR price for ${loc} must be 46`);
        assert.equal(prod.priceMAD, 460, `Simulated MAD price for ${loc} must be 460`);
    });

    // Clean up simulation
    ProductData.resetOverrides();

    LOCALES.forEach(loc => {
        const prod = ProductData.getLocalizedProduct('standard', loc);
        assert.equal(prod.priceEUR, 45, `Cleaned EUR price for ${loc} must revert to 45`);
        assert.equal(prod.priceMAD, 450, `Cleaned MAD price for ${loc} must revert to 450`);
    });
});

test('7. Supabase offline fallback safely returns localized canonical fallbacks', () => {
    LOCALES.forEach(loc => {
        const std = ProductData.getLocalizedProduct('standard', loc);
        assert.equal(std.priceEUR, 45);
        assert.equal(std.priceMAD, 450);

        const priv = ProductData.getLocalizedProduct('private', loc);
        assert.equal(priv.priceEUR, 75);
        assert.equal(priv.priceMAD, 750);

        const privPlus = ProductData.getLocalizedProduct('private-plus', loc);
        assert.equal(privPlus.priceEUR, 119);
        assert.equal(privPlus.priceMAD, 1190);

        const buggy = ProductData.getLocalizedProduct('buggy', loc);
        assert.equal(buggy.priceEUR, 129);
        assert.equal(buggy.priceMAD, 1290);
    });
});

test('8. Reciprocal hreflang and canonical SEO tags across all 12 target pages', () => {
    const targetPages = ['blog.html', 'blog-single.html', 'success.html'];

    targetPages.forEach(page => {
        LOCALES.forEach(loc => {
            const filePath = path.join(ROOT, loc, page);
            assert.ok(fs.existsSync(filePath), `File must exist: ${loc}/${page}`);
            const html = fs.readFileSync(filePath, 'utf-8');

            // Must have canonical tag matching current locale
            const cleanSlug = page.replace('.html', '');
            const expectedCanonical = `<link rel="canonical" href="https://www.marragafay.com/${loc}/${cleanSlug}">`;
            assert.ok(
                html.includes(expectedCanonical),
                `${loc}/${page} must have canonical: ${expectedCanonical}`
            );

            // Must have reciprocal hreflangs for all locales and x-default
            LOCALES.forEach(hloc => {
                const expectedHreflang = `<link rel="alternate" hreflang="${hloc}" href="https://www.marragafay.com/${hloc}/${cleanSlug}">`;
                assert.ok(
                    html.includes(expectedHreflang),
                    `${loc}/${page} must have hreflang for ${hloc}`
                );
            });

            const expectedDefault = `<link rel="alternate" hreflang="x-default" href="https://www.marragafay.com/en/${cleanSlug}">`;
            assert.ok(
                html.includes(expectedDefault),
                `${loc}/${page} must have hreflang x-default`
            );
        });
    });
});

test('9. Arabic pages preserve dir="rtl" and language declaration', () => {
    const arFiles = [
        'packs.html',
        'packages/basic.html',
        'packages/comfort.html',
        'packages/luxe.html',
        'activities/buggy.html',
        'index.html',
        'success.html'
    ];

    arFiles.forEach(relPath => {
        const filePath = path.join(ROOT, 'ar', relPath);
        const html = fs.readFileSync(filePath, 'utf-8');
        assert.ok(
            html.includes('dir="rtl"'),
            `ar/${relPath} must declare dir="rtl"`
        );
        assert.ok(
            html.includes('lang="ar"'),
            `ar/${relPath} must declare lang="ar"`
        );
    });
});

test('10. Target pages expose complete canonical SEO and product bindings', () => {
    const targets = [
        ['index.html', null],
        ['packs.html', null],
        ['packages/basic.html', 'standard'],
        ['packages/comfort.html', 'private'],
        ['packages/luxe.html', 'private-plus'],
        ['activities/buggy.html', 'buggy']
    ];
    const requiredFields = ['title', 'name', 'duration', 'transport', 'inclusions', 'price-eur', 'price-mad'];

    targets.forEach(([relPath, productKey]) => {
        const slug = relPath === 'index.html' ? '' : relPath.replace(/\.html$/, '');
        LOCALES.forEach(loc => {
            const html = fs.readFileSync(path.join(ROOT, loc, relPath), 'utf-8');
            const canonical = `https://www.marragafay.com/${loc}${slug ? '/' + slug : ''}`;
            assert.ok(html.includes(`<link rel="canonical" href="${canonical}">`), `${loc}/${relPath} canonical must be ${canonical}`);
            LOCALES.forEach(hloc => {
                const alternateSlug = slug ? '/' + slug : '';
                const expected = `https://www.marragafay.com/${hloc}${alternateSlug}`;
                assert.ok(html.includes(`<link rel="alternate" hreflang="${hloc}" href="${expected}">`), `${loc}/${relPath} must link ${hloc}`);
            });
            const defaultSlug = slug ? '/' + slug : '';
            assert.ok(html.includes(`<link rel="alternate" hreflang="x-default" href="https://www.marragafay.com/en${defaultSlug}">`), `${loc}/${relPath} must link x-default`);
            assert.match(html, /data-lang="(?:en|fr|es|ar)"/, `${loc}/${relPath} must expose language switcher options`);

            if (productKey) {
                requiredFields.forEach(field => {
                    assert.ok(html.includes(`data-product="${productKey}"`) && html.includes(`data-field="${field}"`), `${loc}/${relPath} must bind ${productKey}.${field}`);
                });
            }
        });
    });
});

test('11. Root and unlocalized product routes redirect to English pages', () => {
    assert.equal(fs.existsSync(path.join(ROOT, 'index.html')), false, 'root index.html must not remain as a homepage');
    const vercel = JSON.parse(fs.readFileSync(path.join(ROOT, 'vercel.json'), 'utf-8'));
    const routes = vercel.routes;
    assert.deepEqual(routes.find(route => route.src === '^/$'), { src: '^/$', headers: { Location: '/en' }, status: 308 });
    assert.deepEqual(routes.find(route => route.src === '^/index\\.html$'), { src: '^/index\\.html$', headers: { Location: '/en' }, status: 308 });
    const legacyRoutes = [
        ['/packs/?', '/en/packs', ['/packs', '/packs.html']],
        ['/packs\\.html', '/en/packs', ['/packs', '/packs.html']],
        ['/packages/basic/?', '/en/packages/basic', ['/packages/basic', '/packages/basic.html']],
        ['/packages/basic\\.html', '/en/packages/basic', ['/packages/basic', '/packages/basic.html']],
        ['/packages/comfort/?', '/en/packages/comfort', ['/packages/comfort', '/packages/comfort.html']],
        ['/packages/comfort\\.html', '/en/packages/comfort', ['/packages/comfort', '/packages/comfort.html']],
        ['/packages/luxe/?', '/en/packages/luxe', ['/packages/luxe', '/packages/luxe.html']],
        ['/packages/luxe\\.html', '/en/packages/luxe', ['/packages/luxe', '/packages/luxe.html']],
        ['/activities/buggy/?', '/en/activities/buggy', ['/activities/buggy', '/activities/buggy.html']],
        ['/activities/buggy\\.html', '/en/activities/buggy', ['/activities/buggy', '/activities/buggy.html']]
    ];
    legacyRoutes.forEach(([pathPattern, destination]) => {
        const src = `^${pathPattern}$`;
        assert.deepEqual(routes.find(route => route.src === src), { src, headers: { Location: destination }, status: 308 });
    });
    const devServer = fs.readFileSync(path.join(ROOT, 'scripts/dev-server.js'), 'utf-8');
    assert.match(devServer, /url\.pathname === '\/' \|\| url\.pathname === '\/index\.html'/);
    assert.ok(devServer.includes("res.setHeader('Location', `${destination}${url.search}`)"));
    legacyRoutes.forEach(([, destination, paths]) => {
        paths.forEach(pathname => {
            const target = `['${pathname}', '${destination}']`;
            assert.ok(devServer.includes(target), `dev server must redirect ${pathname} to ${destination}`);
        });
    });
});

test('12. Product facts are not reintroduced by active homepage package literals', () => {
    LOCALES.forEach(loc => {
        const html = fs.readFileSync(path.join(ROOT, loc, 'index.html'), 'utf-8');
        assert.doesNotMatch(html, /const\s+packageData\s*=/, `${loc}/index.html must resolve modal products from ProductData`);
        assert.match(html, /function\s+buildPackageData\(packageType\)/, `${loc}/index.html must resolve modal products through ProductData`);
    });
});

test('13. All localized product booking bars share the restrained two-corner treatment', () => {
    const productPages = [
        'packages/basic.html',
        'packages/comfort.html',
        'packages/luxe.html',
        'activities/buggy.html'
    ];
    const bookingStyles = fs.readFileSync(path.join(ROOT, 'css/custom-bundle.css'), 'utf-8');

    LOCALES.forEach(loc => {
        productPages.forEach(page => {
            const html = fs.readFileSync(path.join(ROOT, loc, page), 'utf-8');
            assert.ok(html.includes('id="booking-form"'), `${loc}/${page} must contain the product booking form`);
            assert.ok(html.includes('href="/css/custom-bundle.css"'), `${loc}/${page} must load shared booking form styles`);
        });
    });

    assert.match(bookingStyles, /form#booking-form:has\(\.booking-input-cell\)\s*\{[^}]*border-radius:\s*14px\s+0\s+14px\s+0/s);
    assert.match(bookingStyles, /\.booking-input-cell:first-child\s*\{[^}]*border-radius:\s*14px\s+0\s+0\s+0/s);
    assert.match(bookingStyles, />\s*button\s*\{[^}]*border-radius:\s*0\s+0\s+14px\s+0/s);
});
