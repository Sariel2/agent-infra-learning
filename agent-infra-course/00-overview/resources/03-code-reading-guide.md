# 00 总览与准备 代码导读

[返回学习地图](../study-map.md) | [返回模块首页](../README.md) | [上一篇：02-deep-dive.md](./02-deep-dive.md) | [下一篇：04-sources.md](./04-sources.md)

这一页的目标不是带你“看完所有代码”，而是建立第一套稳定的读码顺序。第 00 模块的代码都很小，但它们承担的任务非常关键：把“环境、配置、记录、项目就绪状态”这些看起来不酷的东西，做成后面所有模块的起点。

## 怎么读这一页
- 先读 `01-concepts-and-principles.md` 和 `02-deep-dive.md`，再回来读代码。
- 每次先看数据对象，再看函数，再看测试，最后才回到综合服务。
- 不要一上来就想“这段代码高级不高级”，先问“它在课程主线里承担什么角色”。

## 先看什么，再看什么
推荐顺序：
1. 看 `examples/01-settings-and-logging`
2. 看 `examples/02-project-smoke-test`
3. 看 `module-service/app/service.py`
4. 看 `module-service/app/main.py`
5. 看 `module-service/tests/test_main.py`

这样读的原因是：
- 第一个 example 让你接受“配置和日志上下文本身就是系统对象”
- 第二个 example 让你接受“项目 readiness 也可以被结构化表达”
- 最后的 module-service 则把这两件事收束成一个最小工作区检查服务

## Example 1：`01-settings-and-logging`
入口文件：
- [examples/01-settings-and-logging/app/main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/00-overview/examples/01-settings-and-logging/app/main.py)
- [examples/01-settings-and-logging/tests/test_main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/00-overview/examples/01-settings-and-logging/tests/test_main.py)
- [examples/01-settings-and-logging/walkthrough.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/00-overview/examples/01-settings-and-logging/walkthrough.md)

先看这几个点：
- `Settings`
- `build_log_context()`
- `main()`

第一眼应该理解什么：
- `Settings` 不是为了少写几个变量，而是在告诉你“运行参数应该集中收口”。
- `build_log_context()` 不是普通工具函数，它在表达一种课程主线：系统上下文应该能被结构化保留下来。
- `main()` 很简单，但它故意保持简单，好让你把注意力放在“对象 -> 上下文”的映射上。

接着看测试时要注意：
- 测试其实不是在验证打印，而是在验证结构。
- 你要观察它如何把“配置是否被正确组织”转成可断言的对象行为。

建议你动手改一次：
- 给 `Settings` 增加一个新字段，比如 `course_stage`
- 再补 `build_log_context()` 和测试

这一步会帮你真正理解“配置变化应该先进入对象，再进入行为”。

## Example 2：`02-project-smoke-test`
入口文件：
- [examples/02-project-smoke-test/app/main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/00-overview/examples/02-project-smoke-test/app/main.py)
- [examples/02-project-smoke-test/tests/test_main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/00-overview/examples/02-project-smoke-test/tests/test_main.py)
- [examples/02-project-smoke-test/walkthrough.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/00-overview/examples/02-project-smoke-test/walkthrough.md)

先看这几个点：
- `ProjectStatus`
- `summarize_status()`
- `main()`

第一眼应该理解什么：
- `ProjectStatus` 把“准备状态”变成了显式对象，而不是零散布尔变量。
- `summarize_status()` 非常小，但它实际上在训练一件事：把系统 readiness 转成稳定输出。
- 这就是后面所有“状态对象 -> 结果判断”的最早雏形。

接着看测试时要注意：
- 它不是为了证明函数多聪明，而是为了保护状态判断逻辑不被随意改坏。
- 这里的“smoke test”思维，后面会一路演化到 workflow 和 eval。

建议你动手改一次：
- 新增一个字段，比如 `docs_ready`
- 再决定这个字段是否影响 `ready / needs-work`

这会让你更直观地感受到：状态对象一旦扩展，判断逻辑和测试要一起演进。

## 最后看综合服务：`starter-workspace`
入口文件：
- [module-service/app/service.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/00-overview/module-service/app/service.py)
- [module-service/app/main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/00-overview/module-service/app/main.py)
- [module-service/tests/test_main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/00-overview/module-service/tests/test_main.py)
- [module-service/README.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/00-overview/module-service/README.md)

推荐读码顺序：
1. 先看 `WorkspaceStatus`
2. 再看 `summarize_workspace()`
3. 然后看 `app/main.py` 里的 HTTP 壳
4. 最后看测试如何验证对外输出

第一眼应该理解什么：
- `WorkspaceStatus` 把“学习环境是否准备好”做成显式 schema。
- `summarize_workspace()` 是第 00 模块的收束函数，它告诉你：哪怕是准备阶段，也值得用结构化对象和稳定输出组织。
- `main.py` 的存在，是在提醒你这门课从第一模块开始就站在“服务化”视角，而不是临时脚本视角。

看测试时重点关注：
- 测试是不是围绕输出契约来写
- 服务入口是不是只负责协议层，而不是把所有判断塞进去

## 这一页最容易读偏的地方
- 误区一：觉得代码太简单，不值得细看。
  - 恰恰相反，这一模块在训练最重要的习惯：对象化、结构化、服务化。
- 误区二：只关注能不能打印或返回结果。
  - 更重要的是它如何把“准备状态”变成可验证对象。
- 误区三：跳过测试。
  - 测试在这里不是附属物，而是你第一次接触“结构如何被保护”的地方。

## 读完这一页后应该回哪里
- 如果你想继续执行模块任务：去 [steps.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/00-overview/steps.md)
- 如果你想回顾概念：去 [01-concepts-and-principles.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/00-overview/resources/01-concepts-and-principles.md)
- 如果你想继续看来源：去 [04-sources.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/00-overview/resources/04-sources.md)
