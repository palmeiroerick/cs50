def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):
    if greeting[:5] == "Hello":
        return 0
    elif greeting[0] == "H":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
