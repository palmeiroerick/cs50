select "city", count("school") as "public schools" from "schools"
where "type" = "Public School" group by "city"
order by "public schools" desc, "city" limit 10;
