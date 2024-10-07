import inspect
import os
from functools import wraps, partial

import dotenv
import mariadb
from pytest_unordered import unordered

__all__ = ("connection", "define")

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


class define:
	"""
	一些废案：
	- 写在 sql 文件里，虽然好看但是判定部分难搞，我懒得为它写个插件。
	- 默认参数定义用例，但会被当作未使用而变灰。
	- return 作为关键词跟 SQL 的高亮重了，也不适合定义用例。
	"""

	check_order = False

	def __init__(self, sql: str):
		self.sql = sql

	def __call__(self, schema: str):
		return lambda f: wraps(f)(partial(self._template, schema, f))

	def _template(self, schema: str, func):
		expected = inspect.cleandoc(func.__doc__)
		with connection.cursor() as cursor:
			_execute_script(cursor, schema)
			cursor.execute(self.sql)
			h, b = _parse_ascii_table(expected)
			x = tuple(x[0] for x in cursor.description)
			assert x == h

			result = []
			for row in cursor:
				result.append(tuple(str(x) for x in row))

			if self.check_order:
				assert result == b
			else:
				assert result == unordered(b)
