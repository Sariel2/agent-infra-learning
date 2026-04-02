# 06 转型、简历与面试 逐步执行说明

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

## Step 3：学习 example `01-project-story-api`
- 先读 [examples/01-project-story-api/README.md](./examples/01-project-story-api/README.md)
- 再读 [examples/01-project-story-api/walkthrough.md](./examples/01-project-story-api/walkthrough.md)
- 打开 [examples/01-project-story-api/app/main.py](./examples/01-project-story-api/app/main.py)：先看 `ProjectFacts` 与 `build_story()`，理解“项目讲述”本质上是对事实进行结构化。
- 打开 [examples/01-project-story-api/tests/test_main.py](./examples/01-project-story-api/tests/test_main.py)：看测试如何确保输出至少包含项目名和核心要素。
- 建议命令：
  - `python -m app.main`
  - `pytest`
- 完成标准：你至少做 1 处小改动，并能解释行为变化。

## Step 4：学习 example `02-interview-qa-pack`
- 先读 [examples/02-interview-qa-pack/README.md](./examples/02-interview-qa-pack/README.md)
- 再读 [examples/02-interview-qa-pack/walkthrough.md](./examples/02-interview-qa-pack/walkthrough.md)
- 打开 [examples/02-interview-qa-pack/app/main.py](./examples/02-interview-qa-pack/app/main.py)：先看 `FAQ` 和 `answer_question()`。这里不是在追求生成式回答，而是在训练“稳定回答骨架”。
- 打开 [examples/02-interview-qa-pack/tests/test_main.py](./examples/02-interview-qa-pack/tests/test_main.py)：看未知问题的默认回答结构为什么仍然重要。
- 建议命令：
  - `python -m app.main`
  - `pytest`
- 完成标准：你至少做 1 处小改动，并能解释行为变化。

## Step 5：进入综合服务 `showcase-pack`
- 先读 [module-service/README.md](./module-service/README.md)
- 打开 [module-service/app/service.py](./module-service/app/service.py)：先看 `build_story()` 与 `answer()`，理解“表达”在这里也被当成一种可结构化的工程产物。
- 打开 [module-service/app/main.py](./module-service/app/main.py)：再看 `/story` 和 `/qa` 如何分别承接不同表达任务。
- 打开 [module-service/tests/test_main.py](./module-service/tests/test_main.py)：最后看测试如何保护输出骨架。
- 建议命令：
  - `uvicorn app.main:app --reload`
  - `pytest`
- 完成标准：你能解释这个综合服务如何把本模块知识点串起来。

## Step 6：练习与复盘
- 做 [exercises.md](./exercises.md)
- 用 [review.md](./review.md) 做复盘
- 完成标准：至少写下 1 条失败案例、1 条修复思路、1 条你现在能讲清楚的判断原则。
