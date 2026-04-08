# 02 单 Agent 与 Tools 练习手册

## 这份练习怎么用
- 先按 [steps.md](./steps.md) 跑通 `tool schema` 和 `agent loop` 两个 example，再做题。
- 做题时要同时引用讲义、example 和综合服务，避免只停留在理论描述。
- 本模块每题都要尽量落到“工具边界是否稳定、轨迹是否可观察、失败是否能恢复”这三个核心点。

## 做题前回看
- 学习路线：[study-map.md](./study-map.md)
- 概念讲义：[resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
- 原理细节：[resources/02-deep-dive.md](./resources/02-deep-dive.md)
- 代码导读：[resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md)
- 示例 1：[examples/01-tool-schema/app/main.py](./examples/01-tool-schema/app/main.py)
- 示例 2：[examples/02-agent-loop/app/main.py](./examples/02-agent-loop/app/main.py)
- 综合服务：[module-service/app/main.py](./module-service/app/main.py)
- 综合测试：[module-service/tests/test_main.py](./module-service/tests/test_main.py)

## 练习 1：为什么 tool schema 直接影响 agent 质量
- 先回看：[resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
- 题目：解释“差的 tool schema 会把问题前置到模型决策层”这句话。
- 输出要求：至少写 6 句，并给出一个好 schema 与坏 schema 的对比例子。
- 完成标准：你能说明参数命名、字段约束、返回结构为什么会影响工具选择稳定性。

## 练习 2：为 `create_ticket` 设计 schema
- 先回看：[resources/02-deep-dive.md](./resources/02-deep-dive.md)
- 对应代码：[examples/01-tool-schema/app/main.py](./examples/01-tool-schema/app/main.py)
- 题目：为 `create_ticket` 设计输入输出 schema，要求后续可以被 trace、retry 和人工接管消费。
- 输出要求：写出字段定义，并说明每个字段的工程用途。
- 完成标准：返回结构里必须包含成功标识、错误信息或 ticket id，不允许只返回自由文本。

## 练习 3：解释单 agent loop
- 先回看：[resources/02-deep-dive.md](./resources/02-deep-dive.md)
- 对应代码：[examples/02-agent-loop/app/main.py](./examples/02-agent-loop/app/main.py)
- 题目：用自己的话解释 `think -> act -> observe -> continue` 的状态变化过程，并指出最容易失控的环节。
- 输出要求：按阶段分段说明。
- 完成标准：你必须指出“observe 阶段决定后续是否继续、降级或停止”。

## 练习 4：失败恢复设计
- 先回看：[resources/05-common-mistakes.md](./resources/05-common-mistakes.md)
- 对应代码：[module-service/app/main.py](./module-service/app/main.py)
- 题目：一个工具偶尔超时，但主流程不能直接失败，你会怎样设计恢复策略。
- 输出要求：至少给出 3 层处理方式，例如重试、降级、人工接管。
- 完成标准：你的方案必须能落到结构化返回和轨迹记录上。

## 练习 5：为什么有些场景其实不需要 agent
- 先回看：[resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
- 题目：说明什么情况下只需要 workflow 或显式路由，而不是自由 agent。
- 输出要求：至少举两个反例场景。
- 完成标准：你能讲出“固定步骤、高风险、审核点明确”这些信号。

## 练习 6：综合服务轨迹设计
- 先回看：[project.md](./project.md)
- 对应代码：[module-service/app/main.py](./module-service/app/main.py)
- 对应测试：[module-service/tests/test_main.py](./module-service/tests/test_main.py)
- 题目：为 `support-agent` 设计一份最小工具轨迹格式，要求后面模块可以直接接 trace 与 eval。
- 输出要求：至少定义 `tool_name`、`args`、`status`、`latency_ms`、`error` 五个字段。
- 完成标准：你能解释这些字段分别支持什么调试动作。

## 完成后自检
- 你能自己实现一个最小 agent loop。
- 你能区分“工具没选对”和“工具执行失败”是两类不同问题。
- 你知道何时应该收缩 agent 自由度。
- 你已经能为下一模块的 RAG 工具和知识检索留好接口位置。
