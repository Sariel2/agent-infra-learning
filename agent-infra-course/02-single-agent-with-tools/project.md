# 02 单 Agent 与 Tools 模块综合项目说明

## 项目名
`support-agent`

## 项目定位
这是整门课第一个真正“带工具调用”的综合服务。它的重点不是工具数量，而是把工具 schema、最小 agent loop、统一结果结构和 trace 组合成一个可治理的小型运行时。

## 对应综合服务
- 服务入口：[module-service/app/main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/02-single-agent-with-tools/module-service/app/main.py)
- 服务逻辑：[module-service/app/service.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/02-single-agent-with-tools/module-service/app/service.py)
- 测试入口：[module-service/tests/test_main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/02-single-agent-with-tools/module-service/tests/test_main.py)

## 项目目标
做一个最小 support agent，能够：
- 回答知识类问题
- 查询订单状态
- 创建工单
- 返回统一 trace

## 你最终应该学到什么
- 为什么 tool calling 是动作治理问题
- 为什么 schema 要先于 prompt 治理
- 为什么 trace 必须从早期建立
- 为什么单 agent 已经足够暴露核心 runtime 问题

## 必做项
- 至少实现 3 个工具
- 工具调用必须走统一 schema
- 返回结果必须包含 `answer` 和 `trace`
- 能区分知识查询、状态查询、工单创建三条路径
- 测试覆盖不同工具路径

## 推荐实现顺序
1. 先跑 `examples/01-tool-schema`
2. 再跑 `examples/02-agent-loop`
3. 再读 [resources/03-code-reading-guide.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/02-single-agent-with-tools/resources/03-code-reading-guide.md)
4. 再回到 `support-agent`
5. 最后做 [review.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/02-single-agent-with-tools/review.md)

## 实现清单
- `ToolTrace` 或等价对象必须存在
- 3 个工具函数必须边界清楚
- `run_agent()` 必须把决策、执行和结果统一返回
- HTTP 层不能承接 agent 决策逻辑
- 测试要覆盖不同消息触发不同工具

## 验收清单
- 我能触发 3 条不同工具路径
- 我能解释 `ToolTrace` 为什么存在
- 我能区分选错工具、参数错误、执行失败
- 我能新增 1 个工具并补齐测试
- 我能说清这个项目和“只是调一个函数”的本质区别

## 常见退化点
- 每个工具各自返回不同数据形状
- trace 里只有结果，没有过程
- 所有决策全塞给模型或上游 prompt
- 把工具调用失败都归成“agent 不稳定”

## 加分项
- 增加 timeout
- 增加 retry
- 增加 fallback
- 给 trace 增加 metadata 字段

## 交付物
- 一个可启动的单 agent 服务
- 一组覆盖工具分支的最小测试
- 一份你自己总结的工具失败分类表

## 进入下一模块前，你应该能回答
- 为什么 tool result 要统一结构
- 为什么 observation / trace 会影响后面 RAG 和 workflow
- 为什么 built-in tool 和 custom tool 不应混着理解
