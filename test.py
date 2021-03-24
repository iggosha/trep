import telebot
bot = telebot.TeleBot('1657190690:AAHWdNgw3TNfrlyWbQwVFXdIteIDiEon_II')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот Саша местный. Приятно познакомиться, {message.from_user.first_name}')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if (message.text.lower()
== 'привет') or (message.text.lower() == 'hello') or (message.text.lower()
== 'hi' or message.text.lower() == 'салам алейкум'):
        bot.send_message(message.from_user.id, 'олегам аслам')
    elif message.text.lower() == 'расскажи анекдот':
        bot.send_message(message.from_user.id, 'Идут два рэпера, один в кепке, а другой тоже.')
    else:
        bot.send_message(message.from_user.id, 'Я такое не знаю не пиши сюда')


bot.polling(none_stop=True)
