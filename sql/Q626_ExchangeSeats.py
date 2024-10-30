from sql_questions import define

# 直接想到的，分别 JOIN 配奇偶，最后 UNION 在一起，性能很差。
sql_test = define("""
SELECT a.id, b.student FROM Seat a JOIN Seat b ON a.id + 1 = b.id WHERE a.id % 2 = 1
UNION ALL
SELECT a.id, b.student FROM Seat a JOIN Seat b ON a.id = b.id + 1 WHERE a.id % 2 = 0
UNION ALL
SELECT * FROM Seat WHERE id = (SELECT MAX(id) FROM Seat) AND id % 2 = 1 ORDER BY id
""")

# 用 CASE 判断三种情况，调整 id。
sql_test = define("""
SELECT CASE
	WHEN id = (SELECT MAX(id) FROM Seat) AND id % 2 = 1 THEN
		id
	WHEN id % 2 = 1 THEN
		id + 1
	ELSE
		id - 1
END AS id, student FROM Seat ORDER BY id
""")

sql_test.check_order = True


@sql_test("""\
Create table If Not Exists Seat (id int, student varchar(255));
Truncate table Seat;
insert into Seat (id, student) values ('1', 'Abbot');
insert into Seat (id, student) values ('2', 'Doris');
insert into Seat (id, student) values ('3', 'Emerson');
insert into Seat (id, student) values ('4', 'Green');
insert into Seat (id, student) values ('5', 'Jeames');
""")
def test_example1():
	"""
	+----+---------+
	| id | student |
	+----+---------+
	| 1  | Doris   |
	| 2  | Abbot   |
	| 3  | Green   |
	| 4  | Emerson |
	| 5  | Jeames  |
	+----+---------+
	"""
