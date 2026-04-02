# 01 Python 与 Agent 基础项目任务

## 项目名
`llm-gateway`

## 项目目标
做一个最小 Agent 基础服务，接收用户输入，调用模型，返回结构化 JSON，并具备基础日志、配置管理和测试。

## 必做项
- 提供 `/health`
- 提供 `/generate`
- 用 `Pydantic` 描述输入输出
- 返回固定结构，例如 `answer`、`confidence`、`reasoning_summary`
- 加上日志、超时和错误处理

## 加分项
- 支持切换模型名
- 支持 mock provider
- 支持请求 ID

## 验收标准
- 本地可启动
- curl 可调通
- pytest 有最小覆盖
- 代码结构清晰，不把所有逻辑塞进路由
