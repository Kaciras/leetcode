from sql_questions import define

# 用窗口函数 OVER 来做，注意 RANGE BETWEEN 语句可以指定范围。
# 该 SQL 无法在 MariaDB 上运行，因为它不支持 RANGE BETWEEN INTERVAL。
# 最后的 OFFSET 不能离开 LIMIT 使用，有点恶行。
sql_test = define("""
SELECT
	*,
	ROUND(amount / 7, 2) AS average_amount 
FROM
(
	SELECT
		visited_on,
		SUM(amount) OVER(ORDER BY visited_on RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW) AS amount 
    FROM
		Customer 
) _ 
GROUP BY
	visited_on 
ORDER BY
	visited_on 
LIMIT 99999 OFFSET 6
""")

# 不用窗函数也能做啊，自己分组 + 过滤一下。
sql_test = define("""
SELECT 
	v1.visited_on, SUM(amount) AS amount, ROUND(SUM(amount) / 7, 2) AS average_amount 
FROM 
	(SELECT DISTINCT visited_on FROM Customer) v1 JOIN Customer v2 
ON 
	v2.visited_on <= v1.visited_on AND v2.visited_on + INTERVAL 6 DAY >= v1.visited_on 
GROUP BY 
	v1.visited_on 
HAVING 
	MIN(v2.visited_on) + INTERVAL 6 DAY = v1.visited_on 
ORDER BY 
	v1.visited_on
""")

@sql_test("""\
Create table If Not Exists Customer (customer_id int, name varchar(20), visited_on date, amount int);
Truncate table Customer;
insert into Customer (customer_id, name, visited_on, amount) values ('1', 'Jhon', '2019-01-01', '100');
insert into Customer (customer_id, name, visited_on, amount) values ('2', 'Daniel', '2019-01-02', '110');
insert into Customer (customer_id, name, visited_on, amount) values ('3', 'Jade', '2019-01-03', '120');
insert into Customer (customer_id, name, visited_on, amount) values ('4', 'Khaled', '2019-01-04', '130');
insert into Customer (customer_id, name, visited_on, amount) values ('5', 'Winston', '2019-01-05', '110');
insert into Customer (customer_id, name, visited_on, amount) values ('6', 'Elvis', '2019-01-06', '140');
insert into Customer (customer_id, name, visited_on, amount) values ('7', 'Anna', '2019-01-07', '150');
insert into Customer (customer_id, name, visited_on, amount) values ('8', 'Maria', '2019-01-08', '80');
insert into Customer (customer_id, name, visited_on, amount) values ('9', 'Jaze', '2019-01-09', '110');
insert into Customer (customer_id, name, visited_on, amount) values ('1', 'Jhon', '2019-01-10', '130');
insert into Customer (customer_id, name, visited_on, amount) values ('3', 'Jade', '2019-01-10', '150');
""")
def test_example():
	"""
	+--------------+--------------+----------------+
	| visited_on   | amount       | average_amount |
	+--------------+--------------+----------------+
	| 2019-01-07   | 860          | 122.86         |
	| 2019-01-08   | 840          | 120            |
	| 2019-01-09   | 840          | 120            |
	| 2019-01-10   | 1000         | 142.86         |
	+--------------+--------------+----------------+
	"""

@sql_test(Customer="""\
	+--------------+--------------+----------------+
	| visited_on   | amount       | average_amount |
	+--------------+--------------+----------------+
	| 2019-01-07   | 860          | 122.86         |
	| 2019-01-08   | 840          | 120            |
	| 2019-01-09   | 840          | 120            |
	| 2019-01-10   | 1000         | 142.86         |
	+--------------+--------------+----------------+
""")
def test_example():
	"""
	+--------------+--------------+----------------+
	| visited_on   | amount       | average_amount |
	+--------------+--------------+----------------+
	| 2019-01-07   | 860          | 122.86         |
	| 2019-01-08   | 840          | 120            |
	| 2019-01-09   | 840          | 120            |
	| 2019-01-10   | 1000         | 142.86         |
	+--------------+--------------+----------------+
	"""
