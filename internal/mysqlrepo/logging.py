import pymysql
import json

def dumper(obj):
	try:
		return obj.toJSON()
	except:
		return obj.__dict__

class LogsRepo:
	def __init__(self, host, port, user, password, db):
		self.host = host
		self.port = port
		self.user = user
		self.password = password
		self.db = db
		self.conn =  pymysql.connect(
			host=self.host,
			port=int(self.port),
			user=self.user,
			password=self.password,
			db=self.db,
			charset="utf8",
			use_unicode=True,
		)
	def save_log(self, data):
		# connection = pymysql.connect(
		# 	host=self.host,
		# 	port=int(self.port),
		# 	user=self.user,
		# 	password=self.password,
		# 	db=self.db,
		# 	charset="utf8",
		# 	use_unicode=True,
		# )
		try:
			with self.conn.cursor() as cursor:
				sql = '''INSERT INTO tg_bot_logs (`message_text`, `user_id`, `name`) VALUES (%s, %s, %s)'''
				print("sql", sql)
				print("text", data.text)
				print("user_id", data.from_user.id)
				r = cursor.execute(sql, (data.text, data.from_user.id, data.from_user.username))
				self.conn.commit()
				print(r)
				print(str(data.__dict__))
		except Exception as e:
			print(e)
		# finally:
		# 	connection.close()
