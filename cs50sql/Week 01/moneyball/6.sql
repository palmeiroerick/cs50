-- Query the top teams and then join to teams to get their names

select "name", "total hits" from (
    select "team_id", sum("H") as "total hits" from "performances"
    where "year" = 2001
    group by "team_id"
    order by "total hits" desc
    limit 5
) as "top_teams"
join "teams" on "teams"."id" = "top_teams"."team_id";

-- Join teams and performances and then query for the top team

-- select "name", sum("H") as "total hits" from "teams"
-- join "performances" on "performances"."team_id" = "teams"."id"
-- where "performances"."year" = 2001
-- group by "team_id"
-- order by "total hits" desc
-- limit 5;
