# 01 Python 与 Agent 基础 复盘模板

这一页用来判断：你是真的搭起了最小服务骨架，还是只是调通了几个接口。第 01 模块的关键不是“会不会写 Python”，而是你是否已经建立了结构化输出、provider 抽象和服务分层意识。

## 什么时候做这页复盘
- 完成 [steps.md](./steps.md) 后做
- 跑过两个 example 和 `llm-gateway` 后做
- 进入第 02 模块前再回看一次

## 一、模块总结
请先用 5-8 句话回答：
- 为什么结构化输出是这个模块的第一块地基
- 为什么 provider 的本质是隔离变化
- 为什么 route / service / provider 需要分层
- 为什么 fake provider 是合理起点

如果写不顺，优先回看：
- [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
- [resources/02-deep-dive.md](./resources/02-deep-dive.md)

## 二、自查清单
逐条回答 `是 / 否 / 部分做到`，并补一句证据。

- 我是否已经能不依赖模板写一个最小 FastAPI 服务
- 我是否理解了请求模型、响应模型、配置模型的边界
- 我是否真正把模型调用和路由解耦
- 我是否已经接受“先 fake，再 real”的开发方式
- 我是否能解释 provider 层吸收了哪些变化
- 我的错误处理是不是还停留在 `try/except Exception`

## 三、失败归因表
把你在本模块遇到的问题尽量归到正确层，而不是一律写成“代码没写对”。

| 现象 | 更可能的问题层 | 根因猜测 | 下一步动作 |
|---|---|---|---|
| 接口能返回，但输出不稳定 | schema 层 | 结构化输出边界没立住 | 回看 `01-structured-output` example |
| 换 provider 时牵一发动全身 | 抽象层 | service 仍依赖具体实现 | 回看 provider example 和 `module-service/app/service.py` |
| route 里越写越多 | 分层层 | HTTP 层和业务层边界错位 | 回看 [resources/02-deep-dive.md](./resources/02-deep-dive.md) |
| 测试一改文案就全挂 | 测试层 | 仍在测字符串表面，而不是测 schema | 回看 `tests/test_main.py` 和 code reading guide |

## 四、常见坑对照
看看你是否已经踩中以下任一项。

- 配置直接散落在代码里
- 路由层承担太多逻辑
- provider 名义上存在，但没有真正隔离变化
- 响应虽然是 JSON，但没有稳定 schema
- 测试只覆盖 happy path

如果踩中了，请写：
- 我踩中了哪一条
- 它是如何拖慢后续模块演进的
- 我准备如何修正

## 五、最小输出模板
请至少填完下面 6 项：

- 本阶段最有价值的工程习惯：
- 本阶段最容易退化的边界：
- 我现在最清楚的 1 条 schema 判断：
- 我现在最清楚的 1 条 provider 判断：
- 下阶段做 tool calling 前，当前骨架还需要整理哪里：
- 如果让我从头重搭一次，我最不会再犯的 1 个错误：

## 六、通过标准
满足下面这些条件，才算真的可以进入第 02 模块。

- 我已经能解释 `route -> service -> provider` 数据流
- 我已经能稳定写出结构化输入输出对象
- 我知道 fake provider 的意义
- 我知道后面 tools 会长在 service/provider 哪一层
- 我能看懂最小服务测试在保护什么

## 七、下一步行动
从下面 3 个动作里，至少写 1 个马上要执行的动作。

- 打开 [02-single-agent-with-tools/steps.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/02-single-agent-with-tools/steps.md)，开始 tools 模块
- 在自己的 `llm-gateway` 上补 1 个 provider 变体
- 把当前最不稳定的接口边界重画成一张小图
