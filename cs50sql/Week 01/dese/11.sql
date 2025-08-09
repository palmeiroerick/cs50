select "name", "graduated", "per_pupil_expenditure" from "schools"
join "graduation_rates" on "graduation_rates"."school_id" = "schools"."id"
join "expenditures" on "expenditures"."district_id" = "schools"."district_id"
order by "per_pupil_expenditure" desc, "name";
