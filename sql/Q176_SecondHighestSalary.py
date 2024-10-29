from sql_questions import define

# 通过外面包一层查询，让空集返回 NULL。

sql_test = define("""
SELECT (SELECT DISTINCT Salary FROM Employee ORDER BY salary DESC LIMIT 1 OFFSET 1) as SecondHighestSalary;
""")

@sql_test("""\
Create table If Not Exists Employee (id int, salary int);
Truncate table Employee;
insert into Employee (id, salary) values ('1', '100');
insert into Employee (id, salary) values ('2', '200');
insert into Employee (id, salary) values ('3', '300');
""")
def test_example1():
	"""
	+---------------------+
	| SecondHighestSalary |
	+---------------------+
	| 200                 |
	+---------------------+
	"""

@sql_test("""\
Create table If Not Exists Employee (id int, salary int);
Truncate table Employee;
insert into Employee (id, salary) values ('1', '100');
""")
def test_example2():
	"""
	+---------------------+
	| SecondHighestSalary |
	+---------------------+
	| null                |
	+---------------------+
	"""
