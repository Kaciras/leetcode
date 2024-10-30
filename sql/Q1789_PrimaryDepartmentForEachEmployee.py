from sql_questions import define

# 这题也可以用 COUNT(*) + PARTIION 来过滤只有一个部门的。

sql_test = define(R"""
SELECT employee_id, department_id FROM Employee WHERE primary_flag = 'Y'
UNION
SELECT employee_id, MIN(department_id) FROM Employee GROUP BY employee_id HAVING COUNT(*) = 1
""")


@sql_test("""\
Create table If Not Exists Employee (employee_id int, department_id int, primary_flag ENUM('Y','N'));
Truncate table Employee;
insert into Employee (employee_id, department_id, primary_flag) values ('1', '1', 'N');
insert into Employee (employee_id, department_id, primary_flag) values ('2', '1', 'Y');
insert into Employee (employee_id, department_id, primary_flag) values ('2', '2', 'N');
insert into Employee (employee_id, department_id, primary_flag) values ('3', '3', 'N');
insert into Employee (employee_id, department_id, primary_flag) values ('4', '2', 'N');
insert into Employee (employee_id, department_id, primary_flag) values ('4', '3', 'Y');
insert into Employee (employee_id, department_id, primary_flag) values ('4', '4', 'N');
""")
def test_example1():
	"""
	+-------------+---------------+
	| employee_id | department_id |
	+-------------+---------------+
	| 1           | 1             |
	| 2           | 1             |
	| 3           | 3             |
	| 4           | 3             |
	+-------------+---------------+
	"""
