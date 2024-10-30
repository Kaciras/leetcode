from sql_questions import define

sql_test = define(r"""
SELECT Signups.user_id, ROUND(AVG(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END), 2) AS confirmation_rate
FROM Signups LEFT JOIN Confirmations ON Signups.user_id = Confirmations.user_id GROUP BY Signups.user_id
""")


@sql_test("""\
Create table If Not Exists Signups (user_id int, time_stamp datetime);
Create table If Not Exists Confirmations (user_id int, time_stamp datetime, action text);
Truncate table Signups;
insert into Signups (user_id, time_stamp) values ('3', '2020-03-21 10:16:13');
insert into Signups (user_id, time_stamp) values ('7', '2020-01-04 13:57:59');
insert into Signups (user_id, time_stamp) values ('2', '2020-07-29 23:09:44');
insert into Signups (user_id, time_stamp) values ('6', '2020-12-09 10:39:37');
Truncate table Confirmations;
insert into Confirmations (user_id, time_stamp, action) values ('3', '2021-01-06 03:30:46', 'timeout');
insert into Confirmations (user_id, time_stamp, action) values ('3', '2021-07-14 14:00:00', 'timeout');
insert into Confirmations (user_id, time_stamp, action) values ('7', '2021-06-12 11:57:29', 'confirmed');
insert into Confirmations (user_id, time_stamp, action) values ('7', '2021-06-13 12:58:28', 'confirmed');
insert into Confirmations (user_id, time_stamp, action) values ('7', '2021-06-14 13:59:27', 'confirmed');
insert into Confirmations (user_id, time_stamp, action) values ('2', '2021-01-22 00:00:00', 'confirmed');
insert into Confirmations (user_id, time_stamp, action) values ('2', '2021-02-28 23:59:59', 'timeout');
""")
def test_example1():
	"""\
	+---------+-------------------+
	| user_id | confirmation_rate |
	+---------+-------------------+
	| 6       | 0.00              |
	| 3       | 0.00              |
	| 7       | 1.00              |
	| 2       | 0.50              |
	+---------+-------------------+
	"""
