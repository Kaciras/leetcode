from sql_questions import define

# 数量大于 1 即表示有重复，反之没有，故用分组也能判断。另外 IN 是支持多列的。

sql_test = define(r"""
SELECT ROUND(SUM(tiv_2016)::NUMERIC, 2) AS tiv_2016 FROM Insurance
WHERE 
  tiv_2015 IN (SELECT tiv_2015 FROM Insurance GROUP BY tiv_2015 HAVING COUNT(*) > 1) AND
  (lat, lon) IN (SELECT lat, lon FROM Insurance GROUP BY lat, lon HAVING COUNT(*) = 1)
""")

@sql_test("""\
Create Table If Not Exists Insurance (pid int, tiv_2015 float, tiv_2016 float, lat float, lon float);
Truncate table Insurance;
insert into Insurance (pid, tiv_2015, tiv_2016, lat, lon) values ('1', '10', '5', '10', '10');
insert into Insurance (pid, tiv_2015, tiv_2016, lat, lon) values ('2', '20', '20', '20', '20');
insert into Insurance (pid, tiv_2015, tiv_2016, lat, lon) values ('3', '10', '30', '20', '20');
insert into Insurance (pid, tiv_2015, tiv_2016, lat, lon) values ('4', '10', '40', '40', '40');
""")
def test_example1():
	"""\
	+----------+
	| tiv_2016 |
	+----------+
	| 45.00    |
	+----------+
	"""
