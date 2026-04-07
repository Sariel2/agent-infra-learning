# 00 总览与准备 逐步执行说明

这一页不是抽象提醒，而是本模块真正的执行剧本。你不需要自己决定“今天先看哪一份文档”，按这里顺着走就可以。

## 使用方式
- 每一步都按 `先读 -> 再看代码 -> 再运行 -> 再复盘` 的顺序走。
- 如果某一步卡住，不要硬顶，先按我写的“回跳路径”返回上一层。
- 这一模块的目标不是做复杂功能，而是把后面 6 个模块的学习环境和工程习惯搭稳。

## Step 1：先拿到整张地图
- 先读 [README.md](./README.md)
- 再读 [study-map.md](./study-map.md)
- 然后读 [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
- 这一步要解决什么：
  - 你先要知道 agent infra 是分层系统
  - 你先要知道课程为什么按当前顺序展开
  - 你先要知道“能力点”和“治理点”会一起出现
- 完成标准：
  - 你能口头讲出这门课的 6 层系统图
  - 你知道为什么这门课不是从 multi-agent 开始
- 如果卡住：
  - 回到 [mindmap.md](./mindmap.md)
  - 再回到 [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)

## Step 2：把课程节奏和失败意识先立住
- 读 [resources/02-deep-dive.md](./resources/02-deep-dive.md)
- 再读 [resources/05-common-mistakes.md](./resources/05-common-mistakes.md)
- 最后扫一遍 [tasks.md](./tasks.md)
- 这一步要解决什么：
  - 你要知道为什么课程从最小骨架开始
  - 你要知道为什么记录系统本身就是学习内容
  - 你要知道最常见的错误起点是什么
- 完成标准：
  - 你能说清“为什么最小骨架比大模板更适合入门”
  - 你能说清“为什么记录是学习的一部分”
- 如果卡住：
  - 回到 [resources/02-deep-dive.md](./resources/02-deep-dive.md)
  - 再看 [review.md](./review.md) 里的复盘问题

## Step 3：先跑最小配置和日志例子
- 先读 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md) 里 `01-settings-and-logging` 这一节
- 再读 [examples/01-settings-and-logging/README.md](./examples/01-settings-and-logging/README.md)
- 再读 [examples/01-settings-and-logging/walkthrough.md](./examples/01-settings-and-logging/walkthrough.md)
- 然后打开 [examples/01-settings-and-logging/app/main.py](./examples/01-settings-and-logging/app/main.py)
- 再看 [examples/01-settings-and-logging/tests/test_main.py](./examples/01-settings-and-logging/tests/test_main.py)
- 建议命令：
  - `python -m app.main`
  - `pytest`
- 这一步要重点看什么：
  - `Settings`
  - `build_log_context()`
  - 配置对象如何变成日志上下文
- 建议动手改一次：
  - 新增一个字段，比如 `course_stage`
  - 再把它接进输出和测试
- 完成标准：
  - 你能解释为什么“配置收口”是系统习惯，不是样板代码
- 如果卡住：
  - 回到 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md)
  - 再回到 [resources/04-sources.md](./resources/04-sources.md) 里看 `Pydantic Settings` 的解释

## Step 4：再跑最小项目就绪检查例子
- 先读 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md) 里 `02-project-smoke-test` 这一节
- 再读 [examples/02-project-smoke-test/README.md](./examples/02-project-smoke-test/README.md)
- 再读 [examples/02-project-smoke-test/walkthrough.md](./examples/02-project-smoke-test/walkthrough.md)
- 然后打开 [examples/02-project-smoke-test/app/main.py](./examples/02-project-smoke-test/app/main.py)
- 再看 [examples/02-project-smoke-test/tests/test_main.py](./examples/02-project-smoke-test/tests/test_main.py)
- 建议命令：
  - `python -m app.main`
  - `pytest`
- 这一步要重点看什么：
  - `ProjectStatus`
  - `summarize_status()`
  - 状态对象如何变成 readiness 判断
- 建议动手改一次：
  - 增加 `docs_ready`
  - 再决定它是否影响 `ready / needs-work`
- 完成标准：
  - 你能说清为什么“项目是否准备好”也值得结构化
- 如果卡住：
  - 回到 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md)
  - 再回到 [resources/02-deep-dive.md](./resources/02-deep-dive.md)

## Step 5：把两个小例子收束到综合服务
- 先读 [module-service/README.md](./module-service/README.md)
- 再读 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md) 里 `starter-workspace` 这一节
- 然后打开 [module-service/app/service.py](./module-service/app/service.py)
- 再看 [module-service/app/main.py](./module-service/app/main.py)
- 最后看 [module-service/tests/test_main.py](./module-service/tests/test_main.py)
- 建议命令：
  - `uvicorn app.main:app --reload`
  - `pytest`
- 这一步要重点看什么：
  - `WorkspaceStatus`
  - `summarize_workspace()`
  - 为什么 HTTP 入口也从第 00 模块就开始出现
- 完成标准：
  - 你能解释这个综合服务如何把“配置、记录、ready check”串成一个最小工作区服务
- 如果卡住：
  - 回到 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md)
  - 再看 [project.md](./project.md) 里的综合目标

## Step 6：回头看出处，但只看你现在需要的部分
- 读 [resources/04-sources.md](./resources/04-sources.md)
- 推荐顺序：
  - `Pydantic Settings`
  - `FastAPI Tutorial`
  - `OpenTelemetry Python Instrumentation`
  - `OpenAI Responses API`
- 这一步要解决什么：
  - 把课程里的判断重新接回原始语境
  - 确认你不是只记住教程说法，而是理解出处在解决什么问题
- 完成标准：
  - 你能说出至少 2 条“教程里的判断”和“出处里的原理”之间的对应关系
- 如果卡住：
  - 回到 [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)

## Step 7：做收束练习和复盘
- 做 [exercises.md](./exercises.md)
- 用 [review.md](./review.md) 复盘
- 打开 [project.md](./project.md)，确认你是否已经具备进入第 01 模块的骨架
- 最少写下这 3 件事：
  - 1 条你现在能讲清楚的系统层次判断
  - 1 条你最容易犯的错误起点
  - 1 条你准备在下个模块继续沿用的工程习惯
- 完成标准：
  - 你已经不再把这门课理解成“零散 agent 技巧合集”，而是有了一条稳定主线

## 本模块结束时你应该具备什么
- 你能画出这门课的总图
- 你知道为什么每个模块都会有 `resources / examples / module-service / review`
- 你知道为什么这门课一开始就要求结构化、服务化和记录化
