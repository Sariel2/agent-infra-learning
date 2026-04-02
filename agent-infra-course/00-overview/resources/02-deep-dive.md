# 00 总览与准备 细节深挖

[返回学习地图](../study-map.md) | [返回模块首页](../README.md) | [上一篇：01-concepts-and-principles.md](./01-concepts-and-principles.md) | [下一篇：03-code-reading-guide.md](./03-code-reading-guide.md)

## 1. 课程为什么要按模块递进
这套课程的模块顺序不是随便排的，而是按照复杂度依赖关系排的：
- 先有 Python 工程基础，才能写 provider 和 service。
- 先有结构化输出，才能做稳定 tool calling。
- 先有 tool 和 retrieval，才能谈 workflow 编排。
- 先有 workflow，才能高质量做 trace 和 eval。
- 先有完整工程实践，才有资格谈架构模式和转型表达。

## 2. 学习系统本身也是一个“工程系统”
你会发现本模块的 examples 很简单，但它们在传达一个重要习惯：任何东西都应该有对象模型、最小测试和可观测输出。这不是形式主义，而是在训练你把后面更复杂的 agent 行为也用同样方式拆开。

## 3. 为什么要做学习日志与失败记录
后面调 RAG 或 tool selection 时，最大的敌人不是不会写代码，而是“没有证据”。没有证据你就没法回答：
- 到底是 prompt 变了，还是检索变了。
- 到底是 tool schema 问题，还是调用执行问题。
- 到底是偶发现象，还是系统性退化。

所以这个模块虽然看起来“软”，实际上是在给后面所有硬问题做工程准备。
