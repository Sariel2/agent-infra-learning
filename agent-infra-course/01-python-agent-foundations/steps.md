# 01 Python 与 Agent 基础 逐步执行说明

下面的步骤不是抽象提醒，而是本模块真正的学习顺序。每一步都对应具体讲义文件、代码文件和命令。

## Step 1：先建立概念框架
- 先读 [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
- 再读 [resources/05-common-mistakes.md](./resources/05-common-mistakes.md)
- 目标：先知道这个模块解决什么问题、边界在哪里、最容易错在哪里。
- 完成标准：你能不用看代码先讲清这个模块的核心概念。

## Step 2：读细节和原理
- 读 [resources/02-deep-dive.md](./resources/02-deep-dive.md)
- 参考 [resources/04-sources.md](./resources/04-sources.md) 中的出处链接，但不要跳出去替代教程本身
- 目标：弄清楚这个模块背后的数据流、设计动机和失败模式。
- 完成标准：你能解释“为什么要这样设计”，而不只是“我会用”。

## Step 3：学习 example `01-structured-output`
- 先读 [examples/01-structured-output/README.md](./examples/01-structured-output/README.md)
- 再读 [examples/01-structured-output/walkthrough.md](./examples/01-structured-output/walkthrough.md)
- 打开 [examples/01-structured-output/app/main.py](./examples/01-structured-output/app/main.py)：先看 `StructuredAnswer`，它不是装饰，而是系统契约。再看 `generate_structured_answer`，理解课程为什么先用 deterministic stub。
- 打开 [examples/01-structured-output/tests/test_main.py](./examples/01-structured-output/tests/test_main.py)：看测试如何验证输出形状，而不是只验证一段自由文本。
- 建议命令：
  - `python -m app.main`
  - `pytest`
- 完成标准：你至少做 1 处小改动，并能解释行为变化。

## Step 4：学习 example `02-provider-abstraction`
- 先读 [examples/02-provider-abstraction/README.md](./examples/02-provider-abstraction/README.md)
- 再读 [examples/02-provider-abstraction/walkthrough.md](./examples/02-provider-abstraction/walkthrough.md)
- 打开 [examples/02-provider-abstraction/app/main.py](./examples/02-provider-abstraction/app/main.py)：先看 `Provider` 协议，再看 `EchoProvider` 与 `FakeLLMProvider`，理解“同一接口，不同实现”的工程价值。
- 打开 [examples/02-provider-abstraction/tests/test_main.py](./examples/02-provider-abstraction/tests/test_main.py)：看同一业务函数如何在不同 provider 上被稳定测试。
- 建议命令：
  - `python -m app.main`
  - `pytest`
- 完成标准：你至少做 1 处小改动，并能解释行为变化。

## Step 5：进入综合服务 `llm-gateway`
- 先读 [module-service/README.md](./module-service/README.md)
- 打开 [module-service/app/service.py](./module-service/app/service.py)：先看 `GenerateRequest` 与 `GenerateResponse`，它们定义了系统输入输出契约。再看 `FakeProvider` 和 `generate()`，理解 route 不应该直接管模型。
- 打开 [module-service/app/main.py](./module-service/app/main.py)：再看 HTTP 层如何只做协议转换，而不承担业务逻辑。
- 打开 [module-service/tests/test_main.py](./module-service/tests/test_main.py)：最后看测试，确认接口契约已经被稳定验证。
- 建议命令：
  - `uvicorn app.main:app --reload`
  - `pytest`
- 完成标准：你能解释这个综合服务如何把本模块知识点串起来。

## Step 6：练习与复盘
- 做 [exercises.md](./exercises.md)
- 用 [review.md](./review.md) 做复盘
- 完成标准：至少写下 1 条失败案例、1 条修复思路、1 条你现在能讲清楚的判断原则。
