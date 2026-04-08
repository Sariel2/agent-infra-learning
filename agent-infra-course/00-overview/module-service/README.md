# starter-workspace

把环境检查、学习准备状态和最小服务骨架组织成统一起点。

## 这个综合服务的目标
- 把“环境就绪”“日志准备好”“项目目标明确”这三件事变成可验证状态。
- 给后面 6 个模块提供统一的服务形状：`service.py` 管核心逻辑，`main.py` 管 HTTP，`test_main.py` 管最小验收。
- 让你从第一模块开始就习惯“有结构、有边界、有测试”的工作方式。

## 开始前先回看
- 模块首页：[../README.md](../README.md)
- 学习地图：[../study-map.md](../study-map.md)
- 概念讲义：[../resources/01-concepts-and-principles.md](../resources/01-concepts-and-principles.md)
- 原理细节：[../resources/02-deep-dive.md](../resources/02-deep-dive.md)
- 代码导读：[../resources/03-code-reading-guide.md](../resources/03-code-reading-guide.md)
- 示例 1：[../examples/01-settings-and-logging/app/main.py](../examples/01-settings-and-logging/app/main.py)
- 示例 2：[../examples/02-project-smoke-test/app/main.py](../examples/02-project-smoke-test/app/main.py)

## 先理解这 3 个文件
- 核心逻辑：[app/service.py](./app/service.py)
  先看 `WorkspaceStatus` 和 `summarize_workspace()`，理解“准备完成”为什么也值得被建模。
- HTTP 入口：[app/main.py](./app/main.py)
  看 `/health` 和 `/summary`，理解为什么路由层只做协议转换。
- 最小验收：[tests/test_main.py](./tests/test_main.py)
  看测试如何把“ready”定义成可自动验证的结果。

## 推荐实现顺序
1. 先读 [app/service.py](./app/service.py)，确认 `WorkspaceStatus` 的三个字段各代表什么。
2. 再读 [app/main.py](./app/main.py)，确认 HTTP 层没有偷偷承担业务逻辑。
3. 最后读 [tests/test_main.py](./tests/test_main.py)，把“完成状态”与接口行为对上。
4. 自己加一个新的检查项，例如 `docs_ready`，再推演它会影响哪些层。

## 动手实现时每一步做什么
### Step 1：先稳定状态模型
- 要改的文件：[app/service.py](./app/service.py)
- 要做的事：确认准备状态由 `WorkspaceStatus` 驱动，而不是散落在路由里。
- 验收标准：`summarize_workspace()` 的返回结构保持稳定，包含总状态和详细 checks。

### Step 2：再暴露 HTTP 接口
- 要改的文件：[app/main.py](./app/main.py)
- 要做的事：只暴露 `/health` 和 `/summary`，不在路由里重复写状态判断逻辑。
- 验收标准：访问 `/summary` 时能直接拿到 `summarize_workspace()` 的输出。

### Step 3：最后补测试
- 要改的文件：[tests/test_main.py](./tests/test_main.py)
- 要做的事：把“ready”定义写成断言，确保后续改动不会把基础骨架改坏。
- 验收标准：测试至少覆盖状态码和 `status == "ready"`。

## 建议运行命令
- `uvicorn app.main:app --reload`
- `pytest`

## 常见退化点
- 把状态判断写进路由，导致后面很难复用。
- 返回结构过于随意，后续模块没法承接。
- 测试只测接口通不通，不测输出是否真的表达“准备完成”。

## 学完后你应该能回答
- 为什么课程一开始就要先搭最小服务骨架。
- 为什么“学习准备状态”也值得被建模和测试。
- 后续模块为什么都沿用 `service + main + tests` 这条结构。
