# 02 单 Agent 与 Tools

这一阶段开始进入真正的 Agent 行为。关键不是“让模型会调用工具”这么简单，而是让整个 `tool selection -> parameter generation -> execution -> error recovery` 变得可控。

## 阶段目标
- 跑通单 Agent 的工具调用链路
- 设计稳定的 tool schema
- 给 Agent 加上最小失败恢复能力

## 核心主题
- function calling
- tool schema
- agent loop
- retry 和 fallback
- 执行轨迹记录

## 阶段产出
- 一个 `support-agent`
- 3 个以上工具
- 一份工具调用失败案例集

## 完成标准
- Agent 能按任务自动选工具
- 工具错误不会直接把流程打死
- 你能解释工具调用失败通常出在哪一层
