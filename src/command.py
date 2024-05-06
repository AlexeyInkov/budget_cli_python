from decimal import Decimal

from prettytable import PrettyTable

from .config import settings
from .entry import resave_entries, Entry
from .utils import input_date, input_category, input_amount, input_pk, input_param


def get_balance() -> None:
    """Получение баланса"""
    profit = Decimal("0.00")
    expense = Decimal("0.00")
    for entry in settings.entries:
        if entry.category == "Доход":
            profit += Decimal(entry.amount)
        else:
            expense += Decimal(entry.amount)
    print(f"\nБаланс:{(profit - expense)}\tДоходы:{profit}\tРасходы:{expense}\n")


def add_entry() -> None:
    """Добавление записи"""
    date = input_date()
    category = input_category()
    amount = input_amount()
    description = input("\nВведите описание: ")
    entry = Entry(
        pk=settings.count_entry + 1,
        date=date,
        category=category,
        amount=amount,
        description=description,
    )
    settings.entries.append(entry)
    settings.count_entry += 1
    resave_entries(settings.file_db, settings.encod, settings.entries)


def change_entry() -> None:
    """Изменение записи"""
    pk = input_pk(settings.count_entry)
    entry = settings.entries[pk - 1]
    while True:
        choice_param = input_param(
            settings.params_for_change, "Выберете параметр для изменения: "
        )
        if choice_param == "нет":
            break
        if choice_param == "Дата":
            print(f"Текущее значение: {entry.date}")
            entry.date = input_date()
        elif choice_param == "Категория":
            print(f"Текущее значение: {entry.category}")
            entry.category = input_category()
        elif choice_param == "Сумма":
            print(f"Текущее значение: {entry.amount}")
            entry.amount = input_amount()
        else:
            print(f"Текущее значение: {entry.description}")
            entry.description = input("Введите новое описание: ")
    print()
    resave_entries(settings.file_db, settings.encod, settings.entries)


def search_entry() -> None:
    """Поиск записей"""
    category = None
    date = None
    amount = None

    choice_param = input_param(
        settings.params_for_search, "Выберете параметр для поиска: "
    )
    if choice_param == "Дата":
        date = input_date()

    elif choice_param == "Категория":
        category = input_category()

    elif choice_param == "Сумма":
        amount = input_amount()

    # Вывод таблицы
    output = PrettyTable(["N", "Дата", "Категория", "Сумма", "Описание"])
    for entry in settings.entries:
        if (
            (entry.category == category or category is None)
            and (entry.date == date or date is None)
            and (entry.amount == amount or amount is None)
        ):
            output.add_row(entry.conv_to_output())
    print(output)
    print()
