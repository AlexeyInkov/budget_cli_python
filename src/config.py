import json
import os.path

from .entry import Entry


class Settings:
    count_entry: int = None
    entries: list[Entry] = None
    file_db: str = "entries.json"
    encod = "utf-8"
    params_for_change = {
        "0": "нет",
        "1": "Дата",
        "2": "Категория",
        "3": "Сумма",
        "4": "Описание",
    }
    params_for_search = {
        "0": "нет",
        "1": "Дата",
        "2": "Категория",
        "3": "Сумма",
    }

    def __init__(self):
        if not os.path.exists(self.file_db):
            with open(self.file_db, "w", encoding=self.encod):
                self.count_entry = 0
                self.entries = []
        else:
            with open(self.file_db, "r", encoding=self.encod) as file:
                self.entries = [Entry(**item) for item in json.load(file)]
                self.count_entry = len(self.entries)


settings = Settings()
