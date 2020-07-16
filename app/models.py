import pymysql as sql
from app import *
from app import connection
from flask import *

# User management
def user_exist(conn, username):
	try:
		cursor = conn.cursor()
		sql_info = "SELECT username FROM user WHERE username=%s"
		sql_where = (username)
		cursor.execute(sql_info, sql_where)
		row = cursor.fetchone()

		if row:
			return True
		return False

	except Exception as e:
		print(e)
		return True

def create_user(conn, username, password):
	try:
		cur = conn.cursor()
		cur.execute("INSERT INTO user(username, password) VALUES(%s, %s)",
		[username, password])
		conn.commit()
		cur.close()

	except Exception as e:
		print(e)

def check_pass(conn, username, password):
	try:
		cursor = conn.cursor()
		sql_info = "SELECT password FROM user WHERE username=%s"
		sql_where = (username)
		cursor.execute(sql_info, sql_where)
		_stock_psswd = cursor.fetchone()

		for key, value in _stock_psswd.items():
			if value == password:
				return True
			return False

	except Exception as e:
		print(e)
		return True
	return True

# Task Management
def create_task(conn, title, start, end, status):
	try:
		cursor = conn.cursor()
		cursor.execute("INSERT INTO task(title, status, begin, end) VALUES (%s, %s, %s, %s)",
		[title, status, start, end])
		conn.commit()
		cursor.close()
		return True

	except Exception as e:
		print(e)

def delete_task(conn, title):
	try:
		cursor = conn.cursor()

	except Exception as e:
		print(e)
	return