import telebot

bot = telebot.telebot('8146130222:AAGKo791MxfUgwsuhXisJanZUEE5YHRKk2g')
@bot.message_handler(commands=['/advice'])
def send_meme(message):
    bot.send_message(message.chat.id, "Напиши с чем тибе помочь!")
@bot.message_handler(commands=['/start'])
def start_command(message):
    bot.send_message(message.chat.id, "Привет я бот-помощник, я помогаю людям советам, если нужен совет пиши dvice")
@bot.message_handler(commands=['/help'])
def start_command(message):
    bot.send_message(message.chat.id, "Если произошла какаета проблема, нам на эту почту: govnaisthis@gmail.com")


bot.polling()
