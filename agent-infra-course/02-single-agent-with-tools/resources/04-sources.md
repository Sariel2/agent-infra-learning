# 02 单 Agent 与 Tools 原始来源与出处详解

[返回学习地图](../study-map.md) | [返回模块首页](../README.md) | [上一篇：03-code-reading-guide.md](./03-code-reading-guide.md) | [下一篇：05-common-mistakes.md](./05-common-mistakes.md)

这一页要解决的不是“你该收藏哪些链接”，而是帮你理解：本模块里关于 tool schema、agent loop、observation、fallback 的判断，分别来自哪些外部语境。你看完之后，回头再看官方资料，会更容易把它们读成工程问题，而不是功能清单。

## 怎么使用这一页
- 先把本模块正文读完，再看这一页。
- 看原文时，不要只盯着 API 长什么样，要问“它在治理哪类不确定性”。
- 每个来源最重要的不是接口细节，而是它背后的边界意识。

## 1. [OpenAI Tools Guide](https://platform.openai.com/docs/guides/tools)
- 为什么这个来源重要：这是本模块最关键的一手出处，因为它把 tool calling 正式表述成“模型生成结构化动作，再由系统执行”的能力，而不是“模型帮你随便调个函数”。
- 这个来源原本在解决什么问题：
  - 如何声明工具
  - 如何让模型生成工具动作
  - 如何把工具执行结果回送给模型或上层逻辑
  - 如何把工具能力变成接口契约的一部分
- 你应该从原文里抓到的核心原理：
  - tool calling 的核心是动作契约，而不是函数名本身。
  - 模型不是真的“执行函数”，它是在生成一个结构化意图。
  - 一旦动作是结构化生成，schema、校验、trace、fallback 就都变得必要。
- 本教程吸收成了哪些内容：
  - `tool schema 比 prompt 更值得先做`
  - `ToolResult` 和 observation 的统一包装
  - 第 02 模块里把失败拆成选错工具 / 参数错误 / 执行失败三类
- 读原文时重点看什么：
  - tools 声明方式
  - 参数结构
  - 工具调用生命周期
  - 为什么返回结果也需要被系统化处理
- 读完后你应该能回答：
  - 为什么 tool calling 不等于普通函数调用
  - 为什么没有 schema 就很难谈稳定 agent

## 2. [OpenAI Agents SDK](https://platform.openai.com/docs/guides/agents-sdk/)
- 为什么这个来源重要：它能把课程里的最小单 agent loop 放进一个更成熟 runtime 的语境里。课程故意先用小实现显影结构，而这个来源能帮助你理解：成熟 runtime 为什么会组织出 agent、tool、handoff、trace 这些概念。
- 这个来源原本在解决什么问题：
  - 如何把 agent 定义成一个可运行单元
  - 如何把 tools、handoff、trace 放进统一 runtime 里
  - 如何让 agent 行为不只是 prompt 拼接，而是运行时编排问题
- 你应该从原文里抓到的核心原理：
  - agent 不是“更长的 prompt”，而是带状态、带工具、带轨迹的运行单元。
  - runtime 的存在，是为了把模型动作放进可治理框架里。
  - trace 不是附属品，而是 agent 系统的核心证据。
- 本教程吸收成了哪些内容：
  - `最小 loop` 和 `成熟 runtime` 的对比
  - 为什么课程先手写最小 loop，再带你看框架语境
  - 第 04 模块里 workflow / trace / eval 的后续延伸
- 读原文时重点看什么：
  - agent
  - tool
  - handoff
  - tracing
- 当前不必强行掌握什么：
  - 框架级别的完整 API 细节
- 读完后你应该能回答：
  - 为什么课程示例没有直接照抄成熟 runtime
  - 为什么理解 runtime 组织方式比记框架 API 更重要

## 3. [OpenAI File Search section](https://platform.openai.com/docs/guides/tools-file-search)
- 为什么这个来源重要：虽然本模块重点不是 RAG，但它很好地展示了“平台托管工具”是什么感觉。它能帮助你区分三种东西：
  - custom tool
  - platform built-in tool
  - 完全外部系统能力
- 这个来源原本在解决什么问题：
  - 如何让平台提供的检索能力作为一种工具接入
  - 如何减少开发者自己实现底层检索链路的负担
  - 如何把某类能力做成更高层的托管工具
- 你应该从原文里抓到的核心原理：
  - built-in tool 的价值是降低起步复杂度。
  - 但 built-in tool 通常也意味着你放弃一部分底层控制力。
  - custom tool 更适合帮助你理解 infra 本身是怎么工作的。
- 本教程吸收成了哪些内容：
  - 讲义里对 built-in tool vs custom tool 的区分
  - 第 03 模块里 hosted retrieval vs self-hosted retrieval 的铺垫
  - 为什么课程在单 agent 阶段先强调自定义工具
- 读原文时重点看什么：
  - 托管能力的边界
  - 平台帮你做掉了哪些事
  - 你因此失去了哪些可控点
- 读完后你应该能回答：
  - 为什么“更省事”不一定等于“更适合入门 infra”
  - 为什么课程会故意保留一些自己实现的部分

## 4. [PydanticAI](https://ai.pydantic.dev/)
- 为什么这个来源重要：它最有价值的地方，不是让你现在立刻换框架，而是帮助你看到“类型系统如何帮助 agent 和工具减少不确定性”。
- 这个来源原本在解决什么问题：
  - 如何用类型和 schema 约束 agent 输入输出
  - 如何让工具参数更收紧
  - 如何减少“能跑但边界模糊”的情况
- 你应该从原文里抓到的核心原理：
  - 类型系统不是教条，它能直接降低 agent 调用不确定性。
  - schema 约束越明确，后面的 trace、测试、eval 越容易稳定。
  - 工具调用最怕“看起来大差不差”，类型化能减少这种灰区。
- 本教程吸收成了哪些内容：
  - 本模块对 `ToolResult` 和参数边界的强调
  - 为什么课程持续要求输入输出对象化
  - 第 05 模块里“复杂度控制”背后的类型化思维
- 读原文时重点看什么：
  - 类型化 agent 思路
  - 工具声明和约束方式
  - 为什么 schema 收紧能改善稳定性
- 读完后你应该能回答：
  - 为什么很多 agent 问题最后都能追到边界不清
  - 为什么类型约束不是为了“写得漂亮”，而是为了减少治理成本

## 这一页真正想帮你建立什么
- tool calling 是“模型动作治理”问题，不是“函数调用增强”问题
- 官方 runtime、平台托管工具、类型化框架，其实都在解决不确定性治理
- 你回看这些来源时，应该一直问：它帮我把哪一层不确定性收紧了

## 读完这一页后回到哪里
- 如果你想回到主线：返回 [study-map.md](../study-map.md)
- 如果你想继续执行：去 [steps.md](../steps.md)
- 如果你想重新回顾概念：去 [01-concepts-and-principles.md](./01-concepts-and-principles.md)
