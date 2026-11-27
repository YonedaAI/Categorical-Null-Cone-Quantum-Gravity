# /// script
# requires-python = ">=3.10"
# dependencies = ["pillow==12.0.0", "fonttools[woff]==4.60.1"]
# ///
"""Draw the null sheets of a 2+1 dimensional Minkowski diamond in projection."""
import math
from io import BytesIO
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

SCALE = 2
WIDTH, HEIGHT = 760, 570
image = Image.new("RGB", (WIDTH * SCALE, HEIGHT * SCALE), "#101c25")
ink = ImageDraw.Draw(image)


def point(t, angle):
    radius = 212 * (1 - abs(t))
    return (366 + radius * math.cos(angle), 278 - 222 * t + 0.29 * radius * math.sin(angle))


def stroke(points, color, width=1):
    coords = [(round(x * SCALE), round(y * SCALE)) for x, y in points]
    ink.line(coords, fill=color, width=max(1, round(width * SCALE)))


def ring(time, color, width=1):
    stroke([point(time, math.tau * j / 240) for j in range(241)], color, width)


def dot(x, y, radius):
    ink.ellipse(tuple(round(v*SCALE) for v in (x-radius,y-radius,x+radius,y+radius)),fill="#d7fcf0")


# The time axis continues beyond the two tips. The shared ring is the waist.
stroke([(366, 18), (366, 540)], "#435560")
for level in range(1, 16):
    for sign, color in ((1, "#456b70"), (-1, "#34595c")):
        ring(sign * level / 16, color, .8)
for meridian in range(54):
    angle = math.tau * meridian / 54
    color = "#75b5af" if math.sin(angle) > 0 else "#385b65"
    stroke([point(-1, angle), point(0, angle), point(1, angle)], color, .9)
ring(0, "#d5f4b7", 2.4)
for t in (-1, 1):
    x, y = point(t, 0)
    dot(x, y, 3.8)
# Physical labels are HTML, so that readers can select them and zoom.
root = Path(__file__).resolve().parents[1]
assets = root / "website/assets"
plate = image.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
plate.save(assets / "diamond.png", optimize=True)


def typeface(family, size):
    # Share artwork uses the same two openly licensed fonts as the reader.
    stream = BytesIO()
    font = TTFont(assets / "fonts" / (family + ".woff2"))
    font.flavor = None
    font.save(stream)
    stream.seek(0)
    return ImageFont.truetype(stream, size=size)


def share_card(slug, label, title):
    card = Image.new("RGB", (1200, 630), "#101c25")
    card.paste(plate.resize((572, 429), Image.Resampling.LANCZOS), (623, 88))
    draw = ImageDraw.Draw(card)
    small, headline = typeface("instrument-sans", 25), typeface("instrument-serif", 70)
    draw.text((55, 55), "YonedaAI Research Collective", font=small, fill="#f2f1eb")
    draw.line((55, 113, 1145, 113), fill="#34424a", width=2)
    draw.text((55, 151), label, font=small, fill="#d5f4b7")
    lines = [""]
    for word in title.split():
        proposed = (lines[-1] + " " + word).strip()
        if lines[-1] and draw.textlength(proposed, font=headline) > 645:
            lines.append(word)
        else:
            lines[-1] = proposed
    for i, line in enumerate(lines):
        draw.text((52, 207 + i * 73), line, font=headline, fill="#f2f1eb")
    (assets / "og").mkdir(exist_ok=True)
    card.save(assets / "og" / (slug + ".png"), optimize=True)


for card in (
    ("series", "Research series", "Categorical Null-Cone Quantum Gravity"),
    ("foundations", "Part I", "Categorical Foundations of Null-Cone Quantization"),
    ("reduction", "Part II", "Derived Gauge Reduction and Quantum Observable Algebras"),
    ("gluing", "Part III", "Gravitational Gluing and Categorical Descent"),
    ("synthesis", "Perspective", "The Categorical Null-Cone Realization Conjecture"),
    ("marked-cut", "Supplement", "Ordered probes at a marked null cut"),
):
    share_card(*card)
