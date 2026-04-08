# agent-runtime

把 workflow、trace 和 eval 统一进同一个运行时服务。

## 这个综合服务的目标
- 把“单次运行”与“批量评测”放进同一个运行时视角里理解。
- 用最小 workflow 展示状态节点和执行轨迹。
- 用固定 dataset 让系统优化有可比较的基线。

## 开始前先回看
- 模块首页：[../README.md](../README.md)
- 学习地图：[../study-map.md](../study-map.md)
- 概念讲义：[../resources/01-concepts-and-principles.md](../resources/01-concepts-and-principles.md)
- 原理细节：[../resources/02-deep-dive.md](../resources/02-deep-dive.md)
- 代码导读：[../resources/03-code-reading-guide.md](../resources/03-code-reading-guide.md)
- 示例 1：[../examples/01-stateful-workflow/app/main.py](../examples/01-stateful-workflow/app/main.py)
- 示例 2：[../examples/02-eval-runner/app/main.py](../examples/02-eval-runner/app/main.py)

## 先理解这 3 个文件
- 核心逻辑：[app/service.py](./app/service.py)
  先看 `classify_node()`、`run_runtime()` 和 `evaluate()`，理解“运行一次”和“评估一批”是不同能力。
- HTTP 入口：[app/main.py](./app/main.py)
  看 `/run` 和 `/eval` 为什么要分开暴露。
- 最小验收：[tests/test_main.py](./tests/test_main.py)
  看测试如何把“评测全部匹配”固定成基线。

## 推荐实现顺序
1. 先读 [app/service.py](./app/service.py)，理解 `DATASET`、`classify_node()`、`run_runtime()`、`evaluate()` 之间的关系。
2. 再看 [tests/test_main.py](./tests/test_main.py)，确认基线评测在测什么。
3. 最后读 [app/main.py](./app/main.py)，看 `/run` 和 `/eval` 入口如何分别承接运行与验证。
4. 自己尝试新增一个 message case，观察它会如何同时影响 runtime 和 eval。

## 动手实现时每一步做什么
### Step 1：先固定节点分类逻辑
- 要改的文件：[app/service.py](./app/service.py)
- 要做的事：把 `classify_node()` 写稳定，因为这是整个最小 workflow 的入口判断。
- 验收标准：同一条 message 反复执行时，节点归类保持稳定。

### Step 2：再把 trace 建出来
- 要改的文件：[app/service.py](./app/service.py)
- 要做的事：在 `run_runtime()` 中显式记录 `classify -> node -> respond` 三段轨迹。
- 验收标准：返回值里必须有可读的 `trace`，而不是只有最终答案。

### Step 3：最后接上 eval
- 要改的文件：[app/service.py](./app/service.py)
- 要改的文件：[tests/test_main.py](./tests/test_main.py)
- 要做的事：让 `evaluate()` 基于固定 `DATASET` 批量比较预期节点与实际节点。
- 验收标准：`/eval` 返回中的每一项都带 `matched` 结果。

## 建议运行命令
- `uvicorn app.main:app --reload`
- `pytest`

## 常见退化点
- 把日志当成 trace，用一堆文本替代结构化轨迹。
- 没有固定 dataset，就开始谈“系统更稳定了”。
- workflow 节点和 eval 样本脱节，导致调优没法回归比较。

## 扩展时优先做什么
- 给 trace 增加输入、输出、latency、error 字段。
- 给 eval 增加质量、延迟、成本等更完整指标。
- 引入人工审核节点和失败样本归档。

## 学完后你应该能回答
- 为什么 workflow 和 eval 应该一起考虑。
- 为什么 trace 不是“可有可无的日志升级版”。
- 如果系统“有时好有时坏”，你应该先补什么证据。
