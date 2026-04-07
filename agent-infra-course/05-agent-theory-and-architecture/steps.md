# 05 Agent 原理与架构 逐步执行说明

这一页会把第 05 模块从“模式名词学习”变成真正的架构判断训练。你会先比较 pattern，再做边界判断，最后回到综合实验室统一理解。

## 使用方式
- 本模块一定按 `pattern comparison -> boundary checker -> architecture-lab` 的顺序走。
- 每一步都把注意力放在“控制流、状态边界、复杂度预算”上。
- 不要把它读成框架对比课，它真正训练的是“为什么不用另一个方案”。

## Step 1：先把模式学习从术语拉回判断
- 先读 [study-map.md](./study-map.md)
- 再读 [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
- 再读 [resources/05-common-mistakes.md](./resources/05-common-mistakes.md)
- 这一步要解决什么：
  - 为什么模式学习必须放在工程实践之后
  - workflow、agent、multi-agent 的边界是什么
  - 为什么 multi-agent 不是默认更高级
- 完成标准：
  - 你能不用看代码先讲清“pattern 的本质是控制流设计”
- 如果卡住：
  - 回到 [mindmap.md](./mindmap.md)
  - 再回到 [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)

## Step 2：先把复杂度控制问题想透
- 读 [resources/02-deep-dive.md](./resources/02-deep-dive.md)
- 再读 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md) 的总说明
- 最后扫一遍 [resources/04-sources.md](./resources/04-sources.md)
- 这一步要解决什么：
  - pattern 为什么最终都要落回控制流和状态
  - boundary checker 为什么是关键训练器
  - 错误选型会怎样伤害系统
- 完成标准：
  - 你能说出至少 2 个“看起来高级但其实复杂度失控”的反例
- 如果卡住：
  - 回到 [resources/02-deep-dive.md](./resources/02-deep-dive.md)

## Step 3：先跑 pattern comparison example
- 先读 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md) 中 `01-pattern-comparison` 这一节
- 再读 [examples/01-pattern-comparison/README.md](./examples/01-pattern-comparison/README.md)
- 再读 [examples/01-pattern-comparison/walkthrough.md](./examples/01-pattern-comparison/walkthrough.md)
- 然后打开 [examples/01-pattern-comparison/app/main.py](./examples/01-pattern-comparison/app/main.py)
- 最后看 [examples/01-pattern-comparison/tests/test_main.py](./examples/01-pattern-comparison/tests/test_main.py)
- 建议命令：
  - `python -m app.main`
  - `pytest`
- 这一步要重点看什么：
  - `PatternOutput`
  - `compare_patterns()`
  - 同一任务如何映射成不同步骤结构
- 建议动手改一次：
  - 增加一个 pattern，比如 `supervisor`
  - 再补输出和测试
- 完成标准：
  - 你能解释为什么模式差异最终要落回步骤结构
- 如果卡住：
  - 回到 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md)

## Step 4：再跑 boundary checker example
- 先读 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md) 中 `02-boundary-checker` 这一节
- 再读 [examples/02-boundary-checker/README.md](./examples/02-boundary-checker/README.md)
- 再读 [examples/02-boundary-checker/walkthrough.md](./examples/02-boundary-checker/walkthrough.md)
- 然后打开 [examples/02-boundary-checker/app/main.py](./examples/02-boundary-checker/app/main.py)
- 最后看 [examples/02-boundary-checker/tests/test_main.py](./examples/02-boundary-checker/tests/test_main.py)
- 建议命令：
  - `python -m app.main`
  - `pytest`
- 这一步要重点看什么：
  - `Scenario`
  - `recommend_architecture()`
  - 为什么输入维度比返回字符串更重要
- 建议动手改一次：
  - 增加一个新维度，比如 `human_review_required`
  - 再调整推荐逻辑和测试
- 完成标准：
  - 你能解释为什么架构判断本质上是在做复杂度预算
- 如果卡住：
  - 回到 [resources/02-deep-dive.md](./resources/02-deep-dive.md)

## Step 5：进入综合服务 `architecture-lab`
- 先读 [module-service/README.md](./module-service/README.md)
- 再读 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md) 中 `architecture-lab` 这一节
- 然后打开 [module-service/app/service.py](./module-service/app/service.py)
- 再看 [module-service/app/main.py](./module-service/app/main.py)
- 最后看 [module-service/tests/test_main.py](./module-service/tests/test_main.py)
- 建议命令：
  - `uvicorn app.main:app --reload`
  - `pytest`
- 这一步要重点看什么：
  - `CompareRequest`
  - `RecommendRequest`
  - `compare()`
  - `recommend()`
- 完成标准：
  - 你能解释这个综合服务如何同时承接“模式比较”和“架构推荐”两类任务
- 如果卡住：
  - 回到 [project.md](./project.md)
  - 再回到 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md)

## Step 6：回头对齐平台和框架语境
- 读 [resources/04-sources.md](./resources/04-sources.md)
- 推荐顺序：
  - `LangGraph overview`
  - `OpenAI Agents SDK`
  - `OpenAI new tools for building agents`
- 这一步要解决什么：
  - 把你的模式判断重新接回行业主语境
  - 确认你理解的是“框架为何这样组织”，而不是只记名字
- 完成标准：
  - 你能说出至少 2 条“课程判断”和“出处中的平台/框架设计”之间的映射
- 如果卡住：
  - 回到 [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)

## Step 7：做收束练习并为转型模块交接
- 做 [exercises.md](./exercises.md)
- 用 [review.md](./review.md) 复盘
- 再看 [project.md](./project.md)，确认自己是否准备好进入第 06 模块的项目表达与面试包装
- 最少写下这 4 件事：
  - 1 条关于 workflow vs agent 的判断
  - 1 条关于 multi-agent 的判断
  - 1 条你识别出的复杂度失控反例
  - 1 条你准备在面试里使用的架构表达句式
- 完成标准：
  - 你已经能稳定说出“为什么不用另一个方案”

## 本模块结束时你应该具备什么
- 你能比较常见 pattern 的控制流差异
- 你能做基本架构边界判断
- 你知道真正成熟的架构不是更复杂，而是更克制
