from sql_questions import define

# SUM 也能 OVER 开窗，这里没有写窗口的范围，使用的是默认值：
# 1) 若没有 ORDER BY，则范围为全部。
# 2) 若有 ORDER BY，则范围为 BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW。

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
