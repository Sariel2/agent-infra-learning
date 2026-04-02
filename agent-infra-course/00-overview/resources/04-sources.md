# 00 总览与准备 原始来源与出处详解

[返回学习地图](../study-map.md) | [返回模块首页](../README.md) | [上一篇：03-code-reading-guide.md](./03-code-reading-guide.md) | [下一篇：05-common-mistakes.md](./05-common-mistakes.md)


这一页不是“链接仓库”，而是本模块讲义的出处解释页。你可以把它理解成：我为什么引用这些来源、这些来源里最值得看的部分是什么、以及这些内容在本教程里被翻译成了哪一段讲义。

## 怎么使用这一页
- 先把本模块前面的讲义读完，再来看这里。
- 看每个来源时，不要试图通读整站，只看这里标出的重点。
- 把这一页当成“出处说明 + 精读提示”，不是新的主教程。

## 1. [OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses/list?lang=python)
- 为什么这个来源重要：这个来源的重要性在于，它体现了模型响应接口已经从“只返回文本”演进到了“结构化输出、工具调用、统一响应对象”的主路径。
- 建议重点看：
  - 先看响应对象的基本结构
  - 理解响应中“内容”和“工具/结构化输出”如何共存
  - 只建立接口心智，不必现在深挖所有参数
- 它在本教程里的对应位置：对应本教程里“什么是 agent infra”以及后续所有 provider 和 structured output 的基础认知。
- 我从原文里提炼出的关键结论：
  - 模型接口正在统一化，后面学到的 structured output 与 tools 不是孤立功能。
  - 如果一开始就把模型调用理解成“只拿一段文本”，后面会很难理解 agent runtime。
  - 课程后续所有模块都默认你接受“响应是可结构化的系统对象”这个前提。

## 2. [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- 为什么这个来源重要：它说明了为什么课程里的综合服务都选用 FastAPI 作为最小服务壳：边界清晰、约束适中、测试友好。
- 建议重点看：
  - 读 path operation 和 request/response model 的基础部分
  - 读 testing 的最小用法
  - 不需要现在深入 security、middleware 等扩展主题
- 它在本教程里的对应位置：对应本模块 examples 和 module-service 中“先有服务边界，再谈复杂能力”的设计思路。
- 我从原文里提炼出的关键结论：
  - 课程里用 FastAPI 不是为了追框架，而是为了让服务边界足够明确。
  - 学习 agent infra 时，最小 API 壳能帮助你把思路从脚本提升到服务。

## 3. [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
- 为什么这个来源重要：配置治理会贯穿整套课程，后面所有模块都会不断增加模型名、超时、开关、检索参数。
- 建议重点看：
  - 理解 BaseSettings 的职责
  - 看 env file 与字段映射
  - 理解为什么配置应该集中而不是散落
- 它在本教程里的对应位置：对应本模块“先统一工程习惯，再堆能力”的讲义部分。
- 我从原文里提炼出的关键结论：
  - 配置不是后期清理项，而是前期结构项。
  - 没有统一配置对象，后面任何实验都难以复现。

## 4. [OpenTelemetry Python Instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/)
- 为什么这个来源重要：这个来源给你的是 tracing 的通用语言，而不是某个单一框架的专用说法。
- 建议重点看：
  - 只看 trace、span、attribute 基本概念
  - 先理解“一个请求可被拆成多个结构化步骤”
  - 当前模块不需要写埋点代码
- 它在本教程里的对应位置：对应本模块里“日志 != trace”的核心区分。
- 我从原文里提炼出的关键结论：
  - trace 不是日志加强版，而是过程模型。
  - 后面的 observability 模块会回到这里继续展开。

## 读完这一页后回到哪里
- 如果你想回到主线：返回 [study-map.md](../study-map.md)
- 如果你想继续执行：去 [steps.md](../steps.md)
- 如果你想重新回顾概念：去 [01-concepts-and-principles.md](./01-concepts-and-principles.md)
