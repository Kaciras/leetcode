from sql_questions import define

sql_test = define(r"""
SELECT 
	Students.student_id, 
	student_name,
	Subjects.subject_name, 
	COUNT(Examinations.subject_name) AS attended_exams
FROM 
	Students CROSS JOIN Subjects
LEFT JOIN 
	Examinations 
ON 
	Students.student_id = Examinations.student_id AND
	Subjects.subject_name = Examinations.subject_name
GROUP BY 
	Students.student_id, student_name, Subjects.subject_name
ORDER BY 
	Students.student_id, subject_name
""")

sql_test.check_order = True


@sql_test("""\
Create table If Not Exists Students (student_id int, student_name varchar(20));
Create table If Not Exists Subjects (subject_name varchar(20));
Create table If Not Exists Examinations (student_id int, subject_name varchar(20));
Truncate table Students;
insert into Students (student_id, student_name) values ('1', 'Alice');
insert into Students (student_id, student_name) values ('2', 'Bob');
insert into Students (student_id, student_name) values ('13', 'John');
insert into Students (student_id, student_name) values ('6', 'Alex');
Truncate table Subjects;
insert into Subjects (subject_name) values ('Math');
insert into Subjects (subject_name) values ('Physics');
insert into Subjects (subject_name) values ('Programming');
Truncate table Examinations;
insert into Examinations (student_id, subject_name) values ('1', 'Math');
insert into Examinations (student_id, subject_name) values ('1', 'Physics');
insert into Examinations (student_id, subject_name) values ('1', 'Programming');
insert into Examinations (student_id, subject_name) values ('2', 'Programming');
insert into Examinations (student_id, subject_name) values ('1', 'Physics');
insert into Examinations (student_id, subject_name) values ('1', 'Math');
insert into Examinations (student_id, subject_name) values ('13', 'Math');
insert into Examinations (student_id, subject_name) values ('13', 'Programming');
insert into Examinations (student_id, subject_name) values ('13', 'Physics');
insert into Examinations (student_id, subject_name) values ('2', 'Math');
insert into Examinations (student_id, subject_name) values ('1', 'Math');
""")
def test_example1():
	"""\
	+------------+--------------+--------------+----------------+
	| student_id | student_name | subject_name | attended_exams |
	+------------+--------------+--------------+----------------+
	| 1          | Alice        | Math         | 3              |
	| 1          | Alice        | Physics      | 2              |
	| 1          | Alice        | Programming  | 1              |
	| 2          | Bob          | Math         | 1              |
	| 2          | Bob          | Physics      | 0              |
	| 2          | Bob          | Programming  | 1              |
	| 6          | Alex         | Math         | 0              |
	| 6          | Alex         | Physics      | 0              |
	| 6          | Alex         | Programming  | 0              |
	| 13         | John         | Math         | 1              |
	| 13         | John         | Physics      | 1              |
	| 13         | John         | Programming  | 1              |
	+------------+--------------+--------------+----------------+
	"""
