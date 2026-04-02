# 03 RAG、Memory 与 Knowledge 代码导读

[返回学习地图](../study-map.md) | [返回模块首页](../README.md) | [上一篇：02-deep-dive.md](./02-deep-dive.md) | [下一篇：04-sources.md](./04-sources.md)

## 学习总原则
- 先看讲义，再看代码。
- 先看对象模型和函数签名，再看具体执行逻辑。
- 先跑测试，再改代码，再重新验证。

## Examples 阅读顺序
### 01-local-retrieval：本地检索与 citation
- 这一例子主要解决：RAG 的最小链路是什么，以及为什么 citation 是系统能力。
- 先看 [`01-local-retrieval/app/main.py`](../examples/01-local-retrieval/app/main.py)：先看 `Document`、`RetrievalResult`，再看 `retrieve()`。重点不是算法多高级，而是检索结果如何被结构化保留下来。
- 先看 [`01-local-retrieval/tests/test_main.py`](../examples/01-local-retrieval/tests/test_main.py)：看测试如何验证“排序结果是否符合预期”。
- 建议运行命令：
  - `python -m app.main`
  - `pytest`
- 建议动手实验：
  - 加入新文档，观察排序变化。
  - 修改 query，比较是否还能稳定命中。

### 02-short-term-memory：短期记忆裁剪
- 这一例子主要解决：为什么 memory 不是把对话全文塞回上下文。
- 先看 [`02-short-term-memory/app/main.py`](../examples/02-short-term-memory/app/main.py)：先看 `ConversationMemory` 的 `deque(maxlen=limit)`，这是课程里最小的“有界记忆”模型。
- 先看 [`02-short-term-memory/tests/test_main.py`](../examples/02-short-term-memory/tests/test_main.py)：看测试如何验证旧记忆被淘汰。
- 建议运行命令：
  - `python -m app.main`
  - `pytest`
- 建议动手实验：
  - 把 `limit` 调小或调大，观察记忆窗口变化。

## module-service 阅读顺序
### knowledge-agent
- 这个综合服务的目的：把检索、引用和短期记忆组合成可解释的知识问答服务。
- 先看 [`module-service/app/service.py`](../module-service/app/service.py)：先看 `DOCS`、`Memory`、`retrieve()` 与 `ask()`。你要看到知识、记忆和响应模型是如何被分开的。
- 先看 [`module-service/app/main.py`](../module-service/app/main.py)：再看 `/ask` 路由如何只承担 HTTP 入口职责。
- 先看 [`module-service/tests/test_main.py`](../module-service/tests/test_main.py)：最后看测试如何确认响应里必须包含 citation。
- 建议运行命令：
  - `uvicorn app.main:app --reload`
  - `pytest`
