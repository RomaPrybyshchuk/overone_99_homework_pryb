import random

# # 5_7. Вход: строка. Программа выводит каждый символ строки 2 раза
# strr_5_7 = input()
# for i in strr_5_7:
#     print(i * 2)

# # 5_8. Вход: строка. Программа выводит какждый символ с его индексом, т.е.(индекс, символ)
# strr_5_8 = input()
# for i in enumerate(strr_5_8):
#     print(i)

# # 5_9. Вход: 2 числа a и b Программа выводит те числа на интервале от a до b, которые являются четными и дают
# # остаток 1 при делении на 7. Числа могут быть любыми и подаваться в любом порядке.
#
# a = int(input())
# b = int(input())
# for i in range(min(a, b), max(a, b) + 1):
#     if i % 2 == 0 and i % 7 == 1:
#         print(i)

# # вариант с генерацией списков
# full_nums = [i for i in range(min(a, b), max(a, b) + 1) if i % 2 == 0 and i % 7 == 1]
# print(full_nums)


# # 5_11. Вход: целое число N.
# # Программа помогает Пете учить цвета радуги. Она печатает первые N цветов радуги с большой буквы.
# # Не забудьте, что в радуге только 7 цветов!
# number_5_11 = int(input())
# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
# for i in colors[:number_5_11]:
#     i = i.capitalize()
#     print(i)

# number_5_11 = int(input())
# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
# colors_list = [i.capitalize() for i in colors[:number_5_11]]
# print(colors_list)



# # 5_14. Вход: список целых чисел. Программа создает из него список только с теми числами, что больше 5ти.
# nums = [int(i) for i in input().split() if int(i) > 5]
# print(nums)


# # 5_15. Вход: число N и кол-во строк, равное N. Программа делает список из полученных строк.
# number_5_15 = int(input())
# list_5_15 = input().split()
# list_5 = []
# for i in list_5_15[:number_5_15]:
#     list_5.append(i)
# print(list_5)


# # HT5.1. Программа перемножает все нечетные значения от 1 до 10 включительно
#
# a = 1
# b = 10
# proizv = 1
# for i in range(a, b + 1):
#     if i % 2 != 0:
#         proizv *= i
# print(proizv)


# # HT 5.2. Вход: целое число до 15. Программа выводит лесенку из чисел

# print('task #5_2')
# numberr_stairway = int(input('Введите любое число до 15: '))
# for i in range(1, numberr_stairway + 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()

# print('task HT_5_3')
# list_number = input('Введите числа через ПРОБЕЛ, затем нажмите ВВОД: ').split()
# symbl_multiply = '*'
# for i in list_number:
#     i = int(i) * symbl_multiply
#     print(str(i))

# print('task HT_5_4')
#
# print('генератор списков для задачи 5.4')
# a = int(input('введите любое число: '))
# b = int(input('введите еще одно любое число: '))
# nums_5_4 = [i for i in range(min(a, b), max(a, b) + 1)]
# print(nums_5_4)
#
# print('генератор списков для задачи 5.5')
# a = int(input('введите любое число: '))
# b = int(input('введите еще одно любое число: '))
# nums_5_5 = [i for i in range(min(a, b), max(a, b) + 1) if int(i) % 2 == 0]
# print(nums_5_5)
#
# print('генератор списков для задачи 5.7')
#
# nums_5_7 = [i * 2 for i in input('введите любое слово: ')]
# print(nums_5_7)



# print('task HT_5_4')
#
# cars_list = ('AUDI', 'MERCEDES', 'BMW')
# guess_cars = input('Введите название авто из самой известной немецкой тройки:  ').upper()
# models_count = []
# for i in cars_list:
#     if guess_cars in cars_list:
#         print(f'''Как насчет модельного ряда {guess_cars}. Введи модели в соответствии с маркой авто:
#                     1. Цифры для BMW(пример: 3, т.е. модель 3ей серии)
#                     2. Буквы для Mercedes(пример: С, т.е. модель С класса)
#                     3. Буква с цифрой для Audi(пример: A4, т.е. модель А4 серии)''')
#         models_count = input(f'Вводи модели {guess_cars}: ').split()
#         for j in models_count:
#             while models_count.count(j) > 1:
#                 models_count.remove(j)
#         # print(set(models_count))  # второй способ для удаления повторяющихся элементов
#         print(models_count)
#         new_models_sum = len(models_count)
#         print(new_models_sum)
#         if int(new_models_sum) < 6:
#             print('Не мешало бы почитать про модели :(')
#         elif int(new_models_sum) >= 6:
#             print('Что-то да ты знаешь :)')
#     else:
#         print('Что-то ввели неправильно. Попробуй еще раз.')
#     break
