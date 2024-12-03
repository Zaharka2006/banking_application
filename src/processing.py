def fiter_by_state(dict_list: list, key_value: str = 'EXECUTED') -> list:
    """ Функция возвращает новый список словарей,
    содержащий только те словари, у которых ключ
    state соответствует указанному значению. """
    new_dict_list = []

    for user in dict_list:
        if user['state'] == key_value:
            new_dict_list.append(user)

    return new_dict_list
