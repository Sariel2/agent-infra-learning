# 01 Python 与 Agent 基础

这个模块的任务是把你带进 Python-first agent 工程的最小主线。重点不是 Python 语法本身，而是学会把模型调用组织成稳定的服务边界。

## 这个模块解决什么问题
- 为什么 agent infra 不能从“直接调真实模型”开始。
- 为什么 structured output 是最早必须稳定下来的能力。
- 为什么 provider abstraction 是后续 tool、workflow、eval 的地基。

## 这一模块的最终产出
- 两个可运行 example：
  [examples/01-structured-output](./examples/01-structured-output/README.md)
  [examples/02-provider-abstraction](./examples/02-provider-abstraction/README.md)
- 一个最小 `llm-gateway` 综合服务：
  [module-service/README.md](./module-service/README.md)
- 一套你自己写得出来的 request/response/provider 边界。

## 推荐学习顺序
1. 先看 [mindmap.md](./mindmap.md)，确认本模块知识结构。
2. 再看 [study-map.md](./study-map.md)，明确学习路线。
3. 按顺序读讲义：
   [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
   [resources/02-deep-dive.md](./resources/02-deep-dive.md)
   [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md)
   [resources/04-sources.md](./resources/04-sources.md)
   [resources/05-common-mistakes.md](./resources/05-common-mistakes.md)
4. 跟着 [steps.md](./steps.md) 跑两个 example，再做综合服务。
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
- 用 schema 固定输入输出，而不是依赖自由文本。
- 用 provider 隔离外部模型依赖，而不是让路由直接接模型。
- 用 fake provider 先稳定接口和测试，再考虑接真实模型。

## 通关标准
- 你能解释为什么 structured output 是工程能力，不只是格式要求。
- 你能自己写出一个最小 fake provider。
- 你能运行并解释 [module-service/app/service.py](./module-service/app/service.py) 里的 request、response、provider 和 `generate()`。
- 你能说清如果后面接真实模型，哪些层该改、哪些层不该改。

## 完成后去哪
- 下一站：[02-single-agent-with-tools/README.md](../02-single-agent-with-tools/README.md)
- 进入下一模块前，建议回看 [module-service/README.md](./module-service/README.md) 和 [exercises.md](./exercises.md)。
