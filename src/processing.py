from datetime import datetime

from src.widget import get_date


def fiter_by_state(dict_list: list, key_value: str = 'EXECUTED') -> list:
    """ Функция возвращает новый список словарей,
    содержащий только те словари, у которых ключ
    state соответствует указанному значению. """
    new_dict_list = []

    for user in dict_list:
        if user['state'] == key_value:
            new_dict_list.append(user)

    return new_dict_list


def sort_by_date(dict_list: list, is_reverse: bool = True) -> list:
    """Эта функция, которая сортирует операции по дате в порядке убывания"""

    dates_list = []
    users_list = []

    for item in dict_list:
        dates_list.append(get_date(item["date"]))

    sorted_dates_list = sorted(dates_list, key=lambda date: datetime.strptime(date, "%d.%m.%Y"), reverse=is_reverse)

    for dates in sorted_dates_list:
        for item in dict_list:
            if dates == get_date(item["date"]):
                users_list.append(item)

    return users_list
