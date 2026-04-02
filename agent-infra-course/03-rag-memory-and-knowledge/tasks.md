# 03 RAG、Memory 与 Knowledge任务安排

## Day 1：RAG 基本链路
- 理解文档导入、切分、向量化、检索、拼接上下文
- 先用 hosted file search 跑通一版
- 记录 5 条基础问答 case

## Day 2：自建向量检索
- 用 `Qdrant` 建一版最小向量索引
- 比较 hosted 与 self-hosted 的使用体验
- 记录索引流程与检索参数

## Day 3：知识质量优化
- 比较不同 chunk 策略
- 观察召回条数变化对答案质量的影响
- 补 citation 输出

## Day 4：加入记忆
- 设计短期会话 memory
- 限制记忆长度和保留规则
- 观察记忆是否污染上下文

## Day 5：失败分析
- 记录检索不到、召回错、答案跑偏三类问题
- 为每类问题给出一个修复思路
- 更新项目文档

## 退出条件
- 至少有一版 hosted RAG 和一版 self-hosted RAG
- 至少能说清 5 个检索失败原因
