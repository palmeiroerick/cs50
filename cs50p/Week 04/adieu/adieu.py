import inflect
p = inflect.engine()

names = []

while True:
    try:
        name = input("Name: ")
    except EOFError:
        print()
        break
    else:
        if name != "":
            names.append(name)
 
print(f"Adieu, adieu, to {p.join(names)}")
