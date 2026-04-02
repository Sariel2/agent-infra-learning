# 03 RAG、Memory 与 Knowledge

这一阶段要把 Agent 从“会调用函数”升级成“能基于外部知识可靠工作”。重点不只是调通向量库，而是理解知识管道、检索质量和记忆边界。

## 阶段目标
- 跑通一条完整 RAG 链路
- 理解 hosted retrieval 和 self-hosted retrieval 的区别
- 给 Agent 加上最小可用的对话记忆

## 核心主题
- chunking
- embedding
- indexing
- retrieval
- citation
- short-term memory

## 阶段产出
- 一个 `knowledge-agent`
- 一套资料导入和检索流程
- 一份检索失败分析

## 完成标准
- 回答可以引用知识来源
- 你能解释为什么某些问题检索效果差
- 你能区分 memory 和 retrieval 的职责
