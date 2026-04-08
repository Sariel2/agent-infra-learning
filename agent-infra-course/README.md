# Agent Infra Learning Course

这是一个面向后端工程师的 `6 周 Python-first Agent Infra 讲义型教程`。这套课程的目标不是把你“引到外部网页自己找资料”，而是让你主要通过课程本身的讲义、代码导读、示例、综合服务、练习和考核，把 agent infra 的主线学扎实。外部链接只保留为出处和延伸阅读。

## 这套课程适合谁
- 已经有后端工程经验，但想系统进入 agent infra。
- 更关心“怎么做成一个稳定系统”，而不是只想跑几个 prompt demo。
- 希望主语言用 Python，并通过可运行项目建立手感。

## 这套课程最终会带你达到什么程度
- 你能从零解释 agent infra 的核心组成：`model`、`tool`、`memory`、`retrieval`、`workflow`、`trace`、`eval`。
- 你能做出几个最小但完整的 Python agent 服务，而不是只有脚本级 demo。
- 你能说清不同模式的边界，知道什么时候该用 workflow、single-agent、RAG、eval。
- 你能把课程里的项目整理成简历材料、项目讲稿和面试表达。

## 整套课程怎么学
1. 先看总图：[mindmap.md](./mindmap.md)
2. 进入模块首页，先读该模块的 [README.md](./00-overview/README.md)
3. 再读该模块的 [study-map.md](./00-overview/study-map.md)
4. 按顺序读该模块讲义：
   `resources/01-*` 到 `resources/05-*`
5. 跟着 [steps.md](./00-overview/steps.md) 跑 example 和 `module-service`
6. 完成 [exercises.md](./00-overview/exercises.md) 和 [review.md](./00-overview/review.md)
7. 全部模块完成后，再做总考核：[assessment/README.md](./assessment/README.md)

## 每个模块里的文件分别做什么
- `README.md`
  模块首页，告诉你这个模块在解决什么问题、产出什么、怎么学、怎么验收。
- `mindmap.md`
  模块级思维导图，帮你先建立结构感。
- `study-map.md`
  模块总学习路线，把讲义、example、综合服务串起来。
- `steps.md`
  逐步执行剧本，明确每一步该看哪份讲义、跑哪个 example、改哪个文件。
- `tasks.md`
  冲刺日历，告诉你按 session 应该怎么分配时间。
- `resources/`
  讲义正文，不只是资料摘要。
- `examples/`
  知识点级别的最小可运行实验。
- `module-service/`
  综合本模块能力的最小服务框架。
- `exercises.md`
  练习手册，每题都回链到讲义和代码。
- `project.md`
  本模块综合项目手册。
- `review.md`
  复盘模板、失败归因和下一步行动。

## 6 周主线
- Week 0： [00-overview/README.md](./00-overview/README.md)
  先把环境、日志、学习与实验骨架立起来。
- Week 1： [01-python-agent-foundations/README.md](./01-python-agent-foundations/README.md)
  先稳定 structured output 和 provider abstraction。
- Week 2： [02-single-agent-with-tools/README.md](./02-single-agent-with-tools/README.md)
  让模型开始进入最小 agent loop 和工具调用。
- Week 3： [03-rag-memory-and-knowledge/README.md](./03-rag-memory-and-knowledge/README.md)
  做出能解释、能引用、能记录会话状态的知识问答服务。
- Week 4： [04-workflow-observability-and-evals/README.md](./04-workflow-observability-and-evals/README.md)
  补上 workflow、trace 和 eval，把系统从“能跑”推进到“可治理”。
- Week 5： [05-agent-theory-and-architecture/README.md](./05-agent-theory-and-architecture/README.md)
  把前面做过的内容提炼成模式和架构判断能力。
- Week 6： [06-career-transition-and-interview/README.md](./06-career-transition-and-interview/README.md)
  把项目整理成可展示、可面试、可转型的材料。

## 模块列表
- [00-overview/README.md](./00-overview/README.md)
- [01-python-agent-foundations/README.md](./01-python-agent-foundations/README.md)
- [02-single-agent-with-tools/README.md](./02-single-agent-with-tools/README.md)
- [03-rag-memory-and-knowledge/README.md](./03-rag-memory-and-knowledge/README.md)
- [04-workflow-observability-and-evals/README.md](./04-workflow-observability-and-evals/README.md)
- [05-agent-theory-and-architecture/README.md](./05-agent-theory-and-architecture/README.md)
- [06-career-transition-and-interview/README.md](./06-career-transition-and-interview/README.md)
- [assessment/README.md](./assessment/README.md)

## 学习原则
- 外部链接是出处，不是主学习入口。
- 每学一个概念，都要回到代码里看它如何落地。
- 每个模块都至少保留 1 条失败案例和 1 条改进思路。
- 每个综合服务都要被你亲手运行、修改、验证一次。
- 每次复盘都要回答：我真正理解了什么，我还没吃透什么。

## 什么时候说明你真的学会了
- 你能不看外部网页，只靠课程内容讲清主线。
- 你能运行并改动每个模块的 `module-service`。
- 你能把练习题和总考核题答到“有判断、有证据、有代码映射”。
- 你能把课程项目讲成一段可信的工程故事。
