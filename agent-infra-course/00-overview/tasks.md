# 00 总览与准备任务安排

## Block 1：认知对齐
- 阅读总课程 README 和总思维导图
- 手写一版你理解中的 Agent Infra 链路
- 把以下概念写成一句话定义：`model`、`tool`、`memory`、`retrieval`、`workflow`、`trace`、`eval`、`runtime`

## Block 2：环境搭建
- 安装并确认 Python `3.11+`
- 选择依赖管理工具：`uv` 或 `poetry`
- 初始化一个最小工程，准备 `src/`、`tests/`、`.env.example`
- 安装基础依赖：`fastapi`、`pydantic`、`pytest`、`httpx`

## Block 3：项目主线定义
- 选定统一项目方向：建议做 `企业知识问答 + 工具调用 + 工单创建`
- 写清楚主项目的用户、输入、输出、核心成功指标
- 明确哪些能力会在第 1、2、3、4 阶段逐步加入

## Block 4：学习机制搭建
- 创建 `learning-log.md`
- 创建 `experiments.md`
- 创建 `mistakes.md`
- 创建 `questions.md`

## 退出条件
- 能把主项目用 5 句话讲清楚
- 能把 repo 跑起来
- 能开始进入第 1 阶段而不再纠结方向
