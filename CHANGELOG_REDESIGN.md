# CHANGELOG — Shape as Strategy, ESMOD Portfolio (zine rebuild)

Design `DAHbgasWgM4`, title "Shape as Strategy – ESMOD Portfolio". **The deck is pages 1–8.** Pages 9–26 are the previous build (the "Archive Blush" version and its two unused cover variants). **Delete pages 9–26 by hand** in Canva: the API has no delete-page tool.

Direction: the "Pink Static" section at the top of `DA_CHARTER.md`. It follows the student's brief: a Gen-Z editorial fashion magazine / zine, copied closely from `Reference images/zine_karmic_lesson.jpg`, with fewer textures, more typographic detail, and play with opacity and red ballpoint scribbles.

- Kit generator: `assets/zine/make_zine.py`.
- Canva asset IDs: `assets/zine/canva_ids.json`.
- Fonts to apply by hand: `FONT_TODO.md`.

## What changed from the previous build
- **Removed:** every Pinterest/archive device: crumpled paper and parchment grounds, coffee rings, creases, tape, deckled sheets, script titles, silver foil, stamps and pencil scribbles.
- **Grounds:** a two-page spread on every slide. Blush `#fbe6ec` and paper `#fffafb` pages alternate, with a soft gutter shadow at x 960 and print crop/registration marks on top.
- **Display type:** giant black Inter Display SemiBold (tracking −6 %, leading 0.74) that overlaps and bleeds off the page or across the gutter. Examples: `(shape / as / strat / egy)`, `nova`, `PRETTY PIXIE`, the vertical `COURRÈGES`, `Cour / règes`, `Alaïa & Demna`, `+42 % / +525 % / +49 %`, `Sources & / image credits`.
- **Body text:** mono columns (Space Mono, to be applied by hand), mostly 15–20 px in narrow columns. Labels are red `#b5304b`, captions graphite `#4a4a4a`.
- **Headers:** a running header on every slide: student name, folio `ESMOD PARIS · 2026`, section label. A vertical title appears on slide 3 (section label), slide 4 (`COURRÈGES`) and slides 2 and 5 (subtitle and folio by the gutter).
- **Ghost type:** pale pink Space Mono at 50–75 % opacity, set behind the content.
- **Red marks:** red ballpoint marks and handwritten Reenie Beanie notes, 3–6 per spread (circle, underline, arrow, asterisk, bracket, tick, wave, cross, loop).
- **Detail elements:** barcode, a riso halftone disc, blurred red stems, and the AI pink-halftone orchid and butterfly as cut-outs.

## Pages and review scores
A fresh-context reviewer scored each slide on the 7 charter criteria. Pass = average ≥ 8, no criterion below 7, and integrity = 10. The review ran for 3 rounds at most.

| Slide | Page ID | Round 1 | Round 2 | Round 3 |
|---|---|---|---|---|
| 1 Cover | `PB2MZlNW41Hm7G7T` | 7.71 | **8.29 pass** | – |
| 2 NOVA | `PBGxl07PSp7QMlpZ` | 7.29 | 7.43 | ROUND3_S2 |
| 3 Pretty Pixie / Why ESMOD | `PByXNv9tz148tKvg` | 7.71 | **8.00 pass** | – |
| 4 Courrèges · then | `PBW1bfCKz8yZYpKp` | **8.14 pass** | **8.29 pass** | – |
| 5 Courrèges · now | `PB5mCbzbkZtMHsXN` | 7.14 | **8.29 pass** | – |
| 6 Alaïa & Demna | `PBqb4Lr0Lt2lZyp7` | 7.57 | 7.86 | ROUND3_S6 |
| 7 Current phenomenon | `PBhX91jrwql1Nns7` | 7.57 | **8.57 pass** | – |
| 8 Sources | `PBCDKslSW4JHyjXn` | 7.71 | **8.29 pass** | – |

Small polish was also applied after round 2:
- Slide 1: the orchid was enlarged and now bleeds off the page.
- Slide 3: the "Why ESMOD" column was narrowed to 400 px.

## Frozen content (programmatic check, after the fixes)
- **Text:** every string in `CONTENT_MANIFEST.json` is present unchanged on its slide, either as live text or as the exact alt text of a display or handwritten PNG. Nothing is missing and there are no whitespace near-misses.
- **Extra live text:** only the allowed micro-texts listed below.
- **Images:** 21 of 21 content images are placed, each with its exact manifest alt text. The largest aspect-ratio deviation is 0.03 %, and the largest crop or zoom is 0.47 %.
- **Order:** slide order and reading order are unchanged.

## Added decorative micro-texts (not in the manifest)
| Slide | Live micro-texts | Ghost-type PNGs (words already on the slide) |
|---|---|---|
| 1 | `01/08`, `ESMOD PARIS · 2026` | `2026` |
| 2 | `02/08`, `ESMOD PARIS · 2026` | none |
| 3 | `03/08`, `ESMOD PARIS · 2026` | `Why\nESMOD` |
| 4 | `04/08`, `ESMOD PARIS · 2026` | `1965` |
| 5 | `05/08`, `ESMOD PARIS · 2026` (twice: header and vertical by the gutter) | `then\nand now` |
| 6 | `06/08`, `ESMOD PARIS · 2026` (bottom row) | `the\nsilhouette` |
| 7 | `07/08`, `ESMOD PARIS · 2026` | `desire\nsplits.` |
| 8 | `08/08`, `ESMOD PARIS · 2026` | `2026` |

## Display and handwritten PNGs (alt text = exact manifest string)
| Slide | Alt texts |
|---|---|
| 1 | `(shape as strategy)` |
| 2 | `nova`; `circles → movement`; `curtains,\nnot\nwalls`; `discovered\nroom by\nroom.` |
| 3 | `PRETTY PIXIE`; `Why\nESMOD` |
| 4 | `COURRÈGES`; `a silhouette that defined a decade` |
| 5 | `Courrèges`; `then and now` |
| 6 | `Alaïa`; `&`; `Demna`; `with the logo removed,\nis the image still luxury?`; `One\nobsession\nthe\nsilhouette.` |
| 7 | `When a designer moves,\ndoes desire move with them -\nor stay with the house?`; `+42%`; `+525%`; `+49%`; `signals, not proof of a cause.`; `my reading` |
| 8 | `Sources &`; `image\ncredits` |

## New images and decoration
- *Code-drawn* means original, generated by `assets/zine/make_zine.py` with the system Inter Display, Space Mono (npm `@fontsource/space-mono`) and Reenie Beanie.
- *AI-generated* means Canva generate-image decor only, with no people, garments or campaigns.

| Canva asset | Description and source |
|---|---|
| `MAHbjNMAgNA` → `MAHbjZRm_h4` | AI-generated pink halftone orchid (after `zine_karmic_lesson.jpg`), background removed with Canva |
| `MAHbjH77gr8` → `MAHbjaKMgxk` | AI-generated pink halftone butterfly (after `zine_karmic_lesson.jpg`), background removed with Canva |
| `MAHbjBYj8NY` | code-drawn riso halftone disc |
| `MAHbjEuohEI` | code-drawn blurred red stems (after `zine_karmic_lesson.jpg`) |
| `MAHbjNcLHaA` | code-drawn print crop and registration marks |
| `MAHbjHBiACk` | code-drawn barcode |
| `MAHbjNwzHuQ` | code-drawn spread gutter shadow |
| `sc_*` (12 IDs in `canva_ids.json`) | code-drawn red ballpoint marks: circle, underline, arrow, asterisk, wave, cross, bracket, tick, loop |
| `zt_*`, `zg_*`, `zn_*` | code-drawn display type, ghost type and handwritten notes (exact strings above). Two renders are newer: `zt_pixie_xl` (`MAHbjUynQA0`) and the ink `zt_courreges_ink` (`MAHbjTVtmrQ`), which replaced the white one. |

The reference image `Reference images/zine_karmic_lesson.jpg` is used only as a style reference. Nothing is cropped from it.

## Limits
- **Fonts:** font families cannot be set through the Canva API. All live text uses Canva's default font until the swaps in `FONT_TODO.md` are applied.
- **Effects:** duotone, blend modes and letter spacing are not available through the API. The pink halftone look comes from the PNG assets and opacity.
- **Contact sheet:** PNG export works in Canva, but this container cannot download from `export-download.canva.com` (403), so no contact sheet is saved in the repo.
- **Image generation:** the Canva generate-image quota allowed only 2 images (orchid and butterfly). Every other decor element is code-drawn.
