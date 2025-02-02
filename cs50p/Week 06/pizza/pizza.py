import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1], "r") as file:
        pizzas = [row for row in csv.DictReader(file)]
except FileNotFoundError:
    sys.exit("File does not exist")
else:
    print(tabulate(pizzas, headers="keys", tablefmt="grid"))
