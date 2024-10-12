from sql_questions import define

# 日期运算，使用 INTERVAL <value> <unit> 来定义时长。

sql_test = define("""
SELECT b.id FROM Weather a JOIN Weather b 
ON a.recordDate = b.recordDate - INTERVAL 1 DAY 
WHERE a.temperature < b.temperature
""")

@sql_test("""\
Create table If Not Exists Weather (id int, recordDate date, temperature int);
Truncate table Weather;
insert into Weather (id, recordDate, temperature) values ('1', '2015-01-01', '10');
insert into Weather (id, recordDate, temperature) values ('2', '2015-01-02', '25');
insert into Weather (id, recordDate, temperature) values ('3', '2015-01-03', '20');
insert into Weather (id, recordDate, temperature) values ('4', '2015-01-04', '30');
""")
def test_example1():
	"""\
	+----+
	| id |
	+----+
	| 2  |
	| 4  |
	+----+
	"""

@sql_test("""\
Create table If Not Exists Weather (id int, recordDate date, temperature int);
Truncate table Weather;
insert into Weather (id, recordDate, temperature) values ('1', '2015-01-31', '10');
insert into Weather (id, recordDate, temperature) values ('2', '2015-02-01', '25');
insert into Weather (id, recordDate, temperature) values ('3', '2015-02-03', '20');
insert into Weather (id, recordDate, temperature) values ('4', '2015-02-04', '30');
""")
def test_example2():
	"""\
	+----+
	| id |
	+----+
	| 2  |
	| 4  |
	+----+
	"""
