# 高频问答模板 代码导读

这个 example 的核心目的：为什么面试回答不能只有术语，还要有结构。

## 阅读顺序
- 先看 [app/main.py](./app/main.py)：先看 `FAQ` 和 `answer_question()`。这里不是在追求生成式回答，而是在训练“稳定回答骨架”。
- 先看 [tests/test_main.py](./tests/test_main.py)：看未知问题的默认回答结构为什么仍然重要。

## 建议运行命令
- `python -m app.main`
- `pytest`

## 建议实验
- 新增一个“为什么不用 multi-agent”的问答。

## 学完后你应该能回答
- 这个 example 为什么存在，它在整个模块里对应哪个关键知识点。
- 如果把这个 example 的抽象迁移到 `showcase-pack`，会迁移到哪一层。
