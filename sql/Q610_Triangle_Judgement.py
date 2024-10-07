from leetcode_sql_checker import define

# CASE 是标准的 SQL，用来实现条件逻辑。
sql_test = define("""
	SELECT *, CASE 
		WHEN x + y > z 
		AND  x + z > y 
		AND  y + z > x 
		THEN 'Yes' ELSE 'No' 
		END AS triangle 
	FROM Triangle
""")

@sql_test("""\
	Create table If Not Exists Triangle (x int, y int, z int);
	Truncate table Triangle;
	insert into Triangle (x, y, z) values ('13', '15', '30');
	insert into Triangle (x, y, z) values ('10', '20', '15');
""")
def test_example():
	"""
	+----+----+----+----------+
	| x  | y  | z  | triangle |
	+----+----+----+----------+
	| 13 | 15 | 30 | No       |
	| 10 | 20 | 15 | Yes      |
	+----+----+----+----------+
	"""
