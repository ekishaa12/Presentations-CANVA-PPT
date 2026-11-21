# REDESIGN PLAN — v5 (clean build)

This plan replaces the v4 plan, which is in git history. Content comes from `CONTENT_MANIFEST.json`. Every visual decision comes from `Layout/` (L1, L2) or `Reference images/` (FF, SN, WL, WY). Nothing comes from the old deck. The user approved every gate in advance ("ok for all from now").

Short names for the source files:
- L1 = `Layout/Screenshot 2026-11-21 at 00.21.42.png` (740×1318)
- L2 = `Layout/Screenshot 2026-11-21 at 00.22.16.png` (740×984)
- FF = `Reference images/Flower Farm Business Card _ Business Card Design.jpeg`
- SN = `Reference images/Studio Nomad __ Script Family.jpeg`
- WL = `Reference images/Истории • Instagram.jpeg` ("With Love")
- WY = `Reference images/wooyoung ateez.jpeg` ("Velle est passé")

## 1. Palette (sampled with PIL, median of the region)
| Role | Hex | File | Region (x0,y0,x1,y1) |
|---|---|---|---|
| Poster pink field (cover) | `#f3bdcc` | L1 | (60,200,300,420), top-left pink poster |
| Pink sheet / page | `#dbaeba` | L2 | (500,210,570,300), spread series, pink page |
| Dusty sheet | `#cba4ad` | L1 | (100,720,170,860), spread with pink sheet |
| Mauve (labels, notes) | `#8a6674` | L1 | (400,520,520,600), "FAKE PLASTIC" spread |
| Board cream | `#f6f2eb` | L2 | (130,395,330,420), STYLING BOARD card |
| Poster white (paper) | `#f6f6f5` | L1 | (425,70,445,300), exhibition poster paper |
| Halftone grey (panel, fold) | `#c7c8c4` | L1 | (440,120,580,250), exhibition poster photo |
| Rose accent (numbers, labels) | `#c16c84` | FF | (250,380,420,430), watercolour |
| Script ink (titles) | `#120a12` | SN | dark pixels in (40,60,700,440), script |
| Body ink | `#54585c` | WY | dark pixels in (320,480,640,700), "Velle" script |
| Frame line ink | `#6c756f` | WL | dark pixels in (30,100,710,600), swirl frame |
| Silver | `#bbc3d4` | SN | (250,500,500,600), foil |
| Stain sepia | `#b67f4d` | L1 | dark pixels in (40,900,300,1150), coffee-ring poster |

None of these is one of the banned old hex codes. The raw sample file is in the scratchpad (`palette.json`).

## 2. Type plan
**Option A, recommended: chosen under the blanket ok.** All text stays live, built with `add_text`. You set the fonts by hand from `FONT_TODO.md`:
- Script for titles and short notes: **Pinyon Script**. Source: SN (script family) and WL (copperplate).
- Serif for headings and body: **Cormorant Garamond**. Source: FF ("anna mercer" serif) and L1 FAKE PLASTIC body.
- Sans for labels: **Montserrat**. Source: L2 STYLING BOARD corner labels and L1 poster micro text.

Why A over B: live text keeps the programmatic text QA exact and stays editable. B (PNG titles) would break both.

The cover "Portfolio" is a vector outline of Pinyon Script. Source: SN. Outlining is allowed for the cover only.

## 3. Slide → composition map (Layout DNA)
| Slide | Composition source | How it maps |
|---|---|---|
| 1 Cover | L1 top-left **pink poster**: images in a top band, huge empty pink field, tiny marks | `#f3bdcc` field. A literal FF watercolour crop sits in the top band. "Portfolio" sits low right. The 4 labels are tiny marks down the left edge. |
| 2 NOVA | L2 **STYLING BOARD** (cream card, asymmetric overlapping images, corner labels) + L1 **FAKE PLASTIC** left page (serif title, body columns) | Left page: title + text columns. Right: cream board with the 7 images overlapping; captions as corner and edge labels. |
| 3 Pretty Pixie / Why ESMOD | L1 **spread with pink sheet** (body on sheet, left page) + **marker quote** (right page) | White spread, fold line. Left: pink sheet with the internship text. Right: "Why ESMOD" large, panel text below. |
| 4 Courrèges then | L1 **b/w spread with pink sheet over the left page** | Vogue 1964 spread is a large image. A dusty pink sheet overlaps its left margin and holds the 4 blocks. McCall's and annotations sit in the band below or to the side. |
| 5 Courrèges now | L2 **ULTIMATE EDIT cascade** (white-bordered photos stepping diagonally, tiny caption right) | Right: cascade of the campaign cut-out and 2 SS27 photos over a large faded campaign copy. Left: title, a stacked timeline column, 3 text columns. |
| 6 Alaïa & Demna | L1 **legs/shoes spread** (images across both pages, narrow text column at the outer edge) | Fold at 960. Alaïa images on the left page, Demna on the right. Text columns sit at the outer edges. Shared notes in a bottom band. |
| 7 Phenomenon | L1 **coffee-ring poster** (white field, large stains, small text block lower left, italic quote right) | Stains top-left. Stats across the top right. "my reading" lower left. The question is a large italic quote at lower right. |
| 8 Sources | L1 **exhibition poster** (white paper, thin frame, framed halftone panel, title column left, caption line at the bottom) | Thin frame line. Title column left plus a literal SN foil strip. Lists on a halftone panel. Headers along the bottom. |

**Rules taken from the layouts:**
- Margin 80 px.
- Wide empty fields.
- Overlap is one sheet over one image edge.
- Captions are small and next to their image.
- Body text sits in narrow columns.

## 4. Decor assets (`canvas-design`, code-drawn, `assets_v5/`)
| ID | File | Motif source | Slide |
|---|---|---|---|
| D1 | `D1_coffee_ring.png` | L1 coffee-ring poster | 7 |
| D2 | `D2_halftone.png` | WY halftone grain, L1 exhibition poster halftone | 8 |
| D5 | `D5_flourish.png` | WL swirl frame | 3 |
| stars | Canva shapes (4-point) | SN sparkles | 1, 5 |
| fold / frame lines | Canva shapes | L1 spreads (fold), L1 exhibition poster (frame) | 3, 6, 8 |

## 5. Literal reference placements (third-party: credits are your decision)
| File | Crop | Slide | Role |
|---|---|---|---|
| FF Half Acre card | `R1_halfacre_watercolour_crop.png`: watercolour band, no text | 1 | top band of the poster |
| SN Studio Nomad | `R2_studionomad_foil_crop.png`: silver foil strip, no text | 8 | vertical strip beside the title column |

WY (a photograph of a person) and WL (contains text) are **not** placed literally. They give colour and motif only.

## 6. Build
1. `copy-design` the source into "Shape as Strategy – v5 (clean build)".
2. `add_page` ×8 with sampled backgrounds, then `reorder_page` to put them first.
3. Per page: call 1 creates shapes, images and text. Call 2 formats them (size, colour, image borders). The tool returns the IDs of new elements only after call 1, so formatting needs a second call. This is a deviation from "one call per page".
4. No elements from old pages are used. The 8 old pages stay at the end for you to delete.
