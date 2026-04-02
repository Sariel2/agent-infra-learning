# 01 Python 与 Agent 基础 练习题

## 概念题
1. 为什么 structured output 是 agent infra 的关键起点。
2. provider abstraction 解决了什么工程问题。
3. BaseSettings 与硬编码配置的本质区别是什么。

## 应用题
1. 设计一个 /generate 接口的输入输出模型。
2. 如果后面要接真实模型与 fake 模型，你会怎样设计 provider 接口。

## 排错题
1. 模型调用代码能跑，但测试很难写，通常说明什么问题。
2. 接口返回 JSON 字段经常变化，问题大概率出在哪。

## 设计题
1. 画出 route -> service -> provider 的依赖图。
2. 设计一个支持超时与重试的最小 provider。
