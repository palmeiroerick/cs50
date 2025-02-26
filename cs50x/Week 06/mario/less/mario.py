while True:
    try:
        height = int(input("Height: "))
        if not 1 <= height <= 8:
            raise ValueError
    except ValueError:
        pass
    else:
        break

for i in range(1, height + 1):
    print(" " * (height - i), "#" * i, sep="")
