from datetime import datetime
from decimal import Decimal


def input_date() -> str:
    """Ввод и проверка даты"""
    while True:
        date = input("\nВведите дату год месяц день через пробел(#### ## ##): ")
        try:
            date_format = datetime.strptime(date, "%Y %m %d")
        except ValueError:
            print("Не корректное значение. Попробуйте еще раз")
        else:
            break
    return date_format.strftime("%Y-%m-%d")


def input_category() -> str:
    """Ввод категории"""
    while True:
        cat = input("\n\t1 - Доход\n\t2 - Расход\nВыберете категорию операции: ")
        if cat in ("1", "2"):
            break
        print("Не корректный ввод. Попробуйте еще раз")
    if cat == "1":
        return "Доход"
    return "Расход"


def input_amount() -> str:
    """Ввод суммы"""
    while True:
        amount = input("\nВведите сумму: ")
        try:
            amount = Decimal(amount)
        except ValueError:
            print("Не корректное значение. Попробуйте еще раз")
        else:
            return str(amount)


def input_pk(counter: int) -> int:
    """Ввод и проверка номера записи"""
    while True:
        pk = input(f"\nВведите номер записи(допустимые значения от 1 до {counter}): ")
        try:
            pk = int(pk)
            if 1 > pk > counter:
                raise ValueError
        except ValueError:
            print("Не корректное значение. Попробуйте еще раз")
        else:
            return pk


def input_param(params: dict, question: str) -> str:
    while True:
        print()
        for key, value in params.items():
            print(f"\t{key} - {value}")
        param = input(question)
        if param in params.keys():
            break
        print("Не корректный ввод. Попробуйте еще раз")
    return params[param]
