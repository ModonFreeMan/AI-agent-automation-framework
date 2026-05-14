# Todo CLI Demo 构建产物摘要

## 需求来源

- `自动化构建工程/requirements/current-requirement.md`

## 产物路径

- `自动化构建工程/workspaces/todo-cli-demo/`

## 已生成内容

- `todo_cli/store.py`：JSON 文件存储和待办事项核心逻辑。
- `todo_cli/cli.py`：命令行入口和参数解析。
- `todo_cli/__main__.py`：支持 `python -m todo_cli`。
- `tests/test_store.py`：核心逻辑单元测试。
- `README.md`：运行、测试和命令说明。

## 使用方式

在 `自动化构建工程/workspaces/todo-cli-demo/` 目录运行：

```powershell
python -m todo_cli add "write demo"
python -m todo_cli list
python -m todo_cli done 1
python -m todo_cli delete 1
```

## 测试方式

```powershell
python -m unittest discover -s tests
```

## 验证结果

- 单元测试：4 个测试通过。
- CLI 行为：`add`、`list`、`done`、`delete` 已验证。

## 剩余风险

- 这是 demo 工程，未做打包发布配置。
- 数据文件没有并发写保护，不适合多进程同时写入。
