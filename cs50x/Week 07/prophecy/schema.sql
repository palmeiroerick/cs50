create table if not exists students (
    id integer,
    student_name text not null,
    primary key(id)
);

create table if not exists houses (
    id integer,
    name text not null,
    head text not null,
    primary key(id)
);

create table if not exists house_assignments (
    student_id integer,
    house_id integer,
    foreign key(student_id) references students(id),
    foreign key(house_id) references houses(id)
);
