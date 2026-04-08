# 设置与日志上下文

这个实验用来证明一件事：课程为什么要从配置对象和日志上下文开始，而不是一上来就谈复杂 agent 能力。

## 这个实验要学会什么
- 用配置对象固定系统运行参数。
- 用日志上下文固定最小观测入口。
- 理解“先建立系统形状”为什么是后续所有模块的前提。

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
- 修改 `timeout_seconds`，观察输出如何变化。
- 给 `Settings` 增加一个新字段，再补上测试。

## 跑完之后要观察什么
- 配置为什么要先对象化，而不是散落在函数参数里。
- 日志上下文为什么越早建立，后面越容易排错。
- 这个实验如何映射到 [../../module-service/README.md](../../module-service/README.md) 里的 `starter-workspace`。

## 做完后回哪里
- 综合服务：[../../module-service/README.md](../../module-service/README.md)
- 练习手册：[../../exercises.md](../../exercises.md)
