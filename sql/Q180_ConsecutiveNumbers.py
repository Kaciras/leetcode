from sql_questions import define

# LAG 找前 N 行的指定列，LEAD 找后面的。
# 这题只有三个连续，用 CROSS JOIN 也行；如果连续长度是动态的话，也许 CTE 递归可以做。

sql_test = define("""
SELECT DISTINCT num AS ConsecutiveNums
FROM (
	SELECT *,
		LEAD(num, 1) OVER (ORDER BY id) AS next,
		LAG(num, 1) OVER (ORDER BY id) AS prev
	FROM 
		Logs
) _
WHERE num = prev AND num = next
""")

@sql_test("""\
Create table If Not Exists Logs (id int, num int);
Truncate table Logs;
insert into Logs (id, num) values ('1', '1');
insert into Logs (id, num) values ('2', '1');
insert into Logs (id, num) values ('3', '1');
insert into Logs (id, num) values ('4', '2');
insert into Logs (id, num) values ('5', '1');
insert into Logs (id, num) values ('6', '2');
insert into Logs (id, num) values ('7', '2');
""")
def test_example1():
	"""
	+-----------------+
	| ConsecutiveNums |
	+-----------------+
	| 1               |
	+-----------------+
	"""
