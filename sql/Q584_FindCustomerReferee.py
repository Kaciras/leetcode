from sql_questions import define

# MySQL 有个 <=> 表示等于或为 NULL，PG 冇得。

sql_test = define("SELECT name FROM Customer WHERE NOT referee_id = 2 OR referee_id IS NULL")

@sql_test("""\
Create table If Not Exists Customer (id int, name varchar(25), referee_id int);
Truncate table Customer;
insert into Customer (id, name, referee_id) values ('1', 'Will', NULL);
insert into Customer (id, name, referee_id) values ('2', 'Jane', NULL);
insert into Customer (id, name, referee_id) values ('3', 'Alex', '2');
insert into Customer (id, name, referee_id) values ('4', 'Bill', NULL);
insert into Customer (id, name, referee_id) values ('5', 'Zack', '1');
insert into Customer (id, name, referee_id) values ('6', 'Mark', '2');
""")
def test_example1():
	"""
	+------+
	| name |
	+------+
	| Will |
	| Jane |
	| Bill |
	| Zack |
	+------+
	"""
