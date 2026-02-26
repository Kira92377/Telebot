from config import TOKEN
import telebot
bot = telebot.TeleBot(TOKEN)
from telebot import types

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, '''INFO:
Я Кира, учусь прогараммировать, люблю телеграм ботов :)''')
    
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

@bot.my_chat_member_handler()
def my_chat_m(message: types.ChatMemberUpdated):
    old = message.old_chat_member
    new = message.new_chat_member
    if new.status == "member":
        bot.send_message(message.chat.id,"Somebody added me to group") # Welcome message, if bot was added to group
        bot.leave_chat(message.chat.id)



bot.polling()