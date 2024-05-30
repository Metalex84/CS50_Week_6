from pyfiglet import Figlet
from sys import argv
import random

figlet = Figlet()
fonts = figlet.getFonts()

try:
    if len(argv) == 1:
        figlet.setFont(font=random.choice(fonts))
        str = input("input: ")
        print(figlet.renderText(str))
    elif len(argv) == 3:
        if argv[1] == "-f" or argv[1] == "--font":
            if argv[2] in fonts:
                figlet.setFont(font=argv[2])
                str = input("input: ")
                print(f"Output: {figlet.renderText(str)}")
            else:
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
except:
    sys.exit("Invalid usage")
