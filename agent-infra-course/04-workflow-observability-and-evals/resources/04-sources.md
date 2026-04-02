# 04 Workflow、Observability 与 Evals 原始来源与出处详解

[返回学习地图](../study-map.md) | [返回模块首页](../README.md) | [上一篇：03-code-reading-guide.md](./03-code-reading-guide.md) | [下一篇：05-common-mistakes.md](./05-common-mistakes.md)


这一页不是“链接仓库”，而是本模块讲义的出处解释页。你可以把它理解成：我为什么引用这些来源、这些来源里最值得看的部分是什么、以及这些内容在本教程里被翻译成了哪一段讲义。

## 怎么使用这一页
- 先把本模块前面的讲义读完，再来看这里。
- 看每个来源时，不要试图通读整站，只看这里标出的重点。
- 把这一页当成“出处说明 + 精读提示”，不是新的主教程。

## 1. [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview)
- 为什么这个来源重要：它最重要的价值在于把 workflow / orchestration / stateful runtime 明确成一类问题，而不是零散技巧。
- 建议重点看：
  - 重点看 state、node、edge、conditional routing
  - 把阅读重点放在“为什么需要显式流程图”
- 它在本教程里的对应位置：对应本模块讲义里“workflow 必须显式存在”和 `01-stateful-workflow` example。
- 我从原文里提炼出的关键结论：
  - workflow 的价值是把步骤、状态和分支显式建模。
  - 它不是为了取代 agent，而是为了约束系统复杂度。

## 2. [LangSmith Observability](https://docs.langchain.com/oss/python/langgraph/observability)
- 为什么这个来源重要：它能帮助你直观看到“运行过程可见”到底意味着什么。
- 建议重点看：
  - 看 graph run、节点执行、状态变化的观测方式
  - 重点理解过程视角
- 它在本教程里的对应位置：对应本模块里“trace 不是更详细的日志”这部分。
- 我从原文里提炼出的关键结论：
  - 过程可见性决定了你能否定位问题。
  - 如果只能看到最终答案，很多错误根本无法归因。

## 3. [OpenAI Agents SDK Tracing](https://openai.github.io/openai-agents-python/tracing/)
- 为什么这个来源重要：它提供了 trace / span 的另一套官方语境，帮助你避免把 trace 绑定在单一框架里理解。
- 建议重点看：
  - 看 trace、span、metadata 的概念
  - 不要求现在完全掌握 SDK 细节
- 它在本教程里的对应位置：对应本模块对 trace 字段和元数据的讲解。
- 我从原文里提炼出的关键结论：
  - trace 的价值是跨步骤保留结构化上下文。
  - 元数据决定了后续能否做横向比较和归因。

## 4. [OpenTelemetry Python Instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/)
- 为什么这个来源重要：它给你 tracing 的通用基础语言，让你知道 trace 不是某个 agent 框架独有的概念。
- 建议重点看：
  - 理解 span、attribute、context 的通用含义
  - 把注意力放在“我到底在记录什么”
- 它在本教程里的对应位置：对应本模块的 trace 原理部分。
- 我从原文里提炼出的关键结论：
  - trace 是通用工程能力，在 agent 系统里只是变得更重要。

## 5. [FastAPI Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/)
- 为什么这个来源重要：它帮助你理解哪些工作应该阻塞请求，哪些工作更适合后台执行，例如评测或离线比较。
- 建议重点看：
  - 理解请求生命周期和后台任务边界
- 它在本教程里的对应位置：对应本模块对 eval runner 和后台验证方向的延伸思考。
- 我从原文里提炼出的关键结论：
  - 并不是所有评测、比较和治理逻辑都适合放在同步请求里。

## 读完这一页后回到哪里
- 如果你想回到主线：返回 [study-map.md](../study-map.md)
- 如果你想继续执行：去 [steps.md](../steps.md)
- 如果你想重新回顾概念：去 [01-concepts-and-principles.md](./01-concepts-and-principles.md)
