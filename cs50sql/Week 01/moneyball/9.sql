select "name", "average salary" from (
    select "team_id", round(avg("salary"), 2) as "average salary" from "salaries"
    where year = 2001
    group by "team_id"
    order by "average salary"
    limit 5
) as "lowest paying teams"
join "teams" on "teams"."id" = "team_id";
