# 结构化输出 代码导读

这个 example 的核心目的：模型输出为什么必须尽量变成稳定 schema。

## 阅读顺序
- 先看 [app/main.py](./app/main.py)：先看 `StructuredAnswer`，它不是装饰，而是系统契约。再看 `generate_structured_answer`，理解课程为什么先用 deterministic stub。
- 先看 [tests/test_main.py](./tests/test_main.py)：看测试如何验证输出形状，而不是只验证一段自由文本。

## 建议运行命令
- `python -m app.main`
- `pytest`

## 建议实验
- 给 `StructuredAnswer` 新增字段，再修复实现和测试。
- 把 `confidence` 改成非法值，观察验证失败。

## 学完后你应该能回答
- 这个 example 为什么存在，它在整个模块里对应哪个关键知识点。
- 如果把这个 example 的抽象迁移到 `llm-gateway`，会迁移到哪一层。
