# 02 单 Agent 与 Tools 关键资料重点与总结

## 1. OpenAI Tools Guide
- 为什么值得读：理解工具声明、参数生成与回传的主资料。
- 重点看哪里：工具 schema、tool call 生命周期。
- 一句话总结：tool calling 本质上是结构化动作生成。
- 读完你应该会：你能设计自定义工具接口。
- 阅读说明：必须精读。

## 2. OpenAI Web Search Tool
- 为什么值得读：帮助理解 built-in tools 的思路。
- 重点看哪里：平台托管工具与自定义工具的差别。
- 一句话总结：built-in tool 适合快速拿能力，自定义 tool 更利于理解 infra。
- 读完你应该会：你能区分两类 tool 的边界。
- 阅读说明：选读。

## 3. OpenAI Agents SDK
- 为什么值得读：从官方 runtime 视角理解 agent 组织方式。
- 重点看哪里：agent、tool、handoff、trace。
- 一句话总结：成熟 runtime 的价值在于组织决策与追踪过程。
- 读完你应该会：你能比较课程里的最小 loop 与成熟 runtime 的差距。
- 阅读说明：第二遍重点看 trace。

## 4. PydanticAI
- 为什么值得读：观察类型系统与 agent 的结合方式。
- 重点看哪里：类型化 tool 与模型调用。
- 一句话总结：类型约束能显著减少 tool 调用的不确定性。
- 读完你应该会：你能理解为什么 schema 质量直接影响 agent 质量。
- 阅读说明：补充阅读。
