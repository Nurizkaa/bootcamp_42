import telebot

bot = telebot.TeleBot('8754534207:AAEC4oRIlgN6FRDSW-pOQvap-VQkWW0G6Gs')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет дорогуша')

bot.polling(none_stop=True)
