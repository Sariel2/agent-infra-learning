# 06 转型、简历与面试 逐步执行说明

这一页会把最后一模块真正变成“能力资产打包”流程。你会先把表达原则想清楚，再通过两个 example 把项目故事和高频问答做成稳定骨架，最后收束到 `showcase-pack`。

## 使用方式
- 本模块一定按 `项目故事 -> 高频问答 -> 综合展示包` 的顺序走。
- 不要把这一模块当“最后写几段文案”，它的目标是把前 5 个模块的工程实践重新组织成职业资产。
- 每一步都要围绕 3 个问题走：
  - 我要讲什么事实
  - 我要用什么结构讲
  - 我要怎样让它经得住追问

## Step 1：先把表达原则和错误起点看清
- 先读 [study-map.md](./study-map.md)
- 再读 [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
- 再读 [resources/05-common-mistakes.md](./resources/05-common-mistakes.md)
- 这一步要解决什么：
  - 为什么最后一模块不是附属内容
  - 为什么要同时准备业务版和 infra 版讲法
  - 为什么失败案例会增强说服力
- 完成标准：
  - 你能不用看代码先讲清“可被相信的项目表达”包含哪些元素
- 如果卡住：
  - 回到 [mindmap.md](./mindmap.md)
  - 再回到 [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)

## Step 2：先把项目叙事和面试判断逻辑想透
- 读 [resources/02-deep-dive.md](./resources/02-deep-dive.md)
- 再读 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md) 的总说明
- 最后扫一遍 [resources/04-sources.md](./resources/04-sources.md)
- 这一步要解决什么：
  - 简历 bullet 和项目讲稿到底有什么不同
  - 为什么高频面试题本质上是判断题
  - 为什么表达也应该沉淀成可复用结构
- 完成标准：
  - 你能说出一个完整失败链路该包含哪 5 件事
- 如果卡住：
  - 回到 [resources/02-deep-dive.md](./resources/02-deep-dive.md)

## Step 3：先跑项目故事 example
- 先读 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md) 中 `01-project-story-api` 这一节
- 再读 [examples/01-project-story-api/README.md](./examples/01-project-story-api/README.md)
- 再读 [examples/01-project-story-api/walkthrough.md](./examples/01-project-story-api/walkthrough.md)
- 然后打开 [examples/01-project-story-api/app/main.py](./examples/01-project-story-api/app/main.py)
- 最后看 [examples/01-project-story-api/tests/test_main.py](./examples/01-project-story-api/tests/test_main.py)
- 建议命令：
  - `python -m app.main`
  - `pytest`
- 这一步要重点看什么：
  - `ProjectFacts`
  - `build_story()`
  - `business` 和 `infra` 两种输出口径
- 建议动手改一次：
  - 换成你自己的项目事实
  - 再看输出是否仍然能稳定分成双版本
- 完成标准：
  - 你能解释为什么“项目讲述”本质上是对事实做结构化重组
- 如果卡住：
  - 回到 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md)

## Step 4：再跑高频问答 example
- 先读 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md) 中 `02-interview-qa-pack` 这一节
- 再读 [examples/02-interview-qa-pack/README.md](./examples/02-interview-qa-pack/README.md)
- 再读 [examples/02-interview-qa-pack/walkthrough.md](./examples/02-interview-qa-pack/walkthrough.md)
- 然后打开 [examples/02-interview-qa-pack/app/main.py](./examples/02-interview-qa-pack/app/main.py)
- 最后看 [examples/02-interview-qa-pack/tests/test_main.py](./examples/02-interview-qa-pack/tests/test_main.py)
- 建议命令：
  - `python -m app.main`
  - `pytest`
- 这一步要重点看什么：
  - `FAQ`
  - `answer_question()`
  - 已知问题和未知问题的回答骨架
- 建议动手改一次：
  - 增加一个新主题，比如 `tool-schema`
  - 再给它补上工程化回答
- 完成标准：
  - 你能解释为什么稳定回答骨架比临场发挥更重要
- 如果卡住：
  - 回到 [resources/02-deep-dive.md](./resources/02-deep-dive.md)

## Step 5：进入综合服务 `showcase-pack`
- 先读 [module-service/README.md](./module-service/README.md)
- 再读 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md) 中 `showcase-pack` 这一节
- 然后打开 [module-service/app/service.py](./module-service/app/service.py)
- 再看 [module-service/app/main.py](./module-service/app/main.py)
- 最后看 [module-service/tests/test_main.py](./module-service/tests/test_main.py)
- 建议命令：
  - `uvicorn app.main:app --reload`
  - `pytest`
- 这一步要重点看什么：
  - `StoryRequest`
  - `QARequest`
  - `FAQ`
  - `build_story()`
  - `answer()`
- 完成标准：
  - 你能解释这个服务如何把“项目故事”和“高频问答”收束成可展示资产
- 如果卡住：
  - 回到 [project.md](./project.md)
  - 再回到 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md)

## Step 6：回头把你的项目放回行业主语境
- 读 [resources/04-sources.md](./resources/04-sources.md)
- 推荐顺序：
  - `OpenAI new tools for building agents`
  - `OpenAI Agents SDK`
  - `LangGraph overview`
- 这一步要解决什么：
  - 把你自己的项目表达重新接回行业主叙事
  - 确认你讲的不是“个人作品秀”，而是“对真实问题结构的工程回应”
- 完成标准：
  - 你能说出至少 2 条“我的项目”和“行业主线”之间的对应关系
- 如果卡住：
  - 回到 [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)

## Step 7：做结课收束和面试准备
- 做 [exercises.md](./exercises.md)
- 用 [review.md](./review.md) 复盘
- 再看 [project.md](./project.md)
- 最后回到总考试：
  - [assessment/final-exam.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/assessment/final-exam.md)
  - [assessment/final-exam-answers.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/assessment/final-exam-answers.md)
- 最少写下这 5 件事：
  - 1 条你最强的项目故事主线
  - 1 条你最能讲的失败案例
  - 1 条业务版表述
  - 1 条 infra 版表述
  - 1 条“为什么不用另一个方案”的回答
- 完成标准：
  - 你已经把前 5 个模块学到的东西整理成可展示、可追问、可面试的资产

## 本模块结束时你应该具备什么
- 你能用 3 分钟讲清一个 agent infra 项目
- 你能把同一项目切成业务版和 infra 版
- 你能用真实代码和真实判断支撑自己的表达
