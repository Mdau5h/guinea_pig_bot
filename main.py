import telebot
from telebot import types

token = ''
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('Посчитай! 📈')
    markup.add(button)
    send_msg = f'<b>Привет, {message.from_user.first_name} {message.from_user.last_name}!</b> \nЯ тестовый ' \
               f'подопытный кролик. Изначально я должен выглядеть как программа-напоминалка, а там кто знает, ' \
               f'может я чему-то еще научусь. Рад тебя видеть! :)\n' \
               f'Сейчас я могу считать сложные проценты. Давай попробуем! \n' \
               f'Чтобы начать, нажми кнопку: "Посчитай"\n'
    bot.send_message(message.chat.id, send_msg, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def button_message(message):
    if message.text == 'Посчитай! 📈':
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, 'Введи свой депозит, размер ежемесячного взноса, \nгодовую процентную ставку, '
                                          'и срок вклада (в месяцах). Одной строкой, разделяя значения пробелами.', parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(message, input_data)


def input_data(message):
    try:
        data = list(map(float, (message.text.split())))
        bot.send_message(message.chat.id, f'Итоговая сумма за все периоды: {calc(data[0], data[1], data[2], data[3])}', parse_mode='html')
        bot.send_message(message.chat.id, '/start', parse_mode='html')
    except Exception as ex:
        bot.send_message(message.chat.id, f'Произошла ошибка. Попробуй снова. \nМне не понравилось следующее: {ex}', parse_mode='html')
        bot.register_next_step_handler(message, input_data)


def calc(deposite, fee, bid, time):
    for i in range(int(time)):
        deposite += deposite*(bid/1200)+fee
    return f"{deposite-fee:,.0f} ₽".replace(',', ' ')

bot.polling(none_stop=True)


