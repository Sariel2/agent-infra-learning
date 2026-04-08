# 04 Workflow、Observability 与 Evals 冲刺日历

这一页把第 04 模块拆成一周治理冲刺。重点不是“多画几个流程图”，而是让你真正建立 workflow、trace、eval 的闭环意识。

## 推荐投入
- 总时长：`8-12 小时`
- 推荐拆法：`5 次学习，每次 90-150 分钟`
- 最低保底：如果时间紧，至少完成 `Session 1 + Session 3 + Session 4`

## Session 1：先把治理闭环读懂
- 建议时长：`90 分钟`
- 只做这几件事：
  - 读 [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
  - 读 [resources/05-common-mistakes.md](./resources/05-common-mistakes.md)
- 本次目标：
  - 建立 workflow / trace / eval 三者关系
- 本次产出：
  - 1 条“trace 不是日志加强版”的解释

## Session 2：把过程和比较机制想透
- 建议时长：`90 分钟`
- 只做这几件事：
  - 读 [resources/02-deep-dive.md](./resources/02-deep-dive.md)
  - 看 [resources/04-sources.md](./resources/04-sources.md)
- 本次目标：
  - 明确 trace 元数据和 eval dataset 的作用
- 本次产出：
  - 1 张运行时治理闭环图

## Session 3：跑 workflow 和 eval 两个 example
- 建议时长：`120-150 分钟`
- 只做这几件事：
  - 跑 `examples/01-stateful-workflow`
  - 跑 `examples/02-eval-runner`
  - 各做 1 个小改动
- 本次目标：
  - 把“状态显式化”和“固定样本比较”真正跑一遍
- 本次产出：
  - 1 条新增流程分支
  - 1 条新增 eval case

## Session 4：读懂 agent-runtime 综合服务
- 建议时长：`120-150 分钟`
- 只做这几件事：
  - 读 [project.md](./project.md)
  - 跑 `agent-runtime`
  - 对照 code reading guide 看 `run_runtime()` / `evaluate()`
- 本次目标：
  - 把 workflow、trace、eval 收束成最小 runtime
- 本次产出：
  - 1 份 runtime 结构说明
  - 1 条你最想补的 trace 字段

## Session 5：复盘并交接到 pattern 模块
- 建议时长：`60-90 分钟`
- 只做这几件事：
  - 做 [review.md](./review.md)
  - 看 [05-agent-theory-and-architecture/steps.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/05-agent-theory-and-architecture/steps.md)
- 本次目标：
  - 把运行时治理经验转成后面模式判断的基础
- 本次产出：
  - 1 份复盘
  - 1 份进入 pattern 模块前的复杂度控制提醒

## 时间不够时怎么保底
- 最少完成：
  - `Session 1`
  - `Session 3`
  - `Session 4`
- 可暂时压缩：
  - Session 2 的来源深挖

## 本模块结束标志
- 你已经开始用运行时治理视角看 agent 系统
- 你已经准备好进入 pattern 和架构判断模块
