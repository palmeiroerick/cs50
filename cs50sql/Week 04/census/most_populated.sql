create view most_populated as
select district,
       families,
       households,
       population,
       male,
       female
from census
order by population desc;

-- select district, households from most_populated limit 1;

-- drop view most_populated;
