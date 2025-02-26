from pyfiglet import Figlet
import sys

figlet = Figlet()

fonts = figlet.getFonts()

if len(sys.argv) != 3 and len(sys.argv) != 1:
    sys.exit("Invalid usage")

if len(sys.argv) == 3:
    if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid usage")

print(f"{figlet.renderText(input("Input: "))}")
