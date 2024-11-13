from src import masks

card_number = input("Введите номер карты (16 цифр): ")

print(masks.get_mask_card_number(card_number))
print(masks.get_mask_account(card_number))
