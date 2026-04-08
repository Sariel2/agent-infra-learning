# 02 单 Agent 与 Tools 冲刺日历

这一页帮助你把单 agent 学习拆成一周可执行节奏。这里的核心不是多写几个工具，而是把工具 schema、loop、trace 和失败分类逐层看清。

## 推荐投入
- 总时长：`8-12 小时`
- 推荐拆法：`5 次学习，每次 90-150 分钟`
- 最低保底：如果时间紧，至少完成 `Session 1 + Session 2 + Session 4`

## Session 1：先把工具调用边界看清
- 建议时长：`90 分钟`
- 只做这几件事：
  - 读 [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
  - 读 [resources/05-common-mistakes.md](./resources/05-common-mistakes.md)
- 本次目标：
  - 明确 tool calling 不等于普通函数调用
- 本次产出：
  - 1 条“schema 比 prompt 更值得先治理”的说明

## Session 2：把三类失败和恢复策略想透
- 建议时长：`90 分钟`
- 只做这几件事：
  - 读 [resources/02-deep-dive.md](./resources/02-deep-dive.md)
  - 看 [resources/04-sources.md](./resources/04-sources.md)
- 本次目标：
  - 会拆解选错工具、参数错误、执行失败
- 本次产出：
  - 1 张失败分类表

## Session 3：跑 schema 和 loop 两个 example
- 建议时长：`120-150 分钟`
- 只做这几件事：
  - 跑 `examples/01-tool-schema`
  - 跑 `examples/02-agent-loop`
  - 各做 1 个小改动
- 本次目标：
  - 把工具契约和最小 loop 真的跑一遍
- 本次产出：
  - 1 个新字段或新工具
  - 1 次 trace 变化观察

## Session 4：读懂 support-agent 综合服务
- 建议时长：`120-150 分钟`
- 只做这几件事：
  - 读 [project.md](./project.md)
  - 跑 `support-agent`
  - 对照 code reading guide 看 `ToolTrace` 和 `run_agent()`
- 本次目标：
  - 把 schema、loop 和 trace 串成一个小型运行时
- 本次产出：
  - 1 份 support-agent 结构说明
  - 1 条你最想补的恢复策略

## Session 5：复盘并进入 RAG 链路
- 建议时长：`60-90 分钟`
- 只做这几件事：
  - 做 [review.md](./review.md)
  - 看 [03-rag-memory-and-knowledge/steps.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/03-rag-memory-and-knowledge/steps.md)
- 本次目标：
  - 把工具调用经验沉淀成下个模块的知识入口
- 本次产出：
  - 1 份复盘
  - 1 份进入 RAG 模块前的迁移点

## 时间不够时怎么保底
- 最少完成：
  - `Session 1`
  - `Session 2`
  - `Session 4`
- 可暂时压缩：
  - Session 3 中第二个 example 的深度改造

## 本模块结束标志
- 你已经能把工具调用看成可治理过程
- 你已经准备好进入 retrieval 和 memory 模块
