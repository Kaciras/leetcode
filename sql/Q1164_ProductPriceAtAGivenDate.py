from sql_questions import define

# 太久没写 SQL 敏感性都没了，半天都没想到用 UNION 补足默认值。

sql_test = define("""
SELECT a.product_id, new_price AS price FROM Products a JOIN
(SELECT product_id, MAX(change_date) latest FROM Products WHERE change_date <= '2019-08-16' GROUP BY product_id) b
ON a.product_id = b.product_id AND a.change_date = b.latest
UNION
SELECT product_id, 10 AS price FROM Products GROUP BY product_id HAVING MIN(change_date) > '2019-08-16'
""")

@sql_test("""\
Create table If Not Exists Products (product_id int, new_price int, change_date date);
Truncate table Products;
insert into Products (product_id, new_price, change_date) values ('1', '20', '2019-08-14');
insert into Products (product_id, new_price, change_date) values ('2', '50', '2019-08-14');
insert into Products (product_id, new_price, change_date) values ('1', '30', '2019-08-15');
insert into Products (product_id, new_price, change_date) values ('1', '35', '2019-08-16');
insert into Products (product_id, new_price, change_date) values ('2', '65', '2019-08-17');
insert into Products (product_id, new_price, change_date) values ('3', '20', '2019-08-18');
""")
def test_example1():
	"""
	+------------+-------+
	| product_id | price |
	+------------+-------+
	| 2          | 50    |
	| 1          | 35    |
	| 3          | 10    |
	+------------+-------+
	"""
