# 边界判断器 代码导读

这个 example 的核心目的：什么时候应该选 workflow，什么时候才值得上 agent。

## 阅读顺序
- 先看 [app/main.py](./app/main.py)：先看 `Scenario`，再看 `recommend_architecture()`。它在训练你的不是算法，而是判断维度。
- 先看 [tests/test_main.py](./tests/test_main.py)：看固定场景如何导出稳定建议。

## 建议运行命令
- `python -m app.main`
- `pytest`

## 建议实验
- 设计一个 hybrid 场景，看看推荐是否合理。

## 学完后你应该能回答
- 这个 example 为什么存在，它在整个模块里对应哪个关键知识点。
- 如果把这个 example 的抽象迁移到 `architecture-lab`，会迁移到哪一层。
