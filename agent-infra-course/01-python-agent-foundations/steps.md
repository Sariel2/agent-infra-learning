# 01 Python 与 Agent 基础 逐步执行说明

## Step 1：补齐最小 Python 工程能力
- 要做什么：补齐最小 Python 工程能力
- 为什么现在做：后续每个示例都会依赖 typing、BaseModel、async 和 pytest。
- 具体动作：先跑 examples，再回头补概念。
- 产出物：Python 工程笔记
- 完成判断：你能理解并修改示例里的模型与函数。
- 常见卡点：沉迷语法细节脱离课程主线。
- 如果卡住先检查：确认你在学的是 agent infra 所需的 Python。

## Step 2：运行 Structured Output 示例
- 要做什么：运行 Structured Output 示例
- 为什么现在做：这是把模型输出变成工程接口的起点。
- 具体动作：运行 examples/01-structured-output，修改 schema 再跑测试。
- 产出物：稳定的输入输出结构
- 完成判断：你知道为什么 JSON 更适合系统接入。
- 常见卡点：让模型直接返回自由文本。
- 如果卡住先检查：检查输出是否由 Pydantic 模型约束。

## Step 3：运行 Provider 抽象示例
- 要做什么：运行 Provider 抽象示例
- 为什么现在做：模型调用不应该直接散落在业务代码里。
- 具体动作：切换 fake provider 与 echo provider，观察调用差异。
- 产出物：统一 provider 接口
- 完成判断：你能解释 provider 的职责边界。
- 常见卡点：provider、route、service 写在一起。
- 如果卡住先检查：检查依赖方向是否从外到内。

## Step 4：完成 llm-gateway 服务
- 要做什么：完成 llm-gateway 服务
- 为什么现在做：把零散知识点组装成完整服务。
- 具体动作：启动 module-service，调用 /generate 和 /health，运行测试。
- 产出物：llm-gateway 服务
- 完成判断：服务可跑、可测、可扩展。
- 常见卡点：路由层写满逻辑。
- 如果卡住先检查：检查 schema、provider、service、route 是否分层。
