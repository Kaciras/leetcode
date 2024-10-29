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
def test_example1():
	"""\
	+-------------+
	| customer_id |
	+-------------+
	| 1           |
	| 3           |
	+-------------+
	"""
