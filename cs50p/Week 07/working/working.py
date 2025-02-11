import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    regex = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"

    if matches := re.search(regex, s):
        hours1, minutes1, meridiem1, hours2, minutes2, meridiem2 = matches.groups()

        hours1 = 0 if meridiem1 == "AM" and hours1 == "12" else int(
            hours1) if meridiem1 == "AM" else 12 if hours1 == "12" else int(hours1) + 12
        hours2 = 0 if meridiem2 == "AM" and hours2 == "12" else int(
            hours2) if meridiem2 == "AM" else 12 if hours2 == "12" else int(hours2) + 12

        minutes1 = int(minutes1) if minutes1 else 0
        minutes2 = int(minutes2) if minutes2 else 0

        if meridiem1 == "AM" and hours1 > 12 or meridiem1 == "PM" and hours1 > 24:
            raise ValueError

        if meridiem2 == "AM" and hours2 > 12 or meridiem2 == "PM" and hours2 > 24:
            raise ValueError

        if minutes1 > 59 or minutes2 > 59:
            raise ValueError

        return f"{hours1:02}:{minutes1:02} to {hours2:02}:{minutes2:02}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
