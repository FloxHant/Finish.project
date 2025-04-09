import telebot
import openai

bot = telebot.TeleBot('8146130222:AAGKo791MxfUgwsuhXisJanZUEE5YHRKk2g')
openai.api_key = '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'

@bot.message_handler(commands=['advice'])
def send_advice(message):
    bot.send_message(message.chat.id, "Напиши, с чем тебе помочь!")
    bot.send_message(message.chat.id, "Пожалуйста, формулируй свой вопрос так, чтобы я мог его понять.")

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Привет! Я бот-помощник, я помогаю людям советами. Если нужен совет, пиши /advice")

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, "Если возникла какая-то проблема, напишите на эту почту: govnaisthis@gmail.com")

@bot.message_handler(func=lambda message: True)  # Обработчик всех текстовых сообщений
def handle_message(message):
    user_input = message.text
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        ai_response = response.choices[0].message['content']
        bot.send_message(message.chat.id, ai_response)
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {str(e)}")

# Запускаем бота
bot.polling(none_stop=True)
