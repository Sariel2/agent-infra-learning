# 03 RAG、Memory 与 Knowledge 代码导读

[返回学习地图](../study-map.md) | [返回模块首页](../README.md) | [上一篇：02-deep-dive.md](./02-deep-dive.md) | [下一篇：04-sources.md](./04-sources.md)

这一页要带你把 RAG 读成一条链，而不是几段零散代码。第 03 模块真正要看懂的是：
- 文档怎样被表示
- 检索结果怎样被结构化
- citation 怎样被保留下来
- memory 怎样被限制在有界范围内

## 怎么读这一页
- 先看 retrieval example，再看 memory example，最后回到综合服务。
- 每个文件都先找“最小知识单元对象”，再看流程函数。
- 读的时候不断问：这里是在解决检索问题、引用问题，还是状态问题？

## 推荐总顺序
1. 看 `examples/01-local-retrieval`
2. 看 `examples/02-short-term-memory`
3. 看 `module-service/app/service.py`
4. 看 `module-service/app/main.py`
5. 看 `module-service/tests/test_main.py`

## Example 1：`01-local-retrieval`
入口文件：
- [examples/01-local-retrieval/app/main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/03-rag-memory-and-knowledge/examples/01-local-retrieval/app/main.py)
- [examples/01-local-retrieval/tests/test_main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/03-rag-memory-and-knowledge/examples/01-local-retrieval/tests/test_main.py)
- [examples/01-local-retrieval/walkthrough.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/03-rag-memory-and-knowledge/examples/01-local-retrieval/walkthrough.md)

先看这几个点：
- `Document`
- `RetrievalResult`
- `DOCS`
- `retrieve()`

第一眼应该理解什么：
- `Document` 是最小知识单元。
- `RetrievalResult` 把“检索命中”变成了带分数和 citation 的对象。
- `retrieve()` 虽然算法很朴素，但它把“query -> score -> citation”的链路完整保留下来了。

接着看测试时重点看：
- 排序结果是不是可预测
- citation 是否和命中文档绑定

建议你动手改一次：
- 新增一个文档
- 改 query
- 观察 score 和排序如何变化

## Example 2：`02-short-term-memory`
入口文件：
- [examples/02-short-term-memory/app/main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/03-rag-memory-and-knowledge/examples/02-short-term-memory/app/main.py)
- [examples/02-short-term-memory/tests/test_main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/03-rag-memory-and-knowledge/examples/02-short-term-memory/tests/test_main.py)
- [examples/02-short-term-memory/walkthrough.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/03-rag-memory-and-knowledge/examples/02-short-term-memory/walkthrough.md)

先看这几个点：
- `MemoryEntry`
- `ConversationMemory`
- `add()`
- `summary()`

第一眼应该理解什么：
- `MemoryEntry` 把对话状态对象化，而不是直接堆字符串。
- `ConversationMemory(limit=...)` 通过 `deque(maxlen=limit)` 显式表达“有界记忆”。
- `summary()` 不是花哨功能，它在表达“记忆最终要能被稳定消费”。

接着看测试时重点看：
- 旧消息是否被淘汰
- 记忆窗口大小变化是否可预测

建议你动手改一次：
- 把 `limit` 改成 1 或 4
- 看输出和测试预期如何变化

## 最后看综合服务：`knowledge-agent`
入口文件：
- [module-service/app/service.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/03-rag-memory-and-knowledge/module-service/app/service.py)
- [module-service/app/main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/03-rag-memory-and-knowledge/module-service/app/main.py)
- [module-service/tests/test_main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/03-rag-memory-and-knowledge/module-service/tests/test_main.py)
- [module-service/README.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/03-rag-memory-and-knowledge/module-service/README.md)

推荐读码顺序：
1. 先看 `AskRequest`
2. 再看 `DOCS`
3. 再看 `Memory`
4. 再看 `retrieve()`
5. 最后看 `ask()`

第一眼应该理解什么：
- `DOCS` 和 `Memory` 被明确分开，分别代表知识和状态。
- `retrieve()` 返回的是 `(answer, citation)`，这在强调 citation 不是附属字段。
- `ask()` 把检索、引用和短期记忆串成一个最小 knowledge service。

接着再看 `app/main.py` 时重点看：
- `/ask` 之类的入口是否只承担协议职责
- 知识处理逻辑是否留在 service 层

最后看测试时重点看：
- 响应中是否稳定保留 `citations`
- `memory` 是否随着问题增加而更新

## 这一页最容易读偏的地方
- 误区一：只关注检索算法
  - 这个模块更重要的是链路结构，而不是算法花样。
- 误区二：把 memory 当成附加小功能
  - 它其实是在训练状态边界。
- 误区三：忽略 citation
  - citation 是系统可审计性的最小入口。

## 读完这一页后应该回哪里
- 如果你想继续执行：去 [steps.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/03-rag-memory-and-knowledge/steps.md)
- 如果你想回顾原理：去 [02-deep-dive.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/03-rag-memory-and-knowledge/resources/02-deep-dive.md)
- 如果你想看出处解释：去 [04-sources.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/03-rag-memory-and-knowledge/resources/04-sources.md)
