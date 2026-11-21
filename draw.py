#!/usr/bin/env python3
"""Draw entry.png: a 1024x1024 newspaper front page summing up the world
news of Saturday 21 November 2026.

Original artwork drawn with Pillow shapes and DejaVu Sans text. No photos,
no copied artwork. Deterministic: same script, same bytes.
Run: python3 draw.py
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
FD = "/usr/share/fonts/truetype/dejavu/"
BOLD = FD + "DejaVuSans-Bold.ttf"
REG = FD + "DejaVuSans.ttf"

PAPER = (246, 241, 231)
INK = (20, 33, 61)
INK_SOFT = (52, 68, 96)
RED = (178, 44, 36)
RED_LT = (214, 90, 78)
TEAL = (14, 110, 105)
GOLD = (166, 110, 20)
BLUE = (29, 78, 137)
SKY = (120, 165, 210)
GREEN = (46, 125, 70)
CARD = (255, 255, 255)
LINE = (20, 33, 61)
MUTED = (96, 104, 116)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, fnt, max_w):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(d, x, y, text, fnt, fill, max_w, lead=6):
    for line in wrap(d, text, fnt, max_w):
        d.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + lead
    return y


def kicker(d, x, y, text, color):
    f = font(BOLD, 24)
    d.text((x, y), text, font=f, fill=color)
    return y + 30


def headline(d, x, y, text, size, max_w, fill=INK, lead=4):
    f = font(BOLD, size)
    for line in wrap(d, text, f, max_w):
        d.text((x, y), line, font=f, fill=fill)
        y += size + lead
    return y


def card(d, x, y, w, h, accent, tag, title, body, icon):
    d.rounded_rectangle([x, y, x + w, y + h], radius=14, fill=CARD,
                        outline=LINE, width=2)
    d.rounded_rectangle([x, y, x + w, y + 10], radius=5, fill=accent)
    d.rectangle([x, y + 5, x + w, y + 10], fill=accent)
    icon(x + w - 52, y + 42)
    yy = kicker(d, x + 22, y + 24, tag, accent)
    yy = headline(d, x + 22, yy + 2, title, 28, w - 44)
    para(d, x + 22, yy + 6, body, font(REG, 20), INK_SOFT, w - 44, lead=4)


def icon_burst(d, cx, cy):
    for r, c in ((18, RED_LT), (12, RED), (6, (255, 205, 190))):
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=c)


def icon_drone(d, cx, cy):
    d.ellipse([cx - 18, cy - 5, cx + 18, cy + 5], outline=TEAL, width=3)
    d.line([cx - 24, cy - 11, cx + 24, cy - 11], fill=TEAL, width=3)
    d.line([cx - 24, cy + 11, cx + 24, cy + 11], fill=TEAL, width=3)
    d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=TEAL)


def icon_quake(d, cx, cy):
    for i, r in enumerate((7, 13, 19)):
        d.arc([cx - r, cy - r, cx + r, cy + r], -60, 240,
              fill=(GOLD if i % 2 == 0 else RED), width=4)
    d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=INK)


def icon_leaf(d, cx, cy):
    d.ellipse([cx - 20, cy - 14, cx + 20, cy + 14], outline=GREEN, width=4)
    d.line([cx - 17, cy + 10, cx + 17, cy - 10], fill=GREEN, width=4)


def icon_pill(d, cx, cy):
    d.rounded_rectangle([cx - 22, cy - 9, cx + 22, cy + 9], radius=9,
                        outline=BLUE, width=4)
    d.line([cx, cy - 9, cx, cy + 9], fill=BLUE, width=4)
    d.ellipse([cx - 22, cy - 9, cx, cy + 9], fill=SKY)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---- masthead ----
d.rectangle([0, 0, W, 132], fill=INK)
d.text((36, 20), "THE WORLD TODAY", font=font(BOLD, 52), fill=(246, 241, 231))
d.text((36, 84), "ONE DAY  ·  SIX STORIES  ·  SATURDAY 21 NOVEMBER 2026",
       font=font(BOLD, 24), fill=(233, 178, 62))
d.ellipse([W - 108, 28, W - 48, 88], outline=(233, 178, 62), width=4)
d.ellipse([W - 92, 44, W - 64, 72], fill=(74, 196, 182))
d.line([W - 108, 58, W - 48, 58], fill=(233, 178, 62), width=3)

# ---- top story ----
d.rounded_rectangle([28, 148, W - 28, 440], radius=16, fill=(255, 255, 255),
                    outline=LINE, width=3)
d.rounded_rectangle([28, 148, W - 28, 158], radius=5, fill=RED)
d.rectangle([28, 153, W - 28, 158], fill=RED)
kicker(d, 52, 172, "TOP STORY  —  WAR SPILLS OVER", RED)
y = headline(d, 52, 202, "Missiles land in Poland", 46, 620)
y = para(d, 52, y + 8,
         "Moscow's huge overnight strike on Ukraine crossed the border: "
         "two missiles and a suspected drone came down in Poland.",
         font(REG, 24), INK_SOFT, 620, lead=6)
para(d, 52, y + 6,
     "Poland's PM calls it a deliberate provocation. In Kyiv, bridges "
     "were hit and power was cut.",
     font(BOLD, 24), INK, 620, lead=6)
# right-hand fact box
d.rounded_rectangle([712, 176, 972, 424], radius=12, fill=(20, 33, 61))
d.text((738, 196), "THE STRIKE", font=font(BOLD, 20), fill=(233, 178, 62))
d.text((738, 228), "400+ drones", font=font(BOLD, 28), fill=(255, 255, 255))
d.text((738, 268), "110+ missiles", font=font(BOLD, 28), fill=(255, 255, 255))
d.line([738, 312, 946, 312], fill=(120, 148, 180), width=2)
d.text((738, 328), "at Ukraine overnight", font=font(REG, 21),
       fill=(176, 194, 218))
d.text((738, 360), "Kyiv bridges hit;", font=font(REG, 21),
       fill=(176, 194, 218))
d.text((738, 388), "power cut", font=font(REG, 21), fill=(176, 194, 218))

# ---- middle grid: 2 x 2 ----
gy, gh, gw = 456, 200, 472
gx = [28, 524]
card(d, gx[0], gy, gw, gh, TEAL, "IRAN  ·  GULF",
     "US drone downed over Hormuz",
     "Iran's Revolutionary Guard shot down a US drone as talks stall. "
     "Trump weighs new strikes on Iran.",
     lambda x, y: icon_drone(d, x, y))
card(d, gx[1], gy, gw, gh, GOLD, "DISASTER  ·  PERU",
     "Magnitude 6.9 quake in the Andes",
     "The tremor shook central Peru and was felt in Lima. No damage or "
     "casualties reported at first.",
     lambda x, y: icon_quake(d, x, y))
card(d, gx[0], gy + gh + 16, gw, gh, GREEN, "CLIMATE  ·  COP31",
     "Climate talks run into overtime",
     "Nearly 200 nations in Antalya fail to agree on fossil fuels, and "
     "the summit passes its deadline.",
     lambda x, y: icon_leaf(d, x, y))
card(d, gx[1], gy + gh + 16, gw, gh, BLUE, "HEALTH  ·  BREAKTHROUGH",
     "Cancer pill's big trial result",
     "Daraxonrasib made tumours undetectable in 1 in 12 pancreatic "
     "cancer patients in a trial.",
     lambda x, y: icon_pill(d, x, y))

# ---- also today strip ----
ay = gy + 2 * gh + 18
d.rounded_rectangle([28, ay, W - 28, ay + 92], radius=14, fill=INK)
d.text((52, ay + 10), "ALSO TODAY", font=font(BOLD, 22), fill=(233, 178, 62))
d.text((52, ay + 40),
       "UK & EU sign post-Brexit deals in Brussels  •  Verstappen on pole in Las Vegas",
       font=font(REG, 20), fill=(246, 241, 231))
d.text((52, ay + 66), "Gen Z protests spread across 25 European countries",
       font=font(REG, 20), fill=(246, 241, 231))

# ---- footer ----
d.text((36, H - 36),
       "Sources: Reuters, AP, BBC, Al Jazeera, USGS  ·  Events of 21 November 2026",
       font=font(REG, 17), fill=MUTED)

img.save("entry.png", optimize=True)
print("wrote entry.png", img.size)
