import telebot 
import time
bot = telebot.TeleBot('')


@bot.message_handler(commands=['advice'])
def send_advice(message):
    bot.send_message(message.chat.id, "Напиши, чем тебе помочь!")
    time.sleep(1)
    bot.send_message(message.chat.id, "Болит голова - /headache, болят руки - /handshurt, болят ноги - /legshurt, болит живот - /stomachhurts .")

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Привет👋 Я бот-помощник, я помогаю людям. Если нужна помощь, пиши /advice. 😢Если бот сломался напиши /help😢")

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, "Если возникла какая-то проблема, напишите на эту почту: govnaisthis@gmail.com")
    time.sleep(1)
    bot.send_message(message.chat.id, "Если все помогло и ты хочешь задать ище вопрос то пиши /advice. ")

@bot.message_handler(commands=['headache'])
def headache_command(message):
    bot.send_message(message.chat.id, "Где болит голова, спава - /headacheright, слева - /headacheleft, затылок - /headachebackofthehead")
    time.sleep(1)
    bot.send_message(message.chat.id, "🦴Толька если голова болит от удара об что-то, обратиться к врачу-травматологу🦴")
    time.sleep(1)
    bot.send_message(message.chat.id, "Если все помогло и ты хочешь задать ище вопрос то пиши /advice. ")
    
@bot.message_handler(commands=['handshurt'])
def handshurt_command(message):
    bot.send_message(message.chat.id, "🦴Обратиться к врачу-травматологу🦴")
    time.sleep(1)
    bot.send_message(message.chat.id, "Если все помогло и ты хочешь задать ище вопрос то пиши /advice. ")

@bot.message_handler(commands=['legshurt'])
def legshurt_command(message):
    bot.send_message(message.chat.id, "🦴Обратиться к врачу-травматологу🦴")
    time.sleep(1)
    bot.send_message(message.chat.id, "Если все помогло и ты хочешь задать ище вопрос то пиши /advice. ")

@bot.message_handler(commands=['stomachhurts'])
def stomachhurts_command(message):
    bot.send_message(message.chat.id, "Если живот болит от-того что вы съели что-то нехорошое то выпейте активированного угля.")
    bot.send_message(message.chat.id, "Если живот болит от 🔥ижоги🔥 то выпейте 🥛молоко🥛, раствор соды или съедите картошку. ")
    bot.send_message(message.chat.id, "И если вам ⬆️ не помогло то обратитесь к диетологу. ")
    time.sleep(1)
    bot.send_message(message.chat.id, "🦴Толька если живот болит от удара об что-то, обратиться к врачу-травматологу🦴")
    time.sleep(1)
    bot.send_message(message.chat.id, "Если все помогло и ты хочешь задать ище вопрос то пиши /advice. ")

@bot.message_handler(commands=['headacheright'])
def headacheright_command(message):
    bot.send_message(message.chat.id, "Выпейте что-то из преставленнго списка препаратов: Парацетамол, Цитрамон, Спазмалгон, Некст, Темпалгин, или Нурофен")
    time.sleep(1)
    bot.send_message(message.chat.id, "Если все помогло и ты хочешь задать ище вопрос то пиши /advice. ")

@bot.message_handler(commands=['headacheleft'])
def headacheleft_command(message):
    bot.send_message(message.chat.id, "Выпейте что-то из преставленнго списка препаратов: Парацетамол, Цитрамон, Спазмалгон, Некст, Темпалгин, или Нурофен")
    time.sleep(1)
    bot.send_message(message.chat.id, "Если все помогло и ты хочешь задать ище вопрос то пиши /advice. ") 

@bot.message_handler(commands=['headachebackofthehead'])
def headachebackofthehead_command(message):
    bot.send_message(message.chat.id, "Избавиться от боли можно спомощью холодного компресса – нужно приложить к проблемной зоне смоченную в холодной воде марлевую салфетку или грелку со льдом")
    time.sleep(1)
    bot.send_message(message.chat.id, "Если все помогло и ты хочешь задать ище вопрос то пиши /advice. ")        

bot.polling(none_stop=True)
