#!python3
# -*- coding: utf-8 -*-
import config
import telebot
from mysqlrepo.logging import LogsRepo

db = config.DATABASE
bot = telebot.TeleBot(config.TELEGRAM_TOKEN)

logging = LogsRepo(host=db["host"], port=db["port"], user=db["user"], password=db["password"], db=db["db"])


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	# try:
	logging.save_log((message))
	# except Exception as e:
		# print(e)
	print(message.chat.type)
	if message.chat.type == 'group':
		if message.text.lower() == 'нет':
			bot.send_message(message.chat.id, 'Пидора ответ!')
		elif message.text.lower() == 'нет уж':
			bot.send_message(message.chat.id, 'Хует уж!')
		elif message.text.lower() == 'не':
			bot.send_message(message.chat.id, 'Погряз в голубизне!')
		elif message.text.lower() == 'не знаю':
			bot.send_message(message.chat.id, 'С таких как ты охуеваю!')
		elif message.text.lower() == '-':
			bot.send_message(message.chat.id, 'Хуинус!')
		else:
			strs = message.text.split(' ')
			for str in strs:
				if str[-2:].lower() == 'ов':
					bot.send_message(message.chat.id, 'Каких ' + str + '?')
				if str[-2:].lower() == 'во':
					bot.send_message(message.chat.id, str + 'лоеб')
	else:
		bot.send_message(message.chat.id, 'ты пидор')


bot.polling()
