from keys import TELEGRAM_TOKEN
import telebot



bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	print(message.chat.type)
	if message.chat.type == 'group':
		# if message.text[-2:] == 'во':
		# 	bot.send_message(message.chat.id, message.text + 'лоеб')
		if message.text.lower() == 'нет':
			bot.send_message(message.chat.id, 'пидора ответ')
		elif message.text.lowet() == 'нет уж':
			bot.send_message(message.chat.id, 'хует уж')
		elif message.text.lowet() == 'не':
			bot.send_message(message.chat.id, 'погряз в голубизне')
		else:
			strs = message.text.split(' ')
			for str in strs:
				if str[-2:].lower() == 'ов':
					bot.send_message(message.chat.id, 'Каких ' + str + '?')
				if message.text[-2:].lower() == 'во':
					bot.send_message(message.chat.id, str + 'лоеб')
	else:
		bot.send_message(message.chat.id, 'ты пидор')


bot.polling()
