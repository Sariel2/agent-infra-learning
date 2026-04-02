# 本地检索与 citation 代码导读

这个 example 的核心目的：RAG 的最小链路是什么，以及为什么 citation 是系统能力。

## 阅读顺序
- 先看 [app/main.py](./app/main.py)：先看 `Document`、`RetrievalResult`，再看 `retrieve()`。重点不是算法多高级，而是检索结果如何被结构化保留下来。
- 先看 [tests/test_main.py](./tests/test_main.py)：看测试如何验证“排序结果是否符合预期”。

## 建议运行命令
- `python -m app.main`
- `pytest`

## 建议实验
- 加入新文档，观察排序变化。
- 修改 query，比较是否还能稳定命中。

## 学完后你应该能回答
- 这个 example 为什么存在，它在整个模块里对应哪个关键知识点。
- 如果把这个 example 的抽象迁移到 `knowledge-agent`，会迁移到哪一层。
