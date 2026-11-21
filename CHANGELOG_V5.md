# CHANGELOG — Shape as Strategy v5 (clean build)

Phase 2B clean rebuild. The plan is in `REDESIGN_PLAN.md`, content in `CONTENT_MANIFEST.json`, fonts to apply by hand in `FONT_TODO.md`. The v4 log stays in `CHANGELOG_REDESIGN.md`.

## Designs
- v5 (all edits here): `DAHbgWuPK9Q`, "Shape as Strategy – v5 (clean build)". It is a `copy-design` of the source, used only as a container for the 21 images.
  - Pages 1–8: the new build.
  - Pages 9–16: the old pages, kept as an archive. **Delete them by hand** (there is no delete-page tool).
- Never touched: source `DAHbdUqdmXU`, v1 `DAHbdcxBdW8`, mature v3 `DAHbe2V7_bw`, binder v3 `DAHbfDlGsaE`, v4 `DAHbgHFq6rM`. v4 was not opened.

## New page IDs
| Slide | Page ID | Composition (source) |
|---|---|---|
| 1 | `PBg73DgvCbvF3bLt` | L1 pink poster |
| 2 | `PBS7NMdJqR3ST178` | L2 STYLING BOARD + L1 FAKE PLASTIC page |
| 3 | `PB841vYtlvwcYsgZ` | L1 spread with pink sheet + marker quote |
| 4 | `PBJYrz3XNfms06sn` | L1 b/w spread with pink sheet |
| 5 | `PBzCxJ4HvDrMsT9M` | L2 ULTIMATE EDIT cascade |
| 6 | `PBkVpcpTsqngs5T7` | L1 legs/shoes spread |
| 7 | `PBYdc5jVlnCMvF0v` | L1 coffee-ring poster |
| 8 | `PBF7xzHBJQPn8bm8` | L1 exhibition poster |

## Assets (`assets_v5/`, code-drawn with `canvas-design`, no AI)
| ID | File | Canva asset ID | Slide |
|---|---|---|---|
| D1 | `D1_coffee_ring.png` | `MAHbgVeUTuY` | 7 |
| D2 | `D2_halftone.png` | `MAHbgWj2OXY` | 8 |
| D5 | `D5_flourish.png` | `MAHbgdYhY6c` | 3 |

## Literal third-party placements (credits are your decision)
| File | Crop | Canva asset ID | Slide | Role |
|---|---|---|---|---|
| `Reference images/Flower Farm Business Card _ Business Card Design.jpeg` (Half Acre card) | `assets_v5/R1_halfacre_watercolour_crop.png`, watercolour band, no text | `MAHbgT6tVLQ` | 1 | top band of the cover poster |
| `Reference images/Studio Nomad __ Script Family.jpeg` | `assets_v5/R2_studionomad_foil_crop.png`, silver foil strip, no text | `MAHbgd_O8lM` | 8 | vertical strip beside the title column |

## Log
- 2026-11-21: GATE 0 manifest, GATE 1 plan, GATE 2 decor and uploads. Every gate was pre-approved ("ok for all from now").
- 2026-11-21: 8 pages were added and reordered to the front. Each page was built in 2 `edit-design` calls (create, then format), because new element IDs are only returned after the first call. Only `insert_fill`, `add_text` and `insert_shape` were used. No element was copied from an old page.
- 2026-11-21: the similarity audit failed on slide 5 (8 elements within 25 px of old positions) and slide 6 (3 elements). The fixes:
  - Slide 5: the title block moved right (Courrèges l110, "then and now" l120, timeline l122). The quote moved to l790. The middle and right text columns moved up 40 px.
  - Slide 6: "Alaïa" moved up to t520.

## GATE 4 QA (final)
- **Text:** all 123 strings on slides 1–8 match `CONTENT_MANIFEST.json` exactly. This was a programmatic multiset compare per slide: 6/20/9/16/20/25/18/9.
- **Images:** 21 of 21 content images are placed, with asset IDs matching per slide (2: 7, 4: 3, 5: 4, 6: 7). No aspect ratio is off by more than 1%. No content image is cropped out of ratio.
- **Contact sheet:** the PNG export of pages 1–8 succeeded (job `99e7b2c3-1e97-4bcc-b037-8563114d151d`). The container network blocks `export-download.canva.com` (403), so the PNGs were not saved to the repo. Pages were checked by eye from the edit thumbnails.
- **Overflow and legibility:** checked by eye on every page. No text overlaps after the fixes. Recheck after the font swap.
- **Similarity audit**, against old pages 9–16:
  - No background or element colour uses an old hex.
  - Elements within 25 px of an old element's top-left: 1 / 0 / 1 / 2 / 2 / 2 / 2 / 2 on slides 1–8. Every slide is under 3.
  - Most remaining hits are coincidental: a full-page line shape at (0,0) and the header at t44 l80, which sit near the old full-page frames.
