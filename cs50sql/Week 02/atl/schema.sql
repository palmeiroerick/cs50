create table passengers (
    "id" integer,
    "first_name" text not null,
    "last_name" text not null,
    "age" integer not null check("age" >  0),
    primary key("id")
);

create table check_ins (
    "id" integer,
    "passenger_id" integer,
    "flight_id" integer,
    "date" numeric not null default current_timestamp,
    foreign key("passenger_id") references "passengers"("id"),
    foreign key("flight_id") references "flights"("id")
    primary key("id")
);

create table airlines (
    "id" integer,
    "name" text not null,
    "concourse" text not null check("concourse" in ("A","B","C","D","E","F","T")),
    primary key("id")
);

create table flights (
    "id" integer,
    "flight_number" integer not null,
    "airline_id" integer,
    "departing_from" integer,
    "heading_to" integer,
    "departure_date" numeric,
    "arrival_date" numeric,
    primary key("id"),
    foreign key("airline_id") references "ainrlines"("id")
);
