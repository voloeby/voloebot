from config import TELEGRAM_TOKEN
import telebot



bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	print(message.chat.type)
	if message.chat.type == 'group':
		if message.text.lower() == 'нет':
			bot.send_message(message.chat.id, 'Пидора ответ')
		elif message.text.lower() == 'нет уж':
			bot.send_message(message.chat.id, 'Хует уж')
		elif message.text.lower() == 'не':
			bot.send_message(message.chat.id, 'Погряз в голубизне')
		elif message.text.lower() == 'не знаю':
			bot.send_message(message.chat.id, 'С таких как ты охуеваю')
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
