select "city", count("school") as "public schools" from "schools"
where "type" = "Public School"
group by "city" having "public schools" <= 3
order by "public schools" desc, "city";
