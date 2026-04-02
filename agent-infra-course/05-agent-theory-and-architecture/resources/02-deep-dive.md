# 05 Agent 原理与架构 细节深挖

[返回学习地图](../study-map.md) | [返回模块首页](../README.md) | [上一篇：01-concepts-and-principles.md](./01-concepts-and-principles.md) | [下一篇：03-code-reading-guide.md](./03-code-reading-guide.md)

## 1. pattern 的核心不是形式，而是控制流
很多人区分模式时只看“是不是多轮”。这远远不够。真正要看的，是：
- 决策在哪一层发生
- 状态如何传递
- 工具或子任务如何被组织
- 错误如何传播

## 2. 为什么课程里要做 boundary checker
因为工程里最贵的错误之一就是“明明该用 workflow，却用了自由 agent”；或者“明明只需要单 agent，却为了高级感上了 multi-agent”。边界判断是复杂度控制能力。

## 3. architecture-lab 的价值
这个服务不是为了业务功能，而是为了让你能把模式比较讲清楚。它对应的是后面做架构说明、技术分享和面试表达时最常用的抽象能力。
