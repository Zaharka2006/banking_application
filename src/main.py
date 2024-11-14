from src import widget

account_name = input("Введите название карты и её номера: ")
print(widget.mask_account_card(account_name))

user_date = input("Введите вашу дату и время: ")
print(widget.get_date(user_date))
