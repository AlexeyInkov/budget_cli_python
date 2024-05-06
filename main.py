from src.command import get_balance, add_entry, change_entry, search_entry

COMMANDS = {
    "1": [get_balance, "Вывод баланса"],
    "2": [add_entry, "Добавление записи"],
    "3": [change_entry, "Редактирование записи"],
    "4": [search_entry, "Поиск по записи"],
}


def main() -> None:
    while True:
        for command_key, command in COMMANDS.items():
            print(f"{command_key}. - {command[1]}")
        print()
        while True:
            choice = input("Введите номер команды: ")
            if choice in COMMANDS.keys():
                break
            print("Не корректный выбор. Попробуйте еще раз")

        COMMANDS.get(choice)[0]()


if __name__ == "__main__":
    main()
