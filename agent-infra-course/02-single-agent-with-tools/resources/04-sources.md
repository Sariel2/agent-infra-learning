# 02 单 Agent 与 Tools 原始来源与出处详解

[返回学习地图](../study-map.md) | [返回模块首页](../README.md) | [上一篇：03-code-reading-guide.md](./03-code-reading-guide.md) | [下一篇：05-common-mistakes.md](./05-common-mistakes.md)


这一页不是“链接仓库”，而是本模块讲义的出处解释页。你可以把它理解成：我为什么引用这些来源、这些来源里最值得看的部分是什么、以及这些内容在本教程里被翻译成了哪一段讲义。

## 怎么使用这一页
- 先把本模块前面的讲义读完，再来看这里。
- 看每个来源时，不要试图通读整站，只看这里标出的重点。
- 把这一页当成“出处说明 + 精读提示”，不是新的主教程。

## 1. [OpenAI Tools Guide](https://platform.openai.com/docs/guides/tools)
- 为什么这个来源重要：这是本模块最关键的官方出处，因为它说明了工具声明、参数生成和调用回传在现代模型接口里是怎样被正式组织的。
- 建议重点看：
  - 重点看 tools 的声明方式
  - 理解 tool calling 的生命周期
  - 把注意力放在“动作是结构化生成”而不是“像函数那样调用”
- 它在本教程里的对应位置：对应本模块讲义里“tool schema 比 prompt 更值得先做”的部分。
- 我从原文里提炼出的关键结论：
  - tool calling 的核心是动作契约，而不是函数名本身。
  - 如果 schema 松散，后面 trace、fallback、eval 都会受影响。

## 2. [OpenAI Agents SDK](https://platform.openai.com/docs/guides/agents-sdk/)
- 为什么这个来源重要：它帮助你把课程中的最小单 agent loop 放到更成熟 runtime 的语境里理解。
- 建议重点看：
  - 看 agent、tool、handoff 和 trace 相关概念
  - 不要一开始就被框架细节淹没
- 它在本教程里的对应位置：对应本模块讲义中“最小 loop”和“成熟 runtime”的对比。
- 我从原文里提炼出的关键结论：
  - 课程示例是为了显影结构，不是为了替代成熟 runtime。
  - 理解官方 runtime 的组织方式，有助于你判断哪些能力应该自己实现，哪些适合交给框架。

## 3. [OpenAI File Search section](https://platform.openai.com/docs/guides/tools-file-search)
- 为什么这个来源重要：虽然本模块重点不是 RAG，但它展示了 built-in tools 的一种典型形态，能帮助你区分平台工具和自定义工具。
- 建议重点看：
  - 看工具能力被平台托管时的使用方式
  - 重点理解边界，而不是马上上 RAG
- 它在本教程里的对应位置：对应讲义里“built-in tool 与 custom tool 的区别”。
- 我从原文里提炼出的关键结论：
  - 平台托管工具能快速得到能力，但自定义工具更有助于理解 infra。

## 4. [PydanticAI](https://ai.pydantic.dev/)
- 为什么这个来源重要：这个来源最有价值的地方，不是让你马上换框架，而是帮助你看到“类型系统能怎样帮助 agent 和工具减少不确定性”。
- 建议重点看：
  - 看类型化 agent 与工具声明的思路
  - 重点理解 schema 收紧如何改善稳定性
- 它在本教程里的对应位置：对应本模块对 schema 和 ToolResult 的强调。
- 我从原文里提炼出的关键结论：
  - 类型系统不是教条，它能直接降低工具调用不确定性。

## 读完这一页后回到哪里
- 如果你想回到主线：返回 [study-map.md](../study-map.md)
- 如果你想继续执行：去 [steps.md](../steps.md)
- 如果你想重新回顾概念：去 [01-concepts-and-principles.md](./01-concepts-and-principles.md)
