create database spotify_db;

use spotify_db;

truncate table spotify_artist;

CREATE TABLE IF NOT EXISTS spotify_artist (
    id INT AUTO_INCREMENT PRIMARY KEY,
    artist_name VARCHAR(255),
    Artist_Photo_url VARCHAR(255),
    popularity INT,
    genres VARCHAR(255),
    followers int
);


select artist_name,popularity,genres,followers from spotify_artist order by popularity desc limit 1;

select avg(popularity) from spotify_artist;

select artist_name,genres,followers from spotify_artist where followers > 50000000;

select artist_name,genres,popularity from spotify_artist where popularity > 85;

select artist_name,popularity,
	case
		when popularity >=85 Then 'Very Popular'
        when popularity>=50 Then 'Popular'
        else 'Less Popular'
	END AS popularity_range
FROM spotify_artist;


select 
	case
		when popularity >=85 Then 'Very Popular'
        when popularity >=50 Then 'Popular'
        else 'Less Popular'
	END AS popularity_range,
    COUNT(*) AS popularity_count
FROM spotify_artist
group by popularity_range;


	






