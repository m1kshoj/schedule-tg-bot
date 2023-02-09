import telebot
import pars

token = telebot.TeleBot('6055708123:AAFTrTVZ2V7-ihAYITGGY0ZFlVskbbwyQc4')


@token.message_handler(commands=['start'])
def start(message):
    ms = 'чепуха'
    token.send_message(message.chat.id, ms, parse_mode='html')


@token.message_handler(commands=['help'])
def help(message):
    ms = 'Список команд:\n/help - доступные команды\n/schedule - расписание\nСделали бота мужчины честной судьбы (МЧС) @m1kshoj и @pussyfish'
    token.send_message(message.chat.id, ms, parse_mode='html')


@token.message_handler(commands=['schedule'])
def schedule(message):
    test = pars.VoenmemSchelude('и415б')
    ms = test.GetSchelude()
    token.send_message(message.chat.id, ms, parse_mode='html')


token.polling(none_stop=True)
