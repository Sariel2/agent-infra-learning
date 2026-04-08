# Provider 抽象 逐段读码讲义

这个实验在训练你把“模型接入”从“业务逻辑”里拆出来。关键不是模式名字，而是边界清不清楚。

## 先读前你要带着的问题
- 为什么 provider abstraction 先解决的是解耦和测试性。
- 为什么业务函数不应该直接依赖具体模型实现。
- 这个抽象会怎样迁移到 `llm-gateway`。

## 第 1 步：先看 provider 协议
- 文件：[app/main.py](./app/main.py)
- 先看：`Provider`
- 重点理解：它定义的是“业务侧需要模型提供什么能力”，而不是“模型内部怎么工作”。

## 第 2 步：再看两个实现
- 文件：[app/main.py](./app/main.py)
- 先看：`EchoProvider` 和 `FakeLLMProvider`
- 重点理解：同一接口，不同实现，说明业务逻辑可以不关心底层具体来自哪里。
- 读完后你应该能回答：为什么这个能力会直接提升可测试性。

## 第 3 步：最后看业务函数和测试
- 文件：[app/main.py](./app/main.py)
- 先看：依赖 provider 的业务函数
- 文件：[tests/test_main.py](./tests/test_main.py)
- 重点理解：测试真正锁定的是接口边界，而不是某个具体 provider 的内部实现。

## 建议运行命令
- `python -m app.main`
- `pytest`

## 建议最小实验
- 新增一个 `UppercaseProvider`。
- 不改业务函数，只切换 provider，观察测试如何保持稳定。

## 最后把抽象迁回哪里
- 综合服务：[../../module-service/app/service.py](../../module-service/app/service.py)
- 对应抽象：`FakeProvider` 和 `generate()`

## 学完后你应该能回答
- 为什么 provider abstraction 是后续接真实模型的前提。
- 为什么“先 fake 后真实”会让工程推进更稳。
