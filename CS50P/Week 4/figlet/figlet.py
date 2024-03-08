from pyfiglet import Figlet
import sys
import random

fonts = ["slant", "rectangles", "alphabet"]
font = random.choice(fonts)

if len(sys.argv) not in [1, 3]:
    sys.exit("Invalid usage")
elif len(sys.argv) == 3:
    if sys.argv[1] in ['-f', '--font'] and sys.argv[2] != "":
        font = sys.argv[2]
    else:
        sys.exit("Invalid usage")

try:
    f = Figlet(font=font)
    data = input("Input: ").strip()
    print(f.renderText(data))
except:
    sys.exit("Invalid usage")
