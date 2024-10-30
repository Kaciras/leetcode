from sql_questions import define

# PG 对于未聚合的列不会自动选择分组的第一行，弱智。

sql_test = define(r"""
SELECT 
	a.employee_id, 
	a.name, 
	COUNT(*) AS reports_count, 
	ROUND(AVG(b.age)) AS average_age 
FROM 
	Employees a JOIN Employees b 
ON 
	a.employee_id = b.reports_to 
GROUP BY 
	a.employee_id, a.name 
ORDER BY 
	employee_id
""")

sql_test.check_order = True


@sql_test("""\
Create table If Not Exists Employees(employee_id int, name varchar(20), reports_to int, age int);
Truncate table Employees;
insert into Employees (employee_id, name, reports_to, age) values ('9', 'Hercy', NULL, '43');
insert into Employees (employee_id, name, reports_to, age) values ('6', 'Alice', '9', '41');
insert into Employees (employee_id, name, reports_to, age) values ('4', 'Bob', '9', '36');
insert into Employees (employee_id, name, reports_to, age) values ('2', 'Winston', NULL, '37');
""")
def test_example1():
	"""\
	+-------------+-------+---------------+-------------+
	| employee_id | name  | reports_count | average_age |
	+-------------+-------+---------------+-------------+
	| 9           | Hercy | 2             | 39          |
	+-------------+-------+---------------+-------------+
	"""

# TODO: 从 ASCII 表格生成 SQL 内容。
# @sql_test("""\
# 	+-------------+---------+------------+-----+
# 	| employee_id | name    | reports_to | age |
# 	|-------------|---------|------------|-----|
# 	| 1           | Michael | null       | 45  |
# 	| 2           | Alice   | 1          | 38  |
# 	| 3           | Bob     | 1          | 42  |
# 	| 4           | Charlie | 2          | 34  |
# 	| 5           | David   | 2          | 40  |
# 	| 6           | Eve     | 3          | 37  |
# 	| 7           | Frank   | null       | 50  |
# 	| 8           | Grace   | null       | 48  |
# 	+-------------+---------+------------+-----+
# """)
# def test_example2():
# 	"""\
# 	+-------------+---------+---------------+-------------+
# 	| employee_id | name    | reports_count | average_age |
# 	| ----------- | ------- | ------------- | ----------- |
# 	| 1           | Michael | 2             | 40          |
# 	| 2           | Alice   | 2             | 37          |
# 	| 3           | Bob     | 1             | 37          |
# 	+-------------+---------+---------------+-------------+
# 	"""
