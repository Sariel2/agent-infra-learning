# 结构化输出

这个实验用来证明：模型输出必须尽量收敛成稳定 schema，否则后面所有工程能力都会变脆。

## 这个实验要学会什么
- 为什么 schema 是系统契约，而不是展示格式。
- 为什么测试应该先验证结构，再验证具体文本。
- 为什么 structured output 是 agent infra 的第一层地基。

## 开始前先回看
- 讲义主线：[../../resources/01-concepts-and-principles.md](../../resources/01-concepts-and-principles.md)
- 原理细节：[../../resources/02-deep-dive.md](../../resources/02-deep-dive.md)
- 读码导引：[./walkthrough.md](./walkthrough.md)

## 先看哪些文件
- 核心代码：[app/main.py](./app/main.py)
- 测试文件：[tests/test_main.py](./tests/test_main.py)

## 推荐运行命令
- `python -m app.main`
- `pytest`

## 建议最小改动
- 给 `StructuredAnswer` 新增一个字段。
- 故意把 `confidence` 改成非法值，观察验证如何失败。

## 跑完之后要观察什么
- 为什么结构稳定比输出“看起来聪明”更重要。
- 为什么加一个字段会同时影响实现和测试。
- 这个实验如何映射到 [../../module-service/README.md](../../module-service/README.md) 里的 `GenerateRequest` 和 `GenerateResponse`。

## 做完后回哪里
- 综合服务：[../../module-service/README.md](../../module-service/README.md)
- 练习手册：[../../exercises.md](../../exercises.md)
