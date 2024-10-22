from sql_questions import define

sql_test = define(r"""
SELECT person_name FROM (
  SELECT person_name, SUM(weight) OVER (ORDER BY turn) AS total FROM Queue
) _ 
WHERE total <= 1000 ORDER BY total DESC LIMIT 1
""")


@sql_test("""\
Create table If Not Exists Queue (person_id int, person_name varchar(30), weight int, turn int);
Truncate table Queue;
insert into Queue (person_id, person_name, weight, turn) values ('5', 'Alice', '250', '1');
insert into Queue (person_id, person_name, weight, turn) values ('4', 'Bob', '175', '5');
insert into Queue (person_id, person_name, weight, turn) values ('3', 'Alex', '350', '2');
insert into Queue (person_id, person_name, weight, turn) values ('6', 'John Cena', '400', '3');
insert into Queue (person_id, person_name, weight, turn) values ('1', 'Winston', '500', '6');
insert into Queue (person_id, person_name, weight, turn) values ('2', 'Marie', '200', '4');
""")
def test_example():
	"""\
	+-------------+
	| person_name |
	+-------------+
	| John Cena   |
	+-------------+
	"""
