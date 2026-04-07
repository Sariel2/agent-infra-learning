# 02 单 Agent 与 Tools 逐步执行说明

这一页会把“单 agent + tools”真正串起来。你不需要自己判断先看 schema 还是先看 loop，按这里顺着走即可。

## 使用方式
- 本模块的阅读顺序一定是：`schema -> loop -> trace -> 综合服务`。
- 不要一上来就追求复杂 agent，先把单轮最小骨架看清。
- 每做完一个 example，都回头问：这段代码在治理哪类不确定性？

## Step 1：先把边界和误区看清
- 先读 [study-map.md](./study-map.md)
- 再读 [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
- 再读 [resources/05-common-mistakes.md](./resources/05-common-mistakes.md)
- 这一步要解决什么：
  - 为什么 tool calling 不等于普通函数调用
  - 为什么 tool schema 比 prompt 更值得先治理
  - 为什么 observation 和 trace 会很重要
- 完成标准：
  - 你能讲清“单 agent 的核心不是会调函数，而是会治理模型动作”
- 如果卡住：
  - 回到 [mindmap.md](./mindmap.md)
  - 再回到 [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)

## Step 2：先把失败分类和恢复思路想透
- 读 [resources/02-deep-dive.md](./resources/02-deep-dive.md)
- 再读 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md) 的总说明
- 最后扫一遍 [resources/04-sources.md](./resources/04-sources.md)
- 这一步要解决什么：
  - 选错工具、参数错误、执行失败到底有什么区别
  - 为什么 `timeout / retry / fallback` 不是一回事
  - 为什么单 agent 已经足够暴露核心治理问题
- 完成标准：
  - 你能说清一次工具调用失败应该先归到哪一层
- 如果卡住：
  - 回到 [resources/02-deep-dive.md](./resources/02-deep-dive.md)
  - 再回到 [resources/04-sources.md](./resources/04-sources.md) 里看 `Tools Guide` 的解释

## Step 3：先跑工具 schema example
- 先读 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md) 中 `01-tool-schema` 这一节
- 再读 [examples/01-tool-schema/README.md](./examples/01-tool-schema/README.md)
- 再读 [examples/01-tool-schema/walkthrough.md](./examples/01-tool-schema/walkthrough.md)
- 然后打开 [examples/01-tool-schema/app/main.py](./examples/01-tool-schema/app/main.py)
- 最后看 [examples/01-tool-schema/tests/test_main.py](./examples/01-tool-schema/tests/test_main.py)
- 建议命令：
  - `python -m app.main`
  - `pytest`
- 这一步要重点看什么：
  - `ToolCall`
  - `ToolResult`
  - `search_docs()`
  - 为什么 `Field(min_length=1)` 这种约束重要
- 建议动手改一次：
  - 给 `ToolResult` 增加 `metadata`
  - 补实现和测试
- 完成标准：
  - 你能解释为什么统一返回结构是后面 trace 和 fallback 的前提
- 如果卡住：
  - 回到 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md)

## Step 4：再跑最小 agent loop example
- 先读 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md) 中 `02-agent-loop` 这一节
- 再读 [examples/02-agent-loop/README.md](./examples/02-agent-loop/README.md)
- 再读 [examples/02-agent-loop/walkthrough.md](./examples/02-agent-loop/walkthrough.md)
- 然后打开 [examples/02-agent-loop/app/main.py](./examples/02-agent-loop/app/main.py)
- 最后看 [examples/02-agent-loop/tests/test_main.py](./examples/02-agent-loop/tests/test_main.py)
- 建议命令：
  - `python -m app.main`
  - `pytest`
- 这一步要重点看什么：
  - `StepTrace`
  - `choose_tool()`
  - `TOOLS`
  - `run_agent()`
- 建议动手改一次：
  - 增加一个工具
  - 修改 `choose_tool()`
  - 再补 trace 断言
- 完成标准：
  - 你能解释这段一轮 loop 如何已经具备 agent 骨架
- 如果卡住：
  - 回到 [resources/02-deep-dive.md](./resources/02-deep-dive.md)

## Step 5：进入综合服务 `support-agent`
- 先读 [module-service/README.md](./module-service/README.md)
- 再读 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md) 中 `support-agent` 这一节
- 然后打开 [module-service/app/service.py](./module-service/app/service.py)
- 再看 [module-service/app/main.py](./module-service/app/main.py)
- 最后看 [module-service/tests/test_main.py](./module-service/tests/test_main.py)
- 建议命令：
  - `uvicorn app.main:app --reload`
  - `pytest`
- 这一步要重点看什么：
  - `ToolTrace`
  - 3 个工具函数
  - `run_agent()`
  - route 是否只做输入输出封装
- 完成标准：
  - 你能解释这个综合服务如何把 `schema + loop + trace` 串成一个最小单 agent 系统
- 如果卡住：
  - 回到 [project.md](./project.md)
  - 再看 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md)

## Step 6：回头对齐出处和主流语境
- 读 [resources/04-sources.md](./resources/04-sources.md)
- 推荐顺序：
  - `OpenAI Tools Guide`
  - `OpenAI Agents SDK`
  - `OpenAI File Search section`
  - `PydanticAI`
- 这一步要解决什么：
  - 把你现在读过的代码和官方语境对齐
  - 确认你理解的是“动作契约”和“运行时治理”，不是只是 API 形式
- 完成标准：
  - 你能说出至少 2 条“代码里的设计”和“出处里的原理”映射
- 如果卡住：
  - 回到 [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)

## Step 7：做收束练习并为 RAG 模块交接
- 做 [exercises.md](./exercises.md)
- 用 [review.md](./review.md) 复盘
- 再看 [project.md](./project.md)，确认自己是否准备好进入 retrieval / memory 模块
- 最少写下这 4 件事：
  - 1 条关于 tool schema 的判断
  - 1 条关于 trace 的判断
  - 1 条你观察到的失败分类
  - 1 条你准备带到第 03 模块的工程习惯
- 完成标准：
  - 你已经把工具调用看成“可治理过程”，不是“模型自己乱调函数”

## 本模块结束时你应该具备什么
- 你能解释工具调用的最小运行链路
- 你能区分 3 类常见失败
- 你知道 trace 为什么必须从早期就建立
