# 本地检索与 Citation 逐段读码讲义

这个实验的重点不是检索算法多高级，而是看清“检索结果应该以什么结构进入系统”。

## 先读前你要带着的问题
- 为什么检索结果应该带 citation。
- 为什么 RAG 最小链路里先重要的是结构，而不是模型润色。
- 这个实验里的对象怎样迁移到 `knowledge-agent`。

## 第 1 步：先看文档和结果对象
- 文件：[app/main.py](./app/main.py)
- 先看：`Document` 和 `RetrievalResult`
- 重点理解：文档对象和检索结果对象把“原始资料”和“检索命中”分开了。

## 第 2 步：再看检索函数
- 文件：[app/main.py](./app/main.py)
- 先看：`retrieve()`
- 重点理解：检索阶段最重要的是稳定保留命中内容和来源，而不是追求复杂算法。

## 第 3 步：最后回到测试
- 文件：[tests/test_main.py](./tests/test_main.py)
- 重点理解：测试优先验证排序和命中结果是否稳定，而不是让模型写一段“看起来不错”的回答。

## 建议运行命令
- `python -m app.main`
- `pytest`

## 建议最小实验
- 加入新文档，观察排序变化。
- 修改 query，比较是否还能稳定命中。

## 最后把抽象迁回哪里
- 综合服务：[../../module-service/app/service.py](../../module-service/app/service.py)
- 对应抽象：`retrieve()`、citation 和响应中的证据链

## 学完后你应该能回答
- 为什么 citation 是系统能力。
- 为什么“检到了什么”和“最后怎么答”必须分阶段看。
