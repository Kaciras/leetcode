from leetcode_sql_checker import define

answer = """
SELECT teacher_id, count(distinct subject_id) as cnt FROM Teacher GROUP BY teacher_id
"""

sql_test = define(answer)

@sql_test("""\
	Create table If Not Exists Teacher (teacher_id int, subject_id int, dept_id int);
	Truncate table Teacher;
	insert into Teacher (teacher_id, subject_id, dept_id) values ('1', '2', '3');
	insert into Teacher (teacher_id, subject_id, dept_id) values ('1', '2', '4');
	insert into Teacher (teacher_id, subject_id, dept_id) values ('1', '3', '3');
	insert into Teacher (teacher_id, subject_id, dept_id) values ('2', '1', '1');
	insert into Teacher (teacher_id, subject_id, dept_id) values ('2', '2', '1');
	insert into Teacher (teacher_id, subject_id, dept_id) values ('2', '3', '1');
	insert into Teacher (teacher_id, subject_id, dept_id) values ('2', '4', '1');
""")
def test_example():
	"""
	+------------+-----+
	| teacher_id | cnt |
	+------------+-----+
	| 1          | 2   |
	| 2          | 4   |
	+------------+-----+
	"""
