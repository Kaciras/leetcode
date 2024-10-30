from sql_questions import define

# 复习 COUNT() 函数，通常用法是 COUNT(*)，但也可以提供一个参数用于统计该表达式非 NULL 的行数。
# COUNT() 是聚合函数，统计每组 GROUP BY 的数量，如果没有 GROUP BY 语句则整表为一组。

sql_test = define("""
SELECT 
	customer_id, COUNT(*) AS count_no_trans
FROM 
	Visits 
LEFT JOIN 
	Transactions 
ON 
	Visits.visit_id = Transactions.visit_id 
WHERE 
	transaction_id IS NULL
GROUP BY 
	customer_id;
""")

@sql_test("""\
Create table If Not Exists Visits(visit_id int, customer_id int);
Create table If Not Exists Transactions(transaction_id int, visit_id int, amount int);
Truncate table Visits;
insert into Visits (visit_id, customer_id) values ('1', '23');
insert into Visits (visit_id, customer_id) values ('2', '9');
insert into Visits (visit_id, customer_id) values ('4', '30');
insert into Visits (visit_id, customer_id) values ('5', '54');
insert into Visits (visit_id, customer_id) values ('6', '96');
insert into Visits (visit_id, customer_id) values ('7', '54');
insert into Visits (visit_id, customer_id) values ('8', '54');
Truncate table Transactions;
insert into Transactions (transaction_id, visit_id, amount) values ('2', '5', '310');
insert into Transactions (transaction_id, visit_id, amount) values ('3', '5', '300');
insert into Transactions (transaction_id, visit_id, amount) values ('9', '5', '200');
insert into Transactions (transaction_id, visit_id, amount) values ('12', '1', '910');
insert into Transactions (transaction_id, visit_id, amount) values ('13', '2', '970');
""")
def test_example1():
	"""
	+-------------+----------------+
	| customer_id | count_no_trans |
	+-------------+----------------+
	| 54          | 2              |
	| 30          | 1              |
	| 96          | 1              |
	+-------------+----------------+
	"""
