select title from movies join (
    select movie_id from ratings where movie_id in (
        select movie_id from stars where person_id = (
            select id from people where name = "Chadwick Boseman"
        )
    )
    order by rating desc limit 5
) as highest_rated on highest_rated.movie_id = movies.id;
