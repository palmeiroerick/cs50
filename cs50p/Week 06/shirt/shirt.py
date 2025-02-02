import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if not sys.argv[2].endswith((".jpg", ".jpeg", ".png")):
    sys.exit("Invalid output")

if os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
    sys.exit("Input and output have different extensions")

try:
    shirt = Image.open("shirt.png")
    before = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist")
else:
    before = ImageOps.fit(before, shirt.size)
    before.paste(shirt, shirt)
    before.save(sys.argv[2])
