# 05 Agent 原理与架构 关键资料重点与总结

## 1. LangGraph Overview 回读
- 为什么值得读：带着 workflow 实践回看设计意图。
- 重点看哪里：状态边界、节点职责。
- 一句话总结：workflow 是控制复杂度的架构工具。
- 读完你应该会：你能更清楚哪些步骤适合固定。
- 阅读说明：回读更有效。

## 2. OpenAI Agents SDK 回读
- 为什么值得读：这次重点看 runtime 与 trace，而不是怎么调用。
- 重点看哪里：agent 组织方式、handoff、trace。
- 一句话总结：agent runtime 的价值在于组织模型决策。
- 读完你应该会：你能把自己的最小实现放进更成熟语境里。
- 阅读说明：回读。

## 3. Pattern 相关文章
- 为什么值得读：帮助建立 pattern vocabulary。
- 重点看哪里：ReAct、Router、Plan-and-Execute、Supervisor 的边界。
- 一句话总结：模式的价值是减少重复踩坑。
- 读完你应该会：你能根据任务特征做选型。
- 阅读说明：选读但很重要。
