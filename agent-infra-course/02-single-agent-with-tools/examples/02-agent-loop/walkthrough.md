# 最小 agent loop 代码导读

这个 example 的核心目的：模型决策、工具执行和 observation 是如何组成最小 agent loop 的。

## 阅读顺序
- 先看 [app/main.py](./app/main.py)：先看 `choose_tool`，再看 `run_agent`。这里最重要的是看清“决策点”和“执行点”的分离。
- 先看 [tests/test_main.py](./tests/test_main.py)：看同一个 loop 如何被固定输入稳定验证。

## 建议运行命令
- `python -m app.main`
- `pytest`

## 建议实验
- 增加一个新工具路径，观察 loop 如何扩展。

## 学完后你应该能回答
- 这个 example 为什么存在，它在整个模块里对应哪个关键知识点。
- 如果把这个 example 的抽象迁移到 `support-agent`，会迁移到哪一层。
