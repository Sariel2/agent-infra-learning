# Pattern 对比 逐段读码讲义

这个实验的重点，是把抽象的 pattern 变成你看得见的控制流差异。

## 先读前你要带着的问题
- 为什么模式差异应该被显式比较。
- 为什么任务结构比框架名字更重要。
- 这个实验会如何迁移到 `architecture-lab`。

## 第 1 步：先看输出对象
- 文件：[app/main.py](./app/main.py)
- 先看：`PatternOutput`
- 重点理解：它让不同 pattern 的流程结果有统一承载方式，便于比较。

## 第 2 步：再看对比函数
- 文件：[app/main.py](./app/main.py)
- 先看：`compare_patterns()`
- 重点理解：真正被比较的是控制流形状，而不是“哪个名字更高级”。

## 第 3 步：最后回到测试
- 文件：[tests/test_main.py](./tests/test_main.py)
- 重点理解：测试让模式比较结果稳定，不会随着随意改动失真。

## 建议运行命令
- `python -m app.main`
- `pytest`

## 建议最小实验
- 给 compare 增加一种 supervisor 风格输出。
- 改一个任务描述，观察流程表示如何变化。

## 最后把抽象迁回哪里
- 综合服务：[../../module-service/app/service.py](../../module-service/app/service.py)
- 对应抽象：`compare()`

## 学完后你应该能回答
- 为什么模式比较的核心是流程和边界，不是术语记忆。
- 为什么这类对比会帮助你后面做架构判断。
