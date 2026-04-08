# Provider 抽象

这个实验用来证明：模型调用应该先被抽成稳定接口，再考虑接什么真实模型。

## 这个实验要学会什么
- 为什么 provider abstraction 先解决的是边界和测试性。
- 为什么业务逻辑不应该直接绑死某个具体模型实现。
- 为什么 fake provider 是后面所有工程推进的加速器。

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
- 新增一个 `UppercaseProvider`，但不改业务函数。
- 替换默认 provider，观察测试是否仍然能稳定写。

## 跑完之后要观察什么
- 为什么“同一接口，不同实现”会让工程迭代更轻。
- 为什么 fake provider 能把外部波动和内部设计问题分开。
- 这个实验如何映射到 [../../module-service/README.md](../../module-service/README.md) 里的 `FakeProvider` 和 `generate()`。

## 做完后回哪里
- 综合服务：[../../module-service/README.md](../../module-service/README.md)
- 练习手册：[../../exercises.md](../../exercises.md)
