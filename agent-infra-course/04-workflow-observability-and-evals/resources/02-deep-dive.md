# 04 Workflow、Observability 与 Evals 细节深挖

[返回学习地图](../study-map.md) | [返回模块首页](../README.md) | [上一篇：01-concepts-and-principles.md](./01-concepts-and-principles.md) | [下一篇：03-code-reading-guide.md](./03-code-reading-guide.md)

## 1. workflow 和 agent 的边界
这不是二选一，而是分工问题。workflow 负责固定结构，agent 负责局部开放性决策。很多稳定系统都是“workflow 包住 agent”，而不是“让 agent 接管一切”。

## 2. trace 中最值得记录的元数据
课程里示例简化了元数据，但在真实系统里，至少应该考虑：
- request id
- node name
- elapsed time
- tool name 或 retrieval info
- environment / experiment tag

这些字段决定了你后面能否做跨版本比较、问题归因和性能分析。

## 3. eval dataset 应该长什么样
一个最小 eval case 至少需要：
- 输入
- 期望行为或期望节点
- 评估规则
- 可选的备注或标签

重要的不是题量多，而是覆盖稳定、可重复。课程示例故意做得很小，就是为了让你先建立“固定样本比较”的意识。
