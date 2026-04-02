# 01 Python 与 Agent 基础 概念、细节与原理

[返回学习地图](../study-map.md) | [返回模块首页](../README.md) | [下一篇：02-deep-dive.md](./02-deep-dive.md)

## 1. 这一模块的真正目标
你不是来学“Python 语法大全”的，而是来学如何用 Python 建一个 agent 系统的最小工程骨架。对于 agent infra 来说，Python 的价值主要在三件事上：
- 表达对象模型和约束很轻
- 框架生态成熟，能快速组织实验
- AI 相关库的首发支持通常更好

## 2. 为什么结构化输出是第一块地基
很多人一开始接模型，会让模型直接生成一段文本。这个方式适合 demo，不适合系统。系统需要的不是“看起来像答案”，而是“可被下游消费的稳定结果”。

结构化输出的意义在于：
- 把模型输出转成可验证的契约
- 让 route、service、provider 的边界清晰
- 为后面的 tool calling、RAG response、eval 输出打基础

一个经验法则是：只要输出要被程序继续处理，就尽量先定义 schema。

## 3. Provider abstraction 的原理
provider 的本质是“模型适配层”。它解决的问题不是“调用 API 很麻烦”，而是“模型相关变化不应该污染业务逻辑”。

为什么要有 provider：
- 方便从 fake provider 切到真实 provider
- 方便统一加超时、重试、日志、trace id
- 方便在测试中隔离外部依赖
- 方便未来切换模型、供应商或调用方式

这里最重要的不是模式名称，而是依赖方向：
- route 依赖 service
- service 依赖 provider 接口
- provider 接口再对应具体实现

## 4. 为什么先 fake，再 real
因为在系统早期，最大的风险不是模型质量，而是边界定义错误。fake provider 帮你先验证：
- 输入 schema 对不对
- 输出 schema 对不对
- route 和 service 有没有分层
- 测试是否能独立运行

先把结构做稳，再接真实模型，迭代速度会快很多。
