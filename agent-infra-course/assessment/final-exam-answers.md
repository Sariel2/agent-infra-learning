# Final Exam Answers

## 一、选择题
1. 正确答案：B
- 原因：workflow 负责显式步骤与条件分支建模。
- 常见误区：把 prompt 模板当作流程控制工具。
- 工程判断：当步骤固定且失败成本高时，优先 workflow。

2. 正确答案：B
- 原因：trace 能展示一次运行里的中间节点、工具选择和状态变化。
- 常见误区：只看最终回答或只看日志文本。
- 工程判断：没有过程可见性，就很难稳定迭代 agent。

3. 正确答案：C
- 原因：固定步骤、高失败代价、可审核，都是 workflow 优先信号。
- 常见误区：误以为更自由的 agent 一定更高级。
- 工程判断：能固定的步骤先固定。

4. 正确答案：C
- 原因：citation 的核心价值是让答案能回溯证据。
- 常见误区：把 citation 当成展示细节，而不是质量治理手段。
- 工程判断：没有 citation，RAG 很难做可靠性分析。

5. 正确答案：B
- 原因：provider abstraction 把模型接入从业务逻辑中解耦出来。
- 常见误区：以为 provider 会自动解决成本或性能问题。
- 工程判断：先有清晰 provider 边界，后面才能自由替换真实或 fake 模型。

## 二、判断题
6. 错
- 解析：function calling 只是 agent runtime 的一个能力，完整 runtime 还涉及状态、轨迹、失败恢复和治理。

7. 错
- 解析：日志通常是离散文本，trace 是结构化运行过程记录。

8. 对
- 解析：记忆需要裁剪，否则会带来上下文污染和成本上升。

9. 对
- 解析：固定 eval dataset 才能支持回归比较和版本对照。

10. 错
- 解析：multi-agent 是复杂度更高的模式，不应默认优先。

## 三、简答题参考
11. 先做 fake provider 的原因
- 它能先固定接口与数据流，减少把外部 API 波动和工程设计问题混在一起。
- 它让测试更容易写，也更适合先验证 route、service、schema 边界。
- 工程上，先让接口和测试稳定，再接真实依赖更高效。

12. tool schema 设计不佳的影响
- 模型难以稳定选择工具。
- 参数生成容易出错或缺失。
- 工具失败难以被统一处理。
- trace 很难统一分析，因为返回结构不稳定。

13. memory 与 retrieval 的职责边界
- retrieval 负责从外部知识源取回和当前问题相关的客观资料。
- memory 负责保留会话上下文中的短期用户状态、偏好或最近交流事实。
- retrieval 面向知识，memory 面向对话过程。

14. trace、log、eval 的不同
- log：离散事件记录，便于快速排错。
- trace：结构化过程记录，便于理解一次运行内部发生了什么。
- eval：把系统放到固定数据集上比较质量、稳定性、成本和延迟。

## 四、场景分析题参考
15. 排查顺序示例
- 先看 trace：确认查订单和政策问答分别走了哪些节点。
- 再看 tool：查订单是否稳定选择了 `get_order_status`，参数是否正确。
- 再看 RAG：政策问答是否真的命中了文档，citation 是否正确。
- 再看 workflow：是否把本应固定的路径交给了自由 agent 导致波动。
- 最后补 eval：为这两类任务各建立固定样本，比较修改前后结果。

16. 重构建议
- 把固定步骤、高风险节点抽回 workflow。
- 保留少量真正需要开放性决策的点给 agent。
- 引入 trace 和固定 eval dataset，形成观察和验证闭环。
- 统一 tool schema，减少自由 agent 的无效探索空间。

17. citation 对不上来源的失败模式
- 检索命中了错误文档。
- 回答阶段使用了与 citation 不一致的上下文。
- citation 在接口层被错误拼接或丢失。
- 检索排序合理，但答案综合阶段产生了 drift。

## 五、系统设计题参考
18. support-agent 设计要点
- route：提供 `/run` 和 `/health`。
- service：负责意图识别、工具选择和结果汇总。
- tools：至少有 `search_docs`、`get_order_status`、`create_ticket`。
- trace：记录 tool、args、status、latency。
- fallback：工具失败时返回结构化错误，并允许人工接管或降级回答。
- test：覆盖三类请求路径与至少一种工具失败路径。

19. knowledge-agent 设计要点
- ingestion：导入文档，形成可检索数据源。
- retrieval：根据问题取回候选片段。
- response：返回答案和 citations。
- memory：保留最近几轮对话摘要或关键事实。
- failure log：记录检索 miss、citation mismatch、answer drift。
- eval 指标：hit rate、citation accuracy、answer correctness、latency。

## 六、项目讲解题参考
20. 3 分钟 agent-runtime 讲法
- 目标：解决 demo agent 难调试、难比较的问题。
- 架构：把主流程显式建成 workflow，节点执行写入 trace，并用固定 dataset 做 eval。
- 失败案例：最初把所有步骤都交给模型，导致路径波动大；后来把分类和高风险步骤固定到 workflow 中。
- 收益：问题定位更快，改动后能用同一批 case 做回归比较。

21. 简历描述参考
- 业务版：构建内部支持 Agent 系统，支持知识问答、订单查询与工单创建，提升问题处理效率并增强回答可追溯性。
- Infra 版：设计 Python-first agent runtime，集成 structured output、tool calling、RAG、workflow tracing 与 eval 基线，提升系统稳定性与可调试性。
