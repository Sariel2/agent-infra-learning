# 05 Agent 原理与架构 逐步执行说明

## Step 1：把实践映射到模式
- 要做什么：把实践映射到模式
- 为什么现在做：抽象能力来自对实践的复盘。
- 具体动作：对 ReAct、Router、Plan-and-Execute 各写一页“像什么、不像什么”。
- 产出物：模式对照表
- 完成判断：你不再把所有 agent 都叫 ReAct。
- 常见卡点：模式名会背，边界说不清。
- 如果卡住先检查：检查是否能画出控制流与信息流。

## Step 2：运行 Pattern Comparison 示例
- 要做什么：运行 Pattern Comparison 示例
- 为什么现在做：同一个问题在不同模式下代码形态不同。
- 具体动作：运行 examples/01-pattern-comparison，比较输出结构。
- 产出物：模式输出对比
- 完成判断：你能说清各自优缺点。
- 常见卡点：只看定义，不看代码。
- 如果卡住先检查：确认你真的运行了示例。

## Step 3：运行 Boundary Checker 示例
- 要做什么：运行 Boundary Checker 示例
- 为什么现在做：真正的架构判断来自边界意识。
- 具体动作：运行 examples/02-boundary-checker，输入场景得到 workflow 或 agent 建议。
- 产出物：判断规则样例
- 完成判断：你知道什么时候不该上多 agent。
- 常见卡点：为了高级感盲目复杂化。
- 如果卡住先检查：检查场景是否真的存在开放性决策。

## Step 4：完成 architecture-lab 服务
- 要做什么：完成 architecture-lab 服务
- 为什么现在做：把术语变成可比较的实验入口。
- 具体动作：启动 module-service，用同一个请求比较不同模式。
- 产出物：architecture-lab 服务
- 完成判断：你能拿它做 10 分钟分享。
- 常见卡点：只有文档，没有对比入口。
- 如果卡住先检查：检查是否统一了模式输入输出接口。
