"""Archive Blush asset kit. Code-drawn originals + literal reference crops (named)."""
import math, sys, os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops

OUT = sys.argv[1]; REPO = sys.argv[2]; FD = sys.argv[3]
os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(1961)
PIN = f'{FD}/PinyonScript-Regular.ttf'; REE = f'{FD}/ReenieBeanie.ttf.ttf'
COR = f'{FD}/CormorantGaramond.ttf'; COU = f'{FD}/CourierPrime-Regular.ttf.ttf'

def rgb(h): h = h.lstrip('#'); return np.array([int(h[i:i+2], 16) for i in (0, 2, 4)], float)
INK, ROSE, CREAM, SEPIA, COFFEE, FRAME = map(rgb, ['#453943', '#c16c84', '#fff6ec', '#927160', '#c18d59', '#7d847e'])

def fbm(w, h, octaves=5, base=6):
    acc = np.zeros((h, w)); amp = 1; tot = 0
    for o in range(octaves):
        n = base * 2 ** o
        small = rng.random((max(2, int(h / w * n)), n))
        im = Image.fromarray((small * 255).astype(np.uint8)).resize((w, h), Image.BICUBIC)
        acc += amp * np.asarray(im, float) / 255; tot += amp; amp *= .5
    return acc / tot

def save_rgba(col, alpha, name):
    H, W = alpha.shape
    a = np.zeros((H, W, 4)); a[..., :3] = col; a[..., 3] = np.clip(alpha, 0, 1) * 255
    Image.fromarray(a.astype(np.uint8), 'RGBA').save(f'{OUT}/{name}.png'); print('ok', name, W, H)

# ---------- pencil strokes ----------
def pencil(W, H, paths, col, name, width=3.2, S=3, passes=3):
    m = Image.new('L', (W * S, H * S), 0); d = ImageDraw.Draw(m)
    for pts in paths:
        n = len(pts)
        for p in range(passes):
            off = rng.normal(0, .8, 2)
            for i in range(n - 1):
                t = i / max(1, n - 1)
                press = (.55 + .45 * math.sin(math.pi * t)) * (1 if p == 0 else .6)
                w = max(1, width * press * S * (1 if p == 0 else .55))
                x0, y0 = pts[i]; x1, y1 = pts[i + 1]
                d.line([((x0 + off[0]) * S, (y0 + off[1]) * S), ((x1 + off[0]) * S, (y1 + off[1]) * S)], fill=int(200 + 55 * press), width=int(w))
    m = m.resize((W, H), Image.LANCZOS)
    a = np.asarray(m, float) / 255
    grain = .55 + .45 * fbm(W, H, 3, max(8, W // 6))           # graphite tooth
    save_rgba(col, a * grain, name)

def jit(pts, s=1.2): return [(x + rng.normal(0, s), y + rng.normal(0, s)) for x, y in pts]

def scribbles():
    for tag, col in (('graphite', INK), ('rose', ROSE)):
        # loose loop circle, 1.25 turns, not closed
        W, H = 460, 280; cx, cy = W / 2, H / 2
        pts = [(cx + (190 + 10 * t) * math.cos(a) * (1 + .04 * math.sin(3 * a)), cy + (105 + 8 * t) * math.sin(a))
               for t, a in zip(np.linspace(0, 1, 500), np.linspace(-.4, 2 * math.pi * 1.22 - .4, 500))]
        pencil(W, H, [jit(pts, .6)], col, f'scribble_circle_{tag}')
        # double underline, second pass harder
        W, H = 680, 80
        l1 = [(20 + x, 30 + 6 * math.sin(x / 70) + x * .02) for x in np.linspace(0, 630, 300)]
        l2 = [(40 + x, 52 + 5 * math.sin(x / 55 + 1) - x * .01) for x in np.linspace(0, 590, 300)]
        pencil(W, H, [jit(l1, .4), jit(l2, .4)], col, f'scribble_underline_{tag}', width=3.6)
        # wandering arrow
        W, H = 380, 220
        P0, P1, P2, P3 = (20, 180), (90, 30), (250, 210), (350, 70)
        curve = [((1-t)**3*P0[0]+3*(1-t)**2*t*P1[0]+3*(1-t)*t**2*P2[0]+t**3*P3[0],
                  (1-t)**3*P0[1]+3*(1-t)**2*t*P1[1]+3*(1-t)*t**2*P2[1]+t**3*P3[1]) for t in np.linspace(0, 1, 300)]
        head = [(318, 72), (350, 70), (336, 100)]
        pencil(W, H, [jit(curve, .5), jit(head, .3)], col, f'scribble_arrow_{tag}', width=3.4)
    # asterisk, bracket, squiggle (graphite only)
    W = H = 150; c = 75
    pencil(W, H, [jit([(c + 60 * math.cos(a) * s, c + 60 * math.sin(a) * s) for s in np.linspace(-1, 1, 40)], .5)
                  for a in np.linspace(0, math.pi, 3, endpoint=False) + .3], INK, 'scribble_asterisk', width=3.6)
    W, H = 90, 340
    br = [(60 - 30 * math.sin(math.pi * t) ** .5, 15 + 310 * t) for t in np.linspace(0, 1, 300)]
    pencil(W, H, [jit(br, .4)], INK, 'scribble_bracket', width=3.2)
    W, H = 560, 100
    sq = [(20 + 520 * t + 22 * math.cos(t * 26), 50 + 26 * math.sin(t * 26) * (1 - .3 * t)) for t in np.linspace(0, 1, 900)]
    pencil(W, H, [jit(sq, .3)], INK, 'scribble_loops', width=2.6)

# ---------- coffee rings ----------
def rings(W=900, H=900):
    yy, xx = np.mgrid[0:H, 0:W]; a = np.zeros((H, W))
    warp = (fbm(W, H, 4, 5) - .5) * 30
    for cx, cy, r, s in [(450, 460, 330, 1.0), (540, 400, 280, .6), (300, 650, 120, .35)]:
        d = np.hypot(xx - cx, yy - cy) + warp
        ring = np.exp(-((d - r) / 5) ** 2) * .95 + np.exp(-((d - r + 16) / 18) ** 2) * .25
        gap = (np.sin(np.arctan2(yy - cy, xx - cx) * 2 + s * 4) + 1) / 2
        a += s * (ring * (.3 + .7 * gap) + np.clip(1 - d / r, 0, 1) * .07)
    for _ in range(12):
        x, y, r = rng.uniform(60, 840), rng.uniform(60, 840), rng.uniform(3, 13)
        d = np.hypot(xx - x, yy - y); a += np.exp(-((d - r) / 1.6) ** 2) * .55 + np.clip(1 - d / r, 0, 1) * .25
    save_rgba(COFFEE, np.clip(a * (.75 + .5 * fbm(W, H, 3, 60)), 0, 1) * .8, 'coffee_rings')

# ---------- crease overlay ----------
def creases(W=1920, H=1080):
    w, h, n = 480, 270, 120
    seeds = np.c_[rng.uniform(0, w, n), rng.uniform(0, h, n)]
    yy, xx = np.mgrid[0:h, 0:w]
    d = (xx[..., None] - seeds[:, 0]) ** 2 + (yy[..., None] - seeds[:, 1]) ** 2
    idx = d.argmin(-1); shade = rng.normal(0, .35, n)[idx] + rng.normal(0, .35, n)[idx] * .6
    im = Image.fromarray(((shade - shade.min()) / np.ptp(shade) * 255).astype(np.uint8)).resize((W, H), Image.BICUBIC)
    s = np.asarray(im.filter(ImageFilter.GaussianBlur(2.5)), float) / 255 - .5
    s += (fbm(W, H, 4, 160) - .5) * .2
    a = np.zeros((H, W, 4))
    a[..., :3] = np.where((s > 0)[..., None], np.array([255., 252, 250]), SEPIA * .6)
    a[..., 3] = np.clip(np.abs(s) * 1.5, 0, 1) * 255 * .32
    Image.fromarray(a.astype(np.uint8), 'RGBA').save(f'{OUT}/crease_overlay.png'); print('ok crease_overlay')

# ---------- halftone peach grain (WY) ----------
def halftone(W=1920, H=1080, step=12):
    S = 2; im = Image.new('RGBA', (W * S, H * S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    field = fbm(W, H, 4, 3)
    for j, y in enumerate(range(0, H + step, step)):
        off = step / 2 if j % 2 else 0
        for x in np.arange(off, W + step, step):
            v = field[min(int(y), H - 1), min(int(x), W - 1)]
            r = (v ** 1.8) * step * .5 + rng.normal(0, .3)
            if r > .5:
                c = tuple(int(q) for q in SEPIA) + (int(110 + 80 * v),)
                d.ellipse([x * S - r * S, y * S - r * S, x * S + r * S, y * S + r * S], fill=c)
    im = im.resize((W, H), Image.LANCZOS)
    a = np.asarray(im).copy(); a[..., 3] = (a[..., 3] * .5).astype(np.uint8)
    Image.fromarray(a, 'RGBA').save(f'{OUT}/halftone_peach.png'); print('ok halftone_peach')

# ---------- misted glass ground (WL) ----------
def mist(W=1920, H=1080):
    yy, xx = np.mgrid[0:H, 0:W]
    base = rgb('#cfd0ca'); light = rgb('#eef0ea'); dark = rgb('#a9ada4')
    g = np.clip(1 - (xx / W * .6 + yy / H * .5), 0, 1)
    col = base[None, None] * (1 - g[..., None] * .6) + light[None, None] * g[..., None] * .6
    bok = Image.new('L', (W, H), 0); bd = ImageDraw.Draw(bok)
    for _ in range(160):
        x, y, r = rng.uniform(0, W * .55), rng.uniform(0, H * .5), rng.uniform(4, 22)
        bd.ellipse([x - r, y - r, x + r, y + r], fill=int(rng.uniform(60, 200)))
    b = np.asarray(bok.filter(ImageFilter.GaussianBlur(5)), float)[..., None] / 255
    col = col * (1 - b * .55) + 255 * b * .55
    bars = Image.new('L', (W, H), 0); bd = ImageDraw.Draw(bars)
    for x in (560, 640, 1300):
        bd.rectangle([x, 0, x + 26, H], fill=150)
    bd.ellipse([520, 640, 720, 900], outline=150, width=22); bd.ellipse([1180, 560, 1420, 860], outline=140, width=22)
    br = np.asarray(bars.filter(ImageFilter.GaussianBlur(40)), float)[..., None] / 255
    col = col * (1 - br * .35) + dark * br * .35
    col += ((fbm(W, H, 3, 400) - .5) * 14)[..., None]
    Image.fromarray(np.clip(col, 0, 255).astype(np.uint8)).save(f'{OUT}/ground_mist.png'); print('ok ground_mist')

# ---------- deckled sheets with soft shadow ----------
def sheet(W, H, hexc, name, pad=34, fibre=.06):
    yy, xx = np.mgrid[0:H, 0:W]
    edge = (fbm(W, H, 5, 40) - .5) * 9
    dist = np.minimum.reduce([xx - pad, W - 1 - pad - xx, yy - pad, H - 1 - pad - yy]) + edge
    m = np.clip(dist / 1.5 + .5, 0, 1)
    sh = Image.fromarray((np.clip((dist + 14) / 6, 0, 1) * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(10))
    sh = np.roll(np.asarray(sh, float) / 255, (6, 4), (0, 1)) * .28
    base = rgb(hexc)
    tex = (fbm(W, H, 5, 90) - .5) * 255 * fibre + (fbm(W, H, 2, 4) - .5) * 14
    paper = np.clip(base[None, None] + tex[..., None] - (1 - np.clip(dist / 40, 0, 1))[..., None] * 10, 0, 255)
    rgba = np.zeros((H, W, 4))
    rgba[..., :3] = paper * m[..., None] + rgb('#3a2e2a') * (1 - m[..., None])
    rgba[..., 3] = np.maximum(m, sh * (1 - m)) * 255
    Image.fromarray(rgba.astype(np.uint8), 'RGBA').save(f'{OUT}/{name}.png'); print('ok', name)

# ---------- type helpers ----------
def text_png(txt, font, size, col, name, pad=40, spacing=0, align='left'):
    f = ImageFont.truetype(font, size)
    tmp = ImageDraw.Draw(Image.new('L', (10, 10)))
    bb = tmp.multiline_textbbox((0, 0), txt, font=f, spacing=spacing, align=align)
    W, H = bb[2] - bb[0] + 2 * pad, bb[3] - bb[1] + 2 * pad
    m = Image.new('L', (W, H), 0); ImageDraw.Draw(m).multiline_text((pad - bb[0], pad - bb[1]), txt, font=f, fill=255, spacing=spacing, align=align)
    a = np.asarray(m, float) / 255
    save_rgba(col, a * (.9 + .1 * fbm(W, H, 2, 30)), name)
    return W, H

def monogram(col, name):
    W, H, S = 360, 230, 4
    m = Image.new('L', (W * S, H * S), 0); d = ImageDraw.Draw(m)
    d.rounded_rectangle([10 * S, 10 * S, (W - 10) * S, (H - 10) * S], radius=105 * S, outline=255, width=int(2.4 * S))
    f = ImageFont.truetype(COR, 92 * S)
    d.text((95 * S, 18 * S), 'e', font=f, fill=255)
    d.line([(150 * S, 182 * S), (212 * S, 48 * S)], fill=255, width=int(2.4 * S))
    d.text((205 * S, 72 * S), 's', font=f, fill=255)
    a = np.asarray(m.resize((W, H), Image.LANCZOS), float) / 255
    save_rgba(col, a, name)

def stamp():
    W = H = 420; S = 3; c = W * S / 2
    m = Image.new('L', (W * S, W * S), 0); d = ImageDraw.Draw(m)
    for r, w in ((200, 5), (186, 2), (128, 2)):
        d.ellipse([c - r * S, c - r * S, c + r * S, c + r * S], outline=255, width=w * S)
    f = ImageFont.truetype(COU, 22 * S)
    txt = 'ESMOD PARIS · 2026 · SHAPE AS STRATEGY · '
    n = len(txt)
    for i, ch in enumerate(txt):
        a = 2 * math.pi * i / n - math.pi / 2
        ci = Image.new('L', (40 * S, 40 * S), 0); ImageDraw.Draw(ci).text((10 * S, 4 * S), ch, font=f, fill=255)
        ci = ci.rotate(-math.degrees(a) - 90, resample=Image.BICUBIC)
        x = c + 157 * S * math.cos(a) - 20 * S; y = c + 157 * S * math.sin(a) - 20 * S
        m.paste(255, (int(x), int(y)), ci)
    fp = ImageFont.truetype(PIN, 120 * S)
    bb = d.textbbox((0, 0), 'ES', font=fp); d.text((c - (bb[2] + bb[0]) / 2, c - (bb[3] + bb[1]) / 2), 'ES', font=fp, fill=255)
    a = np.asarray(m.resize((W, H), Image.LANCZOS), float) / 255
    wear = np.clip(fbm(W, H, 4, 40) * 1.6 - .25, 0, 1)
    save_rgba(ROSE, a * wear * .9, 'stamp_es')

def dotmatrix(txt, name, size=230, step=7, ink=False, rad=2.1):
    f = ImageFont.truetype(PIN, size); tmp = ImageDraw.Draw(Image.new('L', (10, 10)))
    bb = tmp.textbbox((0, 0), txt, font=f); W, H = bb[2] - bb[0] + 60, bb[3] - bb[1] + 60
    m = Image.new('L', (W, H), 0); ImageDraw.Draw(m).text((30 - bb[0], 30 - bb[1]), txt, font=f, fill=255)
    mm = np.asarray(m.filter(ImageFilter.MinFilter(3)))
    S = 3; out = Image.new('RGBA', (W * S, H * S), (0, 0, 0, 0)); d = ImageDraw.Draw(out)
    for y in range(0, H, step):
        for x in range((y // step % 2) * step // 2, W, step):
            if mm[y, x] > 128:
                t = x / W; c = INK if ink else (1 - t) * rgb('#8d8f99') + t * rgb('#c9cbd3')
                r = rad * S; d.ellipse([x * S - r, y * S - r, x * S + r, y * S + r], fill=tuple(int(v) for v in c) + (255,))
    out.resize((W, H), Image.LANCZOS).save(f'{OUT}/{name}.png'); print('ok', name, W, H)

def foil(W=1920, H=640):
    f1 = fbm(W, H, 4, 3); ridge = 1 - np.abs(np.sin(f1 * 9)); ridge = np.asarray(Image.fromarray((ridge*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(6)), float)/255
    v = np.clip(.55 + .45 * ridge ** 3 - .25 * fbm(W, H, 3, 3), 0, 1)
    lo, mid, hi = rgb('#7c8494'), rgb('#bbc3d4'), rgb('#f4f6fa')
    col = np.where(v[..., None] < .5, lo + (mid - lo) * (v[..., None] * 2), mid + (hi - mid) * (v[..., None] * 2 - 1))
    col += ((fbm(W, H, 3, 300) - .5) * 10)[..., None]
    Image.fromarray(np.clip(col, 0, 255).astype(np.uint8)).save(f'{OUT}/foil_sleeve.png'); print('ok foil_sleeve')

def torn_strip(hexc, name, W=1920, H=48):
    yy, xx = np.mgrid[0:H, 0:W]
    edge = 18 + (fbm(W, 1, 6, 30)[0] - .5) * 26 + (rng.random(W) - .5) * 3
    a = np.clip((edge[None, :] - yy) / 1.2 + .5, 0, 1)
    fib = np.clip((edge[None, :] + 4 - yy) / 2.5, 0, 1) * .5           # paler fibre lip
    col = np.zeros((H, W, 3)) + rgb(hexc)
    col = col * (1 - (fib - a * .5)[..., None] * .0) + ((fbm(W, H, 4, 120) - .5) * 14)[..., None]
    alpha = np.maximum(a, fib * .6)
    out = np.zeros((H, W, 4)); out[..., :3] = np.clip(col, 0, 255); out[..., 3] = alpha * 255
    Image.fromarray(out.astype(np.uint8), 'RGBA').save(f'{OUT}/{name}.png'); print('ok', name)

# ---------- literal reference cutouts ----------
def ink_cut(src, box, col, name, scale=3, thr_pct=12, keep=None):
    im = Image.open(src).convert('L').crop(box)
    im = im.resize((im.width * scale, im.height * scale), Image.LANCZOS)
    a = np.asarray(im, float)
    lo = np.percentile(a, thr_pct); hi = np.percentile(a, 60)
    alpha = np.clip((hi - a) / max(1, hi - lo), 0, 1) ** 1.3
    if keep is not None: alpha *= keep(alpha.shape)
    save_rgba(col, alpha, name)

def wl_frame():
    src = f'{REPO}/Reference images/Истории • Instagram.jpeg'
    box = (20, 95, 725, 610); W, H = (box[2] - box[0]) * 2, (box[3] - box[1]) * 2
    def keep(shape):
        h, w = shape; yy, xx = np.mgrid[0:h, 0:w]
        # erase the lettering inside the frame: ellipse interior (coords in 2x crop space)
        cx, cy, rx, ry = 395 * 2 - 40, 270 * 2 - 190, 260 * 2, 150 * 2
        inside = ((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2 < 1
        return np.where(inside, 0, 1)
    from scipy import ndimage
    im = Image.open(src).convert('L').crop(box); im = im.resize((W, H), Image.LANCZOS)
    a = np.asarray(im, float); lo = np.percentile(a, 6); hi = np.percentile(a, 60)
    alpha = np.clip((hi - a) / max(1, hi - lo), 0, 1) ** 1.3
    lab, n = ndimage.label(alpha > .35)
    sizes = ndimage.sum(np.ones_like(lab), lab, range(1, n + 1))
    objs = ndimage.find_objects(lab); biggest = int(np.argmax(sizes)) + 1; keep_ids = []
    for i, sl in enumerate(objs, 1):
        y0, y1, x0, x1 = sl[0].start, sl[0].stop, sl[1].start, sl[1].stop
        inside = x0 > 250 and x1 < 1180 and y0 > 200 and y1 < 760
        if i == biggest or (sizes[i - 1] > 150 and not inside): keep_ids.append(i)
    keepm = ndimage.binary_dilation(np.isin(lab, keep_ids), iterations=4)
    alpha = alpha * keepm
    alpha[int(H * .88):, int(W * .6):] = 0
    save_rgba(FRAME, alpha, 'wl_frame_empty')

def sn_swashes():
    src = f'{REPO}/Reference images/Studio Nomad __ Script Family.jpeg'
    ink_cut(src, (378, 18, 505, 125), INK, 'sn_swash_loop', scale=4, thr_pct=4)
    ink_cut(src, (365, 318, 480, 425), INK, 'sn_swash_tail', scale=4, thr_pct=4)

if __name__ == '__main__':
    for f in sys.argv[4:] or ['all']:
        if f in ('scribbles', 'all'): scribbles()
        if f in ('rings', 'all'): rings()
        if f in ('creases', 'all'): creases()
        if f in ('halftone', 'all'): halftone()
        if f in ('mist', 'all'): mist()
        if f in ('foil', 'all'): foil()
        if f in ('sheets', 'all'):
            for c, n in (('#edc6c5', 'pink'), ('#f6f2eb', 'cream'), ('#ebe5d6', 'letter')):
                sheet(900, 1100, c, f'sheet_{n}_portrait'); sheet(1400, 900, c, f'sheet_{n}_landscape')
            sheet(760, 340, '#bbbac1', 'card_label_grey', pad=24, fibre=.03)
        if f in ('marks', 'all'):
            monogram(INK, 'monogram_es_ink'); monogram(CREAM, 'monogram_es_cream'); stamp()
            dotmatrix('Ekisha Sachdeva', 'dotmatrix_name'); dotmatrix('Ekisha Sachdeva', 'dotmatrix_name_ink', ink=True); dotmatrix('Ekisha Sachdeva', 'dotmatrix_name_ink_small', size=120, step=5, ink=True, rad=1.9); dotmatrix('Ekisha Sachdeva', 'dotmatrix_name_ink_bold', size=120, step=4, ink=True, rad=2.0)
            text_png('Ekisha Sachdeva', PIN, 150, INK, 'signature_ink')
            text_png('Portfolio', PIN, 420, INK, 'title_portfolio_ink', pad=60)
            text_png('Portfolio', PIN, 420, CREAM, 'title_portfolio_cream', pad=60)
            text_png('ES', PIN, 300, INK, 'es_script_ink', pad=40)
        if f in ('cuts', 'all'): wl_frame(); sn_swashes()
        if f in ('torn', 'all'): torn_strip('#f6d5de', 'torn_edge_pink')

# ---------- handwritten notes (Reenie Beanie, marker ink) with drawn arrows ----------
MARKER = rgb('#222025')
def note_png(txt, name, size=96, col=None, font=None, pad=30):
    col = MARKER if col is None else col
    f = ImageFont.truetype(font or REE, size); S = 2
    lines = txt.split('\n'); lh = int(size * 1.0)
    tmp = ImageDraw.Draw(Image.new('L', (10, 10)))
    def seg_w(s): b = tmp.textbbox((0, 0), s, font=f); return b[2] - b[0]
    aw = int(size * 1.1)
    widths = [sum(seg_w(p) for p in ln.split('→')) + aw * ln.count('→') for ln in lines]
    W = max(widths) + 2 * pad; H = lh * len(lines) + 2 * pad + int(size * .3)
    m = Image.new('L', (W * S, H * S), 0); d = ImageDraw.Draw(m)
    fS = ImageFont.truetype(font or REE, size * S)
    for i, ln in enumerate(lines):
        x = pad * S; y = (pad + i * lh) * S
        parts = ln.split('→')
        for j, p in enumerate(parts):
            d.text((x, y), p, font=fS, fill=255); x += seg_w(p) * S
            if j < len(parts) - 1:
                cy = y + int(size * .62) * S; x0 = x + int(size * .12) * S; x1 = x + aw * S - int(size * .18) * S
                pts = [(x0 + (x1 - x0) * t, cy + math.sin(t * 3.1) * size * .04 * S) for t in np.linspace(0, 1, 40)]
                d.line(pts, fill=255, width=max(2, int(size * .05 * S)))
                d.line([(x1, cy), (x1 - size * .22 * S, cy - size * .16 * S)], fill=255, width=max(2, int(size * .05 * S)))
                d.line([(x1, cy), (x1 - size * .22 * S, cy + size * .14 * S)], fill=255, width=max(2, int(size * .05 * S)))
                x += aw * S
    a = np.asarray(m.resize((W, H), Image.LANCZOS), float) / 255
    save_rgba(col, a * (.85 + .15 * fbm(W, H, 2, 40)), name)

if __name__ == '__main__' and 'slide2' in sys.argv[4:]:
    text_png('nova', PIN, 340, INK, 'title_nova', pad=50)
    note_png('circles → movement', 'note_circles_movement')
    note_png('curtains,\nnot\nwalls', 'note_curtains_not_walls')
    note_png('discovered\nroom by\nroom.', 'note_discovered_room_by_room')

# ---------- tracked serif caps + script/serif lockup ----------
def tracked_layer(txt, font, size, track):
    f = ImageFont.truetype(font, size); tmp = ImageDraw.Draw(Image.new('L', (10, 10)))
    ws = [tmp.textlength(c, font=f) for c in txt]
    W = int(sum(ws) + track * (len(txt) - 1)); asc, desc = f.getmetrics(); H = asc + desc
    m = Image.new('L', (W + 20, H + 20), 0); d = ImageDraw.Draw(m); x = 10
    for c, w in zip(txt, ws): d.text((x, 10), c, font=f, fill=255); x += w + track
    return m.crop(m.getbbox())

def tracked_png(txt, size, col, name, track, pad=40, font=None):
    m = tracked_layer(txt, font or COR, size, track)
    W, H = m.size[0] + 2 * pad, m.size[1] + 2 * pad
    c = Image.new('L', (W, H), 0); c.paste(m, (pad, pad))
    a = np.asarray(c, float) / 255; save_rgba(col, a * (.9 + .1 * fbm(W, H, 2, 30)), name)

def lockup_png(script, caps, name, col, s_size=300, c_size=110, track=26, pad=40, overlap=.32, xo=.35):
    f = ImageFont.truetype(PIN, s_size); tmp = ImageDraw.Draw(Image.new('L', (10, 10)))
    bb = tmp.textbbox((0, 0), script, font=f)
    sm = Image.new('L', (bb[2] - bb[0] + 20, bb[3] - bb[1] + 20), 0)
    ImageDraw.Draw(sm).text((10 - bb[0], 10 - bb[1]), script, font=f, fill=255); sm = sm.crop(sm.getbbox())
    cm = tracked_layer(caps, COR, c_size, track)
    W = max(sm.size[0], int(sm.size[0] * xo) + cm.size[0]) + 2 * pad
    oy = int(sm.size[1] * (1 - overlap))
    H = max(oy + cm.size[1], sm.size[1]) + 2 * pad
    c = Image.new('L', (W, H), 0)
    c.paste(cm, (pad + int(sm.size[0] * xo), pad + oy))
    c = ImageChops.lighter(c, Image.new('L', (W, H), 0)); s = Image.new('L', (W, H), 0); s.paste(sm, (pad, pad))
    c = ImageChops.lighter(c, s)
    a = np.asarray(c, float) / 255; save_rgba(col, a * (.9 + .1 * fbm(W, H, 2, 30)), name)

if __name__ == '__main__' and 'slide3' in sys.argv[4:]:
    tracked_png('PRETTY PIXIE', 140, INK, 'title_pretty_pixie', track=22)
    lockup_png('Why', 'ESMOD', 'title_why_esmod', INK, xo=1.02, overlap=.55)
