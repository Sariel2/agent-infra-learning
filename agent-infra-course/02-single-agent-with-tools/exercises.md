# 02 单 Agent 与 Tools 练习题

## 概念题
1. 为什么 tool schema 设计质量会直接影响 agent 质量。
2. tool calling 与普通函数调用最大的差异是什么。
3. 什么情况下其实不需要 agent，只需要 workflow。

## 应用题
1. 为 create_ticket 设计输入输出 schema。
2. 设计一个工具失败后的返回结构，要求能被 agent 消费。

## 排错题
1. agent 总是错误选择 search_docs，可能有哪些原因。
2. 一个工具偶尔超时但主流程不能中断，你会怎么处理。

## 设计题
1. 设计一个最小单 agent loop。
2. 设计一个工具轨迹日志格式，要求后面能做 trace 分析。
