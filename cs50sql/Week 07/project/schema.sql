create table categories (
    id integer primary key,
    name text not null unique
);

create table products (
    id integer primary key,
    name text not null,
    category_id int not null,
    quantity int not null check(quantity >= 0),
    price real not null check(price > 0),
    foreign key(category_id) references categories(id)
);

create table users (
    id integer primary key,
    name text not null
);

create table orders (
    id integer primary key,
    user_id int not null,
    total real not null default 0 check(total >= 0),
    year int not null,
    month int not null,
    day int not null,
    foreign key(user_id) references users(id)
);

create table order_items (
    order_id int,
    product_id int,
    quantity int not null check(quantity > 0),
    primary key(order_id, product_id),
    foreign key(order_id) references orders(id) on delete restrict,
    foreign key(product_id) references products(id) on delete restrict
);

create trigger check_stock_on_insert
before insert on order_items
for each row
begin
    select
        case
            when (select quantity from products where id = new.product_id) < new.quantity
            then raise(abort, 'Not enough stock')
        end;
end;

create trigger update_stock_on_insert
after insert on order_items
for each row
begin
    update products set quantity = quantity - new.quantity where id = new.product_id;
end;

create trigger check_stock_on_update
before update on order_items
for each row
begin
    select
        case
            when (new.quantity > old.quantity)
            and (select quantity from products where id = new.product_id) < (new.quantity - old.quantity)
            then raise(abort, 'Not enough stock')
        end;
end;

create trigger update_stock_on_update
after update on order_items
for each row
begin
    update products set quantity = quantity - (new.quantity - old.quantity) where id = new.product_id;
end;

create trigger update_order_total_on_insert
after insert on order_items
for each row
begin
    update orders
    set total = (
        select sum(products.price * order_items.quantity) from order_items
        join products on order_items.product_id = products.id
        where order_items.order_id = orders.id
    )
    where orders.id = new.order_id;
end;

create trigger update_order_total_on_update
after update on order_items
for each row
begin
    update orders
    set total = (
        select sum(products.price * order_items.quantity) from order_items
        join products on order_items.product_id = products.id
        where order_items.order_id = orders.id
    )
    where orders.id = new.order_id;
end;

create trigger update_order_total_on_delete
after delete on order_items
for each row
begin
    update orders
    set total = (
        select sum(products.price * order_items.quantity) from order_items
        join products on order_items.product_id = products.id
        where order_items.order_id = orders.id
    )
    where orders.id = new.order_id;
end;

create trigger update_stock_on_delete
after delete on order_items
for each row
begin
    update products set quantity = quantity + old.quantity where id = old.product_id;
end;


create index idx_orders_user_id on orders(user_id);
CREATE INDEX idx_order_items_order_id ON order_items(order_id);
