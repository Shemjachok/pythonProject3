
import telebot

TOKEN = "6001190744:AAEWW8iibHDc_FWayhc9H7EZWnKAYxTgIo0"
bot = telebot.TeleBot(TOKEN)
bot.polling(none_stop=True)


import telebot

TOKEN = "6001190744:AAEWW8iibHDc_FWayhc9H7EZWnKAYxTgIo0"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=["voice"])
def repeat(message:telebot.types.Message):
    bot.send_message(message.chat.id, "У тебя очень красивый голос!")
bot.polling(none_stop=True)



# # Обрабатываются все документы и аудиозаписи
# @bot.message_handler(content_types=['document', 'audio'])
# def handle_docs_audio(message):
#     pass
#
# @bot.message_handler(commands=['start', 'help'])
# def repeat(message: telebot.types.Message):
#     bot.reply_to(message, f"Добро пожаловать, {message.chat.username}")
#
# bot.polling(none_stop=True)