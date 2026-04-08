# 状态驱动 Workflow 逐段读码讲义

这个实验的关键，是让你看到“状态图”为什么能替代很多不必要的 agent 自由度。

## 先读前你要带着的问题
- 为什么固定步骤任务更适合 workflow。
- 为什么人工审核应该是显式节点。
- 这个实验如何迁移到 `agent-runtime`。

## 第 1 步：先看状态对象
- 文件：[app/main.py](./app/main.py)
- 先看：`WorkflowState`
- 重点理解：状态对象先定义了系统处在哪一步，后面分支只是读取这个状态。

## 第 2 步：再看执行函数
- 文件：[app/main.py](./app/main.py)
- 先看：`run_workflow()`
- 重点理解：这里真正重要的是“状态决定路径”，而不是让模型自由跳转。

## 第 3 步：最后回到测试
- 文件：[tests/test_main.py](./tests/test_main.py)
- 重点理解：测试在锁定高风险路径，例如 refund 场景必须经过人工审核。

## 建议运行命令
- `python -m app.main`
- `pytest`

## 建议最小实验
- 增加一种新意图，设计一个新分支。
- 修改一个状态流转条件，观察测试能否拦住退化。

## 最后把抽象迁回哪里
- 综合服务：[../../module-service/app/service.py](../../module-service/app/service.py)
- 对应抽象：节点分类、状态流和运行轨迹

## 学完后你应该能回答
- 为什么 workflow 不是“低级版 agent”。
- 为什么状态显式化会直接提升可解释性和可审计性。
