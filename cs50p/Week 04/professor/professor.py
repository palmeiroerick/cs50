from random import randint


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x, y = generate_integer(level), generate_integer(level)

        attempts = 3

        while attempts != 0:
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                attempts -= 1
            else:
                if x + y == answer:
                    break
                else:
                    print("EEE")
                    attempts -= 1

            if attempts == 0:
                print(f"{x} + {y} = {x + y}")

        if attempts != 0:
            score += 1

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if not 1 <= level <= 3:
                raise ValueError
        except ValueError:
            pass
        else:
            return level


def generate_integer(level):
    if level == 1:
        return randint(0, 9)
    elif level == 2:
        return randint(10, 99)
    elif level == 3:
        return randint(100, 999)


if __name__ == "__main__":
    main()
