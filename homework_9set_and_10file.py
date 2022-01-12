# s1 = set(input('введите строку 1: '))
# s2 = set(input('введите строку 2: '))
# s = s1 & s2
# print(s1, s2)
# print(s)

# import json
#
# numbers = ['1, 2, 3, 4, 5',
#            '10, 20, 30, 40, 50']
# words = ['hello','beautiful','world']
#
# to_json = {'numbers': numbers, 'words': words}
#
# with open('new.json', 'w') as f:
#     json.dump(to_json, f)
#
# with open('new.json') as f:
#     print(f.read())



# with open('file_10_7.txt', 'a', encoding='utf-8'):
#     while True:
#         with open('file_10_7.txt', 'a', encoding='utf-8') as file_strng:
#             file_strng.write(input('введите слово: ') + '\n')

flag = False
N = int(input())
for i in range(N):
    flag = (i % 10 == 0) or flag
print(flag)
