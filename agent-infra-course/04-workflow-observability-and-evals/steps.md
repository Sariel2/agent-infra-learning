# 04 Workflow、Observability 与 Evals 逐步执行说明

这一页会把本模块变成真正的运行时治理训练。你会先看状态和流程，再看评测，然后把两者收束到带 trace 思维的综合服务。

## 使用方式
- 本模块一定按 `workflow -> eval -> runtime` 的顺序走。
- 每一步都要把“理论上怎么走”和“实际如何被记录”联系起来看。
- 这里最容易走偏的地方是只关注流程图，不看 trace 和 eval 的关系。

## Step 1：先把治理闭环看清
- 先读 [study-map.md](./study-map.md)
- 再读 [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
- 再读 [resources/05-common-mistakes.md](./resources/05-common-mistakes.md)
- 这一步要解决什么：
  - 为什么 workflow 必须显式存在
  - 为什么 workflow 和 agent 不是对立关系
  - 为什么 trace 和 eval 是同一治理闭环的一部分
- 完成标准：
  - 你能不用看代码讲清 `workflow / trace / eval` 三者的关系
- 如果卡住：
  - 回到 [mindmap.md](./mindmap.md)
  - 再回到 [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)

## Step 2：先把过程和比较的原理想透
- 读 [resources/02-deep-dive.md](./resources/02-deep-dive.md)
- 再读 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md) 的总说明
- 最后扫一遍 [resources/04-sources.md](./resources/04-sources.md)
- 这一步要解决什么：
  - workflow 和 agent 的边界是什么
  - trace 里哪些元数据最值得保留
  - eval dataset 到底应该长什么样
- 完成标准：
  - 你能拿一个失败样例，说出应该先看 workflow、trace 还是 eval
- 如果卡住：
  - 回到 [resources/02-deep-dive.md](./resources/02-deep-dive.md)

## Step 3：先跑 stateful workflow example
- 先读 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md) 中 `01-stateful-workflow` 这一节
- 再读 [examples/01-stateful-workflow/README.md](./examples/01-stateful-workflow/README.md)
- 再读 [examples/01-stateful-workflow/walkthrough.md](./examples/01-stateful-workflow/walkthrough.md)
- 然后打开 [examples/01-stateful-workflow/app/main.py](./examples/01-stateful-workflow/app/main.py)
- 最后看 [examples/01-stateful-workflow/tests/test_main.py](./examples/01-stateful-workflow/tests/test_main.py)
- 建议命令：
  - `python -m app.main`
  - `pytest`
- 这一步要重点看什么：
  - `WorkflowState`
  - `run_workflow()`
  - `needs_review`
  - `completed`
- 建议动手改一次：
  - 增加一个新分支场景，比如 `vip refund`
  - 再补状态字段和测试
- 完成标准：
  - 你能解释为什么流程不是一串步骤名，而是状态变化
- 如果卡住：
  - 回到 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md)

## Step 4：再跑 eval runner example
- 先读 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md) 中 `02-eval-runner` 这一节
- 再读 [examples/02-eval-runner/README.md](./examples/02-eval-runner/README.md)
- 再读 [examples/02-eval-runner/walkthrough.md](./examples/02-eval-runner/walkthrough.md)
- 然后打开 [examples/02-eval-runner/app/main.py](./examples/02-eval-runner/app/main.py)
- 最后看 [examples/02-eval-runner/tests/test_main.py](./examples/02-eval-runner/tests/test_main.py)
- 建议命令：
  - `python -m app.main`
  - `pytest`
- 这一步要重点看什么：
  - `EvalCase`
  - `EvalResult`
  - `DATASET`
  - `run_eval()`
- 建议动手改一次：
  - 加一个更容易混淆的新样本
  - 看 `matched` 是否变化
- 完成标准：
  - 你能解释为什么 eval 首先是“固定样本比较机制”，而不是“复杂评分系统”
- 如果卡住：
  - 回到 [resources/02-deep-dive.md](./resources/02-deep-dive.md)

## Step 5：进入综合服务 `agent-runtime`
- 先读 [module-service/README.md](./module-service/README.md)
- 再读 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md) 中 `agent-runtime` 这一节
- 然后打开 [module-service/app/service.py](./module-service/app/service.py)
- 再看 [module-service/app/main.py](./module-service/app/main.py)
- 最后看 [module-service/tests/test_main.py](./module-service/tests/test_main.py)
- 建议命令：
  - `uvicorn app.main:app --reload`
  - `pytest`
- 这一步要重点看什么：
  - `RunRequest`
  - `DATASET`
  - `classify_node()`
  - `run_runtime()`
  - `evaluate()`
- 完成标准：
  - 你能解释这个运行时如何同时承接路径执行和批量验证
- 如果卡住：
  - 回到 [project.md](./project.md)
  - 再回到 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md)

## Step 6：回头把治理语言和一手资料对齐
- 读 [resources/04-sources.md](./resources/04-sources.md)
- 推荐顺序：
  - `LangGraph overview`
  - `LangSmith Observability`
  - `OpenAI Agents SDK Tracing`
  - `OpenTelemetry Python Instrumentation`
  - `FastAPI Background Tasks`
- 这一步要解决什么：
  - 把你在代码里看到的 workflow / trace / eval 重新接回外部语境
  - 确认你理解了“为什么这几类能力必须一起学”
- 完成标准：
  - 你能说出至少 3 条“代码设计”和“出处原理”的映射
- 如果卡住：
  - 回到 [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)

## Step 7：做收束练习并为模式模块交接
- 做 [exercises.md](./exercises.md)
- 用 [review.md](./review.md) 复盘
- 再看 [project.md](./project.md)，确认自己是否准备好进入第 05 模块的 pattern 比较
- 最少写下这 4 件事：
  - 1 条关于 workflow 的判断
  - 1 条关于 trace 的判断
  - 1 条关于 eval 的判断
  - 1 条你准备带到模式模块的复杂度控制意识
- 完成标准：
  - 你已经开始用“运行时治理”视角看 agent 系统

## 本模块结束时你应该具备什么
- 你能解释为什么流程必须显式化
- 你知道 trace 不是日志加强版
- 你能说明 eval 为什么是系统演进的比较机制
