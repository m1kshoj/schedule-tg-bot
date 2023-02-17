import re
import datetime

today = datetime.datetime.today().isoweekday()
separator_days = 'Понедельник|Вторник|Среда|Четверг|Пятница|Суббота|Воскресенье'

alt = 'Расписание занятий группы И415Б на ВЕСЕННИЙ СЕМЕСТР 2022/2023 уч. ' \
      'г.\nРасписание текущей недели выделено цветом\nПонедельник' \
      '\nВремя Дисциплина Преподаватель Аудитория\n10:50 Нечетная лек ФИЗ.ОСН.МИКРОЭЛ Ярыгин Д.М.; 445;' \
      '\n10:50 Четная лек ФИЗ.ОСН.МИКРОЭЛ Ярыгин Д.М.; 492;\n12:40 Нечетная лек ВЫСШ. МАТЕМАТ Тарасов А.А.; 444;' \
      '\n12:40 Четная лек ВЫСШ. МАТЕМАТ Тарасов А.А.; 444;\n14:55 Нечетная пр ВЫСШ. МАТЕМАТ Васильева В.А.; 498;' \
      '\n14:55 Четная пр ВЫСШ. МАТЕМАТ Васильева В.А.; 498;\n16:45 Нечетная пр КОМП. ПРАКТИКУМ Колачев И.О.; 430;' \
      '\n16:45 Четная пр КОМП. ПРАКТИКУМ Колачев И.О.; 430;\nВторник\nВремя Дисциплина Преподаватель Аудитория' \
      '\n10:50 Нечетная лек ПРАВОВЕДЕНИЕ Диденко Л.Г.; 455;\n10:50 Четная пр ПРАВОВЕДЕНИЕ Диденко Л.Г.; 490;' \
      '\n12:40 Нечетная пр ЭК ПО ФК И СПОРТУ\n12:40 Четная пр ЭК ПО ФК И СПОРТУ\nСреда\nВремя Дисциплина Преподаватель Аудитория' \
      '\n9:00 Нечетная лек СИСТЕМНОЕ ПО Устиновский Г.С.; 314;\n9:00 Четная лек СИСТЕМНОЕ ПО Устиновский Г.С.; 315;' \
      '\n10:50 Нечетная лек ОСН.СИСТ.АН. Королев С.Н.; 314;\n10:50 Четная пр ОСН.СИСТ.АН. Королев С.Н.; 346;' \
      '\n12:40 Нечетная пр КОМП. ПРАКТИКУМ Колачев И.О.; 430;\n14:55 Нечетная лаб ФИЗ.ОСН.МИКРОЭЛ Смирнов А.В.; 423а;' \
      '\nЧетверг\nВремя Дисциплина Преподаватель Аудитория\n10:50 Нечетная лаб ТОЭ Образцов А.Н.; 356*;' \
      '\n12:40 Нечетная пр ТОЭ Образцов А.Н.; 360*;\n12:40 Четная пр ТОЭ Образцов А.Н.; 420*;\n14:55 Нечетная пр ЭК ПО ФК И СПОРТУ' \
      '\n14:55 Четная пр ЭК ПО ФК И СПОРТУ\nПятница\nВремя Дисциплина Преподаватель Аудитория' \
      '\n10:50 Нечетная лек ТОЭ Образцов А.Н.; 325*;\n10:50 Четная лек ТОЭ Образцов А.Н.; 325*;' \
      '\n12:40 Нечетная лек ФИЗИКА Князева Т.Н.; 325*;\n12:40 Четная лек ФИЗИКА Князева Т.Н.; 325*;' \
      '\n14:55 Нечетная пр ИН. ЯЗ. Халезова А.И.; 311*;\n14:55 Четная пр ИН. ЯЗ. Халезова А.И.; 311*;' \
      '\n16:45 Четная пр СИСТЕМНОЕ ПО Х2 И5 ?.?.; 218*;\n'

new_split = re.split(separator_days, alt)
input_week = input("Неделя 1 - чет, 2 - нечет")

week_days = {
    '1': 'Нечетная',
    '2': 'Четная',
}

days_week_dict = {}

for idx, i in enumerate(new_split):
    splitting_week = i.split('\n')
    days_week_dict[idx] = []
    for j in splitting_week:
        if week_days[input_week] in j:
            continue
        days_week_dict[idx].append(j)

for value in days_week_dict.values():
    for item in value:
        print(item)

print('-----------------------------------------------')
alt = ""
for (key, value) in days_week_dict.items():
    if key == today:
        for item in value:
            alt+=item
            alt+='\n'

print(alt)
