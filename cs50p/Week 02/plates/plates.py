def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[0:2].isalpha():
        return False
    if not 2 <= len(s) <= 6:
        return False
    if not s.isalnum():
        return False

    for i in range(2, len(s) - 1):
        if s[i].isnumeric() and s[i+1].isalpha():
            return False

    for i in range(2, len(s)):
        if s[i-1].isalpha() and s[i].isnumeric() and s[i] == "0":
            return False

    return True


main()
