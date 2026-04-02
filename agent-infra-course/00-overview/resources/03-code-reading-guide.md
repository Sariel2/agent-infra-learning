# 00 总览与准备 代码导读

[返回学习地图](../study-map.md) | [返回模块首页](../README.md) | [上一篇：02-deep-dive.md](./02-deep-dive.md) | [下一篇：04-sources.md](./04-sources.md)

## 学习总原则
- 先看讲义，再看代码。
- 先看对象模型和函数签名，再看具体执行逻辑。
- 先跑测试，再改代码，再重新验证。

## Examples 阅读顺序
### 01-settings-and-logging：设置与日志上下文
- 这一例子主要解决：为什么课程从配置对象和日志上下文开始。
- 先看 [`01-settings-and-logging/app/main.py`](../examples/01-settings-and-logging/app/main.py)：先看 `Settings` 和 `build_log_context`，理解“先固定系统形状，再讨论复杂能力”。
- 先看 [`01-settings-and-logging/tests/test_main.py`](../examples/01-settings-and-logging/tests/test_main.py)：再看测试，观察课程如何把抽象对象转成可验证行为。
- 建议运行命令：
  - `python -m app.main`
  - `pytest`
- 建议动手实验：
  - 修改 `timeout_seconds`，观察输出变化。
  - 给 `Settings` 增加一个字段，再补测试。

### 02-project-smoke-test：项目状态与 smoke test
- 这一例子主要解决：为什么学习项目也需要最小验证机制。
- 先看 [`02-project-smoke-test/app/main.py`](../examples/02-project-smoke-test/app/main.py)：看 `ProjectStatus` 与 `summarize_status`，理解“能运行”和“已准备好”不是一回事。
- 先看 [`02-project-smoke-test/tests/test_main.py`](../examples/02-project-smoke-test/tests/test_main.py)：看 smoke test 如何把学习状态转成明确检查项。
- 建议运行命令：
  - `python -m app.main`
  - `pytest`
- 建议动手实验：
  - 把 `project_defined` 改成 `False`，确认状态如何变化。

## module-service 阅读顺序
### starter-workspace
- 这个综合服务的目的：把环境、检查项和学习准备状态组织成统一工程骨架。
- 先看 [`module-service/app/service.py`](../module-service/app/service.py)：先看 `WorkspaceStatus` 和 `summarize_workspace`，这是课程里“先建结构”的最小缩影。
- 先看 [`module-service/app/main.py`](../module-service/app/main.py)：再看 FastAPI 路由，理解为什么连“学习准备状态”也值得被建成服务边界。
- 先看 [`module-service/tests/test_main.py`](../module-service/tests/test_main.py)：最后看测试，确认“准备完成”的定义是可以验证的。
- 建议运行命令：
  - `uvicorn app.main:app --reload`
  - `pytest`
