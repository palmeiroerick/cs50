-- In this SQL file, write (and comment!) the typical SQL queries users will run on your database

insert into products (name, category, quantity, price) values
("Medium Roast Ground Coffee", "Food", 23, 32.89);

insert into users (name) values ("Louis Ford");

insert into orders (user_id, year, month, day)
select id, 2025, 10, 28 from users where name = "Louis Ford";

insert into order_items (order_id, product_id, quantity) values (101, 1001, 2);
insert into order_items (order_id, product_id, quantity) values (101, 34, 2);
insert into order_items (order_id, product_id, quantity) values (101, 75, 5);
insert into order_items (order_id, product_id, quantity) values (101, 114, 1);
insert into order_items (order_id, product_id, quantity) values (101, 69, 7);

-- The product with id 9 has 3 in stock, so when you try to order 4, a runtime error occurs.
-- insert into order_items (order_id, product_id, quantity) values (101, 9, 4);

-- The same happens on update:
-- update order_items set quantity = 23 where order_id = 101 and product_id = 1001;

-- When deleting a product from order_items the stock on the products table is restored
-- select quantity from products where id = 75;
-- delete from order_items where order_id = 101 and product_id = 75;

-- The total of a order is automatically updated
-- select total from orders where id = 101;
-- update order_items set quantity = 9 where order_id = 101 and product_id = 69;
-- insert into order_items (order_id, product_id, quantity) values (101, 88, 4);
-- insert into order_items (order_id, product_id, quantity) values (101, 995, 1);

-- Top 10 more expansive Foods
select name, price from products where category_id = (
    select id from categories where name = "Food"
) order by price desc limit 10;

-- All products bought by Scott Parks
select name, order_items.quantity, price * order_items.quantity as total_price from order_items
join (
    select id from orders where user_id = (
        select id from users where name = "Scott Parks"
    )
) as scott_orders on scott_orders.id = order_items.order_id
join products on products.id = order_items.product_id;

-- Users by spending
select name, sum(total) as total_spending from users
join orders on orders.user_id = users.id
group by user_id order by sum(total) desc;

-- Total revenue for the months of 2025.
select month, sum(total) as revenue from orders where year = 2025 group by month order by sum(total) desc;

-- Top 10 products by revenue in 2022
select name, sum(products.price * order_items.quantity) as revenue from order_items
join orders on order_items.order_id = orders.id
join products on order_items.product_id = products.id
where orders.year = 2022 group by products.id order by revenue desc limit 10;
