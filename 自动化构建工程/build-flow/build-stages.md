# 构建阶段说明

## S1 需求读取与完整性检查

读取 `requirements/current-requirement.md`，提取目标、范围、产物、验收标准和风险。

完成后写入 `logs/S1-requirement-intake.md`。

## S2 构建任务拆解

将需求拆解为可执行任务，明确哪些文件需要创建或修改，哪些事项需要人工确认。

完成后写入 `logs/S2-task-decomposition.md`。

## S3 工程工作区准备

根据需求选择目标工作区：

- 如果需求指向已有项目，在原项目内执行。
- 如果需求需要新建工程，在 `workspaces/` 下创建子目录。
- 如果技术栈不明确，先写入阻塞项。

完成后写入 `logs/S3-workspace-prepare.md`。

## S4 实现与构建

按任务拆解执行代码、配置、测试和文档创建。

完成后写入 `logs/S4-implementation-build.md`。

## S5 验证与质量检查

按 `validation/acceptance-checklist.md` 验证功能、测试、静态检查、文档和安全边界。

完成后写入 `logs/S5-verification.md`。

## S6 产物归档

将可交付结果、使用说明、验证记录和剩余风险归档到 `artifacts/`。

完成后写入 `logs/S6-artifact-packaging.md`。
