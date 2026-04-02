# 短期记忆裁剪 代码导读

这个 example 的核心目的：为什么 memory 不是把对话全文塞回上下文。

## 阅读顺序
- 先看 [app/main.py](./app/main.py)：先看 `ConversationMemory` 的 `deque(maxlen=limit)`，这是课程里最小的“有界记忆”模型。
- 先看 [tests/test_main.py](./tests/test_main.py)：看测试如何验证旧记忆被淘汰。

## 建议运行命令
- `python -m app.main`
- `pytest`

## 建议实验
- 把 `limit` 调小或调大，观察记忆窗口变化。

## 学完后你应该能回答
- 这个 example 为什么存在，它在整个模块里对应哪个关键知识点。
- 如果把这个 example 的抽象迁移到 `knowledge-agent`，会迁移到哪一层。
