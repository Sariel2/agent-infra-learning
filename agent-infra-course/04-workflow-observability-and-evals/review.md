# 04 Workflow、Observability 与 Evals 复盘模板

这一页用来判断：你是真的开始从“功能视角”走向“运行时治理视角”，还是只是给系统多加了几个节点和几条日志。第 04 模块真正重要的，是你有没有建立 workflow、trace、eval 之间的闭环。

## 什么时候做这页复盘
- 完成 [steps.md](./steps.md) 后做
- 跑过两个 example 和 `agent-runtime` 后做
- 进入第 05 模块前再回看一次

## 一、模块总结
请先用 5-8 句话回答：
- 为什么 workflow 必须显式存在
- 为什么 trace 不等于更详细的日志
- 为什么 eval 首先是比较机制，而不只是得分系统
- 为什么这三个能力必须一起学

如果写不顺，优先回看：
- [resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
- [resources/02-deep-dive.md](./resources/02-deep-dive.md)

## 二、自查清单
逐条回答 `是 / 否 / 部分做到`，并补一句证据。

- 我是否已经把“流程”从隐式代码里显式抽出来
- trace 是否记录了足够多的信息支持定位问题
- eval dataset 是否固定且可重复
- 我是否能解释 workflow 和 agent 的边界
- 我有没有只做指标收集，却没有形成改进闭环
- 我是否知道当前系统最不稳定的节点在哪里

## 三、失败归因表
把你在本模块遇到的问题尽量归到正确层。

| 现象 | 更可能的问题层 | 根因猜测 | 下一步动作 |
|---|---|---|---|
| 流程能跑，但没人说得清走法 | workflow 层 | 状态和节点没显式建模 | 回看 `WorkflowState` / `run_workflow()` |
| 最终结果错了，但找不到错在哪步 | trace 层 | 中间状态或节点信息缺失 | 回看 `run_runtime()` 中 trace 结构 |
| 感觉系统变好了，但没有证据 | eval 层 | 没有固定 dataset 或比较规则 | 回看 `EvalCase` / `DATASET` |
| 图很复杂，但没人敢改 | 架构层 | workflow 复杂度失控 | 回到第 05 模块前置判断，先减复杂度 |

## 四、常见坑对照
看看你是否已经踩中以下任一项。

- 只记录最终输出，不记录中间状态
- 没有固定评测集，导致每次都在凭感觉比较
- workflow 图过于复杂，没人看得懂
- 指标太多，反而抓不住主问题
- 把 workflow、trace、eval 当成 3 件无关的事

如果踩中了，请写：
- 我踩中了哪一条
- 它让系统治理卡在哪
- 我下一步准备如何收紧

## 五、最小输出模板
请至少填完下面 6 项：

- 当前系统最不稳定的节点：
- 当前 trace 最缺的 1 个字段：
- 当前 eval 最薄弱的 1 类样本：
- 下一轮优化更应该先动 prompt、tool、retrieval，还是 workflow：
- 我现在最能讲清的 1 条运行时治理判断：
- 进入 pattern 模块前，我最想保留的 1 条复杂度控制意识：

## 六、通过标准
满足下面这些条件，才算真的可以进入第 05 模块。

- 我已经能解释 workflow、trace、eval 三者关系
- 我知道 trace 不是日志加强版
- 我已经建立最小固定评测样本
- 我知道“流程显式化”为什么会降低维护成本
- 我能从一个失败样例中说出先该看哪层

## 七、下一步行动
从下面 3 个动作里，至少写 1 个马上要执行的动作。

- 打开 [05-agent-theory-and-architecture/steps.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/05-agent-theory-and-architecture/steps.md)，开始 pattern 模块
- 给当前 `agent-runtime` 增加 1 个新的 eval case
- 给 trace 结构补 1 个你现在最缺的元数据字段
