create table users (
    "id" integer,
    "first_name" text not null,
    "last_name" text not null,
    "username" text not null unique,
    "password" text not null,
    primary key("id")
);

create table schools (
    "id" integer,
    "name" text not null,
    "type" text not null,
    "location" text not null,
    "founded" numeric not null,
    primary key("id")
);

create table companies (
    "id" integer,
    "name" text not null,
    "industry" text not null,
    "location" text not null,
    primary key("id")
);

create table people_connections (
    "id" integer,
    "user_id" integer,
    "following_id" integer,
    primary key("id"),
    foreign key("user_id") references "users"("id"),
    foreign key("following_id") references "users"("id")
);

create table school_connections (
    "id" integer,
    "user_id" integer,
    "school_id" integer,
    "start_date" numeric not null,
    "end_date" numeric,
    "degree_type" text not null,
    primary key("id"),
    foreign key("user_id") references "users"("id"),
    foreign key("school_id") references "schools"("id")
);

create table company_connections (
    "id" integer,
    "user_id" integer,
    "company_id" integer,
    "start_date" numeric not null,
    "end_date" numeric,
    "title" text not null,
    primary key("id"),
    foreign key("user_id") references "users"("id"),
    foreign key("company_id") references "companies"("id")
);
