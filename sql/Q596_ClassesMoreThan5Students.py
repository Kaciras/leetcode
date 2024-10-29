from sql_questions import define

# 用子查询也行，但内置的 HAVING 语句肯定更好。
# sql_test = define("SELECT class FROM (SELECT class, COUNT(*) AS cnt FROM Courses GROUP BY class) _ WHERE cnt >= 5")

# 因为 WHERE 在 GROUP BY 之前执行，所以无法过滤分组后的数据，于是就有 HAVING。
# HAVING 子句可以让我们筛选分组后的数据。
sql_test = define("SELECT class FROM Courses GROUP BY class HAVING COUNT(*) >= 5")

@sql_test("""\
Create table If Not Exists Courses (student varchar(255), class varchar(255));
Truncate table Courses;
insert into Courses (student, class) values ('A', 'Math');
insert into Courses (student, class) values ('B', 'English');
insert into Courses (student, class) values ('C', 'Math');
insert into Courses (student, class) values ('D', 'Biology');
insert into Courses (student, class) values ('E', 'Math');
insert into Courses (student, class) values ('F', 'Computer');
insert into Courses (student, class) values ('G', 'Math');
insert into Courses (student, class) values ('H', 'Math');
insert into Courses (student, class) values ('I', 'Math');
""")
def test_example1():
	"""
	+---------+
	| class   |
	+---------+
	| Math    |
	+---------+
	"""
