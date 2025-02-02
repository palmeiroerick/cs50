import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

try:
    with open(sys.argv[1], "r") as file:
        if (sys.argv[1].split(".")[1] != "py"):
            sys.exit("Not a Python file")

        lines = file.readlines()
except FileNotFoundError:
    sys.exit("File does not exist")
else:
    code_lines = 0

    for line in lines:
        if not line.lstrip(" ").startswith(("\n", "#")):
            code_lines += 1

    print(code_lines)
