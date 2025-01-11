def main():
    fuel = get_fuel("Fraction: ")

    if fuel <= 1:
        print("E")
    elif fuel >= 99:
        print("F")
    else:
        print(f"{round(fuel)}%")


def get_fuel(prompt):
    while True:
        try:
            x, sign, y = input(prompt).partition("/")
            x, y = int(x), int(y)
            if sign != "/":
                continue
        except (ValueError):
            pass
        else:
            if not (x > y or y == 0):
                break
    return x / y * 100


if __name__ == "__main__":
    main()
