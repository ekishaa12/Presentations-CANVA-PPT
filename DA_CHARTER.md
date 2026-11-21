# DA CHARTER — Shape as Strategy · ESMOD Portfolio

Design `DAHbgasWgM4`. Build pages 1–8. Pages 9–16 are the archive. Content is in `CONTENT_MANIFEST.json` (frozen). Sources:
- L1 = `Layout/Screenshot 2026-11-21 at 00.21.42.png`
- L2 = `Layout/Screenshot 2026-11-21 at 00.22.16.png`
- FF = `Reference images/Flower Farm Business Card _ Business Card Design.jpeg`
- SN = `Reference images/Studio Nomad __ Script Family.jpeg`
- WY = `Reference images/wooyoung ateez.jpeg`
- WL = `Reference images/Истории • Instagram.jpeg`

## 1. Mood
- A couture house's research archive: blush parchment, crumpled card, silver foil and coffee-ringed proofs.
- Copperplate script and pencil scribbles over editorial grids. Hand-made, layered and pinned, never flat.
- Quiet luxury and a busy desk: every margin carries a mark, and every text block sits on a calm sheet.

## 2. Palette (PIL median of the region; "dark/light" = 8th or 95th percentile of pixels)
| Role | Hex | Source, region (x0,y0,x1,y1) |
|---|---|---|
| Crumpled pink card (main sheet) | `#edc6c5` | FF (200,520,560,620) |
| Blush watercolour | `#e9c6c9` | FF (120,110,300,200) |
| Deep rose (accent, numbers) | `#c16c84` | FF (250,380,420,430) |
| Script cream (on dark/rose) | `#fff6ec` | FF (60,250,680,440) light |
| Poster pink (cover field) | `#f3bdcc` | L1 (60,200,300,420) |
| Sugar pink (light field) | `#fedef0` | SN (100,20,400,60) |
| Mauve (labels, notes) | `#8a6674` | L1 FAKE PLASTIC (400,520,520,600) |
| Board cream (paper ground) | `#f6f2eb` | L2 STYLING BOARD (130,395,330,420) |
| Halftone peach (warm paper) | `#faf1e2` | WY (380,180,560,300) |
| Mist grey (cool ground) | `#cfd0ca` | WL (40,40,700,100) |
| Letter paper (aged) | `#c9c4b3` | L1 letter spread (470,1080,560,1150) |
| Foil silver | `#bbc3d4` | SN (250,500,500,600) |
| Frame ink (flourishes) | `#7d847e` | WL (30,100,710,600) dark |
| Script ink (titles) | `#453943` | SN (40,60,700,440) dark |
| Body ink | `#4c5154` | WY (320,480,640,700) dark |
| Marker black (handwriting) | `#222025` | L1 marker spread (185,710,345,860) dark |
| Sepia (photo tint, stains) | `#927160` | L1 pink-poster photo (40,40,150,140) |
| Coffee stain | `#c18d59` | L1 coffee poster (40,900,300,1150) dark |
| Olive (rare accent) | `#837e53` | L2 tights (185,175,235,260) |

## 3. Type roles
| Role | Font | How |
|---|---|---|
| Script display (titles, signature) | **Pinyon Script** (SN, FF copperplate) | PNG, transparent, exact string as alt text |
| Handwritten notes (short display notes, quotes) | **Reenie Beanie** (L1 marker letters) | PNG, exact string as alt text |
| Serif body and headings | **Cormorant Garamond** (FF "anna mercer", L1 FAKE PLASTIC body) | live text, `FONT_TODO.md` |
| Small captions, labels, micro-texts | **Courier Prime** (SN mono labels, L1 exhibition micro text) | live text, `FONT_TODO.md` |

Body fonts are limited to 2: Cormorant Garamond and Courier Prime.

## 4. Motifs and cutouts per source
- **FF:**
  - The pink watercolour petal band.
  - Crumpled pink card texture.
  - The "h/a" oval monogram lockup, reused as an **"e/s" oval** monogram.
  - Vertical side text, reused as a vertical folio.
  - Palm-shadow light.
- **SN:**
  - Copperplate swashes and loops (cropped from "Studio"/"Nomad" tails, with no letters).
  - The 4-point sparkles.
  - The dot-matrix script ("by Peachcreme" dot style), redrawn by me for "Ekisha Sachdeva".
  - The silver foil sleeve.
  - The grey card label, as a caption card.
  - The mono spec lines ("thin / bold / reg.").
- **WY:**
  - Peach halftone grain.
  - "• label" dot-callouts placed on images.
  - The two-line script lockup.
- **WL:**
  - The ink flourish frame, with its spirals and arrow tail. The lettering is erased and "ES" goes inside it.
  - Misted glass ground.
  - Faded wrought-iron shadow.
- **L1:**
  - The pink poster: a photo band and an empty pink field.
  - The exhibition poster: a framed halftone panel and vertical micro columns.
  - The pink sheet laid over a b/w spread.
  - The marker handwriting page.
  - FAKE PLASTIC: a serif title and a flower held in a hand.
  - The legs spread: a cutout over white with a narrow text column.
  - Coffee rings.
  - The handwritten letter held over a spread.
- **L2:**
  - The ULTIMATE EDIT cascade of white-bordered photos.
  - The STYLING BOARD: a cream card with 4 corner labels.
  - The moth specimen.
  - The pink-sheet spread series.

## 5. Composition rules (from L1, L2)
1. Keep a margin of 80 px. Every page has 4 corner labels (L2 STYLING BOARD).
2. One dominant sheet or image. Secondary items overlap its edge by 20–60 px (L1 pink sheet over spread).
3. Photos get a white border of 10–14 px and a soft shadow, and step diagonally (L2 cascade).
4. Captions are small and placed next to their image. Dot-callouts sit on the image (WY).
5. Body text goes in narrow columns of 260–340 px, on a calm sheet with ≥85% opacity behind it.
6. Allow one gesture of scale per page: a giant script word or a giant image.
7. No flat empty area larger than about 15% of the page, except a calm sheet behind text.

## 6. Layer recipe (minimum 10 per slide)
1. Ground: parchment, paper or wash.
2. Sheets and frames.
3. Content images.
4. Supporting imagery.
5. Texture overlay (grain, halftone, crease, stain).
6. Scribbles: circles, underlines, arrows, asterisks.
7. Script PNG titles and live body text.
8. Micro-texts, dot-labels, folio, monogram.
9. Ornaments: sparkles, swashes, dot-matrix.
10. Edge details: corner marks, stamp, torn or deckled edge.

## 7. Banned
- The old deck look: binder frame and rings, shadow stack, blue selection box or cursor, UI mock, rotated giant titles, price-tag cards, taped edges, hand-drawn ellipses on cut-outs.
- Old hexes: #ed8fbc #ef6aa3 #d05f8b #b2dbde #56d3e7 #adc9df #d5e37e #8b79b8 #2f6fd8 #efeee8 #f6f3ea #fffdf8 #373632 #1a1c20.
- AI pictures of real people, garments, designers or campaigns.
- Invented facts, quotes, numbers or opinions.
- Any version label in a name.

## 8. Reviewer scoring (1–10 each)
1. Closeness to references and Layout.
2. Richness and density (≥10 layers, finish).
3. Lived-in naturalness.
4. Hierarchy, composition and use of space.
5. Legibility and contrast.
6. Distance from the old deck.
7. Content integrity.

To pass: average ≥8, every criterion ≥7, and criterion 7 = 10.

## 9. Shared asset kit (built once, reused)
- **Grounds:**
  - G1 parchment (AI): `aged blush parchment paper texture, soft fibres, faint foxing, flat lay, no text, 16:9`.
  - G2 crumpled pink card (AI, FF tone).
  - G3 misted glass (AI, WL tone).
  - G4 code-drawn halftone peach grain (WY).
- **Overlays (code-drawn PNG):** crease map, coffee rings (L1), pencil scribble set (circle, double underline, arrow, asterisk, bracket, cross-out tick), deckled-edge sheet masks.
- **Cutouts:**
  - SN swash loops ×3, SN sparkle ×4, SN foil strip.
  - FF watercolour band.
  - WL frame with the lettering erased.
  - L2 moth (AI specimen moth, not copied).
- **Personal kit:**
  - "e/s" oval monogram (FF lockup).
  - "ES" in the WL frame.
  - "Ekisha Sachdeva" Pinyon signature.
  - "Ekisha Sachdeva" dot-matrix (SN).
  - Vertical folio "ESMOD PARIS · 2026".
  - Page markers "01/08" … "08/08".

## 10. Slide plan
Micro-texts are decorative only: they reuse manifest words, page numbers or image-part labels. Every one is logged in `CHANGELOG_REDESIGN.md`.

| # | Composition (source) | Copied and new elements | Added micro-texts | Personal |
|---|---|---|---|---|
| 1 Cover | L1 pink poster: photo band on top, empty pink field (G2 + FF watercolour band) | FF watercolour band, SN swashes around "Portfolio" (Pinyon PNG), SN sparkles, foil strip, crease overlay, deckled edge, corner labels | "01/08", "• shape", "• strategy" | e/s oval monogram, dot-matrix name, signature, vertical folio |
| 2 NOVA | L2 STYLING BOARD (cream card, overlapping images) + L1 FAKE PLASTIC page | 7 content images on the board with white borders; moth (AI); pencil arrows tracing the journey; floor-plan circle scribbles; coffee ring; grain | "02/08", "• portal", "• wardrobe", "• salon" (words from the journey string) | ES monogram corner, folio |
| 3 Pretty Pixie / Why ESMOD | L1 pink sheet spread + marker page | Pink crumpled sheet holding the internship text; "Why ESMOD" Pinyon PNG; marker underline; WL flourish frame; misted ground; sparkles | "03/08", "• New Delhi", "• Gurugram" | signature, folio |
| 4 Courrèges then | L1 b/w spread with pink sheet over the left page | 3 content images (Vogue 1964 large, b/w); dusty pink sheet over the left edge with 4 blocks; halftone overlay; pencil circles on silhouette; foil strip | "04/08", "• 1961", "• 1964", "• white" | folio, monogram stamp |
| 5 Courrèges now | L2 ULTIMATE EDIT cascade | 4 content images stepping with white borders; large faded campaign behind; timeline column on a letter-paper strip; scribble arrows between years; SN mono spec lines | "05/08", "then / now" | folio |
| 6 Alaïa & Demna | L1 legs spread (fold, outer text columns) | 7 content images; WL ink frame around "&"; dot-callouts "• silhouette" on images; coffee ring; deckled sheets behind text | "06/08", "• silhouette", "• shoulder", "• hem" | signature, folio |
| 7 Phenomenon | L1 coffee-ring poster + L1 handwritten-letter spread | Big coffee rings; stats on aged letter paper; the question in Pinyon PNG; marker circles around +42%, +525%, +49%; parchment ground | "07/08", "• attention", "• desire" (from the existing copy) | folio |
| 8 Sources | L1 exhibition poster (framed halftone panel, vertical micro columns) | Halftone panel holding the lists; SN foil strip; title column in Pinyon PNG; vertical folio columns; stamp | "08/08", "• archive" | e/s oval monogram, signature closing the deck |

**Cover gate (GATE 2):** 3 variants inside this charter.
- A, Pink poster: the L1 pink field and FF band.
- B, Foil and script: the SN foil sleeve, a sugar-pink band and swashes.
- C, Misted love letter: the WL misted glass, the ES flourish frame and the letter paper.
