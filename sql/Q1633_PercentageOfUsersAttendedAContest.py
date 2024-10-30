from sql_questions import define

sql_test = define("""
SELECT 
	contest_id, 
	ROUND(COUNT(*)::numeric * 100 / (SELECT COUNT(*) FROM Users), 2) AS percentage 
FROM 
	Users 
JOIN 
	Register 
ON 
	Users.user_id = Register.user_id 
GROUP BY 
	contest_id 
ORDER BY 
	percentage DESC, contest_id
""")


@sql_test("""\
Create table If Not Exists Users (user_id int, user_name varchar(20));
Create table If Not Exists Register (contest_id int, user_id int);
Truncate table Users;
insert into Users (user_id, user_name) values ('6', 'Alice');
insert into Users (user_id, user_name) values ('2', 'Bob');
insert into Users (user_id, user_name) values ('7', 'Alex');
Truncate table Register;
insert into Register (contest_id, user_id) values ('215', '6');
insert into Register (contest_id, user_id) values ('209', '2');
insert into Register (contest_id, user_id) values ('208', '2');
insert into Register (contest_id, user_id) values ('210', '6');
insert into Register (contest_id, user_id) values ('208', '6');
insert into Register (contest_id, user_id) values ('209', '7');
insert into Register (contest_id, user_id) values ('209', '6');
insert into Register (contest_id, user_id) values ('215', '7');
insert into Register (contest_id, user_id) values ('208', '7');
insert into Register (contest_id, user_id) values ('210', '2');
insert into Register (contest_id, user_id) values ('207', '2');
insert into Register (contest_id, user_id) values ('210', '7');
""")
def test_example1():
	"""
	+------------+------------+
	| contest_id | percentage |
	+------------+------------+
	| 208        | 100.00     |
	| 209        | 100.00     |
	| 210        | 100.00     |
	| 215        | 66.67      |
	| 207        | 33.33      |
	+------------+------------+
	"""
