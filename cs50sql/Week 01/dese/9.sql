select "name" from "districts"
where "id" = (
    select "district_id" from "expenditures"
    where "pupils" = (
        select min("pupils") from "expenditures"
    )
);
