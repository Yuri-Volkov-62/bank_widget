#cart_number = input("Введите номер карты: ")
#account_number = input("Введите номер счета: ")


def get_mask_card_number(cart_number: str) -> str:
    """функция возвращает маску номера карты"""
    if len(cart_number) == 16 and cart_number.isdigit() is True:
        cart_number_list = list(cart_number)
        for i in range(6, 12):
            cart_number_list[i] = "X"
            cart_number_string = "".join(cart_number_list)
            cart_number_mask = " ".join([cart_number_string[i: i + 4] for i in range(0, len(cart_number_string), 4)])
        return cart_number_mask
    else:
        return "неправильно введен номер карты"


def get_mask_account(account_number: str) -> str:
    """функция возвращает маску номера счета"""
    if len(account_number) == 20 and account_number.isdigit() is True:
        account_number_mask = "**" + account_number[-4:]
        return account_number_mask
    else:
        return "Неправильно введен номер"
