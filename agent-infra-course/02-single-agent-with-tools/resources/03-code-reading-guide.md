# 02 单 Agent 与 Tools 代码导读

[返回学习地图](../study-map.md) | [返回模块首页](../README.md) | [上一篇：02-deep-dive.md](./02-deep-dive.md) | [下一篇：04-sources.md](./04-sources.md)

## 学习总原则
- 先看讲义，再看代码。
- 先看对象模型和函数签名，再看具体执行逻辑。
- 先跑测试，再改代码，再重新验证。

## Examples 阅读顺序
### 01-tool-schema：工具契约与校验
- 这一例子主要解决：为什么工具调用的首要问题不是 prompt，而是 schema。
- 先看 [`01-tool-schema/app/main.py`](../examples/01-tool-schema/app/main.py)：先看 `ToolCall` 与 `ToolResult`。这两个对象定义了模型与工具之间的协议。再看 `search_docs`，理解工具本身应该尽量简单、可预测。
- 先看 [`01-tool-schema/tests/test_main.py`](../examples/01-tool-schema/tests/test_main.py)：看参数错误如何在进入工具逻辑前就被拦住。
- 建议运行命令：
  - `python -m app.main`
  - `pytest`
- 建议动手实验：
  - 给 `ToolCall` 增加一个新字段，观察测试和函数如何跟着调整。
  - 把 `query` 设为空，感受“失败应该尽早暴露”的价值。

### 02-agent-loop：最小 agent loop
- 这一例子主要解决：模型决策、工具执行和 observation 是如何组成最小 agent loop 的。
- 先看 [`02-agent-loop/app/main.py`](../examples/02-agent-loop/app/main.py)：先看 `choose_tool`，再看 `run_agent`。这里最重要的是看清“决策点”和“执行点”的分离。
- 先看 [`02-agent-loop/tests/test_main.py`](../examples/02-agent-loop/tests/test_main.py)：看同一个 loop 如何被固定输入稳定验证。
- 建议运行命令：
  - `python -m app.main`
  - `pytest`
- 建议动手实验：
  - 增加一个新工具路径，观察 loop 如何扩展。

## module-service 阅读顺序
### support-agent
- 这个综合服务的目的：用统一 trace 结构把单 agent、三个工具和失败恢复组合成支持服务。
- 先看 [`module-service/app/service.py`](../module-service/app/service.py)：先看工具函数，再看 `ToolTrace` 和 `run_agent`。理解为什么 trace 结构必须统一。
- 先看 [`module-service/app/main.py`](../module-service/app/main.py)：再看 `/run` 路由如何只承担协议职责。
- 先看 [`module-service/tests/test_main.py`](../module-service/tests/test_main.py)：最后看服务级测试如何验证工具选择路径。
- 建议运行命令：
  - `uvicorn app.main:app --reload`
  - `pytest`
