#!/usr/bin/env python3
"""Draw the news-image-20261123 dense front page: MONDAY 23 NOVEMBER 2026.
31 stories, 6 regions. All scenes are PIL-drawn illustrations."""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (18, 18, 18)
RED = (178, 34, 34)
DARKRED = (139, 0, 0)
BLUE = (23, 58, 112)
STEEL = (58, 96, 140)
GOLD = (176, 124, 20)
TEAL = (14, 110, 105)
GREEN = (34, 110, 60)
GREY = (110, 108, 100)
LIGHT = (232, 226, 214)
MIDLINE = (200, 192, 176)

FD = "/usr/share/fonts/truetype/dejavu/"
FL = "/usr/share/fonts/truetype/liberation/"


def f(path, size):
    return ImageFont.truetype(path, size)


SERIF_B = lambda s: f(FD + "DejaVuSerif-Bold.ttf", s)
SANS = lambda s: f(FL + "LiberationSans-Regular.ttf", s)
SANS_B = lambda s: f(FL + "LiberationSans-Bold.ttf", s)
SANS_I = lambda s: f(FL + "LiberationSans-Italic.ttf", s)
MONO_B = lambda s: f(FD + "DejaVuSansMono-Bold.ttf", s)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img, "RGBA")


def wrap(text, font, width):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= width:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text(x, y, s, font, fill=INK, anchor="la"):
    d.text((x, y), s, font=font, fill=fill, anchor=anchor)


def rrect(box, fill, outline=None, width=1, radius=4):
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def chip(x, y, label, bg, fg=(255, 255, 255)):
    font = SANS_B(10)
    w = d.textlength(label, font=font) + 10
    rrect([x, y, x + w, y + 15], fill=bg, radius=3)
    d.text((x + 5, y + 2), label, font=font, fill=fg)
    return w


# ---------------------------------------------------------------- masthead
d.rectangle([0, 0, W, 66], fill=INK)
text(16, 6, "THE WORLD TODAY", SERIF_B(40), fill=(247, 243, 234))
text(1008, 12, "ONE DAY · ONE PAGE", SANS_B(13), fill=(220, 200, 120), anchor="ra")
text(1008, 32, "MONDAY 23 NOVEMBER 2026", SANS_B(15), fill=(255, 255, 255), anchor="ra")
text(16, 46, "THE DAY'S WORLD NEWS — 31 STORIES, 6 REGIONS", SANS_B(11),
     fill=(190, 190, 185))

# kicker
text(16, 74, "MARKETS ROUT  ·  UN CALLS FOR AI RULES  ·  AMERICA'S ASIA LEAD AT RECORD LOW",
     SANS_B(13), fill=RED)
d.line([16, 94, 1008, 94], fill=INK, width=2)

# ---------------------------------------------------------------- number strip
nums = [
    ("-3.3%", "KOSPI, SEOUL", RED),
    ("5.3", "US-CHINA POWER GAP", BLUE),
    ("11,762", "EBOLA CASES, DRC", TEAL),
    ("$450M", "SKUBAL TO THE METS", GREEN),
    ("165", "RUSSIAN MISSILES / WEEK", DARKRED),
]
cw = 996 / 5
for i, (n, lab, col) in enumerate(nums):
    x = 16 + i * cw
    text(x + cw / 2, 100, n, SANS_B(30), fill=col, anchor="ma")
    text(x + cw / 2, 134, lab, SANS_B(10), fill=GREY, anchor="ma")
    if i:
        d.line([x, 102, x, 146], fill=MIDLINE, width=1)
d.line([16, 152, 1008, 152], fill=INK, width=1)

# ---------------------------------------------------------------- region bar
regions = [
    ("ASIA-PACIFIC", 7, RED), ("AMERICAS", 8, BLUE), ("EUROPE", 6, GOLD),
    ("MIDDLE EAST", 7, TEAL), ("AFRICA", 2, GREEN), ("WORLD", 1, (90, 60, 140)),
]
x = 16
for name, n, col in regions:
    lab = f"{name} {n}"
    w = d.textlength(lab, font=SANS_B(12)) + 26
    rrect([x, 160, x + w, 182], fill=col, radius=3)
    d.text((x + 13, 165), lab, font=SANS_B(12), fill=(255, 255, 255))
    x += w + 8
text(1008, 164, "31 STORIES TOTAL", SANS_B(12), fill=INK, anchor="ra")

# ---------------------------------------------------------------- THE DAY IN UTC
d.rectangle([16, 192, 1008, 216], fill=BLUE)
text(26, 197, "THE DAY IN UTC", SANS_B(13), fill=(255, 255, 255))
utc = [
    ("~02:00", "KOSPI OPENS"),
    ("~06:00", "GUTERRES"),
    ("~09:00", "PARIS TAX"),
    ("~11:00", "POLAND MISSILES"),
    ("~15:00", "SKUBAL $450M"),
    ("~20:00", "ANTHROPIC IPO"),
]
ux = 150
for t, lab in utc:
    text(ux, 198, t, MONO_B(12), fill=(220, 200, 120))
    tw = d.textlength(t, font=MONO_B(12))
    text(ux + tw + 6, 198, lab, SANS_B(11), fill=(255, 255, 255))
    ux += tw + 6 + d.textlength(lab, font=SANS_B(11)) + 26

# ---------------------------------------------------------------- hero scenes
def scene_kospi(x0, y0, w, h):
    d.rectangle([x0, y0, x0 + w, y0 + h], fill=(24, 24, 30))
    # candlesticks
    import random
    random.seed(7)
    base = y0 + 18
    px = x0 + 14
    price = base + 8
    pts = []
    for i in range(9):
        hh = random.randint(8, 22)
        d.rectangle([px, price, px + 16, price + hh], fill=RED if i % 2 else (200, 60, 60))
        d.line([px + 8, price - 6, px + 8, price + hh + 6], fill=(220, 220, 220), width=2)
        pts.append((px + 8, price + hh // 2))
        price += random.randint(6, 12)
        px += 30
    d.line(pts, fill=(255, 210, 60), width=3)
    # big down arrow
    d.polygon([(x0 + w - 52, y0 + 16), (x0 + w - 20, y0 + 16), (x0 + w - 20, y0 + 44),
               (x0 + w - 6, y0 + 44), (x0 + w - 36, y0 + 84), (x0 + w - 66, y0 + 44),
               (x0 + w - 52, y0 + 44)], fill=(255, 70, 60))
    text(x0 + 12, y0 + h - 26, "-3.3%", SANS_B(24), fill=(255, 90, 80))


def scene_guterres(x0, y0, w, h):
    d.rectangle([x0, y0, x0 + w, y0 + h], fill=(18, 48, 92))
    # UN emblem: circle + laurel arcs
    cx, cy = x0 + w // 2, y0 + 52
    d.ellipse([cx - 30, cy - 30, cx + 30, cy + 30], outline=(255, 255, 255), width=3)
    d.ellipse([cx - 16, cy - 16, cx + 16, cy + 16], fill=(120, 170, 220))
    d.line([cx - 30, cy, cx + 30, cy], fill=(255, 255, 255), width=2)
    d.line([cx, cy - 30, cx, cy + 30], fill=(255, 255, 255), width=2)
    d.arc([cx - 22, cy - 30, cx + 22, cy + 30], 0, 360, fill=(255, 255, 255), width=1)
    # podium
    d.rectangle([x0 + w // 2 - 46, y0 + h - 34, x0 + w // 2 + 46, y0 + h], fill=(120, 90, 50))
    d.rectangle([x0 + w // 2 - 46, y0 + h - 34, x0 + w // 2 + 46, y0 + h - 26], fill=(200, 170, 110))
    # flags
    for i, col in enumerate([(178, 34, 34), (23, 58, 112), (34, 110, 60), (176, 124, 20)]):
        fx = x0 + 18 + i * 22
        d.line([fx, y0 + h - 52, fx, y0 + h - 26], fill=(255, 255, 255), width=2)
        d.polygon([(fx, y0 + h - 52), (fx + 18, y0 + h - 48), (fx, y0 + h - 44)], fill=col)
    text(x0 + 12, y0 + 8, "BRIDGETOWN", SANS_B(11), fill=(255, 210, 60))


def scene_power(x0, y0, w, h):
    d.rectangle([x0, y0, x0 + w, y0 + h], fill=(240, 236, 224))
    # bars US 78.9 vs China 73.6
    bx, by = x0 + 30, y0 + h - 18
    us_h = int((h - 52) * 78.9 / 80)
    cn_h = int((h - 52) * 73.6 / 80)
    d.rectangle([bx, by - us_h, bx + 74, by], fill=BLUE)
    d.rectangle([bx + 104, by - cn_h, bx + 178, by], fill=RED)
    text(bx + 37, by - us_h - 20, "78.9", SANS_B(17), fill=BLUE, anchor="ma")
    text(bx + 141, by - cn_h - 20, "73.6", SANS_B(17), fill=RED, anchor="ma")
    text(bx + 37, by + 2, "USA", SANS_B(11), fill=INK, anchor="ma")
    text(bx + 141, by + 2, "CHINA", SANS_B(11), fill=INK, anchor="ma")
    # gap arrow
    d.line([bx + 74, by - us_h, bx + 104, by - cn_h], fill=GOLD, width=3)
    text(x0 + w - 8, y0 + 8, "GAP 5.3", SANS_B(13), fill=GOLD, anchor="ra")
    text(x0 + 12, y0 + 8, "ASIA POWER INDEX 2026", SANS_B(10), fill=GREY)


heroes = [
    ("AI ROUT HITS ASIA", "KOSPI -3.3% as the AI sell-off spreads from Wall Street. Seoul closes 4,708.54, down 161 points, intraday -5.8%; Samsung -3.1%, SK Hynix -2.5%.",
     "SEOUL · REPORTED", RED, scene_kospi),
    ("GUTERRES: REGULATE AI BEFORE IT'S TOO LATE", "UN chief urges global AI safety rules at the Bridgetown summit. 150 delegates back a risk framework — a blueprint, not a treaty.",
     "BARBADOS · REPORTED", BLUE, scene_guterres),
    ("US LEAD OVER CHINA AT RECORD LOW", "Asia Power Index 2026: US 78.9, China 73.6 — the 5.3-point gap is the narrowest since 2018. US diplomatic influence falls 6 to 76.7; India 3rd at 40.5.",
     "LOWY INSTITUTE · REPORTED", GOLD, scene_power),
]
hy = 226
hw = 318
for i, (head, body, src, col, scene) in enumerate(heroes):
    x0 = 16 + i * (hw + 21)
    rrect([x0, hy, x0 + hw, hy + 246], fill=(255, 255, 255), outline=MIDLINE, width=1, radius=4)
    scene(x0 + 6, hy + 6, hw - 12, 118)
    y = hy + 132
    for ln in wrap(head, SANS_B(15), hw - 20):
        text(x0 + 10, y, ln, SANS_B(15), fill=INK)
        y += 18
    y += 2
    for ln in wrap(body, SANS(12), hw - 20):
        text(x0 + 10, y, ln, SANS(12), fill=(40, 40, 40))
        y += 15
    d.line([x0 + 10, hy + 222, x0 + hw - 10, hy + 222], fill=MIDLINE, width=1)
    text(x0 + 10, hy + 228, src, SANS_B(10), fill=col)
    chip(x0 + hw - 46, hy + 226, "HERO", col)

# ---------------------------------------------------------------- 10 small cards
cards = [
    ("SKUBAL: $450M TO THE METS", "Two-time Cy Young winner signs a nine-year deal — the largest ever for a pitcher.", "NEW YORK · REPORTED", GREEN, "$"),
    ("ANTHROPIC IPO: $107.3B", "Claude maker stages the largest IPO ever, raised at $83 a share on 19 Nov; debut close $97.17.", "NEW YORK · REPORTED", BLUE, "A"),
    ("POLAND: 3 RUSSIAN MISSILES", "Kyiv says three Kh-101 cruise missiles crossed Polish airspace on Friday; Tusk calls it a provocation.", "KYIV · CLAIM", RED, "3"),
    ("COP31: THE DAY AFTER", "Sunday's collapse — 194 nations reject the Antalya pact — draws fury. Guterres 'profoundly frustrated'.", "ANTALYA · REPORTED", TEAL, "C"),
    ("ZELENSKYY: 165 MISSILES A WEEK", "Kyiv says Moscow fired 165 missiles in seven days, as Washington delays Patriot deliveries.", "KYIV · REPORTED", DARKRED, "165"),
    ("MANCHESTER: 12,000 CLEARED", "Thousands cleared after a substance scare in the city centre; no injuries reported.", "MANCHESTER · REPORTED", STEEL, "12k"),
    ("PARIS BACKS 2% BILLIONAIRE TAX", "100+ economists, politicians and unions rally behind France's 2% annual minimum wealth tax.", "PARIS · REPORTED", GOLD, "2%"),
    ("EBOLA: 11,762 CASES IN DRC", "Fighting traps Ebola teams in Ituri; WHO evacuates staff caught in the outbreak zone.", "DRC · REPORTED", TEAL, "E"),
    ("LEBANON SEIZES 264 KG EXPLOSIVES", "Army seizes 264 kg of explosives in a raid; no group has claimed the cache.", "BEIRUT · REPORTED", (90, 60, 140), "264"),
    ("SEOUL READIES 10T-WON FUND", "Seoul readies a 10-trillion-won stabilisation fund as the rout deepens; SK Telecom -7.3%.", "SEOUL · REPORTED", RED, "10T"),
]
cy = 484
ch = 58
for i, (head, body, src, col, glyph) in enumerate(cards):
    row, cc = divmod(i, 2)
    x0 = 16 + cc * (492 + 12)
    y0 = cy + row * (ch + 4)
    rrect([x0, y0, x0 + 492, y0 + ch], fill=(255, 255, 255), outline=MIDLINE, width=1, radius=3)
    # illustration strip
    rrect([x0, y0, x0 + 78, y0 + ch], fill=col, radius=3)
    d.rectangle([x0 + 70, y0, x0 + 78, y0 + ch], fill=col)
    gw = d.textlength(glyph, font=SANS_B(20))
    d.text((x0 + 39 - gw / 2, y0 + 17), glyph, font=SANS_B(20), fill=(255, 255, 255))
    tx = x0 + 88
    text(tx, y0 + 3, head, SANS_B(13), fill=INK)
    for j, ln in enumerate(wrap(body, SANS(11), 492 - 98)):
        if j > 1:
            break
        text(tx, y0 + 20 + j * 13, ln, SANS(11), fill=(50, 50, 50))
    text(tx, y0 + 46, src, SANS_B(9), fill=col)

# ---------------------------------------------------------------- map + ALSO
my = 794
d.rectangle([16, my, 596, my + 108], fill=(16, 42, 78))
text(26, my + 4, "WHERE IT HAPPENED — 13 PINNED STORIES", SANS_B(11), fill=(255, 255, 255))
# rough continents (simple polygons, stylised)
land = (58, 110, 150)
continents = [
    [(60, 52), (95, 40), (130, 48), (140, 66), (120, 84), (86, 84), (62, 70)],   # N America
    [(128, 88), (150, 86), (158, 104), (140, 122), (128, 106)],                  # S America
    [(300, 36), (330, 30), (352, 40), (344, 58), (318, 60), (300, 50)],          # Europe
    [(352, 42), (400, 34), (430, 44), (424, 74), (396, 92), (368, 78), (352, 60)],  # Africa
    [(430, 30), (500, 22), (545, 34), (540, 62), (500, 74), (452, 62)],          # Asia
    [(520, 84), (545, 80), (552, 94), (528, 100)],                                # SE Asia / Oceania
]
for poly in continents:
    d.polygon([(x + 16, y + my + 14) for x, y in poly], fill=land)
pins = [
    (1, 520, 30), (2, 128, 74), (3, 452, 58), (4, 108, 48), (5, 72, 52),
    (6, 322, 32), (7, 336, 66), (8, 354, 44), (9, 296, 26), (10, 306, 50),
    (11, 386, 80), (12, 372, 62), (13, 500, 48),
]
for n, px, py in pins:
    X, Y = 16 + px, my + 14 + py
    d.ellipse([X - 8, Y - 8, X + 8, Y + 8], fill=RED, outline=(255, 255, 255), width=1)
    t = str(n)
    tw = d.textlength(t, font=SANS_B(9))
    d.text((X - tw / 2, Y - 6), t, font=SANS_B(9), fill=(255, 255, 255))

# ALSO list (18 stories)
text(612, my, "ALSO ON MONDAY", SANS_B(13), fill=RED)
also = [
    "Bessent demands Nvidia answers", "FBI probes police-database hack",
    "Trump: Iran strikes may resume", "US futures jump 3% in holiday week",
    "Tom Jackson dies at 75", "10 states sue SpaceX over AI claims",
    "Russian nuclear satellite claim", "Benghazi: UN demands port probe",
    "Israel unity talks resume", "Gaza: two killed in Israeli strike",
    "West Bank settler attacks", "Iran war: no deal in sight",
    "Bahrain: strike hits plant, 2 hurt", "Sudan downs drones over Khartoum",
    "Bangladesh: Hasina jailed if she returns", "Seoul minister quits over AI exams",
    "China eases margin rules", "SK Telecom -7.3% as hype cools",
]
ay = my + 18
for i, item in enumerate(also):
    col, row = divmod(i, 9)
    x0 = 612 + col * 200
    y0 = ay + row * 10
    d.ellipse([x0, y0 + 2, x0 + 5, y0 + 7], fill=RED)
    text(x0 + 9, y0, item, SANS(9), fill=INK)

# ---------------------------------------------------------------- DATE CHECK
dy = 908
rrect([16, dy, 1008, dy + 74], fill=(255, 240, 240), outline=RED, width=2, radius=4)
text(28, dy + 5, "DATE CHECK — WHAT WE LEFT OUT", SANS_B(13), fill=DARKRED)
text(28, dy + 24, "NOT 23 NOVEMBER:", SANS_B(11), fill=DARKRED)
excl = ("Democrats reach 258 (22 Nov)  ·  Sparta II fire (22 Nov)  ·  El Chapo Isidro captured (22 Nov)  ·  "
        "EU–Indonesia pact (21 Nov)  ·  Nigeria boat (21 Nov)  ·  ICJ Myanmar ruling (19 Nov)")
for j, ln in enumerate(wrap(excl, SANS(11), 960)):
    text(28, dy + 38 + j * 13, ln, SANS(11), fill=(60, 20, 20))
text(28, dy + 62, "NOT YET: Dymer search continues (14 missing) · 4 House races uncalled · COP32 venue not set",
     SANS(10), fill=(90, 40, 40))

# ---------------------------------------------------------------- footer
text(16, 990, "SOURCES: AP · REUTERS · BLOOMBERG · AFP · YONHAP · LOWY INSTITUTE · UN NEWS · WIRES READ 23 NOV 2026",
     SANS_B(9), fill=GREY)
text(16, 1004, "CHIPS: REPORTED = confirmed by wires  ·  CLAIM = one side alleges  ·  DENIAL = disputed  ·  ONGOING = still developing",
     SANS(9), fill=GREY)
text(1008, 1004, "Scenes are drawn illustrations, not photographs.", SANS_I(9), fill=GREY, anchor="ra")

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
