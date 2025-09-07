create view "june_vacancies" as
select id, property_type, host_name, days_vacant from listings
join (
    select listing_id, count(available) as days_vacant from availabilities
    where date between "2023-06-01" and "2023-06-30"
    and available = "TRUE" group by listing_id
) as days_vacant on listings.id = listing_id;
