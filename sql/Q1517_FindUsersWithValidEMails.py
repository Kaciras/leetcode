from sql_questions import define

# MySQL 用 mail REGEXP xxx，PG 使用波浪符号。

sql_test = define(r"""
SELECT * FROM Users WHERE mail ~ '^[a-zA-Z][\w.-]*@leetcode\.com$'
""")

@sql_test("""\
Create table If Not Exists Users (user_id int, name varchar(30), mail varchar(50));
Truncate table Users;
insert into Users (user_id, name, mail) values ('1', 'Winston', 'winston@leetcode.com');
insert into Users (user_id, name, mail) values ('2', 'Jonathan', 'jonathanisgreat');
insert into Users (user_id, name, mail) values ('3', 'Annabelle', 'bella-@leetcode.com');
insert into Users (user_id, name, mail) values ('4', 'Sally', 'sally.come@leetcode.com');
insert into Users (user_id, name, mail) values ('5', 'Marwan', 'quarz#2020@leetcode.com');
insert into Users (user_id, name, mail) values ('6', 'David', 'david69@gmail.com');
insert into Users (user_id, name, mail) values ('7', 'Shapiro', '.shapo@leetcode.com');
""")
def test_example1():
	"""\
	+---------+-----------+-------------------------+
	| user_id | name      | mail                    |
	+---------+-----------+-------------------------+
	| 1       | Winston   | winston@leetcode.com    |
	| 3       | Annabelle | bella-@leetcode.com     |
	| 4       | Sally     | sally.come@leetcode.com |
	+---------+-----------+-------------------------+
	"""
