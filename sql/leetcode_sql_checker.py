import functools
import inspect
import os

import dotenv
import mariadb
from pytest_unordered import unordered

dotenv.load_dotenv()

connection = mariadb.connect(
	database=os.getenv("MARIADB_DATABASE"),
	host=os.getenv("MARIADB_HOST"),
	port=int(os.getenv("MARIADB_PORT")),
	user=os.getenv("MARIADB_USER"),
	password=os.getenv("MARIADB_PASSWORD"),
)

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


def _parse_ascii_table(table: str):
	lines = table.splitlines()
	columns = _parse_ascii_line(lines[1])
	data = []
	for line in lines[3:-1]:
		data.append(_parse_ascii_line(line))

	return columns, data


def _parse_ascii_line(line: str):
	return tuple(cell.strip() for cell in line.split("|")[1:-1])


def define(sql: str, check_order=False):
	def sql_test(schema: str):
		def decorator(func):
			@functools.wraps(func)
			def template():
				expected = inspect.cleandoc(func.__doc__)
				with connection.cursor() as cursor:
					_execute_script(cursor, schema)
					cursor.execute(sql)
					h, b = _parse_ascii_table(expected)
					x = tuple(x[0] for x in cursor.description)
					assert x == h

					result = []
					for row in cursor:
						result.append(tuple(str(x) for x in row))

					if check_order:
						assert result == b
					else:
						assert result == unordered(b)

			return template

		return decorator

	return sql_test
