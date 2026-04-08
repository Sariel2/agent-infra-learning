# 03 RAG、Memory 与 Knowledge

这个模块会把 agent 从“会调工具”推进到“能基于知识回答问题”。重点不是把向量库名词背下来，而是把检索、citation、memory 和失败分析做成工程能力。

## 这个模块解决什么问题
- 为什么 RAG 不等于“接个向量库”。
- 为什么 citation 是质量治理能力，不是页面展示细节。
- 为什么 memory 和 retrieval 的职责边界必须分开。

## 这一模块的最终产出
- 两个可运行 example：
  [examples/01-local-retrieval](./examples/01-local-retrieval/README.md)
  [examples/02-short-term-memory](./examples/02-short-term-memory/README.md)
- 一个最小 `knowledge-agent` 综合服务：
  [module-service/README.md](./module-service/README.md)
- 一份可执行的失败样本记录思路。

## 推荐学习顺序
1. 先看 [mindmap.md](./mindmap.md)，确认知识链路与会话链路。
2. 再看 [study-map.md](./study-map.md)，明确主线。
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
- 把检索链路拆成明确阶段，而不是把一切都归因给“模型没答好”。
- 把 citation 设计成响应的一部分，而不是后补字段。
- 把短期 memory 设计成会话状态，而不是无限回塞历史。

## 通关标准
- 你能完整解释最小 RAG 链路包含哪些步骤。
- 你能分清 `retrieval miss`、`citation mismatch`、`answer drift` 这几类失败。
- 你能运行并解释 [module-service/app/service.py](./module-service/app/service.py) 里的 `retrieve()`、`ask()` 和 `Memory`。
- 你能说明为什么 memory 与 retrieval 不能互相替代。

## 完成后去哪
- 下一站：[04-workflow-observability-and-evals/README.md](../04-workflow-observability-and-evals/README.md)
- 进入下一模块前，建议先把本模块的失败样本和 citation 问题记到 [review.md](./review.md)。
