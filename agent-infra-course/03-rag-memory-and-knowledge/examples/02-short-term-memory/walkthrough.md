# 短期记忆裁剪 逐段读码讲义

这个实验在训练你认识 memory 的真实边界：记忆不是越多越好，而是越清楚越好。

## 先读前你要带着的问题
- 为什么短期 memory 应该是有界的。
- 为什么会话状态和外部知识不是一回事。
- 这个实验里的抽象会如何迁移到 `knowledge-agent`。

## 第 1 步：先看记忆结构
- 文件：[app/main.py](./app/main.py)
- 先看：`ConversationMemory`
- 重点理解：`deque(maxlen=limit)` 是课程里最小的有界记忆模型。

## 第 2 步：再看写入和读取逻辑
- 文件：[app/main.py](./app/main.py)
- 重点理解：记忆只保留最近窗口，不负责长期知识检索。

## 第 3 步：最后回到测试
- 文件：[tests/test_main.py](./tests/test_main.py)
- 重点理解：测试在验证旧记忆被淘汰，这说明裁剪不是副作用，而是设计目标。

## 建议运行命令
- `python -m app.main`
- `pytest`

## 建议最小实验
- 把 `limit` 调小或调大。
- 加入更多对话输入，观察淘汰行为。

## 最后把抽象迁回哪里
- 综合服务：[../../module-service/app/service.py](../../module-service/app/service.py)
- 对应抽象：`Memory` 类和有界会话状态

## 学完后你应该能回答
- 为什么 memory 不是把历史全文无限回塞。
- 为什么裁剪本身就是稳定性设计的一部分。
