select title, rating from ratings join (
    select id, title from movies where year = 2010
) as released_in_2010 on ratings.movie_id = released_in_2010.id
order by rating desc, title;
