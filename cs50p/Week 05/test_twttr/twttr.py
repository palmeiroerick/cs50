def main():
    text = shorten(input("Input: "))
    print(f"Output: {text}")


def shorten(word):
    vowels = "aAeEiIoOuU"
    shortened = ""

    for letter in word:
        if letter not in vowels:
            shortened = shortened + letter

    return shortened


if __name__ == "__main__":
    main()
