# showcase-pack

把项目故事、简历 bullet 和问答组织成可展示包。

## 这个综合服务在模块里的位置
它不是一个额外 demo，而是这个模块知识点的收束点。你应该在跑完 examples 之后再来看它，这样你能看出哪些抽象是从 examples 提升而来的。

## 建议阅读顺序
- 先看 [app/service.py](./app/service.py)：先看 `build_story()` 与 `answer()`，理解“表达”在这里也被当成一种可结构化的工程产物。
- 先看 [app/main.py](./app/main.py)：再看 `/story` 和 `/qa` 如何分别承接不同表达任务。
- 先看 [tests/test_main.py](./tests/test_main.py)：最后看测试如何保护输出骨架。

## 建议运行命令
- `uvicorn app.main:app --reload`
- `pytest`

## 学完后你应该能回答
- 这个服务如何把 `06 转型、简历与面试` 的核心概念组合到一起。
- 为什么这些能力要按当前这种分层组织。
- 如果继续扩展，这个服务最先该从哪里演进。
