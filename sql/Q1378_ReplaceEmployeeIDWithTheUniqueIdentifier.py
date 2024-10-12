from sql_questions import define

sql_test = define("SELECT unique_id, name FROM Employees LEFT JOIN EmployeeUNI ON Employees.id = EmployeeUNI.id")

@sql_test("""\
	Create table If Not Exists Employees (id int, name varchar(20));
	Create table If Not Exists EmployeeUNI (id int, unique_id int);
	Truncate table Employees;
	insert into Employees (id, name) values ('1', 'Alice');
	insert into Employees (id, name) values ('7', 'Bob');
	insert into Employees (id, name) values ('11', 'Meir');
	insert into Employees (id, name) values ('90', 'Winston');
	insert into Employees (id, name) values ('3', 'Jonathan');
	Truncate table EmployeeUNI;
	insert into EmployeeUNI (id, unique_id) values ('3', '1');
	insert into EmployeeUNI (id, unique_id) values ('11', '2');
	insert into EmployeeUNI (id, unique_id) values ('90', '3');
""")
def test_example():
	"""
	+-----------+----------+
	| unique_id | name     |
	+-----------+----------+
	| null      | Alice    |
	| null      | Bob      |
	| 2         | Meir     |
	| 3         | Winston  |
	| 1         | Jonathan |
	+-----------+----------+
	"""
