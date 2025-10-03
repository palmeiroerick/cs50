select avg(rating) from ratings join (
    select id, year from movies where year = 2012
) as released_in_2012 on ratings.movie_id = released_in_2012.id;
