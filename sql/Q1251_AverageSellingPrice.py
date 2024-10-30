from sql_questions import define

# COALESCE 可以把 NULL 转为指定的值，且支持表达式；ISNULL 仅支持列。
# BETWEEN 是双闭区间，此题正好是相等的日期也算。

sql_test = define("""
SELECT Prices.product_id, COALESCE(ROUND(SUM(price * units)::numeric / SUM(units), 2), 0) AS average_price
FROM Prices LEFT JOIN UnitsSold 
ON Prices.product_id = UnitsSold.product_id AND purchase_date BETWEEN start_date AND end_date
GROUP BY Prices.product_id
""")

@sql_test("""\
Create table If Not Exists Prices (product_id int, start_date date, end_date date, price int);
Create table If Not Exists UnitsSold (product_id int, purchase_date date, units int);
Truncate table Prices;
insert into Prices (product_id, start_date, end_date, price) values ('1', '2019-02-17', '2019-02-28', '5');
insert into Prices (product_id, start_date, end_date, price) values ('1', '2019-03-01', '2019-03-22', '20');
insert into Prices (product_id, start_date, end_date, price) values ('2', '2019-02-01', '2019-02-20', '15');
insert into Prices (product_id, start_date, end_date, price) values ('2', '2019-02-21', '2019-03-31', '30');
Truncate table UnitsSold;
insert into UnitsSold (product_id, purchase_date, units) values ('1', '2019-02-25', '100');
insert into UnitsSold (product_id, purchase_date, units) values ('1', '2019-03-01', '15');
insert into UnitsSold (product_id, purchase_date, units) values ('2', '2019-02-10', '200');
insert into UnitsSold (product_id, purchase_date, units) values ('2', '2019-03-22', '30');
""")
def test_example1():
	"""
	+------------+---------------+
	| product_id | average_price |
	+------------+---------------+
	| 1          | 6.96          |
	| 2          | 16.96         |
	+------------+---------------+
	"""
