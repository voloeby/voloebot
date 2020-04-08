import pymysql

class LogsRepo:
	def __init__(self, host, port, user, password, db):
		self.host = host
		self.port = port
		self.user = user
		self.password = password
		self.db = db
	def save_log(self, data):
		connection = pymysql.connect(
			host=self.host,
			port=int(self.port),
			user=self.user,
			password=self.password,
			db=self.db,
		)
		try:
			with connection.cursor() as cursor:
				sql = '''INSERT INTO {}.tg_bot_logs (`json_data`) VALUES ("%s")'''.format(self.db)
				print(sql)
				r = cursor.execute(sql, data)
				print(r)
				print(str(data))
		except Exception as e:
			print(e)
		finally:
			connection.close()
