import pymysql

class LogsRepo:
	def __init__(self, host, port, user, password, db):
		self.host = host
		self.port = port
		self.user = user
		self.password = password
		self.db = db
	def save_log(self, str):
		connection = pymysql.connect(
			host=self.host,
			port=int(self.port),
			user=self.user,
			password=self.password,
			db=self.db,
		)
		try:
			with connection.cursor() as cursor:
				sql = '''INSERT INTO {}.tg_bot_logs `data` VALUES %s'''.format(str(str))
				cursor.execute(sql, str)
		finally:
			connection.close()
