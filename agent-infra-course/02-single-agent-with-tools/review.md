# 02 单 Agent 与 Tools 复盘模板

这一页用来判断：你是真的理解了 tool calling 的工程边界，还是只是让模型“看起来会调几个函数”。第 02 模块最关键的不是功能多少，而是你是否已经开始把工具调用看成可治理过程。

## 什么时候做这页复盘
- 完成 [steps.md](./steps.md) 后做
- 跑过两个 example 和 `support-agent` 后做
- 进入第 03 模块前再回看一次

## 一、模块总结
请先用 5-8 句话回答：
- 为什么 tool schema 比 prompt 更值得先治理
- 为什么 observation 不是普通返回值
- 为什么 trace 在单 agent 阶段就必须存在
- 为什么 timeout / retry / fallback 不是一回事

如果写不顺，优先回看：
- [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
- [resources/02-deep-dive.md](./resources/02-deep-dive.md)

## 二、自查清单
逐条回答 `是 / 否 / 部分做到`，并补一句证据。

- 我是否已经能区分 tool schema 和 prompt 的职责
- 我是否知道工具结果为什么必须统一结构
- 我是否能解释一次最小 agent loop 的 5 个步骤
- 我是否能把失败分成选错工具、参数错误、执行失败三类
- 我是否已经在返回结果里保留 trace
- 我是否还把“能跑起来”误当成“设计没问题”

## 三、失败归因表
把你遇到的工具调用问题尽量归到正确层。

| 现象 | 更可能的问题层 | 根因猜测 | 下一步动作 |
|---|---|---|---|
| 工具总是选错 | 决策层 | schema 描述或分类边界不清 | 回看 `choose_tool()` 和 tools guide |
| 参数经常缺失或非法 | 参数层 | schema 太松 / 约束不足 | 回看 `ToolCall`、字段约束和测试 |
| 工具执行失败后系统直接崩 | 执行层 | result wrapper 和恢复策略不足 | 回看 `ToolResult` / `ToolTrace` |
| 回答看起来对，但看不出过程 | 观测层 | trace 没有被稳定保留 | 回看 `StepTrace` 和 `ToolTrace` |

## 四、常见坑对照
看看你是否已经踩中以下任一项。

- 把所有事情都交给模型自由决定
- 只写 prompt，不治理 schema
- 工具返回结构各不相同
- 把所有失败都归结成“agent 不稳定”
- trace 里只剩一个最终结果，没有过程信息

如果踩中了，请写：
- 我踩中了哪一条
- 它让系统出现了什么不稳定现象
- 我下一步准备怎样收紧边界

## 五、最小输出模板
请至少填完下面 6 项：

- 我现在最稳定的 1 条工具边界判断：
- 我最常遇到的 1 类工具失败：
- 我准备怎样识别选错工具和执行失败的区别：
- 当前 trace 最缺的 1 个字段：
- 如果再做一次 schema，我会优先加哪类约束：
- 进入 RAG 模块前，我需要保留的 1 条工程习惯：

## 六、通过标准
满足下面这些条件，才算真的可以进入第 03 模块。

- 我已经能解释最小 agent loop
- 我已经能稳定区分 3 类工具失败
- 我知道 trace 为什么必须从早期就建立
- 我能说清 custom tool 和 built-in tool 的差异
- 我知道 observation 为什么会影响后续状态

## 七、下一步行动
从下面 3 个动作里，至少写 1 个马上要执行的动作。

- 打开 [03-rag-memory-and-knowledge/steps.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/03-rag-memory-and-knowledge/steps.md)，开始 RAG 模块
- 给当前 `support-agent` 增加 1 条更细的 trace 字段
- 复写 1 个工具结果，让它变成统一 `ToolResult` 风格
