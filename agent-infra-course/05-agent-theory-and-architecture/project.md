# 05 Agent 原理与架构 模块综合项目说明

## 项目名
`architecture-lab`

## 项目定位
这是整门课里最偏“架构判断实验室”的项目。它不是业务系统，而是把 pattern 比较和边界判断做成可运行实验，帮助你把抽象架构讨论落回具体控制流和场景维度。

## 对应综合服务
- 服务入口：[module-service/app/main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/05-agent-theory-and-architecture/module-service/app/main.py)
- 服务逻辑：[module-service/app/service.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/05-agent-theory-and-architecture/module-service/app/service.py)
- 测试入口：[module-service/tests/test_main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/05-agent-theory-and-architecture/module-service/tests/test_main.py)

## 项目目标
做一个最小架构实验室，能够：
- 比较不同 pattern 的最小流程结构
- 根据场景特征给出架构建议
- 训练“为什么不用另一个方案”的表达能力

## 你最终应该学到什么
- pattern 的本质是控制流设计
- 边界判断比框架名字更重要
- multi-agent 只是某些场景下的组织方式，而不是默认升级路线
- 真正成熟的架构判断来自复杂度控制

## 必做项
- 至少比较 3 种 pattern
- 至少显式表达 3 个场景维度
- 至少提供一个推荐接口
- 测试覆盖不同 pattern 输出和不同场景推荐

## 推荐实现顺序
1. 先跑 `examples/01-pattern-comparison`
2. 再跑 `examples/02-boundary-checker`
3. 再读 [resources/03-code-reading-guide.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/05-agent-theory-and-architecture/resources/03-code-reading-guide.md)
4. 再回到 `architecture-lab`
5. 最后做 [review.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/05-agent-theory-and-architecture/review.md)

## 实现清单
- `compare()` 能返回不同 pattern 的最小步骤结构
- `recommend()` 能根据输入维度给建议
- 输入维度必须显式，而不是隐式散在逻辑里
- HTTP 层把比较和推荐拆成不同入口
- 测试覆盖 workflow / agent / hybrid 等基本判断

## 验收清单
- 我能比较同一任务在不同 pattern 下的步骤差异
- 我能解释场景维度为什么会改变推荐结果
- 我能新增一个 pattern 或一个新维度并补齐测试
- 我能说清为什么某些需求不值得上 multi-agent
- 我能把项目里的推荐逻辑翻译成面试中的架构判断

## 常见退化点
- 只记 pattern 名字，不落到控制流
- 输入维度不显式，最后全靠口头解释
- 所有结论都变成“视场景而定”
- 复杂度预算没有真正进入推荐逻辑

## 加分项
- 增加 `supervisor` 或 `router+workflow` 这类混合模式
- 增加 `human_review_required` 等新维度
- 给推荐结果补充理由字段
- 输出一段适合面试讲解的架构解释

## 交付物
- 一个可运行的模式比较实验室
- 一组覆盖不同场景的推荐测试
- 一份你自己总结的架构判断原则表

## 进入下一模块前，你应该能回答
- 为什么 pattern 学习不能停在术语层
- 为什么复杂度控制能力比追新框架更重要
- 为什么“为什么不用另一个方案”是高级判断的核心
