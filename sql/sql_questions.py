import inspect
import os
import re
from functools import wraps, partial
from typing import Optional

import dotenv
import psycopg
from pytest_unordered import unordered

__all__ = ("connection", "define")

dotenv.load_dotenv()

_enum_re = re.compile(r"ENUM\(.+?\)", re.IGNORECASE)

connection = psycopg.connect(
	dbname="test",
	host=os.getenv("PG_HOST"),
	port=os.getenv("PG_PORT"),
	user=os.getenv("PG_USER"),
	password=os.getenv("PG_PASSWORD"),
)



def _execute_script(script: str):
	"""
	MariaDB 的连接库不支持一次执行多条语句，所以得自己分割下。
	https://jira.mariadb.org/browse/CONPY-151
	"""
	for statement in script.split(";\n"):
		if not statement:
			continue
		if statement.startswith("--"):
			continue
		if statement.startswith("Create table"):
			statement = transpile_ddl(statement)

		connection.execute(statement)


def transpile_ddl(sql: str):
	sql = sql.replace(" datetime", " timestamp")
	return _enum_re.sub("text", sql)


def _parse_ascii_table(table: str):
	lines = table.splitlines()
	columns = _parse_ascii_line(lines[1])
	data = []
	for line in lines[3:-1]:
		data.append(_parse_ascii_line(line))

	return columns, data


def _parse_ascii_line(line: str):
	return tuple(map(_sql_value_to_py, line.split("|")[1:-1]))


def _sql_value_to_py(value: str):
	value = value.strip()
	return None if value == "null" else value


def _py_value_to_sql(value):
	"""

	"""
	return "null" if value is None else str(value)


class define:
	"""
	一些废案：
	- 写在 sql 文件里，虽然好看但是判定部分难搞，我懒得为它写个插件。
	- 默认参数定义用例，但会被当作未使用而变灰。
	- return 作为关键词跟 SQL 的高亮重了，也不适合定义用例。
	"""

	check_order = False
	delete_table: Optional[str] = None

	def __init__(self, sql: str):
		self.sql = sql

	def __call__(self, schema: str = None, **kwargs):
		return lambda f: wraps(f)(partial(self._template, schema, f))

	def _template(self, schema: str, func):
		expected = inspect.cleandoc(func.__doc__)
		with connection.cursor() as cursor:
			_execute_script(schema)
			cursor.execute(self.sql)

			if self.delete_table:
				cursor.execute(f"SELECT * FROM {self.delete_table}")

			header, body = _parse_ascii_table(expected)
			columns = tuple(x[0].lower() for x in cursor.description)
			assert columns == header

			result = []
			for row in cursor:
				result.append(tuple(map(_py_value_to_sql, row)))

			if self.check_order:
				assert result == body
			else:
				assert result == unordered(body)
