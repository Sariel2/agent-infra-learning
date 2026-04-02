# Pattern 对比 代码导读

这个 example 的核心目的：同一个任务在不同 pattern 下为什么写法不同。

## 阅读顺序
- 先看 [app/main.py](./app/main.py)：先看 `PatternOutput`，再看 `compare_patterns()`。重点不是实现复杂，而是对比不同 pattern 的控制流差异。
- 先看 [tests/test_main.py](./tests/test_main.py)：看测试如何把 pattern 对比变成稳定输出。

## 建议运行命令
- `python -m app.main`
- `pytest`

## 建议实验
- 给 compare 增加 supervisor 风格输出。

## 学完后你应该能回答
- 这个 example 为什么存在，它在整个模块里对应哪个关键知识点。
- 如果把这个 example 的抽象迁移到 `architecture-lab`，会迁移到哪一层。
