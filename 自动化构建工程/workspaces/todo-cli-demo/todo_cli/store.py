from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class TodoItem:
    id: int
    text: str
    done: bool = False


class TodoStore:
    def __init__(self, path: str | Path = "todo-data.json") -> None:
        self.path = Path(path)

    def list_items(self) -> list[TodoItem]:
        return [TodoItem(**item) for item in self._read_items()]

    def add(self, text: str) -> TodoItem:
        text = text.strip()
        if not text:
            raise ValueError("todo text cannot be empty")

        items = self._read_items()
        next_id = max((item["id"] for item in items), default=0) + 1
        item = TodoItem(id=next_id, text=text)
        items.append(asdict(item))
        self._write_items(items)
        return item

    def mark_done(self, item_id: int) -> TodoItem:
        items = self._read_items()
        for item in items:
            if item["id"] == item_id:
                item["done"] = True
                self._write_items(items)
                return TodoItem(**item)
        raise KeyError(f"todo item {item_id} not found")

    def delete(self, item_id: int) -> TodoItem:
        items = self._read_items()
        for index, item in enumerate(items):
            if item["id"] == item_id:
                removed = items.pop(index)
                self._write_items(items)
                return TodoItem(**removed)
        raise KeyError(f"todo item {item_id} not found")

    def _read_items(self) -> list[dict]:
        if not self.path.exists():
            return []
        with self.path.open("r", encoding="utf-8") as file:
            data = json.load(file)
        if not isinstance(data, list):
            raise ValueError("todo data file must contain a list")
        return data

    def _write_items(self, items: list[dict]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("w", encoding="utf-8") as file:
            json.dump(items, file, ensure_ascii=False, indent=2)
            file.write("\n")
