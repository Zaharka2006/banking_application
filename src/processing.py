from datetime import datetime

from src.widget import get_date


def filter_by_state(my_list: list[dict], key_value: str = "EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей,
    содержащий только те словари, у которых ключ
    state соответствует указанному значению."""
    new_operation_list = []

    if key_value != 'EXECUTED' and key_value != 'CANCELED':
        raise ValueError('Неверный статус операции')

    for user in my_list:
        if user["state"] == key_value:
            new_operation_list.append(user)

    return new_operation_list


def sort_by_date(operation_list: list[dict], is_reverse: bool = True) -> list[dict]:
    """Эта функция, которая сортирует операции по дате в порядке убывания"""

    formatted_dates = []
    new_operation_list = []

    for item in operation_list:
        formatted_dates.append(get_date(item["date"]))

    for date in formatted_dates:
        format = "%d.%m.%Y"
        if not bool(datetime.strptime(date, format)):
            raise ValueError

    sorted_dates_list = sorted(formatted_dates,
                               key=lambda date: datetime.strptime(date, "%d.%m.%Y"),
                               reverse=is_reverse)

    for dates in sorted_dates_list:
        for item in operation_list:
            if dates == get_date(item["date"]):
                new_operation_list.append(item)

    return new_operation_list
