select "salary" from "salaries" where "player_id" = (
    select "player_id" from "performances"
    order by "HR" desc limit 1

    -- select "player_id" from "performances" where "HR" = (
    --     select max("HR") from "performances"
    -- )
)
and year = 2001;
