"""
rm students.db
sqlite3 students.db < schema.sql
python students.py
"""

from cs50 import SQL
import csv

db = SQL("sqlite:///students.db")

houses = set()

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        db.execute("insert into students (student_name) values(?)", row["student_name"])

        if row["house"] not in houses:
            houses.add(row["house"])
            db.execute("insert into houses (name, head) values(?, ?)", row["house"], row["head"])

        student_id = db.execute("select id from students where student_name = ?", row["student_name"])[0]["id"]
        house_id = db.execute("select id from houses where name = ?", row["house"])[0]["id"]
        db.execute("insert into house_assignments (student_id, house_id) values(?, ?)", student_id, house_id)

