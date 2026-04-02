# 02 单 Agent 与 Tools 逐步执行说明

## Step 1：定义工具契约
- 要做什么：定义工具契约
- 为什么现在做：tool schema 清晰度会直接决定 agent 的稳定性。
- 具体动作：先写输入输出，再写工具实现。
- 产出物：工具契约表
- 完成判断：你能不看实现就知道工具能做什么。
- 常见卡点：工具描述太泛。
- 如果卡住先检查：检查 schema 是否包含必填参数和错误返回。

## Step 2：运行 Tool Schema 示例
- 要做什么：运行 Tool Schema 示例
- 为什么现在做：先把工具边界收紧，再谈 agent loop。
- 具体动作：运行 examples/01-tool-schema，用正确和错误参数各跑一遍。
- 产出物：工具注册表与统一结果模型
- 完成判断：输入错误时能返回稳定反馈。
- 常见卡点：工具返回结构不一致。
- 如果卡住先检查：检查是否定义了统一 ToolResult。

## Step 3：运行 Agent Loop 示例
- 要做什么：运行 Agent Loop 示例
- 为什么现在做：理解 think、act、observe 的最小实现。
- 具体动作：运行 examples/02-agent-loop，观察工具轨迹。
- 产出物：最小 agent 执行记录
- 完成判断：你能说清模型在何处做了决策。
- 常见卡点：把决策硬编码后误以为那是 agent。
- 如果卡住先检查：检查是否保留了决策点。

## Step 4：完成 support-agent 服务
- 要做什么：完成 support-agent 服务
- 为什么现在做：把工具、意图和失败恢复组合成完整系统。
- 具体动作：启动 module-service，执行问答、查单、建单三类请求。
- 产出物：support-agent 服务
- 完成判断：可记录调用轨迹并优雅处理工具失败。
- 常见卡点：失败时只抛异常。
- 如果卡住先检查：检查 trace 中是否记录 tool、args、status、latency。
