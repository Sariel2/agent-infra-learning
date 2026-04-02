# Agent Infra Learning Course

这是一个面向后端工程师的 `6 周 Python-first Agent Infra 讲义型教程`。这套教程现在的目标不是把你“引导到外部网页自己学”，而是让你主要通过课程本身的讲义、代码导读、示例和综合服务把知识学透；外部链接只保留为出处和延伸阅读。

## 这套教程怎么学
每个模块都按同一条路径推进：
1. 先读 `README.md` 和 `mindmap.md`
2. 再读 `study-map.md`
3. 按顺序读 `resources/01-*` 到 `resources/05-*`
4. 跟着 `steps.md` 去看具体 example 和 module-service 文件
5. 运行 example，做小改动，重新验证
6. 完成本模块 `module-service/`
7. 做 `exercises.md` 和 `review.md`

## 每个模块里的关键文件
- `study-map.md`：本模块的总学习地图，告诉你先学什么、后学什么
- `steps.md`：逐步执行指南，精确关联资源章节、代码文件和运行命令
- `resources/01-concepts-and-principles.md`：概念、边界、设计原则
- `resources/02-deep-dive.md`：细节、原理、调用链、失败模式
- `resources/03-code-reading-guide.md`：应该先看哪些代码文件，以及每段代码在讲什么
- `resources/04-sources.md`：原始来源链接和用途说明
- `resources/05-common-mistakes.md`：常见误区、症状、修复思路
- `examples/`：知识点级别的可运行示例
- `module-service/`：综合本模块能力的最小服务框架

## 模块列表
- [00-overview](./00-overview/README.md)
- [01-python-agent-foundations](./01-python-agent-foundations/README.md)
- [02-single-agent-with-tools](./02-single-agent-with-tools/README.md)
- [03-rag-memory-and-knowledge](./03-rag-memory-and-knowledge/README.md)
- [04-workflow-observability-and-evals](./04-workflow-observability-and-evals/README.md)
- [05-agent-theory-and-architecture](./05-agent-theory-and-architecture/README.md)
- [06-career-transition-and-interview](./06-career-transition-and-interview/README.md)
- [assessment](./assessment/README.md)

## 学习原则
- 外部链接是出处，不是主学习入口。
- 每学一个概念，都要回到本模块代码里看它如何落地。
- 每个模块都至少保留 1 条失败案例和 1 条改进思路。
- 每个综合服务都要被你亲手运行、修改、验证一次。
