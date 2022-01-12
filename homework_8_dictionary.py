
# # task_HT_8_1

from string import ascii_lowercase

 # print(ascii_lowercase)

# print('variant_1')

# tpl_abc = ascii_lowercase
# nmbr_abc = range(1, len(ascii_lowercase) + 1)
# alfabet = {key: value for key, value in zip(tpl_abc, nmbr_abc)}
# print(*alfabet.items())


# print('variant_2')
# alfabet = {key: tpl_abc.index(key) + 1 for key in tpl_abc}
# print(alfabet)


# # task_HT_8_2
#
# ls_8_2 = input('введите три слова: ').split()
# dic_8_2 = {key: len(key) for key in ls_8_2}
# print(dic_8_2)

# # # task_HT_8_3
# #
# nmb_8_3 = input('введите числа: ').split()
# dct_8_3 = {key: round(int(key) * 1.1) for key in nmb_8_3}
# print(dct_8_3)


# # task_HT_8_4

# print('variant 1')
#
# dct_8_4 = {'Россия': 'Москва', 'Украина': 'Киев', 'Италия': 'Рим', 'Испания': 'Мадрид', 'Болгария': 'София'}
# cntry = input('введите название страны: ').capitalize()
# for key in dct_8_4.keys():
#     if key == cntry:
#         print(f'столица: {dct_8_4[key]}')
# # if key in dct_8_4.keys():
# #    print('запусти еще раз прогу')
# # else:
# #     print('проверьте правильно ли ввели название страны, и повторите')

#

# print('variant 2')
# dct_8_4 = {'Россия': 'Москва', 'Украина': 'Киев', 'Италия': 'Рим', 'Испания': 'Мадрид', 'Болгария': 'София'}
# cntry = input('введите название страны: ').capitalize()
# if cntry in tuple(dct_8_4.keys()):
#     print(f'столица: {dct_8_4[cntry]}')
# else:
#     print('проверьте правильно ли ввели название страны')


# # task_HT_8_5

# print('variant 1')
# val_ls = input('введите слова: ').split()
# key_nmb = range(1, len(val_ls) + 1)
# dcn_8_5 = {key_nmb: val_ls for key_nmb, val_ls in zip(key_nmb, val_ls) if key_nmb % 2 == 0}
# print(dcn_8_5)
#
# print('variant 2 - через ключевое слово del')
# val_ls = input('введите слова: ').split()
# key_nmb = range(1, len(val_ls) + 1)
# dcn_8_5 = dict(zip(key_nmb, val_ls))
# dcn_8_5_new = dcn_8_5.copy()
# for key_nmb, val_ls in dcn_8_5_new.items():
#     if key_nmb % 2 != 0:
#         del dcn_8_5[key_nmb]
#
# print(dcn_8_5)