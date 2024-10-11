from leetcode_sql_checker import define

# MySQL 不能同时改动查询的表（MariaDB 倒是可以），有两种方案：
# 1）使用 CTE
# 2）再套一层子查询，这样会创建临时表。

sql_test = define("""
DELETE FROM Person WHERE id NOT IN (SELECT MIN(id) FROM (SELECT * FROM Person) AS temp GROUP BY email)
""")

sql_test.delete_table = "Person"

@sql_test("""\
Create table If Not Exists Person (Id int, Email varchar(255));
Truncate table Person;
insert into Person (id, email) values ('1', 'john@example.com');
insert into Person (id, email) values ('2', 'bob@example.com');
insert into Person (id, email) values ('3', 'john@example.com');
""")

def test_example():
	"""\
	+----+------------------+
	| id | email            |
	+----+------------------+
	| 1  | john@example.com |
	| 2  | bob@example.com  |
	+----+------------------+
	"""
