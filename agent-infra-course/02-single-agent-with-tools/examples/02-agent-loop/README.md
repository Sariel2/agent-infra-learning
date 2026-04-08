# 最小 Agent Loop

这个实验用来证明：agent 的一次运行应该被看成一个决策过程，而不是一次黑盒回答。

## 这个实验要学会什么
- 识别最小 agent loop 的几个阶段。
- 区分“工具选择”和“工具执行”这两类问题。
- 看清 observation 为什么会决定后续继续、停止或改道。

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
- 增加一个新工具路径。
- 改变 `choose_tool` 规则，观察 loop 结果如何变化。

## 跑完之后要观察什么
- 为什么 agent loop 不只是“模型帮你选一下工具”。
- 为什么最小 loop 也应该可测试。
- 这个实验如何映射到 [../../module-service/README.md](../../module-service/README.md) 里的 `run_agent()`。

## 做完后回哪里
- 综合服务：[../../module-service/README.md](../../module-service/README.md)
- 练习手册：[../../exercises.md](../../exercises.md)
