# 04 Workflow、Observability 与 Evals 练习手册

## 这份练习怎么用
- 先按 [steps.md](./steps.md) 跑完 `stateful workflow` 和 `eval runner` 两条主线。
- 本模块练习不是让你背名词，而是训练你把“感觉不稳定”翻译成可定位、可比较的问题。
- 每道题都尽量回答到 `状态`、`证据`、`指标` 三个层面。

## 做题前回看
- 学习路线：[study-map.md](./study-map.md)
- 概念讲义：[resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
- 原理细节：[resources/02-deep-dive.md](./resources/02-deep-dive.md)
- 代码导读：[resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md)
- 示例 1：[examples/01-stateful-workflow/app/main.py](./examples/01-stateful-workflow/app/main.py)
- 示例 2：[examples/02-eval-runner/app/main.py](./examples/02-eval-runner/app/main.py)
- 综合服务：[module-service/app/main.py](./module-service/app/main.py)
- 综合测试：[module-service/tests/test_main.py](./module-service/tests/test_main.py)

## 练习 1：workflow 与自由 agent 的边界
- 先回看：[resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
- 题目：解释为什么“步骤固定、失败代价高、审核点明确”的任务更适合 workflow，而不是完全交给自由 agent。
- 输出要求：从稳定性、可审计性、回归验证三个角度作答。
- 完成标准：你必须指出 workflow 不是更低级，而是更可控。

## 练习 2：trace、log、eval 的职责对比
- 先回看：[resources/02-deep-dive.md](./resources/02-deep-dive.md)
- 对应代码：[examples/02-eval-runner/app/main.py](./examples/02-eval-runner/app/main.py)
- 题目：比较 trace、log、eval 三者分别回答什么问题。
- 输出要求：用表格或三段对比说明。
- 完成标准：你能把三者对应到“单次运行”“局部事件”“版本比较”三种粒度。

## 练习 3：设计人工审核节点
- 先回看：[resources/02-deep-dive.md](./resources/02-deep-dive.md)
- 对应代码：[examples/01-stateful-workflow/app/main.py](./examples/01-stateful-workflow/app/main.py)
- 题目：为一个客服处理流程增加人工审核节点，并解释为什么审核点应该显式成为工作流状态。
- 输出要求：画出流程图并说明状态转移条件。
- 完成标准：你必须定义“进入审核”和“审核后继续/中止”的条件。

## 练习 4：设计最小 trace schema
- 先回看：[resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md)
- 对应代码：[module-service/app/main.py](./module-service/app/main.py)
- 题目：设计一份最小 trace schema，要求后续能看出节点、输入、输出、延迟和错误。
- 输出要求：写字段定义和每个字段的调试价值。
- 完成标准：字段设计必须支持你定位某个节点为什么失败，而不是只记录最终结果。

## 练习 5：设计一组 eval 指标
- 先回看：[project.md](./project.md)
- 对应代码：[examples/02-eval-runner/app/main.py](./examples/02-eval-runner/app/main.py)
- 题目：为 `agent-runtime` 设计一组基础评测指标，覆盖质量、稳定性、延迟和成本。
- 输出要求：每个指标说明定义、采集方式和解读方式。
- 完成标准：至少包括 `success rate`、`latency`、`tool accuracy`、`citation accuracy` 中的三个。

## 练习 6：综合排错演练
- 先回看：[resources/05-common-mistakes.md](./resources/05-common-mistakes.md)
- 对应代码：[module-service/tests/test_main.py](./module-service/tests/test_main.py)
- 题目：系统“有时好有时坏”，但当前没有 trace、eval 也没有固定样本，你会如何补建排错体系。
- 输出要求：分 `先补什么`、`再补什么`、`最后如何验证` 三段来写。
- 完成标准：你的答案必须体现“先补证据，再做优化”。

## 完成后自检
- 你能把一个开放描述的问题转成 workflow 状态图。
- 你能说清为什么日志替代不了 trace。
- 你已经能定义一套最小 eval 指标。
- 你已经具备进入“模式选择与系统设计”模块的证据意识。
