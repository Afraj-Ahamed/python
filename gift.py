import turtle
import random
from PIL import Image, ImageDraw, ImageFont

# ---------- STEP 1: Turn the text into a list of (x, y) points ----------

LINE1 = "SHIMER LOVE"
LINE2 = "HANFA" 

FONT_SIZE = 90
IMG_W, IMG_H = 1400, 300

img = Image.new("L", (IMG_W, IMG_H), 0)          # blank black image
draw = ImageDraw.Draw(img)

try:
    font = ImageFont.truetype("arial.ttf", FONT_SIZE)   # Windows usually has this
except:
    font = ImageFont.load_default()

# Draw line 1 (top) and line 2 (bottom), centered horizontally
def draw_centered(text, y):
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    x = (IMG_W - text_w) // 2
    draw.text((x, y), text, fill=255, font=font)

draw_centered(LINE1, 20)
draw_centered(LINE2, 150)

pixels = img.load()
points = []
STEP = 3   # smaller STEP = more points = denser/clearer letters (but slower)
for x in range(0, IMG_W, STEP):
    for y in range(0, IMG_H, STEP):
        if pixels[x, y] > 128:      # this pixel is part of a letter
            points.append((x, y))

# Center the points around (0, 0), and flip y (image y grows downward,
# turtle y grows upward)
avg_x = sum(p[0] for p in points) / len(points)
avg_y = sum(p[1] for p in points) / len(points)
points = [((px - avg_x), -(py - avg_y)) for px, py in points]

print("Total points to draw:", len(points))

# ---------- STEP 2: Draw the letters directly using little stars ----------

t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(width=1500, height=500)
screen.bgcolor("black")
screen.tracer(30)         # draw in batches so it's fast
t.hideturtle()
t.speed(0)
t.width(2)

colors = ["red", "orange", "yellow", "green", "blue",
          "purple", "cyan", "magenta", "white", "pink"]

for (x, y) in points:
    t.penup()
    t.goto(x, y)
    t.pendown()

    c = random.choice(colors)
    t.color(c)

    # small star burst right at this point (no line back to center,
    # so the letters stay clearly visible)
    for _ in range(8):
        t.forward(3)
        t.backward(3)
        t.right(45)

screen.tracer(1)
turtle.done()