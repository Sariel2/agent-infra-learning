# 设置与日志上下文 代码导读

这个 example 的核心目的：为什么课程从配置对象和日志上下文开始。

## 阅读顺序
- 先看 [app/main.py](./app/main.py)：先看 `Settings` 和 `build_log_context`，理解“先固定系统形状，再讨论复杂能力”。
- 先看 [tests/test_main.py](./tests/test_main.py)：再看测试，观察课程如何把抽象对象转成可验证行为。

## 建议运行命令
- `python -m app.main`
- `pytest`

## 建议实验
- 修改 `timeout_seconds`，观察输出变化。
- 给 `Settings` 增加一个字段，再补测试。

## 学完后你应该能回答
- 这个 example 为什么存在，它在整个模块里对应哪个关键知识点。
- 如果把这个 example 的抽象迁移到 `starter-workspace`，会迁移到哪一层。
