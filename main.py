import telebot

bot = telebot.TeleBot('8146130222:AAGKo791MxfUgwsuhXisJanZUEE5YHRKk2g')

@bot.message_handler(commands=['advice'])
def send_advice(message):
    bot.send_message(message.chat.id, "Напиши, с чем тебе помочь!")

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Привет! Я бот-помощник, я помогаю людям советами. Если нужен совет, пиши /advice")

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, "Если возникла какая-то проблема, напишите на эту почту: govnaisthis@gmail.com")

bot.polling()
