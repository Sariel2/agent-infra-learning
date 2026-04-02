# Provider 抽象 代码导读

这个 example 的核心目的：为什么模型调用必须与业务逻辑解耦。

## 阅读顺序
- 先看 [app/main.py](./app/main.py)：先看 `Provider` 协议，再看 `EchoProvider` 与 `FakeLLMProvider`，理解“同一接口，不同实现”的工程价值。
- 先看 [tests/test_main.py](./tests/test_main.py)：看同一业务函数如何在不同 provider 上被稳定测试。

## 建议运行命令
- `python -m app.main`
- `pytest`

## 建议实验
- 新增一个 `UppercaseProvider`，不改业务函数，只扩展实现。

## 学完后你应该能回答
- 这个 example 为什么存在，它在整个模块里对应哪个关键知识点。
- 如果把这个 example 的抽象迁移到 `llm-gateway`，会迁移到哪一层。
