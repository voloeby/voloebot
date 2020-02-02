
TOKEN = '1086036256:AAEhfZzvm3huQhNM7asL7O1DXUtZsRBocx8'

# from telegram.ext import Updater
# import token
#
# updater = Updater(token=TOKEN, use_context=True)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple Bot to reply to Telegram messages.
This is built on the API wrapper, see echobot2.py to see the same example built
on the telegram.ext bot framework.
This program is dedicated to the public domain under the CC0 license.
"""
# import logging
# import telegram
# from telegram.error import NetworkError, Unauthorized
# from time import sleep
#
#
# update_id = None
#
#
# def main():
#     """Run the bot."""
#     global update_id
#     # Telegram Bot Authorization Token
#     bot = telegram.Bot(TOKEN)
#
#     # get the first pending update_id, this is so we can skip over it in case
#     # we get an "Unauthorized" exception.
#     try:
#         update_id = bot.get_updates()[0].update_id
#     except IndexError:
#         update_id = None
#
#     logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
#     while True:
#         try:
#             echo(bot)
#         except NetworkError:
#             sleep(1)
#         except Unauthorized:
#             # The user has removed or blocked the bot.
#             update_id += 1
#
#
# def echo(bot):
#     """Echo the message the user sent."""
#     global update_id
#     # Request updates after the last update_id
#     for update in bot.get_updates(offset=update_id, timeout=10):
#         update_id = update.update_id + 1
#
#         if update.message:  # your bot can receive updates without messages
#             # Reply to the message
#             update.message.reply_text(update.message.text)

# from telegram.ext import Updater, CommandHandler
# import logging
import telegramtoken
import telebot
from telebot import apihelper

apihelper.proxy = {'http':'https:/115.160.21.243:8000'}

TOKEN = telegramtoken.TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	print(message.chat.type)
	if message.chat.type == 'group':
		if message.text[-2:] == 'во':
			bot.send_message(message.chat.id, message.text + 'лоеб')
		if message.text.lower() == 'нет':
			bot.send_message(message.chat.id, 'пидора ответ')
		strs = message.text.split(' ')
		for str in strs:
			if str[-2:] == 'ов':
				bot.send_message(message.chat.id, 'Каких ' + str + '?')

	else:
		bot.send_message(message.chat.id, 'ты пидор(ка)')


bot.polling()
