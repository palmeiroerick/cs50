def main():
    while True:
        try:
            fraction = input("Fraction: ")
        except (ValueError):
            pass
        else:
            break

    print(gauge(convert(fraction)))


def convert(fraction):
    x, sign, y = fraction.partition("/")
    x, y = int(x), int(y)

    if sign != "/":
        raise ValueError

    if x > y:
        raise ValueError

    return int(round(x / y * 100))


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{round(percentage)}%"


if __name__ == "__main__":
    main()
