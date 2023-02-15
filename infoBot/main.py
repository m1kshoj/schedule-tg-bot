import telebot
import pars
import re
import datetime

token = telebot.TeleBot('6055708123:AAFTrTVZ2V7-ihAYITGGY0ZFlVskbbwyQc4')

separator_days = 'Понедельник|Вторник|Среда|Четверг|Пятница|Суббота|Воскресенье'
week_number = datetime.datetime.today().isocalendar()[1]
today = datetime.datetime.today().isoweekday()
week_days = {
    '1': 'Нечетная',
    '2': 'Четная',
}


@token.message_handler(commands=['start'])
def start(message):
    ms = 'че надо'
    token.send_message(message.chat.id, ms, parse_mode='html')


@token.message_handler(commands=['help'])
def help(message):
    ms = 'Список команд:\n/help - доступные команды\n/today - расписание\n/tomorrow - расписание на завтра\nСделали бота мужчины честной судьбы (МЧС) @m1kshoj и @pussyfish'
    token.send_message(message.chat.id, ms, parse_mode='html')


def ScheduleToday(today, alt):
    test = pars.VoenmemSchelude('и415б')
    ms = test.GetSchelude()
    gg = re.split(separator_days, ms)
    days_week_dict = {}
    if week_number % 10 == 0:
        input_week = '2'
        for idx, i in enumerate(gg):
            splitting_week = i.split('\n')
            days_week_dict[idx] = []
            for j in splitting_week:
                if week_days[input_week] in j:
                    continue
                days_week_dict[idx].append(j)
        for value in days_week_dict.values():
            for item in value:
                alt += item
                alt += "\n"
    else:
        input_week = '1'
        for idx, i in enumerate(gg):
            splitting_week = i.split('\n')
            days_week_dict[idx] = []
            for j in splitting_week:
                if week_days[input_week] in j:
                    continue
                days_week_dict[idx].append(j)
        for (key, value) in days_week_dict.items():
            if key == today:
                for item in value:
                    alt += item
                    alt += '\n'
    return alt


@token.message_handler(commands=['today'])
def schedule(message):
    alt = "Расписание на сегодня:"
    token.send_message(message.chat.id, ScheduleToday(today, alt), parse_mode='html')


@token.message_handler(commands=['tomorrow'])
def schedule(message):
    alt = "Расписание на завтра:"
    token.send_message(message.chat.id, ScheduleToday(today + 1, alt), parse_mode='html')


token.polling(none_stop=True)
