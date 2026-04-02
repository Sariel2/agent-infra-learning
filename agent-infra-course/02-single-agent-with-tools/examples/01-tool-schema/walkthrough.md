# 工具契约与校验 代码导读

这个 example 的核心目的：为什么工具调用的首要问题不是 prompt，而是 schema。

## 阅读顺序
- 先看 [app/main.py](./app/main.py)：先看 `ToolCall` 与 `ToolResult`。这两个对象定义了模型与工具之间的协议。再看 `search_docs`，理解工具本身应该尽量简单、可预测。
- 先看 [tests/test_main.py](./tests/test_main.py)：看参数错误如何在进入工具逻辑前就被拦住。

## 建议运行命令
- `python -m app.main`
- `pytest`

## 建议实验
- 给 `ToolCall` 增加一个新字段，观察测试和函数如何跟着调整。
- 把 `query` 设为空，感受“失败应该尽早暴露”的价值。

## 学完后你应该能回答
- 这个 example 为什么存在，它在整个模块里对应哪个关键知识点。
- 如果把这个 example 的抽象迁移到 `support-agent`，会迁移到哪一层。
