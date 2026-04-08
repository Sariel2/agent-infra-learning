# 工具契约与校验 逐段读码讲义

这个实验要让你看到：工具调用最先坏掉的地方，往往不是 prompt，而是 schema 和参数边界。

## 先读前你要带着的问题
- 为什么 tool schema 会直接影响 agent 质量。
- 为什么参数错误应该尽量在进入工具逻辑前暴露。
- 这些协议对象会如何迁移到 `support-agent`。

## 第 1 步：先看工具调用对象
- 文件：[app/main.py](./app/main.py)
- 先看：`ToolCall` 与 `ToolResult`
- 重点理解：它们定义了模型与工具之间的协议。没有稳定协议，后面 trace 和恢复都难做。

## 第 2 步：再看工具函数
- 文件：[app/main.py](./app/main.py)
- 先看：`search_docs`
- 重点理解：工具本身应该尽量简单、可预测，复杂度应该更多落在调度和治理层。

## 第 3 步：最后回到测试
- 文件：[tests/test_main.py](./tests/test_main.py)
- 重点理解：测试不是在证明工具“看起来能用”，而是在证明坏输入会被及时拦住。

## 建议运行命令
- `python -m app.main`
- `pytest`

## 建议最小实验
- 给 `ToolCall` 增加一个字段。
- 把 `query` 设为空，观察错误如何提前暴露。

## 最后把抽象迁回哪里
- 综合服务：[../../module-service/app/service.py](../../module-service/app/service.py)
- 对应抽象：工具函数与统一工具轨迹的前提

## 学完后你应该能回答
- 为什么工具契约先于 prompt 微调。
- 为什么统一 schema 会让 trace 和恢复设计更容易。
