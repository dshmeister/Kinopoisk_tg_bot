from bot.bot_token import BOT_TOKEN as token
#import telebot
import telebot
from functions import *
from keyboards import *
#from variables import *

bot = telebot.TeleBot(token)

"""
Start function
"""
@bot.message_handler(commands = ['start'])
def start_message(message):
    user_id = message.chat.id
    bot.send_message(user_id, "Hello")


@bot.message_handler()



if __name__ == '__main__':
    bot.infinity_polling()


