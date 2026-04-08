# knowledge-agent

把检索、citation 和短期 memory 组合成可解释的知识问答服务。

## 这个综合服务的目标
- 把“找到资料”和“组织回答”明确拆成不同阶段。
- 让 citation 成为响应的一部分，而不是后补的展示字段。
- 用最小 memory 结构演示“会话状态”和“知识检索”不是一回事。

## 开始前先回看
- 模块首页：[../README.md](../README.md)
- 学习地图：[../study-map.md](../study-map.md)
- 概念讲义：[../resources/01-concepts-and-principles.md](../resources/01-concepts-and-principles.md)
- 原理细节：[../resources/02-deep-dive.md](../resources/02-deep-dive.md)
- 代码导读：[../resources/03-code-reading-guide.md](../resources/03-code-reading-guide.md)
- 示例 1：[../examples/01-local-retrieval/app/main.py](../examples/01-local-retrieval/app/main.py)
- 示例 2：[../examples/02-short-term-memory/app/main.py](../examples/02-short-term-memory/app/main.py)

## 先理解这 3 个文件
- 核心逻辑：[app/service.py](./app/service.py)
  先看 `DOCS`、`Memory`、`retrieve()` 和 `ask()`，理解检索、记忆和回答是怎么拆开的。
- HTTP 入口：[app/main.py](./app/main.py)
  看 `/ask` 如何只承担请求入口，而不是在路由里做检索细节。
- 最小验收：[tests/test_main.py](./tests/test_main.py)
  看测试为什么先断言 `citations`，因为可追溯性是这里的硬要求。

## 推荐实现顺序
1. 先读 [app/service.py](./app/service.py)，重点理解 `retrieve()` 和 `ask()` 的职责区别。
2. 再看 `Memory` 类，确认它只处理最近会话记录，不处理外部知识。
3. 读 [tests/test_main.py](./tests/test_main.py)，理解为什么这里优先测 citation。
4. 最后看 [app/main.py](./app/main.py)，确认接口层没有偷偷拼 citation。

## 动手实现时每一步做什么
### Step 1：先固定知识源与检索函数
- 要改的文件：[app/service.py](./app/service.py)
- 要做的事：先把 `DOCS` 和 `retrieve()` 写成稳定的“取资料”能力。
- 验收标准：`retrieve()` 必须返回“答案片段 + citation”，而不是只有文本。

### Step 2：再增加短期 memory
- 要改的文件：[app/service.py](./app/service.py)
- 要做的事：用 `Memory` 保存最近问题，避免把所有历史都塞回上下文。
- 验收标准：`ask()` 返回里同时能看到 citations 和 memory。

### Step 3：最后暴露问答接口与测试
- 要改的文件：[app/main.py](./app/main.py)
- 要改的文件：[tests/test_main.py](./tests/test_main.py)
- 要做的事：通过 `/ask` 暴露服务，并确保测试固定响应中的 citation 行为。
- 验收标准：问答响应中必须有 `citations` 字段。

## 建议运行命令
- `uvicorn app.main:app --reload`
- `pytest`

## 常见退化点
- 把 citation 当展示装饰，而不是质量治理数据。
- 用 memory 代替 retrieval，导致知识边界混乱。
- 检索命中了正确内容，但回答阶段丢失了 citation。

## 扩展时优先做什么
- 把内存字典替换成更真实的检索源或向量库。
- 记录 `retrieval miss`、`citation mismatch`、`answer drift` 三类失败样本。
- 为后续 eval 增加 `hit rate` 和 `citation accuracy` 指标。

## 学完后你应该能回答
- 为什么 memory 与 retrieval 的职责必须分开。
- 为什么 citation 是工程能力，不只是展示能力。
- 如果问答系统“像答对了但引文不对”，你应该先查哪里。
