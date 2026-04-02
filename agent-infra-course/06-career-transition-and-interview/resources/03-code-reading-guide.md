# 06 转型、简历与面试 代码导读

[返回学习地图](../study-map.md) | [返回模块首页](../README.md) | [上一篇：02-deep-dive.md](./02-deep-dive.md) | [下一篇：04-sources.md](./04-sources.md)

## 学习总原则
- 先看讲义，再看代码。
- 先看对象模型和函数签名，再看具体执行逻辑。
- 先跑测试，再改代码，再重新验证。

## Examples 阅读顺序
### 01-project-story-api：项目故事生成
- 这一例子主要解决：为什么同一个项目需要业务版和 infra 版两套表述。
- 先看 [`01-project-story-api/app/main.py`](../examples/01-project-story-api/app/main.py)：先看 `ProjectFacts` 与 `build_story()`，理解“项目讲述”本质上是对事实进行结构化。
- 先看 [`01-project-story-api/tests/test_main.py`](../examples/01-project-story-api/tests/test_main.py)：看测试如何确保输出至少包含项目名和核心要素。
- 建议运行命令：
  - `python -m app.main`
  - `pytest`
- 建议动手实验：
  - 换一个项目目标，重写业务版与 infra 版表达。

### 02-interview-qa-pack：高频问答模板
- 这一例子主要解决：为什么面试回答不能只有术语，还要有结构。
- 先看 [`02-interview-qa-pack/app/main.py`](../examples/02-interview-qa-pack/app/main.py)：先看 `FAQ` 和 `answer_question()`。这里不是在追求生成式回答，而是在训练“稳定回答骨架”。
- 先看 [`02-interview-qa-pack/tests/test_main.py`](../examples/02-interview-qa-pack/tests/test_main.py)：看未知问题的默认回答结构为什么仍然重要。
- 建议运行命令：
  - `python -m app.main`
  - `pytest`
- 建议动手实验：
  - 新增一个“为什么不用 multi-agent”的问答。

## module-service 阅读顺序
### showcase-pack
- 这个综合服务的目的：把项目故事、简历 bullet 和问答组织成可展示包。
- 先看 [`module-service/app/service.py`](../module-service/app/service.py)：先看 `build_story()` 与 `answer()`，理解“表达”在这里也被当成一种可结构化的工程产物。
- 先看 [`module-service/app/main.py`](../module-service/app/main.py)：再看 `/story` 和 `/qa` 如何分别承接不同表达任务。
- 先看 [`module-service/tests/test_main.py`](../module-service/tests/test_main.py)：最后看测试如何保护输出骨架。
- 建议运行命令：
  - `uvicorn app.main:app --reload`
  - `pytest`
