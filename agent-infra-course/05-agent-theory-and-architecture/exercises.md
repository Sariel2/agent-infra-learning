# 05 Agent 原理与架构 练习手册

## 这份练习怎么用
- 先按 [steps.md](./steps.md) 跑完 `pattern comparison` 和 `boundary checker` 两个 example。
- 本模块练习重点不是背框架名，而是学会“看到场景就知道该选什么模式，不该选什么模式”。
- 每题都尽量结合前四个模块的实际服务来判断，而不是空谈架构。

## 做题前回看
- 学习路线：[study-map.md](./study-map.md)
- 概念讲义：[resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
- 原理细节：[resources/02-deep-dive.md](./resources/02-deep-dive.md)
- 代码导读：[resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md)
- 示例 1：[examples/01-pattern-comparison/app/main.py](./examples/01-pattern-comparison/app/main.py)
- 示例 2：[examples/02-boundary-checker/app/main.py](./examples/02-boundary-checker/app/main.py)
- 综合服务：[module-service/app/main.py](./module-service/app/main.py)
- 综合测试：[module-service/tests/test_main.py](./module-service/tests/test_main.py)

## 练习 1：比较三种常见模式
- 先回看：[resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
- 题目：比较 ReAct、Router、Plan-and-Execute 的核心目标、优点和风险。
- 输出要求：每种模式至少写 4 句。
- 完成标准：你能指出它们最大的差异不在“谁更高级”，而在“谁更适合当前任务结构”。

## 练习 2：workflow 和 agent 的边界判断
- 先回看：[resources/02-deep-dive.md](./resources/02-deep-dive.md)
- 对应代码：[examples/02-boundary-checker/app/main.py](./examples/02-boundary-checker/app/main.py)
- 题目：给一个“客服知识问答 + 查工单 + 创建工单”的场景，判断哪些部分适合 workflow，哪些适合 agent。
- 输出要求：按子任务拆分并逐项说明。
- 完成标准：你必须给出清晰的边界理由，而不是只说“看情况”。

## 练习 3：multi-agent 的复杂度成本
- 先回看：[resources/05-common-mistakes.md](./resources/05-common-mistakes.md)
- 题目：说明什么情况下 multi-agent 其实只是多余复杂度，并举一个如果误用会带来什么工程问题的例子。
- 输出要求：至少覆盖状态同步、调试、成本三个方面。
- 完成标准：你能说明为什么 single-agent 或 workflow 往往是更好的第一选择。

## 练习 4：模式选型 checklist
- 先回看：[project.md](./project.md)
- 对应代码：[examples/01-pattern-comparison/app/main.py](./examples/01-pattern-comparison/app/main.py)
- 题目：设计一份模式选型 checklist，帮助你在新需求出现时快速判断该用哪种模式。
- 输出要求：至少列出 8 个判断问题。
- 完成标准：问题必须覆盖步骤确定性、工具依赖、风险等级、人工审核、结果可验证性。

## 练习 5：用前面项目做架构复盘
- 先回看：[module-service/README.md](./module-service/README.md)
- 对应代码：[module-service/app/main.py](./module-service/app/main.py)
- 题目：回顾前四个模块的综合服务，分别说明它们采用了怎样的模式，以及为什么这就是当时最合适的选择。
- 输出要求：至少覆盖 `llm-gateway`、`support-agent`、`knowledge-agent`、`agent-runtime` 四个项目。
- 完成标准：你能把模式选择与当时的目标、风险和演进阶段联系起来。

## 练习 6：最小实验接口设计
- 先回看：[resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md)
- 对应代码：[module-service/tests/test_main.py](./module-service/tests/test_main.py)
- 题目：设计一个最小实验接口，用来快速对比同一需求下的不同 agent pattern。
- 输出要求：说明输入、输出和比较维度。
- 完成标准：比较维度里至少要有正确性、成本和可调试性。

## 完成后自检
- 你能在新需求进来时先做模式选择，而不是先选框架。
- 你知道什么时候应该收缩复杂度。
- 你已经把前面 4 个模块的项目抽象成可复用模式。
- 你准备好把这些判断转成面试表达和项目讲解。
