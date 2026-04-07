# 03 RAG、Memory 与 Knowledge 原始来源与出处详解

[返回学习地图](../study-map.md) | [返回模块首页](../README.md) | [上一篇：03-code-reading-guide.md](./03-code-reading-guide.md) | [下一篇：05-common-mistakes.md](./05-common-mistakes.md)

这一页的目标，是帮你把 RAG 相关外部资料读成“链路理解”，而不是“框架说明”。本模块最容易掉进的坑，就是只看 embedding、vector DB 或某个库的接口，然后以为自己在学 RAG。实际上，真正重要的是：文档如何进入系统、如何被检索、如何被拼接、如何带 citation、如何与 memory 协同。

## 怎么使用这一页
- 先读完本模块正文，再看这页。
- 回原文时，每次只带一个问题，不要试图一次学完整个平台。
- 用“检索层 / 拼接层 / 回答层 / memory 层”这四个视角去读资料。

## 1. [OpenAI File Search](https://platform.openai.com/docs/guides/tools-file-search)
- 为什么这个来源重要：它给出了一条 hosted retrieval 的官方路径，最适合帮助你先建立“知识问答系统可以跑起来”的成功体验。
- 这个来源原本在解决什么问题：
  - 如何把文件接入平台
  - 如何把检索能力托管给平台
  - 如何让模型基于托管检索结果回答问题
  - 如何降低自建检索链路的起步成本
- 你应该从原文里抓到的核心原理：
  - hosted retrieval 的价值是降低起步复杂度，不是替你理解检索。
  - 即使平台帮你托管了检索，你仍然需要自己理解 citation、失败分析和上下文质量。
  - 平台方案解决的是“先跑起来”，不是“你可以不理解底层”。
- 本教程吸收成了哪些内容：
  - 第 03 模块里先 hosted、后 self-hosted 的学习顺序
  - “先建立成功体验，再理解底层检索责任”的设计
  - 为什么课程强调 citation 是系统能力，不是 UI 装饰
- 读原文时重点看什么：
  - 文件进入系统的方式
  - 托管检索的边界
  - 回答与检索之间的关系
- 读完后你应该能回答：
  - 为什么 hosted retrieval 适合入门
  - 为什么 hosted 不意味着你可以跳过检索链路理解

## 2. [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)
- 为什么这个来源重要：它最重要的价值，是纠正一个非常常见的误解：embedding 只是检索链路的一环，不是 RAG 的全部。
- 这个来源原本在解决什么问题：
  - 如何把文本映射到适合相似度计算的向量空间
  - 为什么语义相近内容可以通过向量表示做近邻检索
  - 为什么 embedding 是 retrieval 的基础能力之一
- 你应该从原文里抓到的核心原理：
  - embedding 解决的是“如何表示文本”，不是“如何保证系统答对”。
  - 就算 embedding 很好，后面仍然可能在 chunk、排序、拼接、引用绑定、回答综合等环节出错。
  - RAG 效果不好时，不能一上来就怪 embedding 模型。
- 本教程吸收成了哪些内容：
  - `RAG 不是向量库` 这条判断
  - 本模块里“不要把所有问题都归因到检索模型”的思路
  - 第 03 模块深挖文档中对三层故障的拆解
- 读原文时重点看什么：
  - embedding 在检索链里的职责
  - 不同文本表示为什么能支持相似搜索
  - 它解决了什么，没有解决什么
- 读完后你应该能回答：
  - 为什么 embedding 很重要但不是全部
  - 为什么 RAG 问题必须按链路拆层分析

## 3. [Qdrant Quickstart](https://python-client.qdrant.tech/quickstart.html)
- 为什么这个来源重要：它帮助你理解 self-hosted vector DB 的最小对象模型。课程不是为了教你某个具体向量库，而是要让你第一次真正摸到“自己承担索引和查询责任”是什么感觉。
- 这个来源原本在解决什么问题：
  - collection 是什么
  - point 是什么
  - query 在自建检索中扮演什么角色
  - 自己管理向量数据意味着什么
- 你应该从原文里抓到的核心原理：
  - self-hosted retrieval 给你更多控制力，也给你更多责任。
  - 你需要开始关心索引、存储、更新、调优和查询行为。
  - “会用向量库”不等于“理解 RAG”，但它能让你更接近底层责任面。
- 本教程吸收成了哪些内容：
  - hosted vs self-hosted retrieval 的对比
  - 为什么第 03 模块会让你同时接触两条路线
  - 为什么知识系统不只是在“问答时查一下”，还包括文档生命周期
- 读原文时重点看什么：
  - collection
  - point
  - insert / query 的最小流程
  - 自己维护检索系统意味着什么
- 读完后你应该能回答：
  - 为什么自建向量库更适合理解 infra
  - 为什么它会带来维护成本和调优责任

## 4. [LlamaIndex Docs](https://docs.llamaindex.ai/)
- 为什么这个来源重要：它能帮助你从更高层抽象看 ingestion、index、retriever、query pipeline 的组织方式。它的价值不是要你改用这个框架，而是让你明白：框架本质上是在替你组织链路，而不是替你理解链路。
- 这个来源原本在解决什么问题：
  - 如何把文档接入、索引、检索和回答整合成更高层管线
  - 如何把 ingestion 和 query 看成两个不同阶段
  - 如何让开发者用更少样板把检索系统串起来
- 你应该从原文里抓到的核心原理：
  - 框架最大的作用，是帮助你组织流程。
  - 如果你不理解底层链路，就会把框架当魔法盒。
  - 如果你先理解链路，再看框架，就会知道框架在替你收敛哪些复杂度。
- 本教程吸收成了哪些内容：
  - 本模块对 `链路视角` 的强调
  - 为什么课程不断区分 ingestion、retrieval、answering、citation
  - 第 05 模块里“框架不是理解替代品”的思路
- 读原文时重点看什么：
  - ingestion pipeline
  - index / retriever / query engine 的角色
  - 框架怎样表达链路分层
- 读完后你应该能回答：
  - 为什么同一个 RAG 系统可以用不同框架实现，但本质问题不变
  - 为什么先理解链路，再学习框架会更稳

## 这一页真正想帮你建立什么
- hosted、self-hosted、framework abstraction 其实分别对应不同控制力度
- RAG 不是单点能力，而是多层链路
- 你回看资料时，应该不断问：它是在解决文档进入、检索、拼接、回答，还是治理问题

## 读完这一页后回到哪里
- 如果你想回到主线：返回 [study-map.md](../study-map.md)
- 如果你想继续执行：去 [steps.md](../steps.md)
- 如果你想重新回顾概念：去 [01-concepts-and-principles.md](./01-concepts-and-principles.md)
