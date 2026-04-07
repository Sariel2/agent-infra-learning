# 01 Python 与 Agent 基础 代码导读

[返回学习地图](../study-map.md) | [返回模块首页](../README.md) | [上一篇：02-deep-dive.md](./02-deep-dive.md) | [下一篇：04-sources.md](./04-sources.md)

这一页要带你建立第一个真正的“服务骨架读码顺序”。第 01 模块的关键，不是 Python 语法，而是你能不能通过代码看懂：
- schema 为什么是地基
- provider 为什么是吸收变化的一层
- route / service / provider 为什么必须分开

## 怎么读这一页
- 一定先看对象，再看行为。
- 先看 example，再看 `module-service`，不要反过来。
- 每看完一个文件，都问自己：这个对象或函数是在收住哪一层复杂度？

## 推荐总顺序
1. 看 `examples/01-structured-output`
2. 看 `examples/02-provider-abstraction`
3. 看 `module-service/app/service.py`
4. 看 `module-service/app/main.py`
5. 看 `module-service/tests/test_main.py`

## Example 1：`01-structured-output`
入口文件：
- [examples/01-structured-output/app/main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/01-python-agent-foundations/examples/01-structured-output/app/main.py)
- [examples/01-structured-output/tests/test_main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/01-python-agent-foundations/examples/01-structured-output/tests/test_main.py)
- [examples/01-structured-output/walkthrough.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/01-python-agent-foundations/examples/01-structured-output/walkthrough.md)

先看这几个点：
- `StructuredAnswer`
- `generate_structured_answer()`
- `main()`

第一眼应该理解什么：
- `StructuredAnswer` 是系统契约，不是输出美化。
- `generate_structured_answer()` 先用 deterministic stub，是为了让你把注意力放在输出边界，而不是模型波动。
- 这里真正训练的是“自由文本如何被压成系统可消费对象”。

接着看测试时重点看：
- 测试如何断言字段和类型，而不是大段字符串
- 为什么结构化输出会让测试更稳

建议你动手改一次：
- 新增字段，比如 `category`
- 然后补实现和测试

只要你做这一遍，就会更直观理解 schema 演进是如何发生的。

## Example 2：`02-provider-abstraction`
入口文件：
- [examples/02-provider-abstraction/app/main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/01-python-agent-foundations/examples/02-provider-abstraction/app/main.py)
- [examples/02-provider-abstraction/tests/test_main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/01-python-agent-foundations/examples/02-provider-abstraction/tests/test_main.py)
- [examples/02-provider-abstraction/walkthrough.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/01-python-agent-foundations/examples/02-provider-abstraction/walkthrough.md)

先看这几个点：
- `Provider` 协议
- `EchoProvider`
- `FakeLLMProvider`
- 业务函数本身

第一眼应该理解什么：
- provider 的价值不是“多包一层”，而是“让上层依赖能力契约而不是具体模型实现”。
- 两个 provider 并存，是为了显影“同一业务接口，不同底层实现”。
- 只要抽象真的立住了，业务函数就不需要知道你到底接了哪个模型。

接着看测试时重点看：
- 同一行为如何在不同 provider 上被重复验证
- 为什么 fake provider 是这门课后面反复使用的训练手段

建议你动手改一次：
- 新增一个 `UppercaseProvider`
- 保持业务函数不动，只扩展实现和测试

## 最后看综合服务：`llm-gateway`
入口文件：
- [module-service/app/service.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/01-python-agent-foundations/module-service/app/service.py)
- [module-service/app/main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/01-python-agent-foundations/module-service/app/main.py)
- [module-service/tests/test_main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/01-python-agent-foundations/module-service/tests/test_main.py)
- [module-service/README.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/01-python-agent-foundations/module-service/README.md)

推荐读码顺序：
1. 先看 `GenerateRequest`
2. 再看 `GenerateResponse`
3. 再看 `FakeProvider.generate()`
4. 最后看 `generate(payload)`

第一眼应该理解什么：
- `GenerateRequest` 和 `GenerateResponse` 分别定义了系统入口和出口。
- `FakeProvider` 是第 01 模块最关键的训练对象，它让你先验证结构，再接真实依赖。
- `generate(payload)` 是 service 层最小形态，后面 tools、RAG、workflow 都会长在这里。

接着再看 `app/main.py` 时重点看：
- route 是否只做协议转换
- 是否没有把模型细节写进 HTTP 层

最后看测试时重点看：
- 测试是否围绕 schema 和行为边界
- 不是围绕模型文案细节

## 这一页最容易读偏的地方
- 误区一：把 provider 看成“形式上的设计模式”
  - 这里它的真实价值是隔离变化。
- 误区二：觉得 fake provider 只是临时凑合
  - 它其实是在替你分离结构问题和外部依赖问题。
- 误区三：只看 route 能不能返回结果
  - 更重要的是 route 有没有保持干净。

## 读完这一页后应该回哪里
- 如果你想继续执行：去 [steps.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/01-python-agent-foundations/steps.md)
- 如果你想回顾原理：去 [02-deep-dive.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/01-python-agent-foundations/resources/02-deep-dive.md)
- 如果你想看出处解释：去 [04-sources.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/01-python-agent-foundations/resources/04-sources.md)
