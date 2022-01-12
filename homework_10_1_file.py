
# # task 10_3
# days = {1: 'Sun', 2: 'Mon', 3: 'Tue', 4: 'Wed', 5: 'Thu', 6: 'Fri', 7: 'Sat'}
#
# with open('file_10_3.txt', 'w') as file_weekday:
#     for key, value in days.items():
#         file_weekday.write(f'{key}: {value}\n')
#
#
# # task 10_4
#
# days_7 = {}
# with open('file_10_3.txt') as file_weekday:
#     for line in file_weekday.readlines():
#         key, val = line.strip().split(':')
#         days_7[key] = val
# print(days_7)

# # task 10_5
# sets_10_5 = {i for i in input('введите числа множества: ').split() if int(i) > 0}
# with open('file_10_5.txt', 'w') as file_set:
#     for i in sets_10_5:
#         file_set.write(str(i) + '\n')
#
# # task_10_6
# sets_out = set()
# with open('file_10_5.txt') as file_set:
#     for i in file_set.readlines():
#         sets_out.add(int(i))
# print(sets_out)

# # task_10_7
#
# strng_10_7 = input('введите слова: '). split()
# with open('file_10_7.txt', 'w') as file_str:
#     for i in strng_10_7:
#         file_str.write(i + '\n')


# # task_10_8
# lst_10_8 = [5, True, 'abc']
# with open('file_10_8.txt', 'w') as file_str:
#     for i in lst_10_8:
#         file_str.write(str(i) + '\n')

# # task_10_9
# lst_10_9 = input('введите числа: ').split()
# with open('file_10_9.txt', 'w') as file_str:
#     for i in lst_10_9:
#         if int(i) % 2 != 0:
#             file_str.write(i + '\n')
