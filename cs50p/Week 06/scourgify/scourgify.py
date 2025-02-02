import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1], "r") as file:
        students = [row for row in csv.DictReader(file)]
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
else:
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in students:
            last, first = student["name"].split(", ")
            writer.writerow({
                "first": first,
                "last": last,
                "house": student["house"]
            })
