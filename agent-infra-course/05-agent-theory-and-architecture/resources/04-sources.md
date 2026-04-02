# 05 Agent 原理与架构 原始来源与出处详解

[返回学习地图](../study-map.md) | [返回模块首页](../README.md) | [上一篇：03-code-reading-guide.md](./03-code-reading-guide.md) | [下一篇：05-common-mistakes.md](./05-common-mistakes.md)


这一页不是“链接仓库”，而是本模块讲义的出处解释页。你可以把它理解成：我为什么引用这些来源、这些来源里最值得看的部分是什么、以及这些内容在本教程里被翻译成了哪一段讲义。

## 怎么使用这一页
- 先把本模块前面的讲义读完，再来看这里。
- 看每个来源时，不要试图通读整站，只看这里标出的重点。
- 把这一页当成“出处说明 + 精读提示”，不是新的主教程。

## 1. [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview)
- 为什么这个来源重要：回看这个来源，是为了重新理解 orchestration 与 stateful runtime 的角色。
- 建议重点看：
  - 重点放在流程和状态边界，而不是具体 API
- 它在本教程里的对应位置：对应本模块对 workflow vs agent 边界的讨论。
- 我从原文里提炼出的关键结论：
  - 模式判断最终都要落回控制流和状态流。

## 2. [OpenAI Agents SDK](https://platform.openai.com/docs/guides/agents-sdk/)
- 为什么这个来源重要：回看这个来源，是为了把课程里的最小实现放回更成熟的 agent runtime 语境。
- 建议重点看：
  - 看 agent、tool、handoff、trace 的组织方式
- 它在本教程里的对应位置：对应本模块对单 agent、handoff 和 runtime 抽象的理解。
- 我从原文里提炼出的关键结论：
  - 模式学习不是记框架，而是理解框架为什么会这样组织。

## 3. [OpenAI new tools for building agents](https://openai.com/index/new-tools-for-building-agents/)
- 为什么这个来源重要：它给你平台演进方向的叙事背景，有助于你把“工具、runtime、trace 一体化”理解成行业趋势而不是课程偏好。
- 建议重点看：
  - 看 tools、agents、tracing 是如何被统一叙述的
- 它在本教程里的对应位置：对应本模块对 agent infra 体系化理解的收束。
- 我从原文里提炼出的关键结论：
  - 平台正在把 agent 系统的多个层面收敛到更统一的开发路径上。

## 读完这一页后回到哪里
- 如果你想回到主线：返回 [study-map.md](../study-map.md)
- 如果你想继续执行：去 [steps.md](../steps.md)
- 如果你想重新回顾概念：去 [01-concepts-and-principles.md](./01-concepts-and-principles.md)
