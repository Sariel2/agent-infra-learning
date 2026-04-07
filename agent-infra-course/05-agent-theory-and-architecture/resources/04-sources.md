# 05 Agent 原理与架构 原始来源与出处详解

[返回学习地图](../study-map.md) | [返回模块首页](../README.md) | [上一篇：03-code-reading-guide.md](./03-code-reading-guide.md) | [下一篇：05-common-mistakes.md](./05-common-mistakes.md)

这一页不是让你回去“补更多框架知识”，而是帮助你把模式判断重新放回一手资料的语境。第 05 模块最容易被误读成“学模式名字”，但真正有价值的是：你要从这些来源里看出为什么不同系统会在控制流、状态边界和运行时组织上分化成不同形态。

## 怎么使用这一页
- 先读完第 05 模块正文，再回看这里。
- 看这些来源时，不要问“这个框架怎么用”，先问“它把哪类复杂度显式化了”。
- 把“控制流、状态、边界、复杂度预算”当成阅读主线。

## 1. [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview)
- 为什么这个来源重要：回看这个来源，不是为了再学一次 workflow，而是为了把第 05 模块里的模式判断重新落回控制流和状态流。它能提醒你：模式差异最终都不是术语差异，而是运行结构差异。
- 这个来源原本在解决什么问题：
  - 如何显式描述图状控制流
  - 如何把 state 做成运行对象
  - 如何通过节点与条件分支组织复杂任务
- 你应该从原文里抓到的核心原理：
  - 所谓模式差异，最终都要落回控制流位置和状态维护方式。
  - orchestration 的核心，不是“多几个节点”，而是“把复杂度集中到可见结构”。
  - workflow / graph 风格的思维，会帮助你识别哪些地方其实不该交给自由 agent。
- 本教程吸收成了哪些内容：
  - `pattern 的本质是控制流设计`
  - `workflow、agent、multi-agent` 的边界比较
  - `architecture-lab` 中的 boundary checker 思路
- 读原文时重点看什么：
  - state
  - graph
  - routing
  - 为什么流程显式化能减少复杂度失控
- 读完后你应该能回答：
  - 为什么模式比较最终都要回到状态和控制流
  - 为什么 graph 思维对架构判断有帮助

## 2. [OpenAI Agents SDK](https://platform.openai.com/docs/guides/agents-sdk/)
- 为什么这个来源重要：它帮助你把课程里的最小实现放回一个更成熟的 agent runtime 语境里理解。到了第 05 模块，你不再只是看“能不能用”，而是要开始看“为什么成熟 runtime 会把能力组织成这样”。
- 这个来源原本在解决什么问题：
  - 如何表达 agent 运行单元
  - 如何把 tools、handoff、trace 放进统一 runtime
  - 如何在更高层组织多步 agent 任务
- 你应该从原文里抓到的核心原理：
  - pattern 学习不是记框架，而是理解框架为什么会采用那样的控制流组织。
  - handoff、tool、trace 这些概念的背后，都是边界和责任分配问题。
  - 单 agent 和多 agent 的差别，不只是数量差别，而是协调成本和状态边界差别。
- 本教程吸收成了哪些内容：
  - 第 05 模块对 ReAct、Router、Plan-and-Execute、Supervisor 的比较
  - 为什么课程反复强调 `多主体不会自动解决单主体问题`
  - `为什么不用另一个方案` 这种架构判断训练
- 读原文时重点看什么：
  - agent
  - handoff
  - tool
  - trace
  - 为什么 runtime 要把这些概念单独立出来
- 读完后你应该能回答：
  - 为什么模式学习不能停留在术语表
  - 为什么 runtime 结构本身就是一种架构表达

## 3. [OpenAI new tools for building agents](https://openai.com/index/new-tools-for-building-agents/)
- 为什么这个来源重要：它提供了平台演进方向的叙事背景，能帮助你把“工具、runtime、tracing 一体化”理解成行业趋势，而不是课程作者的个人偏好。
- 这个来源原本在解决什么问题：
  - 如何把模型、工具、agent runtime、tracing 组织成更统一的开发路径
  - 如何降低开发者在不同层面间来回切换的成本
  - 如何把 agent 系统从“零散能力集合”推向更完整平台形态
- 你应该从原文里抓到的核心原理：
  - 行业正在尝试把 agent 系统的多个层面收敛到更统一的工作流。
  - 这种收敛并不意味着你不需要判断，反而更要求你知道每一层在解决什么。
  - 真正重要的不是“平台替你做了多少”，而是“你是否理解平台在收敛哪些复杂度”。
- 本教程吸收成了哪些内容：
  - 第 05 模块里“pattern 不是孤立技巧，而是系统组织方式”的收束
  - 第 06 模块里“项目表达要能接上行业主语境”的铺垫
  - 为什么课程把 tools、runtime、trace 看成一条连贯主线
- 读原文时重点看什么：
  - tools、agents、tracing 被如何统一叙述
  - 平台在试图替开发者消化哪类复杂度
  - 这和你课程里做过的最小实现之间是什么关系
- 读完后你应该能回答：
  - 为什么理解行业平台演进有助于做架构判断
  - 为什么课程最后要回到“体系化”而不是停在 demo

## 这一页真正想帮你建立什么
- 模式学习最终要落回控制流、状态边界和复杂度预算
- 框架和平台不是你模仿的对象，而是你分析其设计取舍的材料
- 你回看来源时，应该不断问：它在用什么方式显式化复杂度

## 读完这一页后回到哪里
- 如果你想回到主线：返回 [study-map.md](../study-map.md)
- 如果你想继续执行：去 [steps.md](../steps.md)
- 如果你想重新回顾概念：去 [01-concepts-and-principles.md](./01-concepts-and-principles.md)
