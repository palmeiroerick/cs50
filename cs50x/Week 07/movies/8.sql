select name from people where id in (
    select person_id from stars where movie_id in (
        select id from movies where title = "Toy Story"
    )
);

-- select name from people
-- join stars on people.id = stars.person_id
-- join movies on stars.movie_id = movies.id
-- where movies.title = "Toy Story";
