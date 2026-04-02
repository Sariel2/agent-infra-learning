# Agent Infra Final Exam

## 一、选择题
1. 在 agent infra 中，最适合承接“显式步骤与条件分支”的能力是：
A. Prompt 模板
B. Workflow
C. Embedding 模型
D. 简历 bullet

2. 以下哪项最能帮助你定位单次运行中 agent 为什么失败：
A. 只看最终回答
B. trace
C. 只看系统提示词
D. 只看 token 数

3. 如果一个任务步骤固定、失败代价高、人工审核点明确，最优先考虑的是：
A. 自由 agent
B. multi-agent
C. workflow
D. 纯向量检索

4. 在 RAG 系统里，citation 的主要工程价值是：
A. 提升回答长度
B. 让页面更好看
C. 提供答案来源证据
D. 替代 eval

5. provider abstraction 最主要解决的问题是：
A. 提高 GPU 利用率
B. 解耦模型接入实现与业务逻辑
C. 自动降低 token 成本
D. 自动生成前端页面

## 二、判断题
6. 只要引入 function calling，就已经拥有完整的 agent runtime。对 / 错
7. 有日志就等于有 trace。对 / 错
8. 在课程里，memory 的设计原则之一是避免把完整历史无限回塞。对 / 错
9. eval dataset 应该尽量固定，方便回归比较。对 / 错
10. multi-agent 默认比 single-agent 更先进也更值得优先采用。对 / 错

## 三、简答题
11. 为什么这套课程强调先做 fake provider，再接真实模型。
12. 说明 tool schema 设计不佳会如何影响 agent 质量。
13. 解释 memory 与 retrieval 的职责边界。
14. 解释 trace、log、eval 三者的不同。

## 四、场景分析题
15. 一个支持场景 agent 在“查订单”和“回答政策问题”两个任务上表现不稳定。请给出一个排查顺序，覆盖 tool、RAG、workflow、trace 至少 3 个维度。
16. 一个团队把所有场景都做成自由 agent，结果系统难以调试、结果波动大。请给出重构建议。
17. 一个知识问答系统经常“看起来像答对了”，但引用来源总是对不上。请分析可能的失败模式。

## 五、系统设计题
18. 设计一个最小 `support-agent` 服务，要求包含：
- 单 agent loop
- 3 个工具
- 工具轨迹记录
- 失败恢复
- 基础测试思路

19. 设计一个最小 `knowledge-agent` 服务，要求包含：
- 检索
- citation
- 短期 memory
- 失败样本记录
- 1 组基础 eval 指标

## 六、项目讲解题
20. 用 3 分钟口径讲述你做的 `agent-runtime` 项目，至少覆盖目标、架构、失败案例、优化收益。
21. 把你的课程主项目写成 2 条适合简历的项目描述，一条偏业务价值，一条偏 infra 能力。
