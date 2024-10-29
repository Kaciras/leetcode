from sql_questions import define

# MySQL 格式化日期: DATE_FORMAT(trans_date, "%Y-%m")
# PG 格式化日期: TO_CHAR(trans_date, 'yyyy-mm')

sql_test = define("""
SELECT
	TO_CHAR(trans_date, 'yyyy-mm') AS month,
	country,
	COUNT(*) AS trans_count,
	COUNT(CASE WHEN state = 'approved' THEN 1 END) AS approved_count,
	SUM(amount) AS trans_total_amount,
	SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM
	Transactions
GROUP BY
	month, country
""")


@sql_test("""\
Create table If Not Exists Transactions (id int, country varchar(4), state enum('approved', 'declined'), amount int, trans_date date);
Truncate table Transactions;
insert into Transactions (id, country, state, amount, trans_date) values ('121', 'US', 'approved', '1000', '2018-12-18');
insert into Transactions (id, country, state, amount, trans_date) values ('122', 'US', 'declined', '2000', '2018-12-19');
insert into Transactions (id, country, state, amount, trans_date) values ('123', 'US', 'approved', '2000', '2019-01-01');
insert into Transactions (id, country, state, amount, trans_date) values ('124', 'DE', 'approved', '2000', '2019-01-07');
""")
def test_example():
	"""
	+----------+---------+-------------+----------------+--------------------+-----------------------+
	| month    | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
	+----------+---------+-------------+----------------+--------------------+-----------------------+
	| 2018-12  | US      | 2           | 1              | 3000               | 1000                  |
	| 2019-01  | US      | 1           | 1              | 2000               | 2000                  |
	| 2019-01  | DE      | 1           | 1              | 2000               | 2000                  |
	+----------+---------+-------------+----------------+--------------------+-----------------------+
	"""
