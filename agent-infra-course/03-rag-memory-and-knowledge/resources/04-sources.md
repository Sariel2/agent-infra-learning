# 03 RAG、Memory 与 Knowledge 原始来源与出处详解

[返回学习地图](../study-map.md) | [返回模块首页](../README.md) | [上一篇：03-code-reading-guide.md](./03-code-reading-guide.md) | [下一篇：05-common-mistakes.md](./05-common-mistakes.md)


这一页不是“链接仓库”，而是本模块讲义的出处解释页。你可以把它理解成：我为什么引用这些来源、这些来源里最值得看的部分是什么、以及这些内容在本教程里被翻译成了哪一段讲义。

## 怎么使用这一页
- 先把本模块前面的讲义读完，再来看这里。
- 看每个来源时，不要试图通读整站，只看这里标出的重点。
- 把这一页当成“出处说明 + 精读提示”，不是新的主教程。

## 1. [OpenAI File Search](https://platform.openai.com/docs/guides/tools-file-search)
- 为什么这个来源重要：它给出了一条 hosted retrieval 的官方路径，适合帮助你先建立“知识问答可以跑起来”的成功体验。
- 建议重点看：
  - 看文件接入、向量存储与回答引用的大致关系
  - 重点理解 hosted 方案的边界
- 它在本教程里的对应位置：对应讲义里“为什么先理解 hosted retrieval，再看 self-hosted vector DB”。
- 我从原文里提炼出的关键结论：
  - hosted retrieval 的价值在于降低起步复杂度。
  - 但即使平台托管了检索，你仍然要理解 citation 和失败分析。

## 2. [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)
- 为什么这个来源重要：这个来源最重要的价值是纠正误解：embedding 只是检索链路的一环，不是 RAG 的全部。
- 建议重点看：
  - 理解 embedding 在检索中的角色
  - 不必一开始钻模型细节
- 它在本教程里的对应位置：对应讲义中“RAG 不是向量库”的部分。
- 我从原文里提炼出的关键结论：
  - 检索效果取决于 chunk、索引、召回、引用和回答综合，而不只取决于 embedding。

## 3. [Qdrant Quickstart](https://python-client.qdrant.tech/quickstart.html)
- 为什么这个来源重要：它帮助你理解 self-hosted vector DB 的最小组件和操作模型。
- 建议重点看：
  - 看 collection、point、query 这些最小对象
  - 把注意力放在“索引与查询的基本形状”
- 它在本教程里的对应位置：对应讲义里对 hosted 与 self-hosted 的比较。
- 我从原文里提炼出的关键结论：
  - 自建向量库给你更多控制力，但也引入维护成本和调优责任。

## 4. [LlamaIndex Docs](https://docs.llamaindex.ai/)
- 为什么这个来源重要：它能帮助你从更高层次看 ingestion、index 和 query pipeline 的组织方式。
- 建议重点看：
  - 只看检索和索引抽象，不要一开始学完整框架
- 它在本教程里的对应位置：对应本模块的“链路视角”和“框架只是组织方式”这两个观点。
- 我从原文里提炼出的关键结论：
  - 框架不是替代理解，而是建立在理解之上的组织工具。

## 读完这一页后回到哪里
- 如果你想回到主线：返回 [study-map.md](../study-map.md)
- 如果你想继续执行：去 [steps.md](../steps.md)
- 如果你想重新回顾概念：去 [01-concepts-and-principles.md](./01-concepts-and-principles.md)
