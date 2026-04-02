# 04 Workflow、Observability 与 Evals 逐步执行说明

## Step 1：画出流程状态图
- 要做什么：画出流程状态图
- 为什么现在做：你不能调试一个隐形流程。
- 具体动作：把节点、条件分支和人工审核点写出来。
- 产出物：workflow 状态图
- 完成判断：你能说清每个节点的输入输出。
- 常见卡点：代码里有流程，图里没有。
- 如果卡住先检查：检查 retrieval、tool、summary 是否被单独抽出。

## Step 2：运行状态编排示例
- 要做什么：运行状态编排示例
- 为什么现在做：理解 workflow 如何约束 agent 的执行边界。
- 具体动作：运行 examples/01-stateful-workflow，修改状态观察分支。
- 产出物：状态流转示例
- 完成判断：你能解释 workflow 节点和 agent 决策点的区别。
- 常见卡点：把所有步骤都交给模型决定。
- 如果卡住先检查：检查哪些步骤其实应该固定。

## Step 3：运行 Eval Runner 示例
- 要做什么：运行 Eval Runner 示例
- 为什么现在做：没有基线就没有迭代依据。
- 具体动作：运行 examples/02-eval-runner，对固定数据集计算 success 和 notes。
- 产出物：基线评测结果
- 完成判断：你能比较两次运行结果。
- 常见卡点：每次随机选问题。
- 如果卡住先检查：检查是否准备了固定 dataset。

## Step 4：完成 agent-runtime 服务
- 要做什么：完成 agent-runtime 服务
- 为什么现在做：把 workflow、trace 和 eval 放进同一系统。
- 具体动作：启动 module-service，执行请求，查看 trace，再跑 /eval。
- 产出物：agent-runtime 服务
- 完成判断：一条请求可追踪，一组数据可评测。
- 常见卡点：trace 只有最终输出。
- 如果卡住先检查：检查每个节点是否记录 metadata。
