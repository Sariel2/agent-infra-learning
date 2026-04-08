# 03 RAG、Memory 与 Knowledge 练习手册

## 这份练习怎么用
- 先按 [steps.md](./steps.md) 跑通 `local retrieval` 和 `short-term memory` 两个 example。
- 本模块练习一定要同时从“检索链路”和“会话状态”两个维度思考。
- 每道题都尽量回到 citation、失败样本和调优动作上。

## 做题前回看
- 学习路线：[study-map.md](./study-map.md)
- 概念讲义：[resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
- 原理细节：[resources/02-deep-dive.md](./resources/02-deep-dive.md)
- 代码导读：[resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md)
- 示例 1：[examples/01-local-retrieval/app/main.py](./examples/01-local-retrieval/app/main.py)
- 示例 2：[examples/02-short-term-memory/app/main.py](./examples/02-short-term-memory/app/main.py)
- 综合服务：[module-service/app/main.py](./module-service/app/main.py)
- 综合测试：[module-service/tests/test_main.py](./module-service/tests/test_main.py)

## 练习 1：拆解最小 RAG 链路
- 先回看：[resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
- 题目：按顺序解释 `ingestion -> chunking -> indexing -> retrieval -> answer synthesis -> citation` 这条链路每一步在解决什么问题。
- 输出要求：每一步至少写两句。
- 完成标准：你能指出哪一步出错会导致“看起来答得像对，但引用不对”。

## 练习 2：memory 与 retrieval 的边界
- 先回看：[resources/02-deep-dive.md](./resources/02-deep-dive.md)
- 对应代码：[examples/02-short-term-memory/app/main.py](./examples/02-short-term-memory/app/main.py)
- 题目：解释为什么“把历史消息一直塞回上下文”不等于 memory 设计，并说明 retrieval 什么时候不应该承担记忆职责。
- 输出要求：分边界、反例、正确做法三段来写。
- 完成标准：你能说清 memory 面向会话状态，retrieval 面向外部知识。

## 练习 3：设计 citation 响应模型
- 先回看：[resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
- 对应代码：[examples/01-local-retrieval/app/main.py](./examples/01-local-retrieval/app/main.py)
- 题目：设计一个带 citation 的问答响应模型，要求后续 trace 和 eval 能直接使用。
- 输出要求：至少包含 `answer`、`citations`、`retrieval_hits`、`confidence` 四部分。
- 完成标准：citation 字段必须能追到具体文档或 chunk，而不是只有一个模糊来源名。

## 练习 4：排查“回答空泛”
- 先回看：[resources/05-common-mistakes.md](./resources/05-common-mistakes.md)
- 对应代码：[module-service/app/main.py](./module-service/app/main.py)
- 题目：当问题问得很准，但系统总回答空泛，请给出一个从检索到生成的排查顺序。
- 输出要求：至少覆盖 chunk、召回、排序、上下文组装、回答阶段五个点。
- 完成标准：你的排查顺序必须先检查“系统有没有拿到正确材料”，再检查“模型怎么回答”。

## 练习 5：设计失败样本记录表
- 先回看：[project.md](./project.md)
- 对应代码：[module-service/tests/test_main.py](./module-service/tests/test_main.py)
- 题目：设计一份失败样本记录表，要求能区分 `retrieval miss`、`citation mismatch`、`answer drift`。
- 输出要求：写出字段并说明用途。
- 完成标准：表结构必须能支撑后续 eval 与回归比较。

## 练习 6：综合服务讲解
- 先回看：[module-service/README.md](./module-service/README.md)
- 对应代码：[module-service/app/main.py](./module-service/app/main.py)
- 题目：用 2 分钟口径讲清 `knowledge-agent` 的完整链路，并指出最容易退化的两处。
- 输出要求：一段完整口述稿。
- 完成标准：必须覆盖检索、citation、memory、失败记录四个关键词。

## 完成后自检
- 你能解释 citation 为什么是质量治理手段。
- 你能分清“没检到”和“检到了但答偏了”。
- 你已经有一份可执行的失败样本记录表。
- 你知道如何把本模块结果接入下一模块的 trace 和 eval。
