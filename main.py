import telebot
import os
from dotenv import load_dotenv

load_dotenv()
print("ENV Loaded!")

print("BOT TOKEN: " + os.environ("BOT_TOKEN"))

bot = telebot.TeleBot(os.environ("BOT_TOKEN"), parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

print("Test bot is running!")

bot.infinity_polling()