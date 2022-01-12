import random
# # task 7_2
# user = tuple(input().split())
#
# print(user[0], user[-1], sep=', ')

# # task 7_3
# number_7_3 = input().split()
# tpl_7_3 = []
#
# for i in number_7_3:
#     if int(i) % 3 == 0:
#         tpl_7_3.append(i)
#
# print(tuple(tpl_7_3))

# # task_7_4
#
# tpl_7_4 = tuple(range(10))
# print(sum(tpl_7_4))

# # task_7_5
# tpl_7_5 = tuple(input().split())
# tpl_new = ()
# vowels = 'eyuioa'
#
# for i in tpl_7_5:
#     if i in vowels:
#         if i not in list(tpl_new):      # можно ли применить здесь условие сравнения рядом стоящих символов
#             tpl_new += tuple(i)         # по типу задачи №6 с экзамена
#             print(f'Буква {i} в кортеже {tpl_7_5} встречается {tpl_7_5.count(i)} раз(а)')

# # task_7_6
# tpl_temp = tuple(input().split())
# sum = 0
# for i in tpl_temp:
#     sum += int(i)
# midl_temp = sum/len(tpl_temp)
# print(midl_temp)

# # task_HT_7_1
# count_0 = 0
# tpl_1 = tuple(random.randint(-5, 0) for i in range(10))
# tpl_2 = tuple(random.randint(-5, 0) for j in range(10))
# tpl_common = tpl_1 + tpl_2
# print(tpl_common)
# print('количество нулей: ', tpl_common.count(0))
# # for i in tpl_common:
# #     if i == 0:
# #         count_0 += 1
# #
# # print('количество нулей: ', count_0)


# # task_HT_7_2
# tpl_1 = tuple(random.randint(1, 10) for i in range(5))
# print(*tpl_1)
# print(*tpl_1[1:len(tpl_1) - 1])


# # task_HT_7_3
#
# lst_7_3 = [int(i) for i in input().split() if int(i) < 5]
# print(tuple(lst_7_3))

# task_HT_7_4
# tpl_7_4 = (1, [1, 2, 4], 'python', True)
# # tpl_7_4 = input().split()
# for i in tpl_7_4:
#     if type(i) == list:
#         j = tpl_7_4.index(i)
#         tpl_7_4[int(j)].clear()
# # print(type(tpl_7_4))
# # tpl_7_4[3].clear()
# print(tpl_7_4)
