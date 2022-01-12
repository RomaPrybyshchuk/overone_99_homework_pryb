import random

# print('задача 3.1')
# list_colors = input().split()
# print(list_colors)
# list_colors.append(input())
# print(list_colors)

# print('задача 3.2')
# list_3_2 = input().split()
# space_3_2 = [' ']
# print(space_3_2 + list_3_2 + space_3_2)

# print('задача 3.4')
# list_colors_3_4 = input().split()
# # list_colors_3_4 = [input(), input(), input()]
# print(list_colors_3_4)
# list_colors_3_4[2] = 'yellow'
# print(list_colors_3_4)

print('задача 3.6')
list_colors_3_4 = ['cat', 'rabbit', 'elephant']
list_colors_3_4r = ['CAT', 'rabbiT', 'ELEphanT']
index_0 = len(list_colors_3_4[0])
index_1 = len(list_colors_3_4[1])
index_2 = len(list_colors_3_4[2])
print(list_colors_3_4[0] + ' ' + str(index_0), list_colors_3_4[1] + ' ' + str(index_1),
    list_colors_3_4[2] + ' ' + str(index_2))
print(list_colors_3_4r[0].isupper(), list_colors_3_4r[1].isupper(), list_colors_3_4r[2].isupper())

# el1 = (str_1[::-1].capitalize())[::-1]    # переворот,сделать заглавной букву, перевернуть обратно

# print('Task 3.7')
# list_3_7 = input('введите любые числа через пробел: ').split()
# print(list_3_7)
# number_3_7 = input('введите искомое число: ')
# print(number_3_7 in list_3_7)

# print('Task 3.8')
# animals = ['dog', 'cat', 'rat', 'rabbit']
# index_0 = animals[0]
# index_1 = animals[1]
# index_2 = animals[2]
# index_3 = animals[3]
# pig = 'pig'
# print([index_2, index_3, pig, index_0, index_1])

# print('Task 3.9')
# list_3_9 = [1, 2, 3, 4, 5]
# list_3_9_copy = list_3_9.copy()
# del list_3_9_copy[2:]
# print(list_3_9_copy)
# print(list_3_9 == list_3_9_copy)

# print('Task 3.10')
# list_3_9 = [1, 2, 3, 4, 5]
# print(sum(list_3_9))

# print('Task 3.14')
# nums_3_14_10 = list(range(10, 101, 10))
# nums_3_14_3 = list(range(3, 100, 3))
# print(nums_3_14_3)
# print(nums_3_14_10)

# print('Task 3.15')
# list_3_15 = [30, 28, 26, 24, 22, 20, 18, 16, 14]
# list_3_15_new = list_3_15[:-4:-1]
# print(list_3_15_new)


# print('TASK HT_3_1')
# list_HT31 = input().split()
# # list_HT31.reverse()   # var1
# # print(list_HT31)
# print(list_HT31[::-1])  # var2

# print('TASK HT_3_2')
# list_HT32 = list(range(11))
# print(list_HT32)
# print([min(list_HT32), max(list_HT32), sum(list_HT32)])

# print('TASK HT_3_3')
# list_HT33 = input()
# list_HT33 = list_HT33.replace(' ', '*')
# print(list_HT33.count('*'))


# print('TASK HT_3_4')
#


# print('TASK HT_3_5')
# # типа русская рулетка. условно список из 4 студентов. на кого рандом тот и угощает кофе
# list_students = input('введите имена студентов через пробел: ').split()
# print(list_students)
# list_students.sort()
# print('сортировка в алфавитном порядке: ', list_students)
# numbers_students = len(list_students)
# # print(numbers_students)
# list_students_range = list(range(numbers_students))
# num_random = random.randint(0, numbers_students)
# print(num_random)
# print('barista\'s: ', list_students[num_random])
