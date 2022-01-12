# print('Решение задачи №2_1')
# string_1 = 'rythm rough rush shake than'
# string_2 = string_1.replace('a', '')
# print(len(string_1) - len(string_2))
# print('Решение задачи №2_2')
# # string_11 = 'rythm (rough rush shake) than'
# # split_string1 = string_11.split("(")
# # split_string2 = string_11.split(")")
# # print(split_string1[0] + split_string2[-1])
# str_1 = 'rythm (rough rush shake) than'
# first = str_1.find('(')
# last = str_1.find(')')
# print(str_1[:first] + str_1[last + 1:])
# print('Решение задачи №2_3')
# string_12 = 'rythm rough rush shake than'
# print(string_12.count('t'))
# print('Решение задачи №2_4')
string_2_4 = 'rythm rough rush shake than'
first_2_4 = string_2_4.find('h')
last_2_4 = string_2_4.rfind('h')
common_2_4 = string_2_4[first_2_4 + 1: last_2_4]
print(string_2_4[:first_2_4 + 1] + common_2_4[::-1] + string_2_4[last_2_4:])
# print('Решение задачи №2_5')
# string_2_5 = 'rythm rough rush shake than'
# start_2_5 = string_2_5.find('h')
# end_2_5 = string_2_5.rfind('h')
# string_2_5_short = string_2_5[start_2_5 + 1:end_2_5]
# print(string_2_5[:start_2_5 + 1] + string_2_5_short.replace('h', 'H') + string_2_5[end_2_5:])
#
# print('Решение задачи №2_2')
# print('  *  ')
# print(' * * ')
# print('*   *')
# print('*****')
# print('Решение задачи №2_7')
# string_2_7 = 'program'
# print(string_2_7.find('r'))
# print(string_2_7.rfind('r'))
# print('Решение задачи №2_8')
# string_love = 'love'
# string_python = 'python'
# print(string_love.find('o') + string_python.find('o'))
# print('Решение задачи №2_9')
# string_2_9 = '123'
# number = '1'
# print(number in string_2_9)
# print('Решение задачи №2_10')
# string_2_10m = 'Today is monday'
# string_2_10f = 'Tomorrow is friday'
# print(string_2_10m.replace('monday', 'friday'))
# print(string_2_10f.replace( 'friday', 'monday'))
# print('Решение задачи №2_11')
# string_2_11 = 'Anna loves music! She plays the piano very well! Look!'
# # string_2_11 = string_2_11.replace('!', '!*')
# # print(string_2_11.split('*'))
# sep = '!'
# string_2_11spl = [x + sep for x in string_2_11.split(sep)]
# print(string_2_11spl)
# print('Решение задачи №2_13')
# string_2_13 = input('Введите слово: ')
# string_2_13rev = string_2_13[::-1]
# if string_2_13 == string_2_13rev:
#     print('палиндром')
# else:
#     print('не палиндром')
# print('Решение задачи №2_14')
# string_2_14 = 'romario_08PR@mail.ru'
# print(string_2_14.replace('@', ''))
# print('Решение задачи №2_15')
# string_2_15 = 'i am engineer'
# print(string_2_15.count('e'))