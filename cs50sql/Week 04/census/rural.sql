create view rural as
select * from census
where locality like "%Rural%";

-- select count(*) as rural_districts, sum(families) as families from rural;

-- drop view rural;
