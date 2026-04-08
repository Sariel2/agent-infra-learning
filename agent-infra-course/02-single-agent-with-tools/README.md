# 02 单 Agent 与 Tools

这个模块开始把“模型输出结构”升级成“模型能决定是否调用工具”。重点是学会 agent loop、tool schema、执行轨迹和失败恢复的最小工程闭环。

## 这个模块解决什么问题
- 为什么 function calling 不等于完整的 agent runtime。
- 为什么 tool schema 设计质量会直接影响 agent 稳定性。
- 为什么 trace 要从这个阶段就开始纳入设计。

## 这一模块的最终产出
- 两个可运行 example：
  [examples/01-tool-schema](./examples/01-tool-schema/README.md)
  [examples/02-agent-loop](./examples/02-agent-loop/README.md)
- 一个最小 `support-agent` 综合服务：
  [module-service/README.md](./module-service/README.md)
- 一套统一的工具轨迹记录思路。

## 推荐学习顺序
1. 先看 [mindmap.md](./mindmap.md)，确认工具调用链路。
2. 再看 [study-map.md](./study-map.md)，明确本模块推进顺序。
3. 按顺序读讲义：
   [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
   [resources/02-deep-dive.md](./resources/02-deep-dive.md)
   [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md)
   [resources/04-sources.md](./resources/04-sources.md)
   [resources/05-common-mistakes.md](./resources/05-common-mistakes.md)
4. 跟着 [steps.md](./steps.md) 跑 example，再做综合服务。
5. 完成 [exercises.md](./exercises.md) 和 [review.md](./review.md)。

## 关键入口
- 学习地图：[study-map.md](./study-map.md)
- 执行剧本：[steps.md](./steps.md)
- 冲刺日历：[tasks.md](./tasks.md)
- 练习手册：[exercises.md](./exercises.md)
- 复盘模板：[review.md](./review.md)
- 综合项目手册：[project.md](./project.md)
- 综合服务实现指导：[module-service/README.md](./module-service/README.md)

## 你在这里最该学会什么
- 把工具设计成稳定契约，而不是“随便返回点文本”。
- 把 agent 的一次执行看成 `决策 -> 调用 -> 观察 -> 返回` 的状态链。
- 把 trace 当作第一等产物，而不是事后补日志。

## 通关标准
- 你能解释为什么坏的 tool schema 会让 agent 更不稳定。
- 你能自己写出一个最小 `answer + trace` 返回结构。
- 你能运行并解释 [module-service/app/service.py](./module-service/app/service.py) 里的三类工具和 `run_agent()`。
- 你能说明哪些场景其实应该收回 workflow，而不是继续增加 agent 自由度。

## 完成后去哪
- 下一站：[03-rag-memory-and-knowledge/README.md](../03-rag-memory-and-knowledge/README.md)
- 进入下一模块前，建议先完成一次本模块综合服务的失败场景复盘。
