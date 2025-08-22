CREATE TABLE temp (
    name, id, nametype, class, mass, discovery, year, lat, long
);

.import --csv --skip 1 meteorites.csv temp

update temp set mass = null where mass = "";
update temp set year = null where year = "";
update temp set lat = null where lat = "";
update temp set long = null where long = "";

update temp set mass = round(mass, 2);
update temp set lat = round(lat, 2);
update temp set long = round(long, 2);

delete from temp where nametype = "Relict";

-- select * from temp limit 100;

create table meteorites (
    id integer,
    name text,
    class text,
    mass numeric,
    discovery text,
    year integer,
    lat numeric,
    long numeric,
    primary key(id)
);

insert into meteorites (name, class, mass, discovery, year, lat, long)
select name, class, mass, discovery, year, lat, long from temp
order by year, name;

-- select * from meteorites limit 100;

drop table temp;
-- drop table meteorites;
