months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")
        if "," in date:
            month, date = date.split(" ", maxsplit=1)
            day, year = date.split(", ")
            month = months.index(month) + 1
        else:
            month, day, year = date.split("/")
        year, month, day = int(year), int(month), int(day)
    except ValueError:
        pass
    else:
        if not (month > 12 or day > 31):
            print(f"{year}-{month:02}-{day:02}")
            break
