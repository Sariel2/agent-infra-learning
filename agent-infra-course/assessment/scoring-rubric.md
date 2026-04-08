# Scoring Rubric

## 使用方式
- 这份评分标准的目的不是打分本身，而是帮你发现自己究竟卡在概念、判断、设计还是表达。
- 如果某一部分明显失分，优先回到对应模块的 `exercises.md`、`project.md` 和 `review.md`。

## 基础题
- 选择题与判断题：每题 2 分
- 看什么：概念边界是否准确，是否能分清相近概念。
- 失分常见原因：会背名词，但分不清 `log` 与 `trace`、`memory` 与 `retrieval`、`workflow` 与 `agent`。
- 优先回链：[../04-workflow-observability-and-evals/resources/01-concepts-and-principles.md](../04-workflow-observability-and-evals/resources/01-concepts-and-principles.md)

## 简答题
- 每题 6 分
- 得分点：概念正确、边界清晰、能落到工程实践。
- 失分常见原因：答案太抽象，无法落到 schema、trace、测试、恢复策略。
- 优先回链：[../01-python-agent-foundations/exercises.md](../01-python-agent-foundations/exercises.md)
- 优先回链：[../02-single-agent-with-tools/exercises.md](../02-single-agent-with-tools/exercises.md)

## 场景分析题
- 每题 10 分
- 得分点：有排查顺序、有证据意识、有工程取舍。
- 失分常见原因：只堆概念，没有排查先后，也没有说明为什么先看哪里。
- 优先回链：[../03-rag-memory-and-knowledge/exercises.md](../03-rag-memory-and-knowledge/exercises.md)
- 优先回链：[../04-workflow-observability-and-evals/exercises.md](../04-workflow-observability-and-evals/exercises.md)

## 系统设计题
- 每题 15 分
- 得分点：结构完整、边界清楚、包含失败恢复与测试思路。
- 失分常见原因：只写模块名字，不写接口契约、轨迹、降级、测试。
- 优先回链：[../02-single-agent-with-tools/project.md](../02-single-agent-with-tools/project.md)
- 优先回链：[../03-rag-memory-and-knowledge/project.md](../03-rag-memory-and-knowledge/project.md)

## 项目讲解题
- 每题 12 分
- 得分点：能讲目标、架构、失败、优化与结果。
- 失分常见原因：只讲用了什么框架，不讲为什么这样设计，也不讲失败案例。
- 优先回链：[../06-career-transition-and-interview/exercises.md](../06-career-transition-and-interview/exercises.md)

## 评分建议
- 85 分以上：已经具备较完整的 agent infra 工程认知，可以进入更真实的项目迭代。
- 70-84 分：主线清楚，但在架构判断或表达上仍可加强。
- 50-69 分：跑过示例，但对边界、trace、eval 的理解还不稳定。
- 50 分以下：建议重做 examples 与 module-service，并补齐失败案例记录。

## 复习顺序建议
- 如果基础题失分多，先回 `resources/01-concepts-and-principles.md`。
- 如果场景题失分多，先回 `resources/02-deep-dive.md` 和 `project.md`。
- 如果系统设计题失分多，先重做 `module-service` 的综合实现。
- 如果项目讲解题失分多，先回 `06-career-transition-and-interview` 整个模块。
