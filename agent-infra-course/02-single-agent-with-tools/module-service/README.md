# support-agent

用统一 trace 结构把单 agent、三个工具和失败恢复拼成支持服务。

## 这个综合服务的目标
- 让 agent 真正具备“选工具并执行”的最小闭环。
- 用统一的 `ToolTrace` 结构把工具调用变成可观察、可分析的数据。
- 让你看到 tool schema、路由判断和失败恢复是如何组合成一个服务的。

## 开始前先回看
- 模块首页：[../README.md](../README.md)
- 学习地图：[../study-map.md](../study-map.md)
- 概念讲义：[../resources/01-concepts-and-principles.md](../resources/01-concepts-and-principles.md)
- 原理细节：[../resources/02-deep-dive.md](../resources/02-deep-dive.md)
- 代码导读：[../resources/03-code-reading-guide.md](../resources/03-code-reading-guide.md)
- 示例 1：[../examples/01-tool-schema/app/main.py](../examples/01-tool-schema/app/main.py)
- 示例 2：[../examples/02-agent-loop/app/main.py](../examples/02-agent-loop/app/main.py)

## 先理解这 3 个文件
- 核心逻辑：[app/service.py](./app/service.py)
  先看 `ToolTrace`、三个工具函数和 `run_agent()`，这是本模块最重要的执行闭环。
- HTTP 入口：[app/main.py](./app/main.py)
  看 `/run` 如何把 message 转给 service，而不是在路由里做规则判断。
- 最小验收：[tests/test_main.py](./tests/test_main.py)
  看测试如何确保订单场景真的走到了 `get_order_status`。

## 推荐实现顺序
1. 先读 [app/service.py](./app/service.py)，把 `search_docs`、`get_order_status`、`create_ticket` 三个工具的输入输出看清。
2. 接着读 `run_agent()`，看 message 是怎么被路由到不同工具的。
3. 再读 [tests/test_main.py](./tests/test_main.py)，理解为什么这里先测 trace 再测 answer。
4. 最后读 [app/main.py](./app/main.py)，确认 HTTP 层没有吞掉 trace。

## 动手实现时每一步做什么
### Step 1：先把工具边界写清
- 要改的文件：[app/service.py](./app/service.py)
- 要做的事：把三个工具都写成稳定函数，不要返回自由文本大杂烩。
- 验收标准：每个工具都能被 `ToolTrace` 统一记录。

### Step 2：再写 agent loop 的最小决策
- 要改的文件：[app/service.py](./app/service.py)
- 要做的事：在 `run_agent()` 中先根据 message 做最小路由，再生成统一 trace。
- 验收标准：每条路径都返回 `answer + trace`，而不是只有 answer。

### Step 3：最后用接口和测试固定行为
- 要改的文件：[app/main.py](./app/main.py)
- 要改的文件：[tests/test_main.py](./tests/test_main.py)
- 要做的事：通过 `/run` 暴露 agent，并用测试固定关键场景。
- 验收标准：订单请求的 trace 第一条必须是 `get_order_status`。

## 建议运行命令
- `uvicorn app.main:app --reload`
- `pytest`

## 常见退化点
- 工具返回结构不统一，trace 后面很难分析。
- 只看 answer，不看 trace，导致分不清“工具选错”和“工具执行失败”。
- 把本来固定的路径交给过于自由的 agent，结果系统波动变大。

## 扩展时优先做什么
- 给 `ToolTrace` 增加 `status`、`latency_ms`、`error`。
- 给工具失败加重试、降级和人工接管信号。
- 把简单 if/else 路由升级成更清晰的状态机或 workflow。

## 学完后你应该能回答
- 为什么 tool schema 和 trace 结构会直接影响 agent 质量。
- 为什么先让 trace 稳定，比先让模型“更聪明”更重要。
- 哪些场景其实应该回退到 workflow，而不是继续增加 agent 自由度。
