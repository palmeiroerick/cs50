select "first_name", "last_name" from "players" where "id" = (
    select "player_id" from "salaries"
    order by "salary" desc limit 1

    -- select "player_id" from "salaries" where "salary" = (
    --     select max("salary") from "salaries"
    -- )
);
