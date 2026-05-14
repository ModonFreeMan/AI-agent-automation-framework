from __future__ import annotations

import argparse
from pathlib import Path

from .store import TodoStore


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="todo", description="Manage local todo items.")
    parser.add_argument(
        "--data",
        default="todo-data.json",
        help="Path to the JSON data file. Defaults to todo-data.json.",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a todo item.")
    add_parser.add_argument("text", help="Todo item text.")

    subparsers.add_parser("list", help="List todo items.")

    done_parser = subparsers.add_parser("done", help="Mark a todo item as done.")
    done_parser.add_argument("id", type=int, help="Todo item id.")

    delete_parser = subparsers.add_parser("delete", help="Delete a todo item.")
    delete_parser.add_argument("id", type=int, help="Todo item id.")

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    store = TodoStore(Path(args.data))

    try:
        if args.command == "add":
            item = store.add(args.text)
            print(f"Added #{item.id}: {item.text}")
            return 0

        if args.command == "list":
            items = store.list_items()
            if not items:
                print("No todo items.")
                return 0
            for item in items:
                status = "x" if item.done else " "
                print(f"[{status}] #{item.id} {item.text}")
            return 0

        if args.command == "done":
            item = store.mark_done(args.id)
            print(f"Done #{item.id}: {item.text}")
            return 0

        if args.command == "delete":
            item = store.delete(args.id)
            print(f"Deleted #{item.id}: {item.text}")
            return 0
    except (KeyError, ValueError) as exc:
        print(f"Error: {exc}")
        return 1

    return 1
