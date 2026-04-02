# 05 Agent 原理与架构 代码导读

[返回学习地图](../study-map.md) | [返回模块首页](../README.md) | [上一篇：02-deep-dive.md](./02-deep-dive.md) | [下一篇：04-sources.md](./04-sources.md)

## 学习总原则
- 先看讲义，再看代码。
- 先看对象模型和函数签名，再看具体执行逻辑。
- 先跑测试，再改代码，再重新验证。

## Examples 阅读顺序
### 01-pattern-comparison：Pattern 对比
- 这一例子主要解决：同一个任务在不同 pattern 下为什么写法不同。
- 先看 [`01-pattern-comparison/app/main.py`](../examples/01-pattern-comparison/app/main.py)：先看 `PatternOutput`，再看 `compare_patterns()`。重点不是实现复杂，而是对比不同 pattern 的控制流差异。
- 先看 [`01-pattern-comparison/tests/test_main.py`](../examples/01-pattern-comparison/tests/test_main.py)：看测试如何把 pattern 对比变成稳定输出。
- 建议运行命令：
  - `python -m app.main`
  - `pytest`
- 建议动手实验：
  - 给 compare 增加 supervisor 风格输出。

### 02-boundary-checker：边界判断器
- 这一例子主要解决：什么时候应该选 workflow，什么时候才值得上 agent。
- 先看 [`02-boundary-checker/app/main.py`](../examples/02-boundary-checker/app/main.py)：先看 `Scenario`，再看 `recommend_architecture()`。它在训练你的不是算法，而是判断维度。
- 先看 [`02-boundary-checker/tests/test_main.py`](../examples/02-boundary-checker/tests/test_main.py)：看固定场景如何导出稳定建议。
- 建议运行命令：
  - `python -m app.main`
  - `pytest`
- 建议动手实验：
  - 设计一个 hybrid 场景，看看推荐是否合理。

## module-service 阅读顺序
### architecture-lab
- 这个综合服务的目的：把 pattern 对比和边界判断组织成一个可演示的实验服务。
- 先看 [`module-service/app/service.py`](../module-service/app/service.py)：先看 `compare()` 和 `recommend()`，理解“模式对比”和“场景判断”是两个互补维度。
- 先看 [`module-service/app/main.py`](../module-service/app/main.py)：再看如何用不同接口暴露它们。
- 先看 [`module-service/tests/test_main.py`](../module-service/tests/test_main.py)：最后看最小自动验证如何保护判断逻辑。
- 建议运行命令：
  - `uvicorn app.main:app --reload`
  - `pytest`
