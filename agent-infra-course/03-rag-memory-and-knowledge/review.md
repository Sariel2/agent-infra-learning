# 03 RAG、Memory 与 Knowledge 复盘模板

这一页用来判断：你是真的把 RAG 理解成一条可拆层治理的链路，还是只是会跑一个检索 demo。第 03 模块最关键的，不是向量库本身，而是你是否把 retrieval、citation、memory、回答综合这些边界分清楚了。

## 什么时候做这页复盘
- 完成 [steps.md](./steps.md) 后做
- 跑过两个 example 和 `knowledge-agent` 后做
- 进入第 04 模块前再回看一次

## 一、模块总结
请先用 5-8 句话回答：
- 为什么 RAG 不是“把文档塞进向量库”
- retrieval 和 memory 的边界是什么
- citation 为什么是系统能力
- hosted 和 self-hosted retrieval 分别适合什么阶段

如果写不顺，优先回看：
- [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
- [resources/02-deep-dive.md](./resources/02-deep-dive.md)

## 二、自查清单
逐条回答 `是 / 否 / 部分做到`，并补一句证据。

- 我是否已经能把 RAG 链路拆成检索、拼接、回答几层
- citation 是否真的能回溯到来源
- memory 是否帮助了连续问答，而不是制造噪音
- 我是否区分了“没检索到”和“检索到了但回答错了”
- 我是否能说明 hosted 和 self-hosted 的控制力差异
- 我是否还在把主观效果误当成唯一评估方式

## 三、失败归因表
把你遇到的知识问答问题尽量归到正确层。

| 现象 | 更可能的问题层 | 根因猜测 | 下一步动作 |
|---|---|---|---|
| 完全没命中相关内容 | 检索层 | chunk / query / 匹配规则不合适 | 回看 `retrieve()` 和检索 example |
| 命中了但 citation 对不上 | 引用层 | citation 绑定或回答综合有问题 | 回看 `RetrievalResult` 和 `ask()` |
| 上下文里有答案但最终答错 | 回答层 | 综合阶段失真 | 回看 deep dive 对三层故障的拆分 |
| 连续对话越聊越乱 | memory 层 | 记忆无界或噪音过多 | 回看 `ConversationMemory` / `Memory` |

## 四、常见坑对照
看看你是否已经踩中以下任一项。

- 盲目追求大 chunk
- 没有保留原文出处
- 把完整对话都塞回上下文
- 只看主观效果，不记失败样本
- 把所有问题都怪到 embedding 或向量库上

如果踩中了，请写：
- 我踩中了哪一条
- 它具体导致了什么现象
- 我准备怎么收回来

## 五、最小输出模板
请至少填完下面 6 项：

- 哪类问题最适合 RAG：
- 哪类问题更适合直接 tool calling：
- 我当前最常见的 1 类 citation 风险：
- 我当前 memory 设计最可能污染系统的 1 个点：
- 如果继续优化，我会优先动检索、拼接还是回答层：
- 进入 workflow 模块前，我最想保留的 1 条治理意识：

## 六、通过标准
满足下面这些条件，才算真的可以进入第 04 模块。

- 我已经能区分 retrieval 和 memory
- 我知道 citation 为什么必须进入响应结构
- 我能拆分 RAG 的常见故障层次
- 我知道知识服务不等于一次性问答脚本
- 我开始具备“失败样本要留下来”的意识

## 七、下一步行动
从下面 3 个动作里，至少写 1 个马上要执行的动作。

- 打开 [04-workflow-observability-and-evals/steps.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/04-workflow-observability-and-evals/steps.md)，开始 workflow 模块
- 给当前 `knowledge-agent` 增加 1 个新的检索失败样本
- 把你最担心的 citation 错误写成 1 条测试假设
