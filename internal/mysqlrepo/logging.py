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
				sql = '''INSERT INTO {}.tg_bot_logs (`json_data`) VALUES ('{}')'''.format(self.db, json.dumps(data, default=dumper))
				print(sql)

				r = cursor.execute(sql)
				connection.commit()
				print(r)
				print(str(data.__dict__))
		except Exception as e:
			print(e)
		finally:
			connection.close()
