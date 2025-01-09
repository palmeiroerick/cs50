text = input("Input: ").strip()

print("Output: ", end="")

for c in text:
    if c not in "aAeEiIoOuU":
        print(c, end="")

print()
