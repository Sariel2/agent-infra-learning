# 04 Workflow、Observability 与 Evals

这一阶段是从“能跑 demo”走向“接近生产”的关键转折点。你要开始把 Agent 看成一个运行时系统，而不是一次模型调用。

## 阶段目标
- 用 workflow 编排复杂步骤
- 给系统加上 trace 和运行可见性
- 建立基础 eval 体系

## 核心主题
- LangGraph 状态编排
- tracing 与 metadata
- failure analysis
- eval dataset
- latency、cost、quality 指标

## 阶段产出
- 一个 `production-like runtime`
- 一套 trace 记录方式
- 一组 eval case 和回归基线

## 完成标准
- 你能从 trace 里看出流程卡在哪一步
- 你能用数据而不是感觉判断系统质量
- 你能解释 workflow 和自由 agent 的边界
