"""Pink Static zine kit: display type, ghost type, red-ink notes, ballpoint scribbles,
blurred stems, halftone screens and print marks. All code-drawn originals.
Usage: python3 make_zine.py OUT_DIR MONO_DIR [groups...]"""
import math, sys, os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUT, MONO = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)
rng = np.random.default_rng(2026)
INTER = '/usr/share/fonts/opentype/inter/'
SEMI, BOLD, MED = INTER + 'InterDisplay-SemiBold.otf', INTER + 'InterDisplay-Bold.otf', INTER + 'InterDisplay-Medium.otf'
SPACE = f'{MONO}/space-mono-latin-400-normal.woff'
SPACEB = f'{MONO}/space-mono-latin-700-normal.woff'
REE = sys.argv[3] if len(sys.argv) > 3 and sys.argv[3].endswith('.ttf') else None

def rgb(h): h = h.lstrip('#'); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
INK, WHITE, GHOST, RED, GRAPH, PINK = '#141214', '#fffafb', '#f2c6d3', '#b5304b', '#4a4a4a', '#ec9cba'

def save(alpha, col, name, grain=0.0):
    a = np.clip(alpha, 0, 1)
    if grain:
        a = a * (1 - grain * rng.random(a.shape))
    H, W = a.shape
    out = np.zeros((H, W, 4), np.uint8); out[..., :3] = rgb(col); out[..., 3] = (a * 255).astype(np.uint8)
    Image.fromarray(out, 'RGBA').save(f'{OUT}/{name}.png'); print('ok', name, W, H)

def layer(txt, font, size, track):
    f = ImageFont.truetype(font, size); d = ImageDraw.Draw(Image.new('L', (8, 8)))
    ws = [d.textlength(c, font=f) for c in txt]
    asc, desc = f.getmetrics()
    W = int(sum(ws) + track * max(0, len(txt) - 1)) + 40; H = asc + desc + 40
    m = Image.new('L', (W, H), 0); dd = ImageDraw.Draw(m); x = 20
    for c, w in zip(txt, ws):
        dd.text((x, 20), c, font=f, fill=255); x += w + track
    return m.crop(m.getbbox())

def display(lines, name, size, col=INK, font=SEMI, track=-0.06, lead=0.74, offs=None, pad=10, grain=0.0):
    """Stacked display type; lines overlap (lead < 1 of cap height) and can be offset in x."""
    ls = [layer(t, font, size, int(track * size)) for t in lines]
    offs = offs or [0] * len(ls)
    step = int(size * lead)
    W = max(int(o * size) + l.size[0] for o, l in zip(offs, ls)) + 2 * pad
    H = step * (len(ls) - 1) + ls[-1].size[1] + 2 * pad + int(size * 0.25)
    acc = np.zeros((H, W))
    for i, (o, l) in enumerate(zip(offs, ls)):
        y = pad + i * step + (int(size * 0.25) if l.size[1] < size * 0.6 else 0)
        x = pad + int(o * size)
        a = np.asarray(l, float) / 255
        acc[y:y + a.shape[0], x:x + a.shape[1]] = np.maximum(acc[y:y + a.shape[0], x:x + a.shape[1]], a)
    acc = acc[:, :max(1, int(np.nonzero(acc.sum(0))[0].max()) + pad + 1)]
    save(acc, col, name, grain)

def mono_block(txt, name, size, col=GHOST, font=SPACE, lead=1.0, pad=10):
    f = ImageFont.truetype(font, size); d = ImageDraw.Draw(Image.new('L', (8, 8)))
    lines = txt.split('\n'); W = int(max(d.textlength(l, font=f) for l in lines)) + 2 * pad
    H = int(size * lead * len(lines) + size * 0.4) + 2 * pad
    m = Image.new('L', (W, H), 0); dd = ImageDraw.Draw(m)
    for i, l in enumerate(lines): dd.text((pad, pad + i * size * lead), l, font=f, fill=255)
    save(np.asarray(m, float) / 255, col, name)

# ---------- ballpoint / pencil strokes ----------
def stroke(W, H, paths, col, name, width=3.0, passes=2, S=3, alpha=0.92):
    m = Image.new('L', (W * S, H * S), 0); d = ImageDraw.Draw(m)
    for p in paths:
        for k in range(passes):
            pts = [((x + rng.normal(0, 0.8)) * S, (y + rng.normal(0, 0.8)) * S) for x, y in p]
            w = max(1, int(width * S * (0.75 + 0.35 * rng.random())))
            d.line(pts, fill=int(255 * (0.8 if k else 1)), width=w, joint='curve')
    m = m.resize((W, H), Image.LANCZOS).filter(ImageFilter.GaussianBlur(0.4))
    save(np.asarray(m, float) / 255 * alpha, col, name, grain=0.12)

def ellipse(cx, cy, rx, ry, turns=1.15, wob=0.06, start=0.3):
    n = int(220 * turns); out = []
    for i in range(n):
        t = start + 2 * math.pi * turns * i / n
        r = 1 + wob * math.sin(3 * t) + 0.04 * (i / n)
        out.append((cx + rx * r * math.cos(t), cy + ry * r * math.sin(t)))
    return out

def scribbles(col, tag):
    stroke(600, 300, [ellipse(300, 150, 270, 120)], col, f'sc_circle_{tag}')
    stroke(700, 70, [[(10 + i * 6.8, 30 + 4 * math.sin(i / 9)) for i in range(100)],
                     [(30 + i * 6.5, 50 + 3 * math.sin(i / 7 + 1)) for i in range(100)]], col, f'sc_underline_{tag}')
    arrow = [(20 + i * 4.6, 160 - 120 * math.sin(i / 100 * math.pi * .55) + 10 * math.sin(i / 12)) for i in range(100)]
    hx, hy = arrow[-1]
    stroke(520, 200, [arrow, [(hx - 38, hy - 4), (hx, hy), (hx - 22, hy + 30)]], col, f'sc_arrow_{tag}')
    stroke(140, 140, [[(70, 10), (70, 130)], [(15, 40), (125, 100)], [(15, 100), (125, 40)]], col, f'sc_asterisk_{tag}', width=3.5)
    stroke(420, 120, [[(10, 60 + 30 * math.sin(i / 6)) if False else (10 + i * 4, 60 + 28 * math.sin(i / 5.5)) for i in range(100)]], col, f'sc_wave_{tag}')
    stroke(300, 110, [[(10, 90), (290, 20)], [(10, 25), (290, 95)]], col, f'sc_cross_{tag}')
    stroke(80, 420, [[(60, 10), (25, 40), (30, 200), (8, 210), (30, 220), (25, 380), (60, 410)]], col, f'sc_bracket_{tag}')
    stroke(220, 160, [[(10, 90), (70, 150), (210, 10)]], col, f'sc_tick_{tag}', width=4)
    stroke(700, 220, [ellipse(350, 110, 330, 90, turns=2.2, wob=0.1)], col, f'sc_loop_{tag}', width=2.4)

# ---------- handwritten notes (Reenie Beanie) in red ballpoint ----------
def note(txt, name, size=92, col=RED):
    f = ImageFont.truetype(REE, size); d = ImageDraw.Draw(Image.new('L', (8, 8)))
    lines = txt.split('\n'); W = int(max(d.textlength(l, font=f) for l in lines)) + 40
    H = int(size * len(lines) + size * 0.35) + 30
    m = Image.new('L', (W * 2, H * 2), 0); dd = ImageDraw.Draw(m); f2 = ImageFont.truetype(REE, size * 2)
    for i, l in enumerate(lines):
        x = 20 * 2
        for part_i, part in enumerate(l.split('→')):
            dd.text((x, (15 + i * size) * 2), part, font=f2, fill=255); x += int(d.textlength(part, font=f)) * 2
            if part_i < l.count('→'):
                cy = (15 + i * size + size * 0.6) * 2
                dd.line([(x + 10, cy), (x + size * 1.6, cy)], fill=255, width=6)
                dd.line([(x + size * 1.6, cy), (x + size * 1.2, cy - 22)], fill=255, width=6)
                dd.line([(x + size * 1.6, cy), (x + size * 1.2, cy + 22)], fill=255, width=6)
                x += int(size * 1.9)
    m = m.resize((W, H), Image.LANCZOS)
    save(np.asarray(m, float) / 255, col, name, grain=0.1)

# ---------- blurred red stems (after the zine's blurred-flower spread) ----------
def stems(W=900, H=1200):
    m = Image.new('L', (W, H), 0); d = ImageDraw.Draw(m)
    for k in range(9):
        x0 = rng.uniform(120, W - 120); y0 = H - rng.uniform(0, 80)
        x1 = x0 + rng.normal(0, 90); y1 = rng.uniform(180, 600)
        pts = [(x0 + (x1 - x0) * t + 25 * math.sin(t * 4 + k), y0 + (y1 - y0) * t) for t in np.linspace(0, 1, 60)]
        d.line(pts, fill=200, width=int(rng.uniform(3, 7)))
        for j in range(int(rng.uniform(3, 8))):
            cx, cy = x1 + rng.normal(0, 40), y1 + rng.normal(0, 40); r = rng.uniform(8, 28)
            d.ellipse([cx - r, cy - r * .7, cx + r, cy + r * .7], fill=230)
            d.line([(x1, y1), (cx, cy)], fill=180, width=3)
    a = np.asarray(m, float) / 255
    mb = np.zeros_like(a)
    for s in range(0, 60, 3):
        mb += np.roll(a, s, axis=1) * (1 - s / 60)
    mb = mb / mb.max()
    img = Image.fromarray((mb * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(6))
    a = np.asarray(img, float) / 255
    save(a ** 0.8 * 0.85, '#c24257', 'zine_red_stems', grain=0.25)

# ---------- halftone screens ----------
def halftone_disc(W=1000, H=1000, col=PINK, step=11, name='zine_halftone_disc'):
    yy, xx = np.mgrid[0:H, 0:W]
    val = np.clip(1 - np.hypot(xx - W * .5, yy - H * .5) / (W * .5), 0, 1) ** 0.7
    gy, gx = (yy % step) - step / 2, (xx % step) - step / 2
    cell_v = val[(yy // step) * step + step // 2 if False else np.minimum((yy // step) * step + step // 2, H - 1),
                 np.minimum((xx // step) * step + step // 2, W - 1)]
    r = cell_v * step * 0.62
    a = np.clip(r - np.hypot(gx, gy) + 0.5, 0, 1)
    save(a, col, name)

def halftone_band(W=1920, H=520, col=PINK, step=9, name='zine_halftone_band'):
    yy, xx = np.mgrid[0:H, 0:W]
    val = (1 - yy / H) ** 1.3 * (0.6 + 0.4 * np.sin(xx / W * math.pi))
    cy = np.minimum((yy // step) * step + step // 2, H - 1); cx = np.minimum((xx // step) * step + step // 2, W - 1)
    r = val[cy, cx] * step * 0.6
    a = np.clip(r - np.hypot((yy % step) - step / 2, (xx % step) - step / 2) + 0.5, 0, 1)
    save(a, col, name)

# ---------- print marks ----------
def marks():
    m = Image.new('L', (1920, 1080), 0); d = ImageDraw.Draw(m)
    for (x, y, sx, sy) in [(40, 40, 1, 1), (1880, 40, -1, 1), (40, 1040, 1, -1), (1880, 1040, -1, -1)]:
        d.line([(x - 30 * sx, y), (x - 6 * sx, y)], fill=255, width=2); d.line([(x, y - 30 * sy), (x, y - 6 * sy)], fill=255, width=2)
    for cx, cy in [(960, 22), (960, 1058)]:
        d.ellipse([cx - 9, cy - 9, cx + 9, cy + 9], outline=255, width=2)
        d.line([(cx - 15, cy), (cx + 15, cy)], fill=255, width=2); d.line([(cx, cy - 15), (cx, cy + 15)], fill=255, width=2)
    save(np.asarray(m, float) / 255, INK, 'zine_print_marks')
    W, H = 260, 70; a = np.zeros((H, W)); x = 0
    while x < W - 6:
        w = int(rng.choice([2, 2, 3, 4, 6])); a[:, x:x + w] = 1; x += w + int(rng.choice([2, 3, 4, 5]))
    save(a, INK, 'zine_barcode')
    yy, xx = np.mgrid[0:1080, 0:80]
    g = np.exp(-((xx - 40) / 16.0) ** 2) * 0.22 + np.exp(-((xx - 40) / 3.0) ** 2) * 0.18
    save(g, '#6b4a55', 'zine_gutter')

if __name__ == '__main__':
    groups = [g for g in sys.argv[3:] if not g.endswith('.ttf')] or ['all']
    A = lambda g: g in groups or 'all' in groups
    if A('type'):
        display(['(shape', 'as', 'strat', 'egy)'], 'zt_cover', 330, offs=[0, 0.9, 0.15, 0.55])
        display(['nova'], 'zt_nova', 760, track=-0.07)
        display(['PRETTY', 'PIXIE'], 'zt_pixie', 210, lead=0.8, offs=[0, 0.5])
        display(['Why', 'ESMOD'], 'zt_why', 250, lead=0.78, offs=[0.6, 0])
        display(['COURRÈGES'], 'zt_courreges_caps', 170, track=-0.04)
        display(['Cour', 'règes'], 'zt_courreges_white', 360, col=WHITE, offs=[0, 0.7])
        display(['Alaïa'], 'zt_alaia', 330)
        display(['&'], 'zt_amp', 330, font=MED)
        display(['Demna'], 'zt_demna', 330)
        display(['When a designer moves,', 'does desire move with them -', 'or stay with the house?'], 'zt_question', 92, font=MED, track=-0.03, lead=0.92)
        display(['+42%'], 'zt_42', 230, track=-0.05)
        display(['+525%'], 'zt_525', 230, track=-0.05)
        display(['+49%'], 'zt_49', 200, track=-0.05)
        display(['Sources &'], 'zt_sources', 230)
        display(['image', 'credits'], 'zt_credits', 230, lead=0.78, offs=[0.4, 0])
    if A('ghost'):
        for t, n in [('Why\nESMOD', 'zg_why'), ('1965', 'zg_1965'), ('then\nand now', 'zg_then'), ('the\nsilhouette', 'zg_silhouette'),
                     ('desire\nsplits.', 'zg_desire'), ('archive', 'zg_archive'), ('room by\nroom.', 'zg_room'), ('2026', 'zg_2026')]:
            mono_block(t, n, 190, lead=0.95)
    if A('scribbles'):
        scribbles(RED, 'red'); scribbles(GRAPH, 'graphite')
    if A('notes') and REE:
        for t, n in [('circles → movement', 'zn_circles'), ('curtains,\nnot\nwalls', 'zn_curtains'), ('discovered\nroom by\nroom.', 'zn_discovered'),
                     ('a silhouette that\ndefined a decade', 'zn_silhouette'), ('then and now', 'zn_then'),
                     ('with the logo removed,\nis the image still luxury?', 'zn_logo'), ('One\nobsession\nthe\nsilhouette.', 'zn_obsession'),
                     ('signals, not proof of a cause.', 'zn_signals'), ('my reading', 'zn_reading')]:
            note(t, n)
    if A('stems'): stems()
    if A('halftone'): halftone_disc(); halftone_band()
    if A('marks'): marks()
