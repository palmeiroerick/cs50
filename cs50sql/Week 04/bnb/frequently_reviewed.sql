create view frequently_reviewed as
select listings.id, property_type, host_name, reviews from listings
join (
    select listing_id, count(listing_id) as reviews from reviews
    group by listing_id order by reviews desc limit 100
) as reviews on listings.id = listing_id
order by reviews desc, property_type, host_name;
