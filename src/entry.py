import json


class Entry:
    pk: int = None
    date: str = None
    category: str = None
    amount: str = None
    description: str = None

    def __init__(self, pk, date, category, amount, description):
        self.pk = pk
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def conv_to_json(self) -> dict:
        return {
            "pk": self.pk,
            "date": self.date,
            "category": self.category,
            "amount": self.amount,
            "description": self.description,
        }

    def conv_to_output(self) -> list:
        return [
            self.pk,
            self.date,
            self.category,
            self.amount,
            self.description,
        ]


def resave_entries(file_db: str, encoding: str | None, entries: list[Entry]) -> None:
    data = []
    for entry in entries:
        data.append(entry.conv_to_json())
    with open(file_db, "w", encoding=encoding) as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
