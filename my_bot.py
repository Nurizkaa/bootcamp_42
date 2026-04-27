import telebot

bot = telebot.TeleBot('8754534207:AAEC4oRIlgN6FRDSW-pOQvap-VQkWW0G6Gs')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет дорогуша')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,)
@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)
