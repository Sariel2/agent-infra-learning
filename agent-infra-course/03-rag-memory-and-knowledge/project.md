# 03 RAG、Memory 与 Knowledge项目任务

## 项目名
`knowledge-agent`

## 项目目标
让 Agent 可以对接文档资料，支持检索式问答，并给出引用来源，同时保留适度会话记忆。

## 必做项
- 能导入一批 Markdown 或 PDF 资料
- 能建立索引并执行检索
- 回答时附 citation
- 支持简单的对话历史记忆
- 记录检索命中信息

## 加分项
- 比较两种 chunk 方案
- 比较 hosted 与 self-hosted 成本和体验
- 记录 top-k 调优结果

## 验收标准
- 至少 15 条知识问答 case
- 至少 5 条失败 case 有分析
- 能清楚说明当前最影响效果的参数
