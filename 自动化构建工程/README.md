# 自动化构建工程

## 目标

本工程目录用于承接“根据用户需求文档自动执行构建流程”的 Agent 工作流。

Agent 不应从零猜测任务，而应先读取需求文档，再按固定构建流程完成分析、设计、实现、验证和产物归档。

## Agent 固定入口

1. `requirements/current-requirement.md`
2. `build-flow/00-build-entry.md`
3. `build-flow/build-pipeline.yaml`
4. `validation/acceptance-checklist.md`

## 目录职责

```text
自动化构建工程/
├── README.md
├── requirements/
│   ├── current-requirement.md
│   └── requirement-template.md
├── build-flow/
│   ├── 00-build-entry.md
│   ├── build-pipeline.yaml
│   ├── build-stages.md
│   └── agent-runbook.md
├── validation/
│   └── acceptance-checklist.md
├── prompts/
│   └── requirement-to-build-task.md
├── workspaces/
├── artifacts/
└── logs/
```

## 执行原则

- 需求文档是唯一任务源。
- 构建流程必须可追踪、可复现。
- 每个阶段都要有输入、输出和完成标准。
- 无法自动判断的事项写入阻塞项，不擅自扩大范围。
- 任何构建结果必须经过验收清单检查。
