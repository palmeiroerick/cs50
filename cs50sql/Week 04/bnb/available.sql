create view available as
select listings.id, property_type, host_name, available, date from listings
join availabilities on listings.id = listing_id
where available = "TRUE";
