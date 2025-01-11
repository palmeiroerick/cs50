grocery = {}

while True:
    try:
        item = input("").strip().upper()
        if item not in grocery and item != "":
            grocery[item] = 1
        else:
            grocery[item] += 1
    except KeyError:
        pass
    except EOFError:
        print()
        grocery = dict(sorted(grocery.items()))
        for item in grocery:
            print(f"{grocery[item]} {item}")
        break
