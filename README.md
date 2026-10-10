# Kerhotten – Proposition de refonte – Option B « Prestige » (maquette privée)

> **Private redesign proposal, photos © Gîtes de Kerhotten, not for publication without owners' consent.**
> Photos © Gîtes de Kerhotten, reprises de www.gitesdekerhotten.fr pour cette présentation privée uniquement.
> Ne pas publier sans l'accord écrit des propriétaires (Cindy & Eddy).

Option B is a second, more upmarket take on the site. Option A is in `../kerhotten-demo/`.
It is styled as a boutique hotel:

- a full-screen hero with a slow Ken Burns effect
- serif type: Marcellus, Cormorant Garamond italic and Jost, all self-hosted
- the three houses shown as "suites", each with its own page and an accessible lightbox
- a seasonal "experiences" section
- a page for hiring the whole hamlet
- a calendar and booking-engine demo
- FR / EN / DE

## Pages

| File | Contents |
|---|---|
| `index.html` | Hero, history (1697), the 3 suites, the grounds, the seasons, private hire, booking teaser, contact |
| `le-saule.html`, `la-chataigne.html`, `la-grange.html` | Suite pages: specs, layout, price placeholder, gallery and lightbox |
| `privatisation.html` | Whole-hamlet hire: up to 20 beds, occasions, on-request services |
| `reserver.html` | **DEMO** calendar and booking engine. Occupancy is fictitious, there is no price and no payment, and nothing is sent |

Every page has these:

- `<meta name="robots" content="noindex, nofollow">`
- the visible strip "Proposition de refonte – Option B Prestige – maquette"
- the copyright note in an HTML comment and in the footer

`.nojekyll` is at the root.

## Viewing / rebuilding

```bash
cd /workspace/portfolio/kerhotten-demo-b
python3 -m http.server 8770 --bind 127.0.0.1   # http://127.0.0.1:8770/
python3 _build/build.py                        # regenerates the *.html, assets/js/i18n.js and site.min.js
```

- Source files live in `_build/`:
  - `layout.html` is the page shell.
  - `pages/*.html` holds the page bodies.
  - `suites.py` holds the suite data and generates the suite pages.
  - `js-strings.json` holds the JS strings.
- Translations sit inline in the source as `[[FR || EN || DE]]`. Attributes use `{{alt: FR || EN || DE}}`.
- French is served in the HTML. The EN/DE dictionary (`assets/js/i18n.js`) only loads when the visitor switches language.
- `assets/css/site.css` is minified (csso) and inlined into each page. Font URLs are therefore relative to the site root.
- `assets/js/site.js` is minified to `site.min.js` with terser.
- The build needs `/tmp/tools`, which has csso and terser.

## Content rules followed

- **Facts come only from www.gitesdekerhotten.fr.** No prices, reviews, ratings or statistics were invented. Unknown values are shown as dashed "À compléter / À définir" placeholders.
- Travel times are the ones the owners give: lakes at 10, 15 and 25 min, beaches at 45 min, Guémené 10 min, Pontivy 25 min. Splitting them into four seasons is an editorial choice; each claim under a season comes from the site.
- Photos are the owners' own, re-encoded to WebP at 480/800/1280 with a JPEG fallback. Two very low-resolution gallery images were left out: the Christmas tree (150 px) and the decorations (320 px).

## Inconsistencies on the current site (to confirm with the owners)

| Topic | On the site | In this mock-up |
|---|---|---|
| Date of the hamlet | **1697** (home page, inscribed in the Grange gable stone), but **1692** appears elsewhere | **1697** (home page figure) |
| Le Saule | 90 m² / 5 pers. (home page) vs 85 m² / 4 pers. ("Les gîtes" page) | 90 m² / 5 pers. |
| La Châtaigne | 130 m² vs 115 / 120 m² | 130 m², 8 to 10 pers. |
| La Grange | 7 pers. vs 6 pers. | 7 pers., 95 m² |
| Whole-hamlet capacity | "20 couchages max", but 5 + 10 + 7 = 22 | "jusqu'à 20" (the per-house figures are not summed) |
| "La Ferme" | Listed as a gîte, but it is the owners' home | Not presented as a gîte |
| Spelling | Kervoten / Kervotten | "Hameau de Kervotten" (postal address) |
| Pool | "chauffée" vs "chauffée solaire" | "chauffée" |
| "Ouvert toute l'année" | Weak source | Left out |
| GPS, prices, ratings | Not reliable or not published | Left out |

## Booking demo: what it shows and where real services plug in

- **Calendar:** the occupancy pattern is fictitious and deterministic. In production it would come from an iCal sync or a channel manager (Gîtes de France / Airbnb / Booking).
- **Checks:** the demo checks that the chosen nights don't include a booked night, and that guests don't exceed the capacity (5 / 10 / 7 / 20).
- **Price:** shows "À définir". The real rate grid has to come from the owners.
- **Payment:** a dashed placeholder marks where a provider would go (deposit, then balance). It contains no card fields and makes no network request.
- **Fallback:** a `mailto:` link prepares a message to kerhotten@outlook.fr. Nothing is sent unless the visitor clicks it and then sends from their own mail app.
- `reserver.html?suite=saule|chataigne|grange|hameau` preselects the accommodation.

## Accessibility and motion

- Lightbox: native `<dialog>`, focus trapped on its 3 controls, ← / → to navigate, Escape or a backdrop click to close, and focus returns to the opened thumbnail.
- `prefers-reduced-motion` turns off the Ken Burns effect, the reveals and the transitions. Scroll reveals use CSS `animation-timeline`, so they cost no JS.
- Lighthouse accessibility is 100 on every page.

## Before publishing (checklist)

1. **Written consent from the owners** to reuse their photos and text, and confirmation of every figure in the table above.
2. Real **prices**, terms and conditions (CGV), cancellation policy, deposit amount.
3. Choose and integrate the **booking / payment** solution (PSP or booking platform) and the **calendar sync**. Then remove the "Démonstration" banners and the fictitious occupancy.
4. **Legal notices**, privacy policy, publisher/host details (currently "(à compléter)").
5. **Remove the `noindex`** and the "maquette" strip, delete the comment, add a sitemap, robots.txt and absolute canonical / og:image URLs on the final domain.
6. Have the **German translation** (and the English) proofread by native speakers.
7. Hosting: HTTPS, an HTTP→HTTPS redirect, long cache lifetimes on `assets/` (Lighthouse "cache" warning), compression.
8. If the owners can supply higher-resolution photos, replace the small ones. Some are only 760 px wide.
