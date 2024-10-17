from sql_questions import define

sql_test = define("""
SELECT 
	project_id, ROUND(AVG(experience_years), 2) AS average_years 
FROM 
	Project 
JOIN 
	Employee 
ON 
	Project.employee_id = Employee.employee_id 
GROUP BY 
	project_id
""")


@sql_test("""\
Create table If Not Exists Project (project_id int, employee_id int);
Create table If Not Exists Employee (employee_id int, name varchar(10), experience_years int);
Truncate table Project;
insert into Project (project_id, employee_id) values ('1', '1');
insert into Project (project_id, employee_id) values ('1', '2');
insert into Project (project_id, employee_id) values ('1', '3');
insert into Project (project_id, employee_id) values ('2', '1');
insert into Project (project_id, employee_id) values ('2', '4');
Truncate table Employee;
insert into Employee (employee_id, name, experience_years) values ('1', 'Khaled', '3');
insert into Employee (employee_id, name, experience_years) values ('2', 'Ali', '2');
insert into Employee (employee_id, name, experience_years) values ('3', 'John', '1');
insert into Employee (employee_id, name, experience_years) values ('4', 'Doe', '2');
""")
def test_example():
	"""
	+-------------+---------------+
	| project_id  | average_years |
	+-------------+---------------+
	| 1           | 2.00          |
	| 2           | 2.50          |
	+-------------+---------------+
	"""
