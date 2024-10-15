from sql_questions import define

# 注意 UNION 会去重而 UNION ALL 不会。

sql_test = define("""
(
	SELECT name AS results 
	FROM Users JOIN MovieRating ON Users.user_id = MovieRating.user_id 
	GROUP BY Users.user_id 
	ORDER BY COUNT(*) DESC, name ASC LIMIT 1
)
UNION ALL
(
	SELECT title AS results 
	FROM Movies JOIN MovieRating ON Movies.movie_id = MovieRating.movie_id
	WHERE YEAR(created_at) = 2020 AND MONTH(created_at) = 2
	GROUP BY Movies.movie_id
	ORDER BY AVG(rating) DESC, title ASC LIMIT 1
)
""")

sql_test.check_order = True


@sql_test("""\
Create table If Not Exists Movies (movie_id int, title varchar(30));
Create table If Not Exists Users (user_id int, name varchar(30));
Create table If Not Exists MovieRating (movie_id int, user_id int, rating int, created_at date);
Truncate table Movies;
insert into Movies (movie_id, title) values ('1', 'Avengers');
insert into Movies (movie_id, title) values ('2', 'Frozen 2');
insert into Movies (movie_id, title) values ('3', 'Joker');
Truncate table Users;
insert into Users (user_id, name) values ('1', 'Daniel');
insert into Users (user_id, name) values ('2', 'Monica');
insert into Users (user_id, name) values ('3', 'Maria');
insert into Users (user_id, name) values ('4', 'James');
Truncate table MovieRating;
insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '1', '3', '2020-01-12');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '2', '4', '2020-02-11');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '3', '2', '2020-02-12');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('1', '4', '1', '2020-01-01');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('2', '1', '5', '2020-02-17');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('2', '2', '2', '2020-02-01');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('2', '3', '2', '2020-03-01');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('3', '1', '3', '2020-02-22');
insert into MovieRating (movie_id, user_id, rating, created_at) values ('3', '2', '4', '2020-02-25');
""")
def test_example():
	"""
	+--------------+
	| results      |
	+--------------+
	| Daniel       |
	| Frozen 2     |
	+--------------+
	"""
