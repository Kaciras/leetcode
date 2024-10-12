from sql_questions import define

answer = """
SELECT name FROM Employee AS a JOIN 
(SELECT managerId, COUNT(managerId) AS reports FROM Employee GROUP BY managerId) AS b 
ON a.id = b.managerId WHERE reports >= 5
"""

sql_test = define(answer)

@sql_test("""\
	Create table If Not Exists Employee (id int, name varchar(255), department varchar(255), managerId int);
	Truncate table Employee;
	insert into Employee (id, name, department, managerId) values ('101', 'John', 'A', NULL);
	insert into Employee (id, name, department, managerId) values ('102', 'Dan', 'A', '101');
	insert into Employee (id, name, department, managerId) values ('103', 'James', 'A', '101');
	insert into Employee (id, name, department, managerId) values ('104', 'Amy', 'A', '101');
	insert into Employee (id, name, department, managerId) values ('105', 'Anne', 'A', '101');
	insert into Employee (id, name, department, managerId) values ('106', 'Ron', 'B', '101');
""")
def test_example():
	"""
	+------+
	| name |
	+------+
	| John |
	+------+
	"""
