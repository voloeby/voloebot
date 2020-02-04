import telegramtoken
import telebot

TOKEN = telegramtoken.TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	print(message.chat.type)
	if message.chat.type == 'group':
		# if message.text[-2:] == 'во':
		# 	bot.send_message(message.chat.id, message.text + 'лоеб')
		if message.text.lower() == 'нет':
			bot.send_message(message.chat.id, 'пидора ответ')
		strs = message.text.split(' ')
		for str in strs:
			if str[-2:].lower() == 'ов':
				bot.send_message(message.chat.id, 'Каких ' + str + '?')
			if message.text[-2:].lower() == 'во':
				bot.send_message(message.chat.id, str + 'лоеб')
	else:
		bot.send_message(message.chat.id, 'ты пидор')


bot.polling()
