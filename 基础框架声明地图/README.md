# AI Agent 自动化工程框架说明

## 目的

本目录用于定义一套 AI Agent 可以自动读取、定位、执行和验证的软件工程框架。

它解决三个问题：

1. Agent 接到任务后，如何知道先读哪些说明。
2. Agent 面对不同任务类型时，如何找到对应工程规则。
3. Agent 修改代码后，如何验证、交付并遵守安全边界。

## Agent 入口

任何 AI Agent 进入项目后，应优先读取：

- `00-agent-entry.md`：总入口和工作流程。
- `agent-locator.yaml`：机器可读的文件定位表。
- `protocols/task-routing.md`：任务类型到文档路径的路由规则。
- `governance/safety-boundaries.md`：不可越过的安全边界。

如果任务是根据用户需求文档自动构建，继续读取：

- `../自动化构建工程/requirements/current-requirement.md`
- `../自动化构建工程/build-flow/00-build-entry.md`
- `../自动化构建工程/build-flow/build-pipeline.yaml`

## 文档结构

```text
基础框架声明地图/
├── README.md
├── 00-agent-entry.md
├── agent-locator.yaml
├── 基础框架.txt
├── layers/
│   ├── 01-task-entry.md
│   ├── 02-project-knowledge.md
│   ├── 03-dev-environment.md
│   ├── 04-tool-execution.md
│   ├── 05-quality-verification.md
│   ├── 06-cicd-delivery.md
│   ├── 07-runtime-observability.md
│   └── 08-governance-security.md
├── protocols/
│   ├── task-routing.md
│   └── document-contract.md
├── templates/
│   ├── agent-task-brief.md
│   └── layer-doc-template.md
└── governance/
    └── safety-boundaries.md
```

## 使用方式

人类维护者负责把项目事实写进这些说明文档。

AI Agent 负责按文档定位任务、执行变更、验证结果，并在发现文档缺失或过期时提出修订建议。
