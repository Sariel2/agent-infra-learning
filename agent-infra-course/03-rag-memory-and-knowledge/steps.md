# 03 RAG、Memory 与 Knowledge 逐步执行说明

这一页会把 RAG 学习从“看几个概念”变成真正的链路练习。按这里走，你会从最小检索开始，一路过渡到带 citation 和短期 memory 的综合服务。

## 使用方式
- 本模块一定按 `retrieval -> memory -> 综合服务` 的顺序走。
- 每读一个文件，都问自己：这里是在处理知识、状态，还是回答输出？
- 不要过早纠结算法花样，先把链路边界读清。

## Step 1：先把 RAG 链路和边界建立起来
- 先读 [study-map.md](./study-map.md)
- 再读 [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
- 再读 [resources/05-common-mistakes.md](./resources/05-common-mistakes.md)
- 这一步要解决什么：
  - 为什么 RAG 不是“把文档塞进向量库”
  - retrieval 和 memory 的边界是什么
  - citation 为什么是系统能力
- 完成标准：
  - 你能不用看代码先讲清这条链：`文档 -> 检索 -> 上下文 -> 回答 -> citation`
- 如果卡住：
  - 回到 [mindmap.md](./mindmap.md)
  - 再回到 [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)

## Step 2：把故障层次和 memory 失败模式看透
- 读 [resources/02-deep-dive.md](./resources/02-deep-dive.md)
- 再读 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md) 的总说明
- 最后扫一遍 [resources/04-sources.md](./resources/04-sources.md)
- 这一步要解决什么：
  - 检索层、拼接层、回答层怎么区分
  - memory 为什么必须有界
  - hosted 和 self-hosted retrieval 的差异到底是什么
- 完成标准：
  - 你能拿一个错误样例，初步判断它更像哪一层问题
- 如果卡住：
  - 回到 [resources/02-deep-dive.md](./resources/02-deep-dive.md)
  - 再回到 [resources/04-sources.md](./resources/04-sources.md) 看对应出处

## Step 3：先跑本地检索 example
- 先读 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md) 中 `01-local-retrieval` 这一节
- 再读 [examples/01-local-retrieval/README.md](./examples/01-local-retrieval/README.md)
- 再读 [examples/01-local-retrieval/walkthrough.md](./examples/01-local-retrieval/walkthrough.md)
- 然后打开 [examples/01-local-retrieval/app/main.py](./examples/01-local-retrieval/app/main.py)
- 最后看 [examples/01-local-retrieval/tests/test_main.py](./examples/01-local-retrieval/tests/test_main.py)
- 建议命令：
  - `python -m app.main`
  - `pytest`
- 这一步要重点看什么：
  - `Document`
  - `RetrievalResult`
  - `DOCS`
  - `retrieve()`
- 建议动手改一次：
  - 新增一个文档
  - 改 query
  - 观察 score、排序和 citation 是否变化
- 完成标准：
  - 你能解释为什么 citation 应该和命中文档一起被结构化返回
- 如果卡住：
  - 回到 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md)

## Step 4：再跑短期 memory example
- 先读 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md) 中 `02-short-term-memory` 这一节
- 再读 [examples/02-short-term-memory/README.md](./examples/02-short-term-memory/README.md)
- 再读 [examples/02-short-term-memory/walkthrough.md](./examples/02-short-term-memory/walkthrough.md)
- 然后打开 [examples/02-short-term-memory/app/main.py](./examples/02-short-term-memory/app/main.py)
- 最后看 [examples/02-short-term-memory/tests/test_main.py](./examples/02-short-term-memory/tests/test_main.py)
- 建议命令：
  - `python -m app.main`
  - `pytest`
- 这一步要重点看什么：
  - `MemoryEntry`
  - `ConversationMemory`
  - `add()`
  - `summary()`
- 建议动手改一次：
  - 把 `limit` 改成 1 或 4
  - 再观察测试和输出变化
- 完成标准：
  - 你能解释为什么 memory 不是“把所有历史都塞回上下文”
- 如果卡住：
  - 回到 [resources/02-deep-dive.md](./resources/02-deep-dive.md)

## Step 5：进入综合服务 `knowledge-agent`
- 先读 [module-service/README.md](./module-service/README.md)
- 再读 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md) 中 `knowledge-agent` 这一节
- 然后打开 [module-service/app/service.py](./module-service/app/service.py)
- 再看 [module-service/app/main.py](./module-service/app/main.py)
- 最后看 [module-service/tests/test_main.py](./module-service/tests/test_main.py)
- 建议命令：
  - `uvicorn app.main:app --reload`
  - `pytest`
- 这一步要重点看什么：
  - `AskRequest`
  - `DOCS`
  - `Memory`
  - `retrieve()`
  - `ask()`
- 完成标准：
  - 你能解释这个服务如何把知识、citation 和短期 memory 分层组织
- 如果卡住：
  - 回到 [project.md](./project.md)
  - 再看 [resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md)

## Step 6：回头对齐 hosted、自建和框架视角
- 读 [resources/04-sources.md](./resources/04-sources.md)
- 推荐顺序：
  - `OpenAI File Search`
  - `OpenAI Embeddings Guide`
  - `Qdrant Quickstart`
  - `LlamaIndex Docs`
- 这一步要解决什么：
  - 把你现在读过的链路重新接回一手资料
  - 确认你理解了 hosted、自建、框架抽象分别在解决什么
- 完成标准：
  - 你能说出至少 3 条“代码观察”和“出处原理”的对应关系
- 如果卡住：
  - 回到 [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)

## Step 7：做收束练习并为 workflow 模块交接
- 做 [exercises.md](./exercises.md)
- 用 [review.md](./review.md) 复盘
- 再看 [project.md](./project.md)，确认自己是否已经准备好进入 workflow / trace / eval 模块
- 最少写下这 4 件事：
  - 1 条关于 citation 的判断
  - 1 条关于 memory 的判断
  - 1 条你识别出的故障层次
  - 1 条你准备带到第 04 模块的治理意识
- 完成标准：
  - 你已经把 RAG 理解成“可拆层治理的链路”，而不是黑盒问答技巧

## 本模块结束时你应该具备什么
- 你能区分 retrieval 和 memory
- 你能解释 citation 的工程价值
- 你知道为什么 knowledge service 不等于一次性问答 demo
