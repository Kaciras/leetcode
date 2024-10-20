from sql_questions import define

sql_test = define(r"""
SELECT customer_id FROM Customer GROUP BY customer_id 
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product)
""")


@sql_test("""\
Create table If Not Exists Customer (customer_id int, product_key int);
Create table Product (product_key int);
Truncate table Customer;
insert into Customer (customer_id, product_key) values ('1', '5');
insert into Customer (customer_id, product_key) values ('2', '6');
insert into Customer (customer_id, product_key) values ('3', '5');
insert into Customer (customer_id, product_key) values ('3', '6');
insert into Customer (customer_id, product_key) values ('1', '6');
Truncate table Product;
insert into Product (product_key) values ('5');
insert into Product (product_key) values ('6');
""")
def test_example():
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
