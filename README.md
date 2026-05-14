# AI Agent Automation Framework

一个面向 AI Agent 的自动化工程框架，用来描述如何让 Agent 根据需求文档自动完成任务定位、工程构建、验证和产物归档。

本项目的核心目标是搭建一套环境、工具、文档、测试、CI/CD、监控和治理规则，让 AI Agent 能可靠地开发、测试、提交、修复和交付软件。

## 项目结构

```text
.
├── Target.txt
├── 基础框架声明地图/
│   ├── README.md
│   ├── 00-agent-entry.md
│   ├── agent-locator.yaml
│   ├── layers/
│   ├── protocols/
│   ├── templates/
│   └── governance/
└── 自动化构建工程/
    ├── README.md
    ├── requirements/
    ├── build-flow/
    ├── validation/
    ├── prompts/
    ├── workspaces/
    ├── logs/
    └── artifacts/
```

## 两个核心模块

### 基础框架声明地图

`基础框架声明地图/` 是给 AI Agent 使用的工程导航层。

Agent 进入项目后应优先读取：

1. `基础框架声明地图/00-agent-entry.md`
2. `基础框架声明地图/agent-locator.yaml`
3. `基础框架声明地图/protocols/task-routing.md`
4. `基础框架声明地图/governance/safety-boundaries.md`

它定义了八个工程层级：

- 任务入口层
- 项目知识层
- 开发环境层
- 工具执行层
- 质量验证层
- CI/CD 交付层
- 运行观测层
- 治理与安全层

### 自动化构建工程

`自动化构建工程/` 用于承接“用户需求文档 -> 自动构建流程 -> 验证 -> 产物归档”的完整链路。

Agent 执行自动构建时应读取：

1. `自动化构建工程/requirements/current-requirement.md`
2. `自动化构建工程/build-flow/00-build-entry.md`
3. `自动化构建工程/build-flow/build-pipeline.yaml`
4. `自动化构建工程/validation/acceptance-checklist.md`

构建流程分为 S1 到 S6：

- S1：需求读取与完整性检查
- S2：构建任务拆解
- S3：工程工作区准备
- S4：实现与构建
- S5：验证与质量检查
- S6：产物归档

## 快速使用

1. 在 `自动化构建工程/requirements/current-requirement.md` 中写入用户需求。
2. 将需求状态设置为 `status: ready`。
3. 让 Agent 读取 `自动化构建工程/build-flow/build-pipeline.yaml`。
4. Agent 按 S1-S6 执行构建。
5. 查看 `自动化构建工程/logs/` 和 `自动化构建工程/artifacts/`。

推荐提示词：

```text
请读取 自动化构建工程/requirements/current-requirement.md，
并按照 自动化构建工程/build-flow/build-pipeline.yaml
自动执行构建流程。
```

## Demo

当前仓库内置了一个 demo：

```text
自动化构建工程/workspaces/todo-cli-demo/
```

它是一个根据需求文档自动生成的 Python 命令行待办事项工具，支持：

- 添加待办事项
- 查看待办事项
- 标记完成
- 删除待办事项
- 使用本地 JSON 文件保存数据

运行 demo：

```powershell
cd 自动化构建工程/workspaces/todo-cli-demo
python -m todo_cli add "write demo"
python -m todo_cli list
python -m todo_cli done 1
python -m todo_cli delete 1
```

运行测试：

```powershell
python -m unittest discover -s tests
```

## 安全边界

本框架默认要求 Agent 遵守以下原则：

- 不写入密钥、令牌或密码。
- 不伪造测试结果。
- 不绕过审批、鉴权或审计。
- 不自动执行生产部署、生产回滚或生产数据库变更。
- 高风险操作必须等待人工确认。

详细规则见：

```text
基础框架声明地图/governance/safety-boundaries.md
```

## 当前状态

项目已经包含：

- AI Agent 工程导航文档
- 机器可读定位文件 `agent-locator.yaml`
- 需求驱动自动构建流水线
- 构建阶段日志模板和示例
- Python todo CLI demo
- 验收清单和产物归档示例
