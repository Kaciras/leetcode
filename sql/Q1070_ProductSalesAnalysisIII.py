from sql_questions import define

# 用 ROW_NUMBER 不对，难道 product_id + year 有重复？

sql_test = define("""
SELECT product_id, year AS first_year, quantity, price FROM 
(SELECT *, RANK() OVER(PARTITION BY product_id ORDER BY year) AS k FROM Sales) _ WHERE k=1
""")

@sql_test("""\
Create table If Not Exists Sales (sale_id int, product_id int, year int, quantity int, price int);
Create table If Not Exists Product (product_id int, product_name varchar(10));
Truncate table Sales;
insert into Sales (sale_id, product_id, year, quantity, price) values ('1', '100', '2008', '10', '5000');
insert into Sales (sale_id, product_id, year, quantity, price) values ('2', '100', '2009', '12', '5000');
insert into Sales (sale_id, product_id, year, quantity, price) values ('7', '200', '2011', '15', '9000');
Truncate table Product;
insert into Product (product_id, product_name) values ('100', 'Nokia');
insert into Product (product_id, product_name) values ('200', 'Apple');
insert into Product (product_id, product_name) values ('300', 'Samsung');
""")
def test_example1():
	"""\
	+------------+------------+----------+-------+
	| product_id | first_year | quantity | price |
	+------------+------------+----------+-------+
	| 100        | 2008       | 10       | 5000  |
	| 200        | 2011       | 15       | 9000  |
	+------------+------------+----------+-------+
	"""
