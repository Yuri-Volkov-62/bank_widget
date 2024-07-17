from datetime import datetime
from typing import Any

from masks import get_mask_account, get_mask_card_number


def mask_account_card(bank_data: str) -> Any:
    """Возвращает маску номера карты или счета"""
    try:
        bank_data_list = bank_data.rsplit(" ", 1)
        bank_data_number = bank_data_list[1]
        if len(bank_data_number) == 16:
            number_mask_card = get_mask_card_number(cart_number=bank_data_number)
            mask_card = bank_data_list[0] + " " + number_mask_card
            return mask_card
        elif len(bank_data_number) == 20:
            number_mask_account = get_mask_account(account_number=bank_data_number)
            mask_account = bank_data_list[0] + " " + number_mask_account
            return mask_account
        else:
            return "Неправильный ввод данных"
    except IndexError:
        return "Неправильный ввод данных"


def get_date(date_input: str) -> Any:
    """меняет формат времени"""
    try:
        dt = datetime.strptime(date_input, "%Y-%m-%dT%H:%M:%S.%f")
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        return "Введена некорректная дата"
