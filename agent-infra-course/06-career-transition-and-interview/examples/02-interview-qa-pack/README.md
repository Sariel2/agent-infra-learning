# 高频问答模板

这个实验用来证明：面试回答不能只有术语堆砌，还需要稳定的回答骨架。

## 这个实验要学会什么
- 用模板组织高频技术问答。
- 把“目标、设计、失败、取舍、结果”变成默认回答骨架。
- 让表达材料具备复用性，而不是每次重来。

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
- 新增一个“为什么不用 multi-agent”的问答。
- 改写默认回答模板，观察结构是否更稳定。

## 跑完之后要观察什么
- 为什么结构化表达会显著提高面试稳定性。
- 为什么未知问题也应该有默认回答骨架。
- 这个实验如何映射到 [../../module-service/README.md](../../module-service/README.md) 里的 `answer()`。

## 做完后回哪里
- 综合服务：[../../module-service/README.md](../../module-service/README.md)
- 练习手册：[../../exercises.md](../../exercises.md)
