# ----------TASK 13_1---VARIANT 1-----
#
#
# def summa_every_number(nmb):
#     summa = 0
#     while nmb != 0:
#         nmb, smm = divmod(nmb, 10)
#         summa += smm
#     return summa
#
#
# print(sorted([summa_every_number(int(i)) for i in input('Enter numbers: ').split()]))


# ----------TASK 13_1---VARIANT 2(with function map)-----
#
#
# def summa_every_number(nmb):
#     lst_st = map(int, list(nmb))
#     return sum(lst_st)
#
#
# print(sorted([summa_every_number(int(i)) for i in input('Enter numbers: ').split()]))


# ----------TASK 13_2----------

#
# def get_fx(nmb):
#
#     def less_minus2(number):
#         return 1 - (number + 2) ** 2
#
#     def between(number):
#         return - number / 2
#
#     def more_2(number):
#         return (number - 2) ** 2 + 1
#
#     if nmb <= -2:
#         return less_minus2(nmb)
#     elif -2 < nmb <= 2:
#         return between(nmb)
#     elif nmb > 2:
#         return more_2(nmb)
#
#
# print(get_fx(int(input('Enter number: '))))


# ----------TASK 13_3----------
#
#
# def division_on_two(i):
#     return i / 2
#
#
# print([division_on_two(int(i)) for i in input('enter numbers: ').split() if int(i) % 2 == 0])


# ----------TASK 13_4----------

# import random
#
#
# def random_list(min_number, max_number):
#     count = 0
#     ls = []
#     while count != max_number // 2:
#         ls.append(random.randint(min_number, max_number))
#         count += 1
#     return ls
#
#
# lst_13_4 = [int(i) for i in input('Enter numbers: ').split()]
# print(random_list(min(lst_13_4), max(lst_13_4)))


# ----------TASK 13_5----------

# biscuits = {'наполеон': [['масло', 'мука', 'сахар'], 7, 1000],
#             'медовик': [['мука', 'мед', 'сметана'], 4, 1500],
#             'киевский': [['орехи', 'мука', 'сгущенка'], 6, 800],
#             }
#
#
# def choice(pie, item):
#     for k, v in biscuits.items():
#         if pie == k:
#             if item == 'описание':
#                 return print(f'Торт {pie} состоит из', *v[0])
#             elif item == 'цена':
#                 return print(f'Торт {pie} стоит {v[1]} р.')
#             elif item == 'количество':
#                 return print(f'Торт {pie} осталось {v[2]} грамм')
#
#
# def sell_biscuit(func):
#     def wrapper_sell():
#         buy_or_not = input('Желаете купить (да/нет): ')
#         if buy_or_not == 'да':
#             vl = input('Сколько торта вам положить: ')
#             if int(vl) < biscuits[biscuit][2]:
#                 return func(vl)
#             elif int(vl) > biscuits[biscuit][2]:
#                 print(f'К сожалению, торта {biscuit} осталось {biscuits[biscuit][2]} грамм')
#                 buy_2 = input(f'Вам положить оставшийся торт {biscuit} (да/нет): ')
#                 if buy_2.lower() == 'да':
#                     all_or_part = input('Весь или часть: ')
#                     if all_or_part.lower() == 'весь':
#                         return func(biscuits[biscuit][2])
#                     elif all_or_part.lower() == 'часть':
#                         vl = input('Сколько Вы хотите: ')
#                         return func(vl)
#                 else:
#                     return print('Ок). Могу предложить что-то другое?')
#         else:
#             return print('Ок)')
#     return wrapper_sell
#
#
# biscuit = input('Какой торт вы хотите приобрести: ').lower()
# itm_or_cost = input('Что бы вы хотели уточнить: ').lower()
#
# choice(biscuit, itm_or_cost)
#
#
# @sell_biscuit
# def calculating(vol):
#     cost = int(vol) * biscuits[biscuit][1] / 100
#     return print(f'К оплате {cost} р.', f'\nТорта {biscuit} осталось {biscuits[biscuit][2] - int(vol)} грамм')
#
#
# calculating()

# ----------TASK 13_6----------

#
# def factorial(nmb):
#     if nmb == 1:
#         return 1
#     return factorial(nmb-1) * nmb
#
#
# print(factorial(int(input('Enter number for calculation factorial: '))))
