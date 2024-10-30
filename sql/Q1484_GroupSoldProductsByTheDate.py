from sql_questions import define

# MySQL 用 GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ',')
# PG    用 STRING_AGG(DISTINCT product, ',' ORDER BY product)
#
# 还有这题有错误，T-Shirt 的 S 大小写给的是错的，MySQL 倒是正好给搞错。

sql_test = define("""
SELECT
	sell_date,
	COUNT(DISTINCT product) AS num_sold,
	STRING_AGG(DISTINCT product, ',' ORDER BY product) AS products
FROM
	Activities
GROUP BY
	sell_date
ORDER BY
	sell_date
""")

@sql_test("""\
Create table If Not Exists Activities (sell_date date, product varchar(20));
Truncate table Activities;
insert into Activities (sell_date, product) values ('2020-05-30', 'Headphone');
insert into Activities (sell_date, product) values ('2020-06-01', 'Pencil');
insert into Activities (sell_date, product) values ('2020-06-02', 'Mask');
insert into Activities (sell_date, product) values ('2020-05-30', 'Basketball');
insert into Activities (sell_date, product) values ('2020-06-01', 'Bible');
insert into Activities (sell_date, product) values ('2020-06-02', 'Mask');
insert into Activities (sell_date, product) values ('2020-05-30', 'T-Shirt');
""")
def test_example():
	"""
	+------------+----------+------------------------------+
	| sell_date  | num_sold | products                     |
	+------------+----------+------------------------------+
	| 2020-05-30 | 3        | Basketball,Headphone,T-Shirt |
	| 2020-06-01 | 2        | Bible,Pencil                 |
	| 2020-06-02 | 1        | Mask                         |
	+------------+----------+------------------------------+
	"""
