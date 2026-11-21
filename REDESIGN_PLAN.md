# REDESIGN PLAN — Shape as Strategy v4 (`DAHbgHFq6rM`)

Status: draft for GATE 1. Nothing edited on the slides yet.
Sources: `Layout/` (2 screenshots) give the layout. `Reference images/` (4 files) give the aesthetic. Text, the 21 content images, slide order and reading order stay frozen (handover Section 3).

## 0. Layout grammar (from `Layout/`)
These rules apply on every slide.
- **Field.** Full-bleed flat paper colour. Wide empty areas are intentional: the poster with the large empty field, the styling board.
- **Sheets.** Coloured rectangles (pink or cream) overlap one another and the photos, slightly offset. This is the "pink sheet over b/w spread" motif. Text sits on sheets.
- **Prints.** Content images get a white or ivory border (12–16 px) and a soft shadow. A few are stacked with a slight tilt of ±2–4°. Most stay straight, so the page reads as editorial and not as scrapbook.
- **Micro-labels.** Four tiny tracked-caps labels sit in the corners of each slide, as on the styling board ("STYLING · BOARD · STUDIO · AETHER"). The two existing header strings fill the top corners. Bottom corners stay empty or carry decor. No new text strings.
- **Captions.** Small and close to their image. A dot-label style ("• caption") borrows the halftone portrait's annotations. The dot is a shape, not a text character, so the strings stay unchanged.
- **Margins.** 80 px outer margin. A 12-column grid at 1920: column 120, gutter 40.

## 1. Per-slide layout

### Slide 1 — Cover
- Field: blush watercolour wash (asset A1) over cream.
- "Portfolio": large script, centred slightly left at about x480–1440, y380–700.
- The 4 labels go to the 4 corners of an invisible frame around the wordmark, like the styling-board corners:
  - `(Ekisha Sachdeva)` at top-left.
  - `(shape as strategy)` at top-right.
  - `ESMOD Paris` at bottom-left.
  - `2026` at bottom-right.
- Header strings stay in the page corners.
- A cluster of 4-point stars (A5) near the wordmark. A thin flourish swash (A4) under it.
- Delete: the binder frame, the blue swirls, the selection box, the handles, the cursor arrow and the pink outline boxes.

### Slide 2 — NOVA
- Left column (x80–640): `nova` in big script. Under it the blurb, the journey line and the three lists on a cream sheet (x60–660, full height).
- Right side: a moodboard-style board.
  - The wardrobe moodboard and the floor plan are large prints, side by side at the top.
  - The poster and the 4 reference photos (salon, rail, reception, shoes) form a lower row of smaller prints. Some overlap.
- Captions sit as dot-labels next to their prints.
- The notes "curtains, not walls", "discovered room by room." and "circles → movement" become handwritten-style accents near the floor plan.
- Reading order kept: title, blurb, journey, skills and learned, then images in the order moodboard, plan, poster, salon, rail, reception, shoes.

### Slide 3 — Pretty Pixie + Why ESMOD
- Field: cream.
- `PRETTY PIXIE` stays vertical at the left edge, in script or display.
- The internship text sits in a column at x260–1060.
- "Why ESMOD": a pink sheet (x1180–1880), overlapping onto the field by a few px with a slight offset second sheet behind. This is the layout's double-sheet motif.
- The `02 - EXPERIENCE & MOTIVATION` tag stays at the bottom of the sheet.
- No images.

### Slide 4 — Courrèges THEN
- The Vogue 1964 spread is a large print, centre-left (about 1000x649 kept). It sits on a pale field.
- A pink sheet overlaps its lower-left corner. It carries Identity, Codes, Today's Client and Legacy Moment. This mirrors the "pink sheet over b/w spread" layout.
- `COURRÈGES` stays vertical at the left.
- The two McCall's prints are stacked and slightly tilted at the bottom right, with the long caption under them.
- The right column keeps the annotations ("published in Vogue…", "a silhouette…", "Now").

### Slide 5 — Courrèges NOW
- The faded campaign image becomes a full-height bleed on the right half, at low opacity, as it is today.
- The campaign cut-out and the 2 SS27 runway prints are stacked white-bordered prints on top of it.
- Left side:
  - `Courrèges` in big script, with `then and now` under it.
  - The timeline sits as a row of 5 dot-labels on one hairline.
  - The three text blocks (Communication, What I question, My proposal) sit in columns on a cream sheet.
- "codes so clear, always in style." is a script accent.

### Slide 6 — Alaïa & Demna
- A two-page spread split at x960, with a faint fold shadow (not the binder).
- Left page: Alaïa.
  - The sculpted dress is a large print.
  - The atelier photo, the logo-removal study and the Lebon campaign sit as a row of smaller prints.
- Right page: Demna.
  - Gucci look 44 is a large print.
  - La Famiglia and The Characters are smaller prints.
- `Alaïa`, `&` and `Demna` keep their vertical or stacked placement.
- Centre notes sit on a narrow pink sheet across the fold: "Two outsiders…" and "One obsession…".
- The old pink blocks become sheets in the new palette.

### Slide 7 — Current phenomenon
- The question in big type at the top-left.
- Three pink sheets, equal width, in place of the price tags. Each sheet holds a label, a big number, a description and a source.
- The "my reading" card is a cream card with a faint flourish frame (A4). It sits right and is slightly overlapping.
- The caveat lines are small, at the top-right.
- Large empty field around the sheets.

### Slide 8 — Sources
- A cream styling-board card covers most of the page.
- `Sources &` and `image credits` in script, at the left. `research that shaped this project.` sits under them.
- `IMAGES` and `TEXT & DATA` lists are small type in two columns.
- Corner micro-labels carry the header strings.
- Delete: the blue taped card and the swatch legend.

## 2. Palette
| Role | Hex |
|---|---|
| Field, cream | `#f4efe6` |
| Paper, ivory (print borders, cards) | `#fbf8f2` |
| Blush pink (sheets) | `#f2d4df` |
| Rose pink (accents, numbers) | `#d98aa8` |
| Deep rose (watercolour shade, rare) | `#b45f82` |
| Silver grey (hairlines, foil) | `#c9ccd1` |
| Ink blue-grey (body text) | `#3a414a` |
| Ink deep (titles) | `#23272d` |
| Sepia (stains, rare accent) | `#a9825e` |

No candy colours. Contrast: ink text on blush or cream is about 9:1 or better. Rose `#d98aa8` is never used for body text, only for big numbers and decor.

## 3. Type plan
`format_text` cannot change font family. Fonts are applied by hand from `FONT_TODO.md`. That file lists each locator ID, its current font and the font to apply.

| Role | Font (Canva) | Size | Elements |
|---|---|---|---|
| Display script | **Pinyon Script** (fallback: Great Vibes) | 120–260 | `nova`, `PRETTY PIXIE`?, `COURRÈGES`?, `Courrèges`, `Alaïa`, `&`, `Demna`, `Sources &`, `image credits`, short accent notes |
| Headings, serif | **Cormorant Garamond** semibold | 32–56 | `The journey`, `Why ESMOD`, `What I question`, the question on slide 7, and similar |
| Body, serif | **Cormorant Garamond** medium | 20–24 | All paragraphs and lists |
| Labels and captions, sans | **Montserrat** regular, tracked caps | 12–14 | Header strings, section tags, captions, `HISTORICAL REFERENCE`, and similar |
| Numbers | Cormorant Garamond light | 96–120 | `+42%`, `+525%`, `+49%` |

- The script is used only for short words (1–2 words). Long or all-caps titles (`PRETTY PIXIE`, `COURRÈGES`) may stay in the serif. I will decide by eye at the slide 1 test.
- Sizes, colours, line height and alignment are set by tool. The CHANGELOG logs any size, width or wrapping change.
- Cover "Portfolio": I will outline Pinyon Script glyphs into SVG paths and replace the old blue vector. This is allowed for the cover only. I will do it with `fonttools` and the OFL font file. If that fails, "Portfolio" becomes a text box and you set the font by hand.

## 4. Decor assets (`canvas-design`, original, no tracing)
| ID | Asset | Format | Used on |
|---|---|---|---|
| A1 | Blush watercolour wash, soft bloom | PNG 1920x1080 | 1, faint on 8 |
| A2 | Crumpled-paper grain, pink tint | PNG 1920x1080, transparent, low alpha | sheet overlays on 3, 4, 7 |
| A3 | Halftone dot grain | PNG 1920x1080, transparent | overlay on 5, 6 (faint) |
| A4 | Script flourish frame (oval with swirls) | PNG transparent | 7 ("my reading"), maybe 1 |
| A5 | 4-point star set (3 sizes) | drawn as Canva SVG shapes, no PNG | 1, 2, 5, 8 |
| A6 | Coffee-ring stain, sepia | PNG transparent | 8, maybe 2 |
| A7 | Dot-label bullets and hairlines | Canva SVG shapes | captions on all slides |

A5 and A7 are drawn directly with `insert_shape`, so they need no upload.

## 5. Old frame elements to delete (every page)
- The backdrop full-bleed candy rect. It is replaced by a recoloured field.
- The paper sheet 1840x1000 and its shadow stack (`#eceae5`, and the `#1a1c20` layers at opacity .05–.12).
- The speckle grain (`#5e5953`) and the wavy hand-lines (`#ed8fbc` / `#8a847c`).
- The centre fold strip and line, except on slide 6, where a new fold is drawn.
- The binding band, its hairlines, and the 6 rings with all their layers (holes, lips, shades, highlights).
- The page-stack edge lines.
- The crumpled margin strips (`MAHbeyJlCBI`) and the paper overlay (`MAHbe-ziJ2o`), wherever present.
- Per-slide old decor:
  - Slide 1: swirls, selection box, cursor, outline boxes.
  - Slide 2: ellipse outlines, tape.
  - Slide 6: the pink blocks become sheets.
  - Slide 7: the tag punch-holes.
  - Slide 8: the blue taped card and the swatches.

Exact locator IDs are listed per page at edit time. Every deletion is checked to make sure none of the 21 images or any text element is removed.

## 6. Defaults taken (your Phase 1 questions had no answer)
1. Pink is part of the palette (blush, not candy).
2. The script is for short headings only. Body text is serif.
3. Canva fonts are close matches. The fonts named above are standard Canva fonts.
4. "Portfolio" is redrawn as script outlines (see section 3).
5. The binder frame is dropped.
6. The 21 content images keep their original colour. There is no b/w conversion.

## 7. Process
- GATE 2: assets.
- GATE 3: slide 1 as the style test.
- Then slides 2–8, one `edit-design` batch per page, with before/after thumbnails and a commit after your ok.
- GATE 4: QA against the handover.
