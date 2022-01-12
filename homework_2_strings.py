# # 2_1
# str_1 = 'rythm rough rush shake than'
# mew_str = str_1.replace('a', '')
#
# deleted = len(str_1) - len(mew_str)
# print(deleted)


# # 2_2
# str_1 = 'rythm (rough rush shake) than'
#
# a, b = str_1.split('(')
# b, c = b.split(')')
#
# str_1 = str(a + c)
#
# print(str_1)
#
#
# # 2_3
# str_1 = 'rythm rough rush shake than'
#
# print(str_1.count('t'))
#
#
# # 2_4
# str_1 = 'rythm rough rush shake than'
#
# a = str_1[:str_1.find('h')]
# b = str_1[str_1.find('h'):str_1.rfind('h') + 1]
# c = str_1[str_1.rfind('h') + 1]
#
# print(a)
# print(b)
# print(c)
#
# str_1 = a + b[::-1] + c + str_1[-1]
#
# print(str_1)
#
#
# # 2_5
# str_1 = 'rythm rough rush shake than'

# a = str_1[:str_1.find('h')]
# b = str_1[str_1.find('h'):str_1.rfind('h') + 1]
# c = str_1[str_1.rfind('h') + 1]
#
# str_1 = a + b.replace('h', 'H') + c + str_1[-1]
#
# print(str_1)

while True: print(eval(input('>>>')))
