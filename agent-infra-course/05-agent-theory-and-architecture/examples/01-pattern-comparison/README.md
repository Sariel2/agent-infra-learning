# Pattern 对比

这个实验用来证明：同一个任务换一种 pattern，控制流和工程边界就会跟着变。

## 这个实验要学会什么
- 看清不同 pattern 的流程差异。
- 理解模式选择不是“谁更高级”，而是“谁更适合当前任务结构”。
- 学会把抽象模式压缩成可以运行的最小对比实验。

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
- 给 compare 增加一种 supervisor 风格输出。
- 改一个任务描述，观察不同模式的流程表示是否仍清晰。

## 跑完之后要观察什么
- 为什么模式差异应该被显式比较，而不是只靠直觉。
- 为什么流程结构比框架名字更重要。
- 这个实验如何映射到 [../../module-service/README.md](../../module-service/README.md) 里的 `compare()`。

## 做完后回哪里
- 综合服务：[../../module-service/README.md](../../module-service/README.md)
- 练习手册：[../../exercises.md](../../exercises.md)
