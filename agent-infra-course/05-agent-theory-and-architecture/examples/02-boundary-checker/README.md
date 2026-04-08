# 边界判断器

这个实验用来证明：很多“该不该上 agent”的问题，本质上是在做任务边界判断。

## 这个实验要学会什么
- 用任务特征判断 workflow、agent 或 hybrid。
- 理解“固定步骤”和“开放探索”是两类不同任务。
- 学会把架构选择变成显式规则，而不是经验口感。

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
- 设计一个 hybrid 场景。
- 调整一个判断条件，观察推荐结果是否符合预期。

## 跑完之后要观察什么
- 为什么模式选择应该有稳定判断维度。
- 为什么很多任务用 workflow 就已经足够。
- 这个实验如何映射到 [../../module-service/README.md](../../module-service/README.md) 里的 `recommend()`。

## 做完后回哪里
- 综合服务：[../../module-service/README.md](../../module-service/README.md)
- 练习手册：[../../exercises.md](../../exercises.md)
