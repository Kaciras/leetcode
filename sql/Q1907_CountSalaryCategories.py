from sql_questions import define

# UNION 不加 ALL 会进行去重，导致顺序变化，UNION ALL 则按照添加的顺序返回。

sql_test = define(R"""
SELECT 'Low Salary' AS category, COUNT(*) AS accounts_count FROM Accounts WHERE income < 20000
UNION ALL
SELECT 'Average Salary' AS category, COUNT(*) AS accounts_count FROM Accounts WHERE income BETWEEN 20000 AND 50000
UNION ALL
SELECT 'High Salary' AS category, COUNT(*) AS accounts_count FROM Accounts WHERE income > 50000
""")


@sql_test("""\
Create table If Not Exists Accounts (account_id int, income int);
Truncate table Accounts;
insert into Accounts (account_id, income) values ('3', '108939');
insert into Accounts (account_id, income) values ('2', '12747');
insert into Accounts (account_id, income) values ('8', '87709');
insert into Accounts (account_id, income) values ('6', '91796');
""")
def test_example1():
	"""
	+----------------+----------------+
	| category       | accounts_count |
	+----------------+----------------+
	| Low Salary     | 1              |
	| Average Salary | 0              |
	| High Salary    | 3              |
	+----------------+----------------+
	"""
