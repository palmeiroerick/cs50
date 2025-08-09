select "first_name", "last_name", "salary", "HR", "performances"."year" from "players"
join "performances" on "performances"."player_id" = "players"."id"
join "salaries" on "salaries"."player_id" = "players"."id"
                and "performances"."year" = "salaries"."year"
order by "players"."id", "performances"."year" desc, "HR" desc, "salary" desc;
