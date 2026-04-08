# 03 RAG、Memory 与 Knowledge 冲刺日历

这一页把 RAG 模块拆成一周节奏，重点不是让你一口气学完整个检索生态，而是先把检索、citation、memory 和失败分析稳定走一遍。

## 推荐投入
- 总时长：`8-12 小时`
- 推荐拆法：`5 次学习，每次 90-150 分钟`
- 最低保底：如果时间紧，至少完成 `Session 1 + Session 3 + Session 5`

## Session 1：先把链路和边界看清
- 建议时长：`90 分钟`
- 只做这几件事：
  - 读 [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
  - 读 [resources/05-common-mistakes.md](./resources/05-common-mistakes.md)
- 本次目标：
  - 建立 retrieval / memory / citation 边界
- 本次产出：
  - 1 条“RAG 不是向量库”的解释

## Session 2：把故障层次和来源语境对齐
- 建议时长：`90 分钟`
- 只做这几件事：
  - 读 [resources/02-deep-dive.md](./resources/02-deep-dive.md)
  - 看 [resources/04-sources.md](./resources/04-sources.md)
- 本次目标：
  - 会拆检索层、拼接层、回答层问题
- 本次产出：
  - 1 张故障层次表

## Session 3：跑 retrieval 和 memory 两个 example
- 建议时长：`120-150 分钟`
- 只做这几件事：
  - 跑 `examples/01-local-retrieval`
  - 跑 `examples/02-short-term-memory`
  - 各做 1 个小改动
- 本次目标：
  - 把 citation 和有界记忆真的看成系统对象
- 本次产出：
  - 1 次排序变化观察
  - 1 次 memory 窗口变化观察

## Session 4：读懂 knowledge-agent 综合服务
- 建议时长：`120-150 分钟`
- 只做这几件事：
  - 读 [project.md](./project.md)
  - 跑 `knowledge-agent`
  - 对照 code reading guide 看 `retrieve()` / `ask()`
- 本次目标：
  - 把知识、citation、memory 串成最小知识服务
- 本次产出：
  - 1 份知识服务结构说明
  - 1 条最影响效果的参数记录

## Session 5：失败分析和交接到 runtime 模块
- 建议时长：`60-90 分钟`
- 只做这几件事：
  - 做 [review.md](./review.md)
  - 看 [04-workflow-observability-and-evals/steps.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/04-workflow-observability-and-evals/steps.md)
- 本次目标：
  - 把本模块经验沉淀成后面 workflow / trace / eval 的输入
- 本次产出：
  - 1 份失败归因记录
  - 1 份 runtime 模块进入前迁移点

## 时间不够时怎么保底
- 最少完成：
  - `Session 1`
  - `Session 3`
  - `Session 5`
- 可暂时压缩：
  - Session 4 中 hosted / self-hosted 的扩展比较

## 本模块结束标志
- 你已经把知识问答看成一条可治理链路
- 你已经准备好进入 workflow、trace、eval 模块
