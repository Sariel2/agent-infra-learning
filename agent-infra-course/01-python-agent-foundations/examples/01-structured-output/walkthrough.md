# 结构化输出 逐段读码讲义

这个实验的重点不是“把文本包成 JSON”，而是理解为什么 schema 是后续所有工程能力的契约起点。

## 先读前你要带着的问题
- 为什么 structured output 比自由文本更适合工程系统。
- 为什么测试优先验证结构，而不是验证“回答像不像人写的”。
- 这个实验里的抽象会怎么迁移到 `llm-gateway`。

## 第 1 步：先读输出模型
- 文件：[app/main.py](./app/main.py)
- 先看：`StructuredAnswer`
- 重点理解：这个对象定义了系统承诺返回什么。它不是装饰，而是契约。
- 读完后你应该能回答：如果后面要增加字段，为什么实现和测试都要一起改。

## 第 2 步：再读生成函数
- 文件：[app/main.py](./app/main.py)
- 先看：`generate_structured_answer`
- 重点理解：课程这里先用 deterministic stub，不是为了偷懒，而是为了先稳定数据流。
- 读完后你应该能回答：为什么先 fake 再接真实模型更容易把边界理清。

## 第 3 步：最后回到测试
- 文件：[tests/test_main.py](./tests/test_main.py)
- 重点理解：测试在验证输出形状稳定，而不是只验证某一段文本恰好长什么样。
- 读完后你应该能回答：如果只测字符串包含某些词，后面会带来什么风险。

## 建议运行命令
- `python -m app.main`
- `pytest`

## 建议最小实验
- 给 `StructuredAnswer` 新增一个字段，再修复实现和测试。
- 把 `confidence` 改成非法值，观察验证失败。

## 最后把抽象迁回哪里
- 综合服务：[../../module-service/app/service.py](../../module-service/app/service.py)
- 对应抽象：`GenerateRequest`、`GenerateResponse` 和稳定输出契约

## 学完后你应该能回答
- 为什么 structured output 是 agent infra 的第一层地基。
- 为什么 schema 稳定会直接影响后面的工具、workflow 和 eval。
