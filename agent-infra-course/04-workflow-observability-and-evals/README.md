# 04 Workflow、Observability 与 Evals

这个模块会把课程主线从“能跑”推进到“可定位、可比较、可持续优化”。重点是让 workflow、trace 和 eval 一起成为系统的一部分。

## 这个模块解决什么问题
- 为什么很多 agent demo 一上生产就失控。
- 为什么没有 trace 你很难解释一次失败是怎么发生的。
- 为什么没有固定 eval dataset，你就很难证明系统真的变好了。

## 这一模块的最终产出
- 两个可运行 example：
  [examples/01-stateful-workflow](./examples/01-stateful-workflow/README.md)
  [examples/02-eval-runner](./examples/02-eval-runner/README.md)
- 一个最小 `agent-runtime` 综合服务：
  [module-service/README.md](./module-service/README.md)
- 一套最小 trace 和 eval 基线思路。

## 推荐学习顺序
1. 先看 [mindmap.md](./mindmap.md)，确认 workflow、观测、评测的关系。
2. 再看 [study-map.md](./study-map.md)，明确推进顺序。
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
- 用 workflow 固定该固定的步骤，而不是把一切交给自由 agent。
- 用 trace 看清单次运行的内部路径，而不是只盯最终答案。
- 用 eval 把“感觉更好了”变成“可比较的证据”。

## 通关标准
- 你能解释 log、trace、eval 三者的边界和职责。
- 你能自己设计一个最小 workflow 状态图和最小 trace schema。
- 你能运行并解释 [module-service/app/service.py](./module-service/app/service.py) 里的 `classify_node()`、`run_runtime()` 和 `evaluate()`。
- 你能说清没有固定 dataset 时，为什么优化结论不可信。

## 完成后去哪
- 下一站：[05-agent-theory-and-architecture/README.md](../05-agent-theory-and-architecture/README.md)
- 进入下一模块前，建议先整理一次自己的 trace 观察和 eval 指标。
