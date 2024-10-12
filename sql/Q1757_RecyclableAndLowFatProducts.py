from sql_questions import define

sql_test = define("SELECT product_id FROM Products WHERE low_fats='Y' AND recyclable='Y'")

@sql_test("""\
	Create table If Not Exists Products (product_id int, low_fats ENUM('Y', 'N'), recyclable ENUM('Y','N'));
	Truncate table Products;
	insert into Products (product_id, low_fats, recyclable) values ('0', 'Y', 'N');
	insert into Products (product_id, low_fats, recyclable) values ('1', 'Y', 'Y');
	insert into Products (product_id, low_fats, recyclable) values ('2', 'N', 'Y');
	insert into Products (product_id, low_fats, recyclable) values ('3', 'Y', 'Y');
	insert into Products (product_id, low_fats, recyclable) values ('4', 'N', 'N');
""")
def test_example():
	"""
	+-------------+
	| product_id  |
	+-------------+
	| 1           |
	| 3           |
	+-------------+
	"""
