# 工具契约与校验

这个实验用来证明：工具调用最先要解决的不是 prompt，而是 schema 和边界。

## 这个实验要学会什么
- 为什么 tool schema 会直接影响工具选择质量。
- 为什么参数校验应该尽早发生。
- 为什么工具返回值也需要稳定结构。

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
- 给 `ToolCall` 增加一个新字段。
- 把 `query` 设为空，观察失败是如何提前暴露的。

## 跑完之后要观察什么
- 为什么 schema 坏了，后面的 agent loop 再聪明也会出问题。
- 为什么参数错误越早暴露越容易治理。
- 这个实验如何映射到 [../../module-service/README.md](../../module-service/README.md) 里的工具函数和 trace 结构。

## 做完后回哪里
- 综合服务：[../../module-service/README.md](../../module-service/README.md)
- 练习手册：[../../exercises.md](../../exercises.md)
