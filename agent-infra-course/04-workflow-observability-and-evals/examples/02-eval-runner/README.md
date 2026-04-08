# 固定数据集评测

这个实验用来证明：没有固定数据集，就很难判断一次优化到底是真的变好，还是只是样本碰巧换了。

## 这个实验要学会什么
- 为什么 eval 要依赖固定 dataset。
- 为什么回归比较比“主观感觉”更重要。
- 为什么评测逻辑本身也应该被测试。

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
- 故意改坏 `choose_tool()`。
- 增加一个新的样本 case，并观察 `run_eval()` 结果。

## 跑完之后要观察什么
- 为什么同一批样本是“版本比较”的前提。
- 为什么评测输出也应该稳定结构化。
- 这个实验如何映射到 [../../module-service/README.md](../../module-service/README.md) 里的 `DATASET` 和 `evaluate()`。

## 做完后回哪里
- 综合服务：[../../module-service/README.md](../../module-service/README.md)
- 练习手册：[../../exercises.md](../../exercises.md)
