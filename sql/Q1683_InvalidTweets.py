from sql_questions import define

sql_test = define("SELECT tweet_id FROM Tweets WHERE LENGTH(content) > 15")


@sql_test("""\
Create table If Not Exists Tweets(tweet_id int, content varchar(50));
Truncate table Tweets;
insert into Tweets (tweet_id, content) values ('1', 'Let us Code');
insert into Tweets (tweet_id, content) values ('2', 'More than fifteen chars are here!');
""")
def test_example1():
	"""
	+----------+
	| tweet_id |
	+----------+
	| 2        |
	+----------+
	"""
