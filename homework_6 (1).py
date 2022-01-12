
# print('task 6_7')
# a = int(input())
# ls = []
# while a != 0:
#     ls.append(a)
#     a = int(input())
# print(ls.index(max(ls)))


# print('task 6_8')
# a = int(input())
# ls = []
# while a != 0:
#     if a % 2 == 0:
#         ls.append(a)
#     a = int(input())
# print(len(ls))


# print('task 6_9')
# a = int(input('введите первое число - '))
# ls = []
# b = int(input('введите второе число - '))
# while a != 0:
#     if a > b:
#         ls.append(a)
#     b = a
#     a = int(input('введите число повторно - '))
# print(len(ls))


# print('task 6_12')
#
# strng_1 = input('напишите строку: ')
# lst_str = []
# while strng_1 != '':
#     print('Великолепно, пишите еще')
#     strng_1 = input('строка: ')
#     lst_str.append(strng_1)
# else:
#     if len(lst_str) >= 1:
#         print('Эти строки запомнятся надолго')
#     elif len(lst_str) == 0:
#         print('Нет вдохновения? Ну ничего, напишите завтра')




# print('task HT_6_1')
#
# number_6_1 = int(input('Введите число: '))
# summa_6_1 = 0
# while number_6_1 != 0:
#     if number_6_1 % 5 == 0:
#         summa_6_1 += number_6_1
#     number_6_1 = int(input('Введите число повторно: '))
# print(summa_6_1)


# print('task HT_6_2')
#
# number_6_2 = int(input('Введите число: '))
# ls_minus = []
# ls_plus = []
# while number_6_2 != 0:
#     if number_6_2 > 0:
#         ls_plus.append(number_6_2)
#     elif number_6_2 < 0:
#         ls_minus.append(number_6_2)
#     number_6_2 = int(input('Введите число повторно: '))
# print(f'Количесво положительных элементов {len(ls_plus)}')
# print(f'Количесво отрицательных элементов {len(ls_minus)}')


# print('task HT_6_3')
#
# number_6_3 = int(input('Введите число больше 3: '))
# ls_6_3 = []
# while number_6_3 > 3:
#     for i in range(2, 4):
#         if number_6_3 % i == 0:
#             ls_6_3.append(number_6_3)
#         continue
#     if len(ls_6_3) == 0:
#         print('простое число')
#     else:
#         print('сложное число')
#     break

#
# print('task HT_6_4')
# zp_jo = int(input('Зарплата Джона: '))
# count_zp_jo = 0
# cost_prod = 0
# without_last_pro = 0
# while count_zp_jo <= zp_jo:
#
#     cost_prod = int(input('Введите цену товара: '))
#     count_zp_jo = count_zp_jo + cost_prod
#     without_last_pro = count_zp_jo - cost_prod
#
# else:
#     print(f'Стоп, Джон. У тебя осталось {zp_jo - without_last_pro} $')
#
# print('task HT_6_4 - with cycle while True')
# zp_jo = int(input('Зарплата Джона: '))
# count_zp_jo = 0
# cost_prod = 0
# while True:
#     cost_prod = int(input('Введите цену товара: '))
#     if count_zp_jo + cost_prod >= zp_jo:
#         break
#     count_zp_jo += cost_prod
# print(f'Стоп, Джон. У тебя осталось {zp_jo - count_zp_jo} $')


# print('task HT_6_5')
