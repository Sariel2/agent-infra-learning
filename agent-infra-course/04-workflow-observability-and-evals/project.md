# 04 Workflow、Observability 与 Evals 模块综合项目说明

## 项目名
`agent-runtime`

## 项目定位
这是整门课从“功能 demo”走向“运行时系统”的关键项目。它要把 workflow、trace 和 eval 串成一个最小治理闭环，而不是只增加几条流程分支。

## 对应综合服务
- 服务入口：[module-service/app/main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/04-workflow-observability-and-evals/module-service/app/main.py)
- 服务逻辑：[module-service/app/service.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/04-workflow-observability-and-evals/module-service/app/service.py)
- 测试入口：[module-service/tests/test_main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/04-workflow-observability-and-evals/module-service/tests/test_main.py)

## 项目目标
做一个 production-like 的最小 runtime，能够：
- 显式执行 workflow
- 返回结构化 trace
- 跑固定 eval dataset
- 形成最小回归比较机制

## 你最终应该学到什么
- 为什么流程必须显式化
- 为什么 trace 是过程模型
- 为什么 eval 是系统演进比较器
- 为什么这三者必须一起治理

## 必做项
- 至少有一个显式 workflow 分支
- 至少有一个 trace 返回结构
- 至少有一组固定 eval dataset
- 至少有一个 `/run` 和一个 `/eval` 类入口
- 测试覆盖最小运行链和评测链

## 推荐实现顺序
1. 先跑 `examples/01-stateful-workflow`
2. 再跑 `examples/02-eval-runner`
3. 再读 [resources/03-code-reading-guide.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/04-workflow-observability-and-evals/resources/03-code-reading-guide.md)
4. 再回到 `agent-runtime`
5. 最后做 [review.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/04-workflow-observability-and-evals/review.md)

## 实现清单
- `classify_node()` 或等价入口分流存在
- `run_runtime()` 保留节点级 trace
- `evaluate()` 基于固定 dataset 做比较
- HTTP 层区分运行和评测两个入口
- 测试既验证流程，也验证评测结果结构

## 验收清单
- 我能清楚说明流程图对应哪段代码
- 我能指出 trace 里最关键的字段
- 我能展示固定 dataset 如何参与比较
- 我能新增 1 条 eval case 并说明意义
- 我能解释这个项目为什么比前几个模块更接近运行时系统

## 常见退化点
- 只有流程图，没有执行骨架
- trace 里没有足够上下文
- eval 只是手工试几个 case
- workflow 越做越复杂，但没有治理价值

## 加分项
- 给 trace 增加 request id / run id / metadata
- 把某些评测逻辑拆到异步路径
- 增加更细的节点状态
- 对不同路径做最小成本/延迟记录

## 交付物
- 一个最小 runtime 服务
- 一组固定评测样本
- 一份你自己总结的治理闭环说明

## 进入下一模块前，你应该能回答
- 为什么 workflow 不是 agent 的对立面
- 为什么 trace 和 eval 会决定你是否真的能维护系统
- 为什么运行时治理比“多加功能点”更关键
