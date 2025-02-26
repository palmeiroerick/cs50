import re


def main():
    print(validate(int(input("Number: "))))


def validate(number):
    str_copy = str(number)

    sum = 0

    while number:
        last = number % 10
        number = int(number / 10)

        sum += last

        last = number % 10 * 2
        number = int(number / 10)

        sum += last // 10 + last % 10

    if sum % 10 != 0:
        return "INVALID"

    number = str_copy

    amex = r"^(?:34|37)\d{13}"
    mastercard = r"^(?:51|52|53|54|55)\d{14}"
    visa = r"^4(?:\d{12}|\d{15})"

    if re.match(amex, number):
        return "AMEX"
    elif re.match(mastercard, number):
        return "MASTERCARD"
    elif re.match(visa, number):
        return "VISA"
    else:
        return "INVALID"


if __name__ == "__main__":
    main()
