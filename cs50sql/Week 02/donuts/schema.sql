create table ingredients (
    "id" integer,
    "name" text not null,
    "price" integer not null,
    primary key("id")
);

create table donuts (
    "id" integer,
    "name" text not null,
    "gluten-free" boolean not null,
    "price" integer not null,
    primary key("id")
);

create table donuts_ingredients (
    "donut_id" integer,
    "ingredients_id" integer,
    foreign key ("donut_id") references "donuts"("id"),
    foreign key ("ingredients_id") references "ingredients"("id")
);

create table orders (
    "id" integer,
    "order_number" integer,
    "donut_id" integer,
    "customer_id" integer,
    primary key("id"),
    foreign key("donut_id") references "donuts"("id"),
    foreign key("customer_id") references "customers"("id")
);

create table customers (
    "id" integer,
    "first_name" text not null,
    "last_name" text not null,
    primary key("id")
);

create table order_history (
    "customer_id" integer,
    "order_id" integer,
    foreign key("customer_id") references "custumers"("id"),
    foreign key("order_id") references "orders"("id")
);
