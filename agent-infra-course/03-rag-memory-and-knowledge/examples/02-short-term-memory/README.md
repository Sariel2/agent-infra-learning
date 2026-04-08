# 短期记忆裁剪

这个实验用来证明：memory 的关键不是“记更多”，而是“记得有边界、记得有目的”。

## 这个实验要学会什么
- 为什么短期 memory 应该有窗口和裁剪。
- 为什么 memory 和 retrieval 不能混在一层。
- 为什么旧记忆淘汰也是一种设计选择。

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
- 把 `limit` 调小或调大。
- 增加更多对话输入，观察旧记忆何时被淘汰。

## 跑完之后要观察什么
- 为什么“把对话全塞回去”不是 memory 设计。
- 为什么有界记忆会让系统更可控。
- 这个实验如何映射到 [../../module-service/README.md](../../module-service/README.md) 里的 `Memory`。

## 做完后回哪里
- 综合服务：[../../module-service/README.md](../../module-service/README.md)
- 练习手册：[../../exercises.md](../../exercises.md)
