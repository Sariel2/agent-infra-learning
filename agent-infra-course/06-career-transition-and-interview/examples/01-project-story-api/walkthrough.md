# 项目故事生成 代码导读

这个 example 的核心目的：为什么同一个项目需要业务版和 infra 版两套表述。

## 阅读顺序
- 先看 [app/main.py](./app/main.py)：先看 `ProjectFacts` 与 `build_story()`，理解“项目讲述”本质上是对事实进行结构化。
- 先看 [tests/test_main.py](./tests/test_main.py)：看测试如何确保输出至少包含项目名和核心要素。

## 建议运行命令
- `python -m app.main`
- `pytest`

## 建议实验
- 换一个项目目标，重写业务版与 infra 版表达。

## 学完后你应该能回答
- 这个 example 为什么存在，它在整个模块里对应哪个关键知识点。
- 如果把这个 example 的抽象迁移到 `showcase-pack`，会迁移到哪一层。
