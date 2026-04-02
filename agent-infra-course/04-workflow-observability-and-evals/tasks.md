# 04 Workflow、Observability 与 Evals任务安排

## Day 1：编排重构
- 把前面分散的 agent 流程画成状态图
- 用 `LangGraph` 或同类编排方式重构主流程
- 区分固定节点和模型决策节点

## Day 2：状态与分支
- 为流程定义 state
- 增加条件分支
- 预留人工审核节点或手动中断节点

## Day 3：接 tracing
- 记录每次运行的 trace id
- 给关键节点加 metadata
- 记录模型耗时、工具耗时、检索耗时

## Day 4：建立 eval
- 准备一组固定任务集
- 定义 success rate、citation quality、latency、cost
- 跑第一次基线评测

## Day 5：失败分析与回归
- 选 5 个失败 case 做归因
- 调整 1-2 个关键节点
- 再跑一次回归评测

## 退出条件
- 有一份可重复运行的评测集
- 至少能比较两次结果
- 出现失败时能定位到具体节点
