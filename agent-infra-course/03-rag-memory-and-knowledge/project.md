# 03 RAG、Memory 与 Knowledge 模块综合项目说明

## 项目名
`knowledge-agent`

## 项目定位
这是整门课第一个真正的知识服务。它不是一次性“问文档” demo，而是要把检索、citation、短期 memory 和失败记录组合成一个可解释的知识问答系统。

## 对应综合服务
- 服务入口：[module-service/app/main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/03-rag-memory-and-knowledge/module-service/app/main.py)
- 服务逻辑：[module-service/app/service.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/03-rag-memory-and-knowledge/module-service/app/service.py)
- 测试入口：[module-service/tests/test_main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/03-rag-memory-and-knowledge/module-service/tests/test_main.py)

## 项目目标
让 agent 可以对接文档资料，支持检索式问答，并且：
- 返回 citation
- 保留适度短期 memory
- 记录知识命中与失败样本

## 你最终应该学到什么
- retrieval 和 memory 的边界
- citation 为什么是系统能力
- hosted 和 self-hosted retrieval 的差异
- 为什么知识服务要以链路视角治理

## 必做项
- 至少有一批结构化文档或文本资料
- 能执行最小检索
- 回答时必须附 citation
- 支持简单有界 memory
- 能解释至少 1 类失败来自哪一层

## 推荐实现顺序
1. 先跑 `examples/01-local-retrieval`
2. 再跑 `examples/02-short-term-memory`
3. 再读 [resources/03-code-reading-guide.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/03-rag-memory-and-knowledge/resources/03-code-reading-guide.md)
4. 再回到 `knowledge-agent`
5. 最后做 [review.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/03-rag-memory-and-knowledge/review.md)

## 实现清单
- `DOCS` 或等价知识集合明确存在
- `retrieve()` 明确返回命中和 citation
- `Memory` 或等价对象明确有界
- `ask()` 把检索、citation、memory 串起来
- 测试必须检查 citations 是否出现在响应中

## 验收清单
- 我能演示至少 10-15 条知识问答案例
- 我能指出至少 3-5 条失败样例并做简单归因
- 我能解释当前最影响效果的 1-2 个参数
- 我能说明哪些问题适合 RAG，哪些更适合 tool calling
- 我能解释 memory 为什么不能无限增长

## 常见退化点
- 只有回答，没有 citation
- 检索能跑，但知识和对话状态混在一起
- 只关注命中，不关注回答和引用是否一致
- 只凭感觉调效果，不保留失败样本

## 加分项
- 比较两种 chunk 方案
- 比较 hosted 与 self-hosted 体验
- 记录 top-k、chunk size 等调参结论
- 为 citation mismatch 设计一条单独分析记录

## 交付物
- 一个可解释的知识问答服务
- 一组带 citations 的最小测试
- 一份失败样本记录和初步归因表

## 进入下一模块前，你应该能回答
- 为什么 RAG 问题必须拆层分析
- 为什么 citation 不能缺席
- 为什么 knowledge system 比单次问答复杂得多
