# CHANGELOG — Shape as Strategy v4 (redesign)

## Designs
- Source (read-only, never edited): `DAHbdUqdmXU`, "Shape as Strategy – v2 (working copy)". It was resolved from https://canva.link/ww2ho1fyqv97176.
- Working copy (all edits here): `DAHbgHFq6rM`, "Shape as Strategy – v4 (redesign)".
  - Edit: https://www.canva.com/d/2GfXRaYXUVmCqlo
  - View: https://www.canva.com/d/sPFyOg82XvfkonZ
- Never touched: v1 `DAHbdcxBdW8`, v2 `DAHbdUqdmXU`, mature v3 `DAHbe2V7_bw`, binder v3 `DAHbfDlGsaE`.

## Decor assets (code-drawn with `canvas-design`, `assets/`, no AI)
| ID | File | Canva asset ID | Used on |
|---|---|---|---|
| A1 | `assets/A1_blush_wash.png` | `MAHbgMK4Y6c` | slide 1 background |
| A2 | `assets/A2_crumple_grain.png` | `MAHbgPRE1NA` | uploaded, not placed |
| A3 | `assets/A3_halftone_grain.png` | `MAHbgCevHU4` | uploaded, not placed |
| A4 | `assets/A4_flourish_frame.png` | `MAHbgDRsztk` | slide 7, "my reading" |
| A6 | `assets/A6_coffee_ring.png` | `MAHbgASWbu4` | slide 8 |

- The cover wordmark "Portfolio" is a vector outline of Pinyon Script (OFL font), drawn with fontTools. It replaces the old blue vector. Element: `PBLyg1NDD9Z1XnfZ-LB3gL3GK33HbhvTd`.
- Stars, dot markers, crop marks and hairlines are Canva shapes drawn by path.

## Log
- 2026-11-21: `copy-design` of `DAHbdUqdmXU` produced `DAHbgHFq6rM`. The title was changed and committed.
- 2026-11-21: the 5 assets were uploaded through `upload-asset-from-url` from the public repo at commit `3dff142`.
- 2026-11-21: slides 1–8 were restyled and committed, one page per transaction. The user pre-approved all gates ("ok for all dont ask again").
  - Removed on every page: the binder frame (paper sheet, shadow stack, grain, wavy lines, fold, binding band, all 6 rings and their layers) and the old candy backdrops. The old decor went too: blue swirls, selection box, cursor, ellipse outlines, asterisks, tape, punch holes, ruled lines, swatches, and the blue or cyan cards.
  - Applied: cream field `#f4efe6`, blush sheets `#f2d4df`, ivory offset sheets `#fbf8f2`. Ink `#23272d` / `#3a414a`, deep rose `#b45f82` for labels, rose `#d98aa8` for decor. Images became prints with a 10–12 px ivory border, some with ±2–3° tilt.
  - Slide 6: the old fold (`LBdyW4xTpLjwJhHk`, `LBdMhxSXpRXv68gj`) was kept on purpose as the spread's fold.
- 2026-11-21: QA passed.
  - Every text string is identical to the source on all 8 slides, checked by programmatic multiset compare against the pre-edit data.
  - 21 content images: slide 2 has 7, slide 4 has 3, slide 5 has 4, slide 6 has 7. All aspect ratios are unchanged (within 1%).
  - The contact-sheet export ran, but the container network blocks the download host. Pages were checked from thumbnails instead.

## Text-affecting changes
Columns: slide, element ID, old → new, reason.

| Slide | Element | Change | Why |
|---|---|---|---|
| 1 | `LBXdldDwJ3bjzvQN`, `LBxtNw9Vl9fj7Q5N` | size 26 → 22, bold → normal | quieter corner labels for the styling-board layout |
| 1 | `LBQMN2D70G2NHRbp` | size 26 → 22, bold → normal, width 237 → 320, align start → end | right-aligned corner label |
| 1 | `LBzWrMn42THNMF8Z` (`2026`) | size 28 → 22, bold → normal, width 62 → 320, align start → end | right-aligned corner label |
| 1 | `LBfSx0cnvphgWmTV` | width 131 → 300, align start → end | right-aligned header |
| 7 | `LBNfMckNV96RqvWM`, `LB6Ynrrsscy0S6H4` | size 36.8 → 26 | labels overlapped; same fix as handover note (font 26) |

Text colours changed everywhere (palette swap). Colour is aesthetic, so it is not listed per element. No string, line break, line height or letter spacing was changed.
