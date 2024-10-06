import os
from io import StringIO

import dotenv
import mariadb
from rich.box import ASCII2
from rich.console import Console
from rich.table import Table

dotenv.load_dotenv()

connection = mariadb.connect(
	database=os.getenv("MARIADB_DATABASE"),
	host=os.getenv("MARIADB_HOST"),
	port=int(os.getenv("MARIADB_PORT")),
	user=os.getenv("MARIADB_USER"),
	password=os.getenv("MARIADB_PASSWORD"),
)

_solution_sql: str


def set_solution(sql: str):
	global _solution_sql
	_solution_sql = sql



def _execute_script(cursor: mariadb.Cursor, script: str):
	"""
	MariaDB 的连接库不支持一次执行多条语句，所以得自己分割下。
	https://jira.mariadb.org/browse/CONPY-151
	"""
	lines = script.split(";\n")
	for statement in lines:
		if not statement:
			continue
		if statement.startswith("--"):
			continue
		cursor.execute(statement)


def _sql_table(cursor: mariadb.Cursor):
	table = Table(box=ASCII2)
	for column in cursor.description:
		table.add_column(column[0])
	for row in cursor:
		table.add_row(*map(str, row))

	console = Console(file=StringIO(), width=120)
	console.print(table)
	return console.file.getvalue()


import functools
import inspect


def define_answer(sql: str):
	def sql_test(schema: str):
		def decorator(func):
			@functools.wraps(func)
			def template():
				expected = inspect.cleandoc(func.__doc__)
				with connection.cursor() as cursor:
					_execute_script(cursor, schema)
					cursor.execute(sql)
					actual = _sql_table(cursor)
					assert actual == expected + "\n"

			return template

		return decorator

	return sql_test
