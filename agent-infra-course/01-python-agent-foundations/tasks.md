# 01 Python 与 Agent 基础 冲刺日历

这一页负责节奏安排，不替代 [steps.md](./steps.md)。如果 `steps.md` 负责告诉你“怎么做”，这里负责告诉你“这一周怎样分配时间最稳”。

## 推荐投入
- 总时长：`8-12 小时`
- 推荐拆法：`5 次学习，每次 90-150 分钟`
- 最低保底：如果时间很紧，至少完成 `Session 1 + Session 3 + Session 5`

## Session 1：把骨架认知立住
- 建议时长：`90 分钟`
- 只做这几件事：
  - 读 [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
  - 读 [resources/02-deep-dive.md](./resources/02-deep-dive.md)
  - 看 [mindmap.md](./mindmap.md)
- 本次目标：
  - 建立 `schema / provider / route / service` 的边界
- 本次产出：
  - 1 份最小服务数据流图
  - 1 条“为什么先 fake 再 real”的说明

## Session 2：把结构化输出跑起来
- 建议时长：`90-120 分钟`
- 只做这几件事：
  - 跑 `examples/01-structured-output`
  - 读对应 `walkthrough.md`
  - 改 1 个字段并修测试
- 本次目标：
  - 真正理解结构化输出是系统契约，不是输出美化
- 本次产出：
  - 1 次 schema 演进记录
  - 1 组测试通过截图或文字记录

## Session 3：把 provider 抽象跑起来
- 建议时长：`90-120 分钟`
- 只做这几件事：
  - 跑 `examples/02-provider-abstraction`
  - 增加 1 个 provider 变体
  - 看 `tests/test_main.py`
- 本次目标：
  - 理解 provider 如何吸收变化
- 本次产出：
  - 1 个新 provider
  - 1 条“切换 provider 为什么不该影响 route”的结论

## Session 4：读懂综合服务 llm-gateway
- 建议时长：`120-150 分钟`
- 只做这几件事：
  - 读 [project.md](./project.md)
  - 跑 `module-service`
  - 对照 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md) 看 service 和 main
- 本次目标：
  - 把 example 里的能力点收束成真正服务骨架
- 本次产出：
  - 1 份 `route -> service -> provider` 说明
  - 1 个你想继续补的边界点

## Session 5：复盘和交接到 tools 模块
- 建议时长：`60-90 分钟`
- 只做这几件事：
  - 读 [resources/04-sources.md](./resources/04-sources.md)
  - 做 [review.md](./review.md)
  - 看 [02-single-agent-with-tools/steps.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/02-single-agent-with-tools/steps.md)
- 本次目标：
  - 把本模块代码、原理、出处和下阶段衔接一次
- 本次产出：
  - 1 份模块复盘
  - 1 份 tools 模块进入前清单

## 时间不够时怎么保底
- 最少完成：
  - `Session 1`
  - `Session 3`
  - `Session 5`
- 可暂时压缩：
  - Session 4 的深入扩展

## 本模块结束标志
- 你已经能读懂最小 Python agent 服务骨架
- 你已经具备进入 tool calling 模块的分层基础
