# 00 总览与准备 原始来源与出处详解

[返回学习地图](../study-map.md) | [返回模块首页](../README.md) | [上一篇：03-code-reading-guide.md](./03-code-reading-guide.md) | [下一篇：05-common-mistakes.md](./05-common-mistakes.md)

这一页不是“链接仓库”，而是本模块的出处细读讲义。它回答的是 4 个问题：
- 为什么这个来源值得放进课程
- 它原本在解决什么问题
- 本教程把它吸收成了哪些判断
- 你回去看原始资料时，应该重点抓什么

你可以把这一页理解成“我替你先读一遍，然后告诉你该带着什么问题回去看原文”。

## 怎么使用这一页
- 先读完 `01-concepts-and-principles.md` 和 `02-deep-dive.md`，再来看这里。
- 这一页的目标不是替代原始资料，而是让你看原文时不迷路。
- 每个来源我都会讲“它的原始语境”和“它在本教程里的落点”，这样你不会只记住链接名。

## 1. [OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses/list?lang=python)
- 为什么这个来源重要：这个来源的重要性在于，它体现了模型接口已经从“给我一段文本”演进成“返回一个可结构化处理的响应对象”。这对整套课程非常关键，因为后面无论是 structured output、tool calling，还是 trace / eval，前提都是你不再把模型响应当成一段纯文本。
- 这个来源原本在解决什么问题：
  - 如何统一不同模型能力的调用入口
  - 如何把文本、结构化内容和工具动作放进一个共同响应模型
  - 如何让上层应用在面对更复杂模型能力时仍然有相对稳定的接口心智
- 你应该从原文里抓到的核心原理：
  - 响应对象不是“结果字符串”，而是系统对象。
  - 模型输出开始具备机器可消费性，而不仅仅是人类可阅读性。
  - 一旦你接受这个前提，后面课程里的 provider、schema、tool result 就都顺了。
- 本教程吸收成了哪些内容：
  - `00-overview/resources/01-concepts-and-principles.md` 里对“模型接口层”的定义
  - 第 01 模块中对 structured output 的强调
  - 后续所有模块里“输出要能进入系统而不是只给人看”的判断
- 读原文时重点看什么：
  - 响应对象的组织方式
  - 结构化内容和普通文本共存的方式
  - 为什么接口被设计成“统一响应对象”而不是一堆零散特性
- 读完后你应该能回答：
  - 为什么 agent 系统不能再把模型当成简单字符串生成器
  - 为什么模型响应接口的结构，会直接影响后面的 runtime 设计

## 2. [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- 为什么这个来源重要：课程里的所有综合服务都需要一个最小服务壳。FastAPI 在这套课程里的作用，不是“框架教学”，而是让你快速拥有一个边界清晰、测试友好的 HTTP 层。
- 这个来源原本在解决什么问题：
  - 如何把请求、响应、参数校验和路由组织成清晰的 API 层
  - 如何让服务接口和内部逻辑分离
  - 如何在 Python 里比较自然地表达 request/response schema
- 你应该从原文里抓到的核心原理：
  - route 的职责是协议边界，不是业务编排。
  - request model / response model 是契约，不只是样例。
  - 测试友好的 API 层，会显著降低后续 agent 功能接入的混乱度。
- 本教程吸收成了哪些内容：
  - `00-overview/examples/` 和 `module-service/` 中统一的服务入口风格
  - 第 01 模块里 route / service / provider 的分层
  - 后面模块里所有“先把能力接成服务，再谈复杂功能”的做法
- 读原文时重点看什么：
  - path operation
  - request body / response model
  - testing 的最小模式
- 不必现在深挖什么：
  - 安全、部署、中间件、复杂依赖注入都可以暂时不展开
- 读完后你应该能回答：
  - 为什么这套课不把例子写成纯脚本
  - 为什么服务边界对 agent infra 学习很重要

## 3. [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
- 为什么这个来源重要：很多人直到系统开始变复杂，才意识到配置治理的重要性。但 agent infra 的参数面特别广，如果一开始不建立配置中心，后面会非常难复现和比较实验结果。
- 这个来源原本在解决什么问题：
  - 如何把环境变量和配置字段统一收口
  - 如何用结构化对象管理运行参数
  - 如何让配置成为系统的一部分，而不是散落在代码角落
- 你应该从原文里抓到的核心原理：
  - 配置对象不是“方便取值”，而是“稳定系统边界”。
  - 配置必须集中，才能做实验复现、版本对比和问题回放。
  - 模型名、超时、开关、检索参数这类东西，越早结构化越好。
- 本教程吸收成了哪些内容：
  - `00-overview/examples/01-settings-and-logging` 的设计
  - 各模块 `module-service/.env.example` 的组织方式
  - 第 04 模块里“不要只靠感觉比较系统变化”的证据意识
- 读原文时重点看什么：
  - `BaseSettings` 的职责
  - env file 和字段映射
  - 为什么配置应该统一入口
- 读完后你应该能回答：
  - 为什么配置治理不是“最后再整理”
  - 为什么课程一开始就要求主项目有统一配置骨架

## 4. [OpenTelemetry Python Instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/)
- 为什么这个来源重要：它给你 tracing 的通用语言。课程后面当然会进入 agent trace、run metadata、节点路径这些更具体的内容，但如果没有一个通用 tracing 视角，你很容易把 trace 错当成“更详细的日志”。
- 这个来源原本在解决什么问题：
  - 如何把一次请求拆成多个可追踪步骤
  - 如何给步骤挂 attribute / metadata
  - 如何在系统层面重建一次执行过程
- 你应该从原文里抓到的核心原理：
  - trace 是过程模型，不是日志加强版。
  - span 的价值是给步骤边界命名并记录上下文。
  - 一旦系统有多步调用、工具调用、检索、回退，日志就不够了。
- 本教程吸收成了哪些内容：
  - 第 00 模块中“证据先于感觉”的思路
  - 第 04 模块里对 workflow / trace / eval 闭环的建立
  - 后续所有“失败要能回放到具体步骤”的要求
- 读原文时重点看什么：
  - trace / span / attribute 的基本概念
  - 为什么需要结构化步骤视角
  - 为什么跨步骤关联比单点日志更重要
- 现在不用硬学什么：
  - 完整的 SDK 接入细节可以等到第 04 模块再补
- 读完后你应该能回答：
  - 为什么 agent 系统里 trace 比普通 Web 应用更关键
  - 为什么后面课程会反复强调“过程证据”

## 这一页真正想帮你建立什么
- 外部资料不是主教程，而是课程判断的出处
- 每个来源都应该被翻译成“系统层次、边界和设计理由”
- 你不是为了记住链接而读这些来源，而是为了让自己的工程判断更稳

## 读完这一页后回到哪里
- 如果你想回到主线：返回 [study-map.md](../study-map.md)
- 如果你想继续执行：去 [steps.md](../steps.md)
- 如果你想重新回顾概念：去 [01-concepts-and-principles.md](./01-concepts-and-principles.md)
