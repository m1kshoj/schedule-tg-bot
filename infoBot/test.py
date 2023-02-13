import datetime
from calendar import weekday

today = datetime.datetime.today().isoweekday()
print(today)







# import datetime
# from calendar import weekday
#
# listKeys = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
#
# curDay = (['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'])
# gg = alt.split()
# dic = {k: [] for k in curDay}
# smtext = ""
# print(dic)
# print('\n')
#
# for i in range(len(gg)):
#     smtext = ""
#     if gg[i] in curDay:
#         k = gg[i]
#         i += 1
#         for j in range(i):
#             if gg[i] == "Время" or gg[i] == "Дисциплина" or gg[i] == "Преподаватель" or gg[i] == "Аудитория":
#                 i += 1
#             smtext += gg[i]
#             smtext += " "
#             i += 1
#             if gg[j] in curDay:
#                 dic[k].append(smtext)
#                 break
#
# for i in dic:
#     print(i + ' ' + str(dic[i]))
#
# print('\n')
# print(dic)
#
# # cur = 0
# # dic = {k: [] for k in curDay}
# # print(dic)
# # for i in range(len(gg)):
# #     if gg[i] in curDay:
# #         k = gg[i]
# #         dic[k].append(k)
# #         i += 1
# #         for j in range(i):
# #             dic[k].append(gg[i])
# #
# #             i += 1
# #             if gg[j] in curDay:
# #                 break
# #         cur += 1
# #
# # for i in dic:
# #     print(i + ' ' + str(dic[i]))
# # print(dic)
