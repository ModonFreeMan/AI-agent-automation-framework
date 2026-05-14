import tempfile
import unittest
from pathlib import Path

from todo_cli import TodoStore


class TodoStoreTests(unittest.TestCase):
    def test_add_and_list_items(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            store = TodoStore(Path(temp_dir) / "todo-data.json")

            item = store.add("write demo")
            items = store.list_items()

            self.assertEqual(item.id, 1)
            self.assertEqual(items[0].text, "write demo")
            self.assertFalse(items[0].done)

    def test_mark_done(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            store = TodoStore(Path(temp_dir) / "todo-data.json")
            item = store.add("test done")

            updated = store.mark_done(item.id)

            self.assertTrue(updated.done)
            self.assertTrue(store.list_items()[0].done)

    def test_delete(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            store = TodoStore(Path(temp_dir) / "todo-data.json")
            item = store.add("delete me")

            removed = store.delete(item.id)

            self.assertEqual(removed.text, "delete me")
            self.assertEqual(store.list_items(), [])

    def test_empty_text_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            store = TodoStore(Path(temp_dir) / "todo-data.json")

            with self.assertRaises(ValueError):
                store.add("   ")


if __name__ == "__main__":
    unittest.main()
