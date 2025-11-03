from faker import Faker
import csv
import os
import sqlite3
import random

if os.path.exists("ecommerce.db"):
    os.remove("ecommerce.db")

fake = Faker()
con = sqlite3.connect("ecommerce.db")
cur = con.cursor()

con.executescript(open("schema.sql").read())

# Users
for _ in range(49):
    cur.execute("insert into users (name) values (?)", (fake.name(),))

# Arbitray user for some queries
cur.execute("insert into users (name) values (?)", ("Scott Parks",))

# Products
with open("products.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cur.execute("SELECT id FROM categories WHERE name = ?", (row["category"],))
        result = cur.fetchone()

        if result:
            category_id = result[0]
        else:
            cur.execute("INSERT INTO categories (name) VALUES (?)", (row["category"],))
            category_id = cur.lastrowid

        cur.execute(
            "insert into products (name, category_id, quantity, price) values (?, ?, ?, ?)",
            (row["name"], category_id, int(row["quantity"]), float(row["price"]))
        )

# Orders
for order_id in range(1, 501):
    user_id = random.randint(1, 50)
    date = fake.date_time_between(start_date="-10y", end_date="now").date()
    cur.execute("insert into orders (user_id, total, year, month, day) values (?, 0, ?, ?, ?)",
                (user_id, date.year, date.month, date.day))

    products_in_order = random.sample(
        range(1, 1000 + 1), random.randint(1, 21))

    for product_id in products_in_order:
        quantity = random.randint(1, 5)

        try:
            cur.execute(
                "INSERT INTO order_items (order_id, product_id, quantity) VALUES (?, ?, ?)",
                (order_id, product_id, quantity)
            )
        except sqlite3.IntegrityError as e:
            if "Not enough stock" in str(e):
                pass
            else:
                raise


con.commit()
con.close()
