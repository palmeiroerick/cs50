select "first_name", "last_name", "dollars per hit" from (
    select "salaries"."player_id", "salary" / "H" as "dollars per hit" from "performances"
    join "salaries" on "salaries"."player_id" = "performances"."player_id"
                    and "salaries"."year" = "performances"."year"
    where "H" > 0 and "salaries"."year" = 2001 order by "dollars per hit" limit 10
) as "least expensive players per hit"
join "players" on "players"."id" = "least expensive players per hit"."player_id"
order by "dollars per hit", "first_name", "last_name";
