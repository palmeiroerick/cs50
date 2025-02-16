import sys
import re

from datetime import date
from inflect import engine

def main():
    birth_date = get_date(input("Date of Birth: "))
    minutes = (birth_date - date.today()).days * -1440
    print(engine().number_to_words(minutes, andword="").capitalize() + " minutes")


def get_date(birth_date):
    regex = r"^(\d{4})-(\d{2})-(\d{2})"

    if matches := re.search(regex, birth_date):
        year, month, day = matches.groups()
    else:
        sys.exit("Invalid date")

    return date(int(year), int(month), int(day))


if __name__ == "__main__":
    main()
