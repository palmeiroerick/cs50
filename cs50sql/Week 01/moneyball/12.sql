select "first_name", "last_name" from (
    select "least expensive players per hit"."player_id" from (
        select "salaries"."player_id", "salary" / "H" as "dollars per hit" from "performances"
        join "salaries" on "salaries"."player_id" = "performances"."player_id"
                        and "salaries"."year" = "performances"."year"
        where "H" > 0 and "salaries"."year" = 2001 order by "dollars per hit" limit 10
    ) as "least expensive players per hit"
    join (
        select "salaries"."player_id", "salary" / "RBI" as "dollars per RBI" from "performances"
        join "salaries" on "salaries"."player_id" = "performances"."player_id"
                        and "salaries"."year" = "performances"."year"
        where "RBI" > 0 and "salaries"."year" = 2001 order by "dollars per RBI" limit 10
    ) as "least expensive players per RBI"
    on "least expensive players per RBI"."player_id" = "least expensive players per hit"."player_id"
) as "players among"
join "players" on "players"."id" = "players among"."player_id"
order by "players"."id";
