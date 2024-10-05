import os

import dotenv
import mariadb

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


def check(schema: str, rows):
	with connection.cursor() as cursor:
		_execute_script(cursor, schema)
		cursor.execute(_solution_sql)
		assert cursor.fetchall() == rows


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
