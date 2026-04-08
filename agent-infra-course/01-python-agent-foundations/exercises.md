# 01 Python 与 Agent 基础 练习手册

## 这份练习怎么用
- 先按 [steps.md](./steps.md) 走完 `structured output` 和 `provider abstraction` 两条主线，再开始做题。
- 做题时优先引用本模块讲义和代码，不要直接跳出课程去找答案。
- 每题都尽量把结论落到接口、类型、目录结构或测试策略上。

## 做题前回看
- 学习路线：[study-map.md](./study-map.md)
- 概念讲义：[resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
- 原理细节：[resources/02-deep-dive.md](./resources/02-deep-dive.md)
- 代码导读：[resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md)
- 示例 1：[examples/01-structured-output/app/main.py](./examples/01-structured-output/app/main.py)
- 示例 2：[examples/02-provider-abstraction/app/main.py](./examples/02-provider-abstraction/app/main.py)
- 综合服务：[module-service/app/main.py](./module-service/app/main.py)
- 综合测试：[module-service/tests/test_main.py](./module-service/tests/test_main.py)

## 练习 1：为什么 structured output 是起点
- 先回看：[resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
- 题目：解释为什么这套课程把 structured output 放在 agent infra 的第一个工程能力位置，而不是先讲 tool calling。
- 输出要求：至少写 6 句，覆盖稳定性、测试性、系统边界三个角度。
- 完成标准：你的答案要能解释“没有稳定输出结构，后续 tool、workflow、eval 都会变难”。

## 练习 2：拆解 provider abstraction
- 先回看：[resources/02-deep-dive.md](./resources/02-deep-dive.md)
- 对应代码：[examples/02-provider-abstraction/app/main.py](./examples/02-provider-abstraction/app/main.py)
- 对应测试：[examples/02-provider-abstraction/tests/test_main.py](./examples/02-provider-abstraction/tests/test_main.py)
- 题目：说明 provider abstraction 解决了什么问题，它没有解决什么问题。
- 输出要求：分成“解决的问题”和“没有解决的问题”两段来写。
- 完成标准：你必须指出它主要解决解耦和可测试性，不会自动带来成本优化或质量提升。

## 练习 3：设计 `/generate` 接口
- 先回看：[resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
- 对应代码：[examples/01-structured-output/app/main.py](./examples/01-structured-output/app/main.py)
- 题目：为一个 `/generate` 接口设计输入输出模型，要求支持 `prompt`、`temperature`、`trace_id`，并返回稳定的结构化响应。
- 输出要求：写出请求 schema、响应 schema、错误 schema。
- 完成标准：schema 必须能自然落到 `Pydantic` 模型上。

## 练习 4：读码改造小实验
- 先回看：[resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md)
- 对应代码：[examples/01-structured-output/app/main.py](./examples/01-structured-output/app/main.py)
- 对应测试：[examples/01-structured-output/tests/test_main.py](./examples/01-structured-output/tests/test_main.py)
- 题目：把 example 中的输出模型增加一个 `confidence` 字段，再说明这会影响哪些层。
- 输出要求：至少写出 route、service、provider、test 四层里各自要改什么。
- 完成标准：你能说明“加字段”不是只改接口返回，还会影响假数据、断言和调用契约。

## 练习 5：为什么先 fake provider 再接真实模型
- 先回看：[resources/02-deep-dive.md](./resources/02-deep-dive.md)
- 对应代码：[module-service/app/main.py](./module-service/app/main.py)
- 题目：回答为什么课程里要先 fake provider 再接真实模型，并举一个如果反过来做会造成什么混乱的例子。
- 输出要求：两部分，先讲理由，再讲反例。
- 完成标准：你的回答里必须区分“外部依赖波动”和“内部工程边界不清”。

## 练习 6：综合服务拆层
- 先回看：[project.md](./project.md)
- 对应代码：[module-service/app/main.py](./module-service/app/main.py)
- 对应测试：[module-service/tests/test_main.py](./module-service/tests/test_main.py)
- 题目：画出 `route -> service -> provider -> schema` 的依赖图，并解释每层最应该稳定的东西是什么。
- 输出要求：一张图加四段文字。
- 完成标准：你能说明为什么测试优先围绕稳定边界写，而不是围绕具体实现写。

## 完成后自检
- 你能自己实现一个最小 fake provider。
- 你能解释 structured output 与普通自由文本返回的工程差别。
- 你能指出本模块综合服务里最适合优先测试的三处边界。
- 你已经为下一个模块的 tool calling 做好了 schema 和 provider 基础。
