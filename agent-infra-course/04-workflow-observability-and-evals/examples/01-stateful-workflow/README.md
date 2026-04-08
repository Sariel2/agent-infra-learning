# 状态驱动 Workflow

这个实验用来证明：固定步骤和高风险节点应该显式建成 workflow 状态，而不是交给自由 agent 随机游走。

## 这个实验要学会什么
- 理解状态如何决定分支。
- 理解为什么人工审核点应该是显式节点。
- 理解 workflow 为什么是控制风险的手段，而不是“低级方案”。

## 开始前先回看
- 讲义主线：[../../resources/01-concepts-and-principles.md](../../resources/01-concepts-and-principles.md)
- 原理细节：[../../resources/02-deep-dive.md](../../resources/02-deep-dive.md)
- 读码导引：[./walkthrough.md](./walkthrough.md)

## 先看哪些文件
- 核心代码：[app/main.py](./app/main.py)
- 测试文件：[tests/test_main.py](./tests/test_main.py)

## 推荐运行命令
- `python -m app.main`
- `pytest`

## 建议最小改动
- 增加一种新意图，并设计一个新分支。
- 改一个状态流转条件，观察测试是否能拦住退化。

## 跑完之后要观察什么
- 为什么状态图让系统更容易解释和调试。
- 为什么高风险路径应该显式入图。
- 这个实验如何映射到 [../../module-service/README.md](../../module-service/README.md) 里的 `classify_node()` 和 trace。

## 做完后回哪里
- 综合服务：[../../module-service/README.md](../../module-service/README.md)
- 练习手册：[../../exercises.md](../../exercises.md)
