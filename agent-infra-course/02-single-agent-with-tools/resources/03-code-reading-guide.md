# 02 单 Agent 与 Tools 代码导读

[返回学习地图](../study-map.md) | [返回模块首页](../README.md) | [上一篇：02-deep-dive.md](./02-deep-dive.md) | [下一篇：04-sources.md](./04-sources.md)

这一页要帮你把“tool calling 是系统能力”这件事落实到代码里。第 02 模块最值得看的，不是 if/else 本身，而是这些小对象和小函数如何把：
- schema
- tool result
- trace
- 最小 agent loop
组织成一个可治理的小系统。

## 怎么读这一页
- 先看对象模型，再看路由逻辑。
- 每看完一个 example，都回头问：这段代码在收紧哪一层不确定性？
- 最后再看 `support-agent`，把各个能力点拼起来。

## 推荐总顺序
1. 看 `examples/01-tool-schema`
2. 看 `examples/02-agent-loop`
3. 看 `module-service/app/service.py`
4. 看 `module-service/app/main.py`
5. 看 `module-service/tests/test_main.py`

## Example 1：`01-tool-schema`
入口文件：
- [examples/01-tool-schema/app/main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/02-single-agent-with-tools/examples/01-tool-schema/app/main.py)
- [examples/01-tool-schema/tests/test_main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/02-single-agent-with-tools/examples/01-tool-schema/tests/test_main.py)
- [examples/01-tool-schema/walkthrough.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/02-single-agent-with-tools/examples/01-tool-schema/walkthrough.md)

先看这几个点：
- `ToolCall`
- `ToolResult`
- `search_docs()`

第一眼应该理解什么：
- `ToolCall` 让“动作”先变成对象，而不是自由字符串。
- `query = Field(min_length=1)` 这种约束非常重要，它在告诉你 schema 会直接影响稳定性。
- `ToolResult` 的价值不是“统一返回格式好看”，而是让成功 / 失败路径以后都能被上游消费。

接着看测试时重点看：
- 测试如何围绕 schema 和 result 形态写
- 为什么这里哪怕代码很小，也要先把 `ToolResult` 这种统一对象立住

建议你动手改一次：
- 给 `ToolResult` 增加 `metadata`
- 然后补实现和测试

## Example 2：`02-agent-loop`
入口文件：
- [examples/02-agent-loop/app/main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/02-single-agent-with-tools/examples/02-agent-loop/app/main.py)
- [examples/02-agent-loop/tests/test_main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/02-single-agent-with-tools/examples/02-agent-loop/tests/test_main.py)
- [examples/02-agent-loop/walkthrough.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/02-single-agent-with-tools/examples/02-agent-loop/walkthrough.md)

先看这几个点：
- `StepTrace`
- `TOOLS`
- `choose_tool()`
- `run_agent()`

第一眼应该理解什么：
- `choose_tool()` 在表达“决策层”。
- `TOOLS` 在表达“执行层”。
- `StepTrace` 在表达“observation / 轨迹层”。
- `run_agent()` 虽然只有一轮，但已经把 agent loop 的最小骨架显影出来了。

接着看测试时重点看：
- 是否验证了工具选择结果
- 是否验证 trace 里保留了足够信息

建议你动手改一次：
- 增加一个新工具
- 修改 `choose_tool()`
- 再补测试，看看 trace 是否仍然可读

## 最后看综合服务：`support-agent`
入口文件：
- [module-service/app/service.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/02-single-agent-with-tools/module-service/app/service.py)
- [module-service/app/main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/02-single-agent-with-tools/module-service/app/main.py)
- [module-service/tests/test_main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/02-single-agent-with-tools/module-service/tests/test_main.py)
- [module-service/README.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/02-single-agent-with-tools/module-service/README.md)

推荐读码顺序：
1. 先看 `AgentRequest`
2. 再看 `ToolTrace`
3. 再看 3 个工具函数：`search_docs()`、`get_order_status()`、`create_ticket()`
4. 最后看 `run_agent()`

第一眼应该理解什么：
- `ToolTrace` 是这个服务最值得先看懂的对象，它把“执行过程”变成稳定证据。
- 3 个工具函数非常简单，但它们分别代表不同类别能力：查知识、查状态、触发动作。
- `run_agent()` 的价值不在 if/else，而在它如何把决策、执行、结果打包成统一返回。

接着再看 `app/main.py` 时重点看：
- HTTP 层是不是只接收消息、返回结果
- 有没有把 agent 决策逻辑塞进 route

最后看测试时重点看：
- 测试是否覆盖不同工具路径
- 返回结果里是否既有 `answer` 又有 `trace`

## 这一页最容易读偏的地方
- 误区一：觉得 agent loop 太简单，不像真正 agent
  - 这里的目标是显影骨架，不是一次性做复杂系统。
- 误区二：只看 `run_agent()` 的分支，不看对象
  - 真正决定系统能不能长大的，是对象边界。
- 误区三：忽略 trace
  - 这一模块最关键的工程意识之一，就是过程必须被保留下来。

## 读完这一页后应该回哪里
- 如果你想继续执行：去 [steps.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/02-single-agent-with-tools/steps.md)
- 如果你想回顾原理：去 [02-deep-dive.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/02-single-agent-with-tools/resources/02-deep-dive.md)
- 如果你想看出处解释：去 [04-sources.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/02-single-agent-with-tools/resources/04-sources.md)
