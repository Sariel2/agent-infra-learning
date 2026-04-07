# 04 Workflow、Observability 与 Evals 原始来源与出处详解

[返回学习地图](../study-map.md) | [返回模块首页](../README.md) | [上一篇：03-code-reading-guide.md](./03-code-reading-guide.md) | [下一篇：05-common-mistakes.md](./05-common-mistakes.md)

这一页要做的事，是把 workflow、trace、eval 相关来源翻译成真正可吸收的工程判断。这个模块最容易出现的误区，是把流程图、可观测性和评测当成三块彼此独立的知识。实际上，它们是在回答同一件事：系统应该怎么走、实际怎么走、走出来是不是更好。

## 怎么使用这一页
- 先把本模块前面的 3 份讲义读完，再来看这里。
- 回原文时，不要把注意力放在“框架 API 怎么写”，先看“为什么这类能力会存在”。
- 带着“它如何帮助我治理复杂度”这个问题去看每个来源。

## 1. [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview)
- 为什么这个来源重要：它最重要的价值，不是教你一个框架，而是把 workflow / orchestration / stateful runtime 明确成一类独立问题。很多人前面做 agent 时，系统还是一团隐式流程代码；这个来源会帮助你第一次清楚看到：流程、状态和分支其实应该被显式建模。
- 这个来源原本在解决什么问题：
  - 如何把多步执行组织成图结构
  - 如何把 state 作为一等对象维护
  - 如何通过 node / edge / conditional routing 表达流程控制
  - 如何让复杂流程不再藏在 if/else 和 prompt 里
- 你应该从原文里抓到的核心原理：
  - workflow 的价值是显式状态和显式分支。
  - orchestration 不是“多写几个节点”，而是把控制流拉到台前。
  - 当系统开始有分类、tool dispatch、retrieval、审核和 fallback 时，隐式流程会迅速失控。
- 本教程吸收成了哪些内容：
  - `workflow 必须显式存在`
  - `workflow 包住 agent` 这条判断
  - `01-stateful-workflow` example 里对状态机骨架的处理
- 读原文时重点看什么：
  - state
  - node
  - edge
  - conditional routing
  - 为什么图结构更适合承载多步执行
- 读完后你应该能回答：
  - 为什么流程图不只是展示物，而应该进入执行骨架
  - 为什么 workflow 不是 agent 的对立面

## 2. [LangSmith Observability](https://docs.langchain.com/oss/python/langgraph/observability)
- 为什么这个来源重要：它能帮助你直观看到“运行过程可见”到底意味着什么。很多人知道应该加 trace，但不知道 trace 的价值到底在哪。这个来源的价值就在于，它让“过程可见”变成具体可感的东西。
- 这个来源原本在解决什么问题：
  - 如何查看 graph run
  - 如何观察节点执行和状态变化
  - 如何把运行过程从黑箱变成可回放的过程证据
- 你应该从原文里抓到的核心原理：
  - 可观测性不是让日志更多，而是让因果链更清楚。
  - 如果只能看到最终结果，很多问题根本无法归因。
  - trace 的价值，在于让系统的真实路径对你可见。
- 本教程吸收成了哪些内容：
  - `trace 不是更详细的日志`
  - 第 04 模块中“路径、节点、耗时、失败点”这些观察面
  - 为什么课程把 trace 放进 agent runtime，而不是单独当作调试技巧
- 读原文时重点看什么：
  - graph run 的视角
  - 节点执行信息
  - 状态变化如何被展示
  - 为什么过程可见会改变排障方式
- 读完后你应该能回答：
  - 为什么看最终答案不足以维护一个 agent 系统
  - 为什么 workflow 和 observability 天然应该一起理解

## 3. [OpenAI Agents SDK Tracing](https://openai.github.io/openai-agents-python/tracing/)
- 为什么这个来源重要：它提供了 trace / span / metadata 的另一套官方语境，能帮助你避免把 trace 只绑定到某一个框架上理解。课程希望你把 trace 看成通用 runtime 能力，而不是某个生态的私有术语。
- 这个来源原本在解决什么问题：
  - 如何给一次 agent 运行建立 trace
  - 如何给步骤或子任务建立 span
  - 如何记录 metadata，支持事后比较、归因和调试
- 你应该从原文里抓到的核心原理：
  - trace 的本质是跨步骤保留上下文。
  - span 的本质是给步骤边界命名。
  - metadata 的本质是让你后面能够比较不同运行、不同版本、不同实验条件。
- 本教程吸收成了哪些内容：
  - 第 04 模块里对 trace 字段的强调
  - `request id / run id / node name / elapsed time / experiment tag` 这些思路
  - 为什么后续 eval 会需要 trace 和 metadata 一起配合
- 读原文时重点看什么：
  - trace
  - span
  - metadata
  - 为什么这些对象不是“额外附加字段”
- 读完后你应该能回答：
  - 为什么不记录 metadata 就很难做版本比较
  - 为什么 trace 和 eval 最终会产生协同关系

## 4. [OpenTelemetry Python Instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/)
- 为什么这个来源重要：它给你 tracing 的通用工程语言。课程里虽然会结合 agent / workflow 来讲 trace，但如果你只在 agent 框架语境下理解它，很容易把 trace 看成专有概念。OpenTelemetry 让你知道：trace 是通用工程能力，只是在 agent 系统里更刚需。
- 这个来源原本在解决什么问题：
  - 什么是 trace / span / context
  - 如何通过 attribute 描述步骤信息
  - 如何把单次运行拆成有结构的过程
- 你应该从原文里抓到的核心原理：
  - trace 是过程模型，不是日志升级版。
  - 结构化过程记录，是定位复杂系统问题的通用方法。
  - agent 场景只是把这件事的重要性放大了。
- 本教程吸收成了哪些内容：
  - 第 00 模块里对证据和过程的强调
  - 第 04 模块里对 `trace != log` 的专门拆解
  - 为什么课程里一直要求“失败要落回具体步骤”
- 读原文时重点看什么：
  - span
  - attribute
  - context
  - 为什么跨步骤关联比单条日志更重要
- 读完后你应该能回答：
  - 为什么 agent runtime 需要工程级 tracing 思维
  - 为什么 process visibility 是长期维护能力，不是一次性调试技巧

## 5. [FastAPI Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/)
- 为什么这个来源重要：它帮助你理解哪些工作应该阻塞请求，哪些工作更适合后台执行。对本模块来说，这个问题很实在，因为 eval、回归比较、某些观察任务，并不总适合同步挂在主请求链路上。
- 这个来源原本在解决什么问题：
  - 请求处理和后台工作的边界
  - 什么任务适合异步/延后执行
  - 如何避免主请求承担过多治理型任务
- 你应该从原文里抓到的核心原理：
  - 并不是所有系统治理动作都应该阻塞主流程。
  - 同步路径和后台治理路径应该分开思考。
  - workflow runtime 不只是一条请求链，也可能伴随异步观察和评测行为。
- 本教程吸收成了哪些内容：
  - `eval runner` 这类能力更适合做成独立流程的判断
  - 第 04 模块中“生产化不是把一切塞进同步请求”的思路
  - 后面第 06 模块里“展示资产”和主服务分开的组织意识
- 读原文时重点看什么：
  - 请求生命周期
  - 后台任务边界
  - 哪些事不该阻塞主响应
- 读完后你应该能回答：
  - 为什么某些评测和治理动作更适合异步化
  - 为什么 production-like system 往往不止一条同步调用链

## 这一页真正想帮你建立什么
- workflow、observability、eval 不是三块零散知识，而是系统治理闭环
- 你回看这些来源时，应该一直问：它是在帮助我显式流程、显式过程，还是显式比较
- 真正的工程化，不是把系统做得更花，而是让系统更可理解、更可回放、更可比较

## 读完这一页后回到哪里
- 如果你想回到主线：返回 [study-map.md](../study-map.md)
- 如果你想继续执行：去 [steps.md](../steps.md)
- 如果你想重新回顾概念：去 [01-concepts-and-principles.md](./01-concepts-and-principles.md)
