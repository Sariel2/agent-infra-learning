# 05 Agent 原理与架构

这个模块不是重新讲一遍前面的知识点，而是把前四个模块做过的东西提炼成稳定的模式判断与架构判断能力。重点是学会“看到场景就知道该选什么，不该选什么”。

## 这个模块解决什么问题
- 为什么很多人会把“框架选择”误当成“架构设计”。
- 为什么 workflow、single-agent、multi-agent、hybrid 都有各自边界。
- 为什么复杂度控制本身就是 agent infra 的核心能力。

## 这一模块的最终产出
- 两个可运行 example：
  [examples/01-pattern-comparison](./examples/01-pattern-comparison/README.md)
  [examples/02-boundary-checker](./examples/02-boundary-checker/README.md)
- 一个最小 `architecture-lab` 综合服务：
  [module-service/README.md](./module-service/README.md)
- 一份你自己的模式选型 checklist。

## 推荐学习顺序
1. 先看 [mindmap.md](./mindmap.md)，确认模式与边界关系。
2. 再看 [study-map.md](./study-map.md)，明确本模块主线。
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
- 先做模式选择，再做框架选择。
- 用任务确定性、风险、工具变化度、结果可验证性来判断方案。
- 把复杂度压到刚好够用，而不是默认越自由越高级。

## 通关标准
- 你能比较 ReAct、Router、Plan-and-Execute 的适用场景。
- 你能解释为什么很多任务 workflow 就已经足够。
- 你能运行并解释 [module-service/app/service.py](./module-service/app/service.py) 里的 `compare()` 和 `recommend()`。
- 你已经形成一套自己的模式选型标准，而不是只会背名词。

## 完成后去哪
- 下一站：[06-career-transition-and-interview/README.md](../06-career-transition-and-interview/README.md)
- 进入下一模块前，建议先把前四个模块的综合服务各自归类成你自己的模式地图。
