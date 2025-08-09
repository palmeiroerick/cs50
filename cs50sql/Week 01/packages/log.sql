
-- *** The Lost Letter ***

select * from "scans"
where "package_id" = (
    select "id" from "packages"
    where "from_address_id" = (
        select "id" from "addresses"
        where "address" = "900 Somerville Avenue"
    )
    and "contents" = "Congratulatory letter"
)
and "address_id" = (
    select "id" from "addresses"
    where "address" = "2 Finnigan Street"
);

select * from "addresses"
where "id" = (
    select "to_address_id" from "packages"
    where "from_address_id" = (
        select "id" from "addresses"
        where "address" = "900 Somerville Avenue"
    )
    and "contents" = "Congratulatory letter"
);


-- *** The Devious Delivery ***

select * from "packages" where "from_address_id" is null;

select * from "addresses"
where "id" = (
    select "address_id" from "scans"
    where "package_id" = (
        select "id" from "packages" where "from_address_id" is null
    )
    and "action" = "Drop"
);


-- *** The Forgotten Gift ***

select * from "packages"
where "from_address_id" = (
    select "id" from "addresses"
    where "address" = "109 Tileston Street"
)
and "to_address_id" = (
    select "id" from "addresses"
    where "address" = "728 Maple Place"
);


select * from "drivers"
where "id" = (
    select "driver_id" from "scans"
    where "package_id" = (
        select "id" from "packages"
        where "from_address_id" = (
            select "id" from "addresses"
            where "address" = "109 Tileston Street"
        )
        and "to_address_id" = (
            select "id" from "addresses"
            where "address" = "728 Maple Place"
        )
    )
    order by "timestamp" desc
    limit 1
);
