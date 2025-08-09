select "name", "per_pupil_expenditure" from "districts"
join "expenditures" on "expenditures"."district_id" = "districts"."id"
where "type" = "Public School District"
order by "per_pupil_expenditure" desc limit 10;
