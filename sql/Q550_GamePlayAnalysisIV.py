from sql_questions import define

solution1 = R"""
SELECT ROUND(COUNT(*)::numeric / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM Activity a0 
JOIN Activity a1 ON a0.player_id = a1.player_id AND a0.event_date + INTERVAL '1 day' = a1.event_date
WHERE a0.event_date = (SELECT MIN(event_date) FROM Activity WHERE player_id = a0.player_id)
"""

sql_test = define(R"""
SELECT ROUND(COUNT(*)::numeric / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM Activity
WHERE (player_id, event_date - INTERVAL '1 day') IN (
	SELECT player_id, MIN(event_date) FROM Activity GROUP BY player_id
)
""")


@sql_test("""\
Create table If Not Exists Activity (player_id int, device_id int, event_date date, games_played int);
Truncate table Activity;
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-01', '5');
insert into Activity (player_id, device_id, event_date, games_played) values ('1', '2', '2016-03-02', '6');
insert into Activity (player_id, device_id, event_date, games_played) values ('2', '3', '2017-06-25', '1');
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '1', '2016-03-02', '0');
insert into Activity (player_id, device_id, event_date, games_played) values ('3', '4', '2018-07-03', '5');
""")
def test_example1():
	"""
	+-----------+
	| fraction  |
	+-----------+
	| 0.33      |
	+-----------+
	"""
