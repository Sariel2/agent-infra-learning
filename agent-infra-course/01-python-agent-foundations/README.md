# 01 Python 与 Agent 基础

这是正式进入实战的第一阶段。你的目标不是成为“Python 语法专家”，而是把 Python 学成一种能快速搭 Agent 服务、能写实验、能做封装的工程语言。

## 阶段目标
- 补齐 Agent Infra 最需要的 Python 工程能力
- 跑通第一个 LLM API 服务
- 完成模型调用的工程封装

## 关键主题
- Python 工程结构
- 异步与 HTTP 调用
- 配置管理
- structured output
- provider abstraction

## 阶段产出
- 一个 `llm-gateway`
- 一个统一的模型调用层
- 一组基础测试

## 完成标准
- 能写出最小 FastAPI 服务
- 能调用模型并返回结构化结果
- 能解释为什么要做 provider 层封装
