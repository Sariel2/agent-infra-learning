# 05 Agent 原理与架构 代码导读

[返回学习地图](../study-map.md) | [返回模块首页](../README.md) | [上一篇：02-deep-dive.md](./02-deep-dive.md) | [下一篇：04-sources.md](./04-sources.md)

这一页要帮你把“模式判断”落回可运行结构。第 05 模块最容易漂在概念层，所以代码导读的目标很明确：让你看到不同 pattern 和边界判断，最终都会落实成对象、步骤和推荐逻辑。

## 怎么读这一页
- 先看 pattern comparison，再看 boundary checker，最后回到 architecture-lab。
- 每次都先问：这里在比较流程，还是在做选型判断？
- 不要把代码当玩具脚本，它们是在为架构判断建立最小可运行模型。

## 推荐总顺序
1. 看 `examples/01-pattern-comparison`
2. 看 `examples/02-boundary-checker`
3. 看 `module-service/app/service.py`
4. 看 `module-service/app/main.py`
5. 看 `module-service/tests/test_main.py`

## Example 1：`01-pattern-comparison`
入口文件：
- [examples/01-pattern-comparison/app/main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/05-agent-theory-and-architecture/examples/01-pattern-comparison/app/main.py)
- [examples/01-pattern-comparison/tests/test_main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/05-agent-theory-and-architecture/examples/01-pattern-comparison/tests/test_main.py)
- [examples/01-pattern-comparison/walkthrough.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/05-agent-theory-and-architecture/examples/01-pattern-comparison/walkthrough.md)

先看这几个点：
- `PatternOutput`
- `compare_patterns()`

第一眼应该理解什么：
- `PatternOutput` 在把“模式差异”对象化。
- `compare_patterns()` 的重点不是返回什么字符串，而是把同一任务映射成不同控制流步骤。
- 这里真正训练的是“模式比较要落回步骤结构”。

接着看测试时重点看：
- 不同 pattern 是否产生不同步骤序列
- 输出是否足够结构化，能够被后续比较

建议你动手改一次：
- 增加一种 pattern，比如 `supervisor`
- 再补输出结构和测试

## Example 2：`02-boundary-checker`
入口文件：
- [examples/02-boundary-checker/app/main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/05-agent-theory-and-architecture/examples/02-boundary-checker/app/main.py)
- [examples/02-boundary-checker/tests/test_main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/05-agent-theory-and-architecture/examples/02-boundary-checker/tests/test_main.py)
- [examples/02-boundary-checker/walkthrough.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/05-agent-theory-and-architecture/examples/02-boundary-checker/walkthrough.md)

先看这几个点：
- `Scenario`
- `recommend_architecture()`

第一眼应该理解什么：
- `Scenario` 把架构选型输入变成了显式维度：开放性、步骤固定度、工具变异性。
- `recommend_architecture()` 在训练一种很重要的能力：先做复杂度判断，再决定架构。
- 这里的代码很小，但它是在给“为什么不用另一个方案”建立最小可执行骨架。

接着看测试时重点看：
- 固定步骤场景是否推荐 workflow
- 开放问题场景是否推荐 agent

建议你动手改一次：
- 新增一个维度，比如 `human_review_required`
- 再观察推荐逻辑是否要改变

## 最后看综合服务：`architecture-lab`
入口文件：
- [module-service/app/service.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/05-agent-theory-and-architecture/module-service/app/service.py)
- [module-service/app/main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/05-agent-theory-and-architecture/module-service/app/main.py)
- [module-service/tests/test_main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/05-agent-theory-and-architecture/module-service/tests/test_main.py)
- [module-service/README.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/05-agent-theory-and-architecture/module-service/README.md)

推荐读码顺序：
1. 先看 `CompareRequest`
2. 再看 `RecommendRequest`
3. 再看 `compare()`
4. 最后看 `recommend()`

第一眼应该理解什么：
- `compare()` 负责把同一任务映射成不同 pattern 的最小执行图。
- `recommend()` 负责把场景特征映射成架构建议。
- 这两个函数合在一起，分别对应“理解模式差异”和“做边界判断”。

接着再看 `app/main.py` 时重点看：
- 比较能力和推荐能力是否被拆成两个接口
- route 层是不是只做输入输出封装

最后看测试时重点看：
- 输出结构是否稳定
- 推荐逻辑是否覆盖了固定步骤、开放步骤和混合情形

## 这一页最容易读偏的地方
- 误区一：觉得代码太简单，体现不出架构
  - 这里的目标是把架构判断最小化显影出来。
- 误区二：只看返回值，不看输入维度
  - 第 05 模块最重要的是场景维度如何被显式表达。
- 误区三：把模式学习理解成记名词
  - 代码真正训练的是“模式差异如何落在流程和边界上”。

## 读完这一页后应该回哪里
- 如果你想继续执行：去 [steps.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/05-agent-theory-and-architecture/steps.md)
- 如果你想回顾原理：去 [02-deep-dive.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/05-agent-theory-and-architecture/resources/02-deep-dive.md)
- 如果你想看出处解释：去 [04-sources.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/05-agent-theory-and-architecture/resources/04-sources.md)
