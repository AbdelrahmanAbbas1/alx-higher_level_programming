-- Lists all genres from hbtn_0d_tvshows and displays
-- the number of shows linked to each
SELECT g.name AS 'genre', count(t.genre_id) AS 'number_of_shows'
FROM tv_show_genres t
LEFT JOIN tv_genres g
ON t.genre_id = g.id
GROUP BY genre
ORDER BY number_of_shows DESC;
