from src import masks


def mask_account_card(account: str) -> str:
    """Функция, которая маскирует аккаунт,
    введённый пользователем, используя маску"""

    card_type = list()
    card_number = list()

    if not isinstance(account, str):
        raise TypeError

    for item in account.split(" "):
        if item.isalpha():
            card_type.append(item)
        if item.isdigit():
            card_number.append(item)

    card_type_str = " ".join(card_type)
    card_number_str = " ".join(card_number)

    if (
        card_type_str != "Maestro"
        and card_type_str != "MasterCard"
        and card_type_str != "Счет"
        and card_type_str != "Visa Classic"
        and card_type_str != "Visa Platinum"
        and card_type_str != "Visa Gold"
    ):
        raise ValueError('Неверное имя карты или счёта')

    if card_type_str != "Счет":
        masked_account = f"{card_type_str} {masks.get_mask_card_number(card_number_str)}"
    else:
        masked_account = f"{card_type_str} {masks.get_mask_account(card_number_str)}"

    return masked_account


def get_date(date: str) -> str:
    """Функция, которая форматирует введённую дату"""
    if len(date) != 26:
        raise ValueError('Неверный формат даты')

    if date.isdigit() or date.isalpha():
        raise ValueError('Неверный формат даты')

    elif '-' not in date:
        raise ValueError('Неверный формат даты')

    counter_dash = 0

    for element in date:
        if element == '-':
            counter_dash += 1

    if counter_dash != 2:
        raise ValueError('Неверный формат даты')

    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
