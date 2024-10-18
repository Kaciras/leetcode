from sql_questions import define

sql_test = define("""
SELECT user_id, COUNT(*) AS followers_count FROM Followers GROUP BY user_id ORDER BY user_id
""")

@sql_test("""\
Create table If Not Exists Followers(user_id int, follower_id int);
Truncate table Followers;
insert into Followers (user_id, follower_id) values ('0', '1');
insert into Followers (user_id, follower_id) values ('1', '0');
insert into Followers (user_id, follower_id) values ('2', '0');
insert into Followers (user_id, follower_id) values ('2', '1');
""")
def test_example():
	"""\
	+---------+----------------+
	| user_id | followers_count|
	+---------+----------------+
	| 0       | 1              |
	| 1       | 1              |
	| 2       | 2              |
	+---------+----------------+
	"""
