# print('task 4_5')
# len_1 = int(input('длина отрезка 1:'))
# len_2 = int(input('длина отрезка 2:'))
# len_3 = int(input('длина отрезка 3:'))
# if len_1 + len_2 > len_3 and len_1 + len_3 > len_2 and len_2 + len_3 > len_1:
#     print('правильный треугольник')
# else:
#     print('проверьте правильность введенных данных')


# print('task 4_6')
# coord_x = float(input('введите х'))
# coord_y = float(input('введите y'))
# if coord_x > 0 and coord_y > 0:
#     print('I четверть')
# elif coord_x < 0 and coord_y > 0:
#     print('II четверть')
# elif coord_x < 0 and coord_y < 0:
#     print('III четверть')
# elif coord_x > 0 and coord_y < 0:
#     print('IV четверть')


# print('task 4_7')
# month = int(input('введите номер месяца: '))
# if 1 <= month < 3 or month == 12:
#     print ('winter')
# elif 3 <= month < 6:
#     print ('spring')
# elif 6 <= month < 9:
#     print ('summer')
# elif 9 <= month < 12:
#     print ('autumn')


# print('task 4_8')
# str_1 = input()
# str_2 = input()
# str_3 = input()
# is_1 = (str_1 == 'python')
# is_2 = (str_2 == 'python')
# is_3 = (str_3 == 'python')
# if is_1 == True:
#     print('1')
# elif is_2 == True:
#     print('2')
# elif is_3 == True:
#     print('3')


# string_48 = input('введите три слова через пробел: ')
# string_48 = string_48.split()
# print(string_48)
# if 'python' in string_48:
#     print(string_48.index('python'))
# else:
#     print('слова \'python\' нет')


# print('task 4_10')
# str = input()
# is_master = (str == 'Master')
# print(is_master)

# int_4_11 = int(input())
# is_kratno = (int_4_11 % 3 == 0)
# print(is_kratno)


# print('task HT4.1')
# var_4_1 = int(input('введите любое целое число со знаком \'+\' или \'-\': '))
# if var_4_1 > 0:
#     print('вы ввели положительно число')
# elif var_4_1 < 0:
#     print('вы ввели отрицательное число')
# elif var_4_1 == 0:
#     print('вы ввели 0')


# print('task HT4.2')
# num_temp = float(input('введите значение температуры: '))
# kind_temp = input('введите единицу измерения температуры \'F\' или \'C\': ').upper()
# if kind_temp == 'C':
#     temp_po_faren = 9 / 5 * num_temp + 32
#     print('температура по Фаренгейту: {0:1.2f}'.format(temp_po_faren))
# elif kind_temp == 'F':
#     temp_po_cels = 5 / 9 * (num_temp - 32)
#     print('температура по Фаренгейту: {0:1.2f}'.format(temp_po_cels))


# print('task HT4.3 calculator')
# number_1 = int(input('введите число: '))
# number_2 = int(input('введите число: '))
# sign = input('введите один из знаков действия: \'+\'; \'-\'; \'*\'; \'/\':  ')
# if sign == '+':
#     print(number_1 + number_2)
# elif sign == '-':
#     print(number_1 - number_2)
# elif sign == '*':
#     print(number_1 * number_2)
# elif sign == '/':
#     print(number_1 / number_2)


# print('task HT4.4')
# str_1 = input()
# str_2 = input()
# sort_str_1 = sorted(str_1)
# sort_str_2 = sorted(str_2)
# if len(str_1) == len(str_2):
#     if sort_str_1 == sort_str_2:
#         print(str_1, ' и ',str_2,' являются анаграммой')
#     else:
#         print(str_1, ' и ',str_2,' не являются анаграммой')
# else:
#     print(str_1, ' и ',str_2,' не являются анаграммой')


print('task HT4.5')

print('Расчет частоты вращения шпинделя')
cut_speed = 1  # как правильно определить переменную
cut_diam = 1
speed_rotation: float = 318.5 * cut_speed / cut_diam

gruppa_material = input('''Выберите группу металлов:
\tP - сталь \n\tN - легкие сплавы\n\tH - закаленная сталь
\tM - нержавеющая сталь\n\t''').upper()
if gruppa_material.isalpha() == True and 65 <= ord(gruppa_material) <= 90:
    if gruppa_material == 'P':
        print('Рекоменд. скорость рез.: 90...130')
        cut_speed = int(input('Введите скорость рез.: '))
        cut_diam = float(input('Введите диам. обр.: '))
        # speed_rotation = 318.5 * cut_speed / cut_diam
        print('Частота вращения шпинд.: {0:1.1f}'.format(speed_rotation))
    elif gruppa_material == 'N':
        print('Рекоменд. скорость рез.: 160...210')
        cut_speed = int(input('Введите скорость рез.: '))
        cut_diam = float(input('Введите диам. обр.: '))
        # speed_rotation = 318.5 * cut_speed / cut_diam
        print('Частота вращения шпинд.: {0:1.1f}'.format(speed_rotation))
    elif gruppa_material == 'H':
        print('Рекоменд. скорость рез.: 50...60')
        cut_speed = int(input('Введите скорость рез.: '))
        cut_diam = float(input('Введите диам. обр.: '))
        # speed_rotation = 318.5 * cut_speed / cut_diam
        print('Частота вращения шпинд.: {0:1.1f}'.format(speed_rotation))
    elif gruppa_material == 'M':
        print('Рекоменд. скорость рез.: 65...85')
        cut_speed = int(input('Введите скорость рез.: '))
        cut_diam = float(input('Введите диам. обр.: '))
        # speed_rotation = 318.5 * cut_speed / cut_diam
        print(f'Частота вращения шпинд.: {speed_rotation:1.1f}')
else:
    print('Проверьте правильность введенных данных. Возможные причины:'
          '\t 1. Введена цифра, а не буква.'
          '\t 2. Введен лишний пробел.'
          '\t 3. Введены русские буквы.')
