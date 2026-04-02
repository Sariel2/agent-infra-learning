# 固定数据集评测 代码导读

这个 example 的核心目的：为什么没有基线数据集，就无法做稳定迭代。

## 阅读顺序
- 先看 [app/main.py](./app/main.py)：先看 `DATASET`、`choose_tool()` 和 `run_eval()`。重点不是复杂评分，而是“固定样本 + 稳定比较”。
- 先看 [tests/test_main.py](./tests/test_main.py)：看测试如何把评测逻辑也纳入可验证范围。

## 建议运行命令
- `python -m app.main`
- `pytest`

## 建议实验
- 故意改坏 `choose_tool()`，看 eval 如何暴露退化。

## 学完后你应该能回答
- 这个 example 为什么存在，它在整个模块里对应哪个关键知识点。
- 如果把这个 example 的抽象迁移到 `agent-runtime`，会迁移到哪一层。
