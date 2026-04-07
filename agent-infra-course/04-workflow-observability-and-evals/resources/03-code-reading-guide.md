# 04 Workflow、Observability 与 Evals 代码导读

[返回学习地图](../study-map.md) | [返回模块首页](../README.md) | [上一篇：02-deep-dive.md](./02-deep-dive.md) | [下一篇：04-sources.md](./04-sources.md)

这一页要带你看到：workflow、trace、eval 在代码里其实是同一条治理链的不同切面。第 04 模块最应该看懂的，不是节点名字，而是：
- 状态怎样进入流程
- 路径怎样被显式化
- 结果怎样被比对

## 怎么读这一页
- 先看 workflow example，再看 eval example，最后回到综合运行时。
- 每个文件都先看对象模型，再看执行函数。
- 读的时候一直问：这里是在描述“应该怎么走”、还是“实际怎么走”、还是“走得好不好”？

## 推荐总顺序
1. 看 `examples/01-stateful-workflow`
2. 看 `examples/02-eval-runner`
3. 看 `module-service/app/service.py`
4. 看 `module-service/app/main.py`
5. 看 `module-service/tests/test_main.py`

## Example 1：`01-stateful-workflow`
入口文件：
- [examples/01-stateful-workflow/app/main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/04-workflow-observability-and-evals/examples/01-stateful-workflow/app/main.py)
- [examples/01-stateful-workflow/tests/test_main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/04-workflow-observability-and-evals/examples/01-stateful-workflow/tests/test_main.py)
- [examples/01-stateful-workflow/walkthrough.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/04-workflow-observability-and-evals/examples/01-stateful-workflow/walkthrough.md)

先看这几个点：
- `WorkflowState`
- `run_workflow()`

第一眼应该理解什么：
- `WorkflowState` 是流程显式化的关键对象。
- `needs_review` 和 `completed` 这类字段，在提醒你：流程不是一串步骤名，而是状态变化。
- `run_workflow()` 返回步骤列表虽然很简化，但它已经把“条件分支”和“人工审核位”显式表达出来。

接着看测试时重点看：
- `refund` 场景是否进入 `human_review`
- 固定路径和带审核路径是否都被覆盖

建议你动手改一次：
- 新增一个需要特殊分支的场景，比如 `vip refund`
- 再补状态字段和测试

## Example 2：`02-eval-runner`
入口文件：
- [examples/02-eval-runner/app/main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/04-workflow-observability-and-evals/examples/02-eval-runner/app/main.py)
- [examples/02-eval-runner/tests/test_main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/04-workflow-observability-and-evals/examples/02-eval-runner/tests/test_main.py)
- [examples/02-eval-runner/walkthrough.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/04-workflow-observability-and-evals/examples/02-eval-runner/walkthrough.md)

先看这几个点：
- `EvalCase`
- `EvalResult`
- `DATASET`
- `choose_tool()`
- `run_eval()`

第一眼应该理解什么：
- `EvalCase` 把测试样本对象化。
- `DATASET` 是这门课里“固定样本”意识的最小实现。
- `run_eval()` 的价值不在复杂评分，而在“固定输入 -> 稳定比较”。

接着看测试时重点看：
- 评测结果是否可重复
- 是否只比较必要行为，而不是过度复杂指标

建议你动手改一次：
- 加一个容易混淆的新 case
- 观察 `matched` 是否变化

## 最后看综合服务：`agent-runtime`
入口文件：
- [module-service/app/service.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/04-workflow-observability-and-evals/module-service/app/service.py)
- [module-service/app/main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/04-workflow-observability-and-evals/module-service/app/main.py)
- [module-service/tests/test_main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/04-workflow-observability-and-evals/module-service/tests/test_main.py)
- [module-service/README.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/04-workflow-observability-and-evals/module-service/README.md)

推荐读码顺序：
1. 先看 `RunRequest`
2. 再看 `DATASET`
3. 再看 `classify_node()`
4. 再看 `run_runtime()`
5. 最后看 `evaluate()`

第一眼应该理解什么：
- `classify_node()` 在表达流程入口分流。
- `run_runtime()` 把 trace 明确保存成节点列表。
- `evaluate()` 把固定样本比较做成运行时自带能力，而不是外部随手测几条。

接着再看 `app/main.py` 时重点看：
- 运行接口和评测接口是否分开
- route 层有没有把 runtime 逻辑掺进去

最后看测试时重点看：
- trace 结构是否被验证
- eval 输出是否保持稳定

## 这一页最容易读偏的地方
- 误区一：只把 workflow 看成“多几个步骤”
  - 更重要的是状态和分支被显式表达。
- 误区二：只把 eval 看成“给个分数”
  - 这里它首先是稳定比较机制。
- 误区三：忽略 trace 返回结构
  - 第 04 模块最关键的工程意识之一，就是过程要能被复盘。

## 读完这一页后应该回哪里
- 如果你想继续执行：去 [steps.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/04-workflow-observability-and-evals/steps.md)
- 如果你想回顾原理：去 [02-deep-dive.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/04-workflow-observability-and-evals/resources/02-deep-dive.md)
- 如果你想看出处解释：去 [04-sources.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/04-workflow-observability-and-evals/resources/04-sources.md)
