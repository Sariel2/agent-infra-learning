# Final Exam Answers

## 使用说明
- 这份答案不是只给结果，而是给你一条复习路径。
- 每道题后面的“回链模块”都指向最适合复习的课程位置。
- 如果你答错，不要只看正确答案，先回到对应模块重做一遍 example 或综合服务。

## 一、选择题
1. 正确答案：B
- 为什么对：workflow 负责显式步骤、条件分支和状态流转，这正是固定流程任务最需要的能力。
- 为什么其他选项不对：prompt 模板只是在组织输入，不承担稳定流程控制；embedding 模型与流程建模无关；简历 bullet 更不是运行时机制。
- 工程判断：当步骤固定且失败代价高时，优先 workflow。
- 回链模块：[04-workflow-observability-and-evals/resources/01-concepts-and-principles.md](../04-workflow-observability-and-evals/resources/01-concepts-and-principles.md)

2. 正确答案：B
- 为什么对：trace 能展示一次运行里的中间节点、工具选择、输入输出与状态变化。
- 为什么其他选项不对：只看最终回答只能看到结果，看不到过程；只看提示词无法确认模型到底经历了什么；token 数只能看成本，不能定位故障。
- 工程判断：没有过程可见性，就很难稳定迭代 agent。
- 回链模块：[04-workflow-observability-and-evals/resources/02-deep-dive.md](../04-workflow-observability-and-evals/resources/02-deep-dive.md)

3. 正确答案：C
- 为什么对：固定步骤、高失败代价、可审核，都是 workflow 优先信号。
- 为什么其他选项不对：自由 agent 和 multi-agent 都会引入更高的不确定性；纯向量检索不负责流程控制。
- 工程判断：能固定的步骤先固定。
- 回链模块：[05-agent-theory-and-architecture/resources/01-concepts-and-principles.md](../05-agent-theory-and-architecture/resources/01-concepts-and-principles.md)

4. 正确答案：C
- 为什么对：citation 的核心价值是让答案能回溯证据，从而支持质量治理。
- 为什么其他选项不对：citation 不是为了让内容更长、更好看，也不能替代 eval。
- 工程判断：没有 citation，RAG 很难做可靠性分析。
- 回链模块：[03-rag-memory-and-knowledge/resources/01-concepts-and-principles.md](../03-rag-memory-and-knowledge/resources/01-concepts-and-principles.md)

5. 正确答案：B
- 为什么对：provider abstraction 把模型接入实现从业务逻辑里拆出来，利于测试和替换。
- 为什么其他选项不对：它不会自动提高 GPU 利用率，也不会自动降低成本或生成 UI。
- 工程判断：先有清晰 provider 边界，后面才能自由替换真实或 fake 模型。
- 回链模块：[01-python-agent-foundations/resources/02-deep-dive.md](../01-python-agent-foundations/resources/02-deep-dive.md)

## 二、判断题
6. 错
- 解析：function calling 只是 agent runtime 的一个能力，完整 runtime 还涉及状态、轨迹、失败恢复和治理。
- 回链模块：[02-single-agent-with-tools/resources/02-deep-dive.md](../02-single-agent-with-tools/resources/02-deep-dive.md)

7. 错
- 解析：日志通常是离散文本事件，trace 是结构化运行过程记录。两者都重要，但不是一回事。
- 回链模块：[04-workflow-observability-and-evals/resources/01-concepts-and-principles.md](../04-workflow-observability-and-evals/resources/01-concepts-and-principles.md)

8. 对
- 解析：记忆需要裁剪和提炼，否则会带来上下文污染、成本上升和行为漂移。
- 回链模块：[03-rag-memory-and-knowledge/resources/02-deep-dive.md](../03-rag-memory-and-knowledge/resources/02-deep-dive.md)

9. 对
- 解析：固定 eval dataset 才能支撑回归比较和版本对照，否则你无法判断优化是真有效还是只是样本变化。
- 回链模块：[04-workflow-observability-and-evals/resources/02-deep-dive.md](../04-workflow-observability-and-evals/resources/02-deep-dive.md)

10. 错
- 解析：multi-agent 是复杂度更高的模式，不应默认优先。很多任务用 single-agent 或 workflow 就足够。
- 回链模块：[05-agent-theory-and-architecture/resources/05-common-mistakes.md](../05-agent-theory-and-architecture/resources/05-common-mistakes.md)

## 三、简答题参考
11. 先做 fake provider 的原因
- 它能先固定接口与数据流，减少把外部 API 波动和工程设计问题混在一起。
- 它让测试更容易写，也更适合先验证 route、service、schema 边界。
- 工程上，先让接口和测试稳定，再接真实依赖更高效。
- 回链模块：[01-python-agent-foundations/exercises.md](../01-python-agent-foundations/exercises.md)

12. tool schema 设计不佳的影响
- 模型难以稳定选择工具。
- 参数生成容易出错或缺失。
- 工具失败难以被统一处理。
- trace 很难统一分析，因为返回结构不稳定。
- 回链模块：[02-single-agent-with-tools/resources/01-concepts-and-principles.md](../02-single-agent-with-tools/resources/01-concepts-and-principles.md)

13. memory 与 retrieval 的职责边界
- retrieval 负责从外部知识源取回和当前问题相关的客观资料。
- memory 负责保留会话上下文中的短期用户状态、偏好或最近交流事实。
- retrieval 面向知识，memory 面向对话过程。
- 回链模块：[03-rag-memory-and-knowledge/resources/02-deep-dive.md](../03-rag-memory-and-knowledge/resources/02-deep-dive.md)

14. trace、log、eval 的不同
- log：离散事件记录，便于快速排错。
- trace：结构化过程记录，便于理解一次运行内部发生了什么。
- eval：把系统放到固定数据集上比较质量、稳定性、成本和延迟。
- 回链模块：[04-workflow-observability-and-evals/exercises.md](../04-workflow-observability-and-evals/exercises.md)

## 四、场景分析题参考
15. 排查顺序示例
- 先看 trace：确认查订单和政策问答分别走了哪些节点。
- 再看 tool：查订单是否稳定选择了 `get_order_status`，参数是否正确。
- 再看 RAG：政策问答是否真的命中了文档，citation 是否正确。
- 再看 workflow：是否把本应固定的路径交给了自由 agent 导致波动。
- 最后补 eval：为这两类任务各建立固定样本，比较修改前后结果。
- 回链模块：[02-single-agent-with-tools/project.md](../02-single-agent-with-tools/project.md)
- 回链模块：[03-rag-memory-and-knowledge/project.md](../03-rag-memory-and-knowledge/project.md)
- 回链模块：[04-workflow-observability-and-evals/project.md](../04-workflow-observability-and-evals/project.md)

16. 重构建议
- 把固定步骤、高风险节点抽回 workflow。
- 保留少量真正需要开放性决策的点给 agent。
- 引入 trace 和固定 eval dataset，形成观察和验证闭环。
- 统一 tool schema，减少自由 agent 的无效探索空间。
- 回链模块：[05-agent-theory-and-architecture/exercises.md](../05-agent-theory-and-architecture/exercises.md)

17. citation 对不上来源的失败模式
- 检索命中了错误文档。
- 回答阶段使用了与 citation 不一致的上下文。
- citation 在接口层被错误拼接或丢失。
- 检索排序合理，但答案综合阶段产生了 drift。
- 回链模块：[03-rag-memory-and-knowledge/resources/05-common-mistakes.md](../03-rag-memory-and-knowledge/resources/05-common-mistakes.md)

## 五、系统设计题参考
18. support-agent 设计要点
- route：提供 `/run` 和 `/health`。
- service：负责意图识别、工具选择和结果汇总。
- tools：至少有 `search_docs`、`get_order_status`、`create_ticket`。
- trace：记录 tool、args、status、latency。
- fallback：工具失败时返回结构化错误，并允许人工接管或降级回答。
- test：覆盖三类请求路径与至少一种工具失败路径。
- 回链模块：[02-single-agent-with-tools/module-service/app/main.py](../02-single-agent-with-tools/module-service/app/main.py)

19. knowledge-agent 设计要点
- ingestion：导入文档，形成可检索数据源。
- retrieval：根据问题取回候选片段。
- response：返回答案和 citations。
- memory：保留最近几轮对话摘要或关键事实。
- failure log：记录检索 miss、citation mismatch、answer drift。
- eval 指标：hit rate、citation accuracy、answer correctness、latency。
- 回链模块：[03-rag-memory-and-knowledge/module-service/app/main.py](../03-rag-memory-and-knowledge/module-service/app/main.py)

## 六、项目讲解题参考
20. 3 分钟 agent-runtime 讲法
- 目标：解决 demo agent 难调试、难比较的问题。
- 架构：把主流程显式建成 workflow，节点执行写入 trace，并用固定 dataset 做 eval。
- 失败案例：最初把所有步骤都交给模型，导致路径波动大；后来把分类和高风险步骤固定到 workflow 中。
- 收益：问题定位更快，改动后能用同一批 case 做回归比较。
- 回链模块：[04-workflow-observability-and-evals/module-service/app/main.py](../04-workflow-observability-and-evals/module-service/app/main.py)

21. 简历描述参考
- 业务版：构建内部支持 Agent 系统，支持知识问答、订单查询与工单创建，提升问题处理效率并增强回答可追溯性。
- Infra 版：设计 Python-first agent runtime，集成 structured output、tool calling、RAG、workflow tracing 与 eval 基线，提升系统稳定性与可调试性。
- 回链模块：[06-career-transition-and-interview/exercises.md](../06-career-transition-and-interview/exercises.md)
