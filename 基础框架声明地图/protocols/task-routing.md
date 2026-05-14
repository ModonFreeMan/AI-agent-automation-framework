# 任务路由协议

## 适用任务

Agent 需要把用户自然语言请求映射到工程说明文档时使用。

## 路由步骤

1. 判断任务主类型。
2. 在 `agent-locator.yaml` 的 `task_routes` 中找到阅读顺序。
3. 读取对应 `layers/*.md`。
4. 如果任务跨层，优先读取安全、验证和项目知识相关文档。
5. 如果无法分类，按 `task_entry -> project_knowledge -> governance_security` 读取。

## 任务类型定义

- `feature`：新增能力、页面、接口、脚本、自动化流程。
- `auto_build`：根据用户需求文档自动构建工程、代码、测试、配置、文档或交付产物。
- `bugfix`：修复错误、异常、失败测试或行为偏差。
- `refactor`：不改变外部行为的结构调整。
- `test`：增加、修复或运行测试。
- `deploy`：构建、发布、部署、回滚。
- `incident`：线上问题、性能异常、日志排查。
- `documentation`：说明文档、架构图、开发规范。
- `security`：权限、密钥、数据安全、合规约束。

## 输出产物

Agent 完成路由后，应能回答：

- 当前任务属于哪些类型。
- 需要读取哪些说明文档。
- 是否需要人工审批。
- 最小可执行下一步是什么。

## 自动构建路由

当任务包含“根据需求文档构建”“自动构建”“按需求生成工程”“从需求生成代码”等意图时，Agent 应额外读取：

- `../自动化构建工程/requirements/current-requirement.md`
- `../自动化构建工程/build-flow/00-build-entry.md`
- `../自动化构建工程/build-flow/build-pipeline.yaml`
- `../自动化构建工程/validation/acceptance-checklist.md`
