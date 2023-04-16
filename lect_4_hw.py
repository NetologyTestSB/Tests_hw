# Задание 5(Необязательное)
# Напишите код для преобразования произвольного списка вида ['2018-01-01', 'yandex', 'cpc', 100]
# (он может быть любой длины) в словарь {'2018-01-01': {'yandex': {'cpc': 100}}}
src_list = ['2018-01-01', 'yandex', 'cpc', 100]

# решение задачи №5, выполненное в начале обучения
# def nested_dict(src_list):
#     dict_cur = {}
#     length = len(src_list)
#     if length >= 2:
#         dict_cur = {src_list[-2]: src_list[-1]}
#         for i in range(3, length + 1):
#             dict_cur = {src_list[-i]: dict_cur}
#     return dict_cur

# решение задачи №5, выполненное после завершения модулей по Python
def nested_dict(src_list):
    if src_list:
        if len(src_list) == 1:
            return src_list[0]
        else:
            return {src_list[0]: nested_dict(src_list[1:])}


# Задание 4
# Дана статистика рекламных каналов по объемам продаж.
# Напишите скрипт, который возвращает название канала с максимальным объемом.
# Т.е. в данном примере скрипт должен возвращать 'yandex'.
stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

# решение задачи №4, выполненное в начале обучения
# def statistics(stats):
#     chanels = list(stats.keys())
#     sells = list(stats.values())
#     if not chanels:
#         return ''
#     max_sells = 0
#     max_sells_chanel_num = None
#     for num, sell in enumerate(sells):
#         if sell > max_sells:
#             max_sells = sell
#             max_sells_chanel_num = num
#     return chanels[max_sells_chanel_num]

# решение задачи №4, выполненное после завершения модулей по Python
def statistics(stats):
    if stats:
        return max(stats, key=lambda k: stats[k])


# Задание 2
# Выведите на экран все уникальные гео-ID из значений словаря ids.
# Т.е. список вида [213, 15, 54, 119, 98, 35]
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

# решение задачи №2, выполненное в начале обучения
# def uniq_id(ids):
#     if not ids:
#         return []
#     result_set = set()
#     for user_num in range(1,4):
#       key_word = 'user' + str(user_num)
#       result_set = result_set | set(ids[key_word])
#     return list(result_set)

# решение задачи №2, выполненное после завершения модулей по Python
def uniq_id(ids):
    if ids:
        result_set = set()
        for val in ids.values():
            result_set = result_set | set(val)
        return list(result_set)


if __name__ == '__main__':
    print(nested_dict(src_list))
    print(statistics(stats))
    print(uniq_id(ids))
