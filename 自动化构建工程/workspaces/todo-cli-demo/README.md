# Todo CLI Demo

一个根据需求文档自动构建的 Python 命令行待办事项工具。

## 运行要求

- Python 3.10+

## 使用方式

在本目录运行：

```powershell
python -m todo_cli add "write demo"
python -m todo_cli list
python -m todo_cli done 1
python -m todo_cli delete 1
```

默认数据文件为当前目录下的 `todo-data.json`。

也可以指定数据文件：

```powershell
python -m todo_cli --data ./tmp/todos.json add "custom data file"
```

## 测试

```powershell
python -m unittest discover -s tests
```

## 命令

- `add <text>`：添加待办事项。
- `list`：查看所有待办事项。
- `done <id>`：标记待办事项完成。
- `delete <id>`：删除待办事项。
