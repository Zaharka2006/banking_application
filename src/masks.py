def get_mask_card_number(number: str) -> str:
    """Функция, которая маскирует номер карты в формате 'XXXX XX** **** XXXX'"""
    if not isinstance(number, str):
        raise ValueError("Номер карты должен быть строкой, а не числом")

    if len(number) != 16 or not number.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр")

    mask_card_number = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"

    return mask_card_number


def get_mask_account(number: str) -> str:
    """Функция, которая маскирует номер счёта в формате '**XXXX'"""
    if not isinstance(number, str):
        raise ValueError("Номер счёта должен быть строкой, а не числом")

    if len(number) != 20 or not number.isdigit():
        raise ValueError("Номер счёта должен содержать 20 цифр")

    mask_card_number = f"**{number[-4:]}"

    return mask_card_number
