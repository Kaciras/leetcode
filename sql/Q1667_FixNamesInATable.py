from sql_questions import define

sql_test = define("""
SELECT user_id, CONCAT(
	UPPER(SUBSTRING(NAME, 1, 1)), 
	LOWER(SUBSTRING(NAME, 2))
) AS name
FROM Users ORDER BY user_id
""")

sql_test.check_order = True

@sql_test("""\
	Create table If Not Exists Users (user_id int, name varchar(40));
	Truncate table Users;
	insert into Users (user_id, name) values ('1', 'aLice');
	insert into Users (user_id, name) values ('2', 'bOB');
""")
def test_example():
	"""
	+---------+-------+
	| user_id | name  |
	+---------+-------+
	| 1       | Alice |
	| 2       | Bob   |
	+---------+-------+
	"""
