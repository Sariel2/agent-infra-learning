# 边界判断器 逐段读码讲义

这个实验在训练你把“架构争论”压缩成明确判断维度。

## 先读前你要带着的问题
- workflow 和 agent 的边界到底该怎么判断。
- 为什么很多场景其实不需要 agent。
- 这个实验如何迁移到 `architecture-lab`。

## 第 1 步：先看场景对象
- 文件：[app/main.py](./app/main.py)
- 先看：`Scenario`
- 重点理解：架构选择不是对空气做判断，而是对任务特征做判断。

## 第 2 步：再看推荐函数
- 文件：[app/main.py](./app/main.py)
- 先看：`recommend_architecture()`
- 重点理解：它把任务特征压成明确规则，这正是边界判断的核心。

## 第 3 步：最后回到测试
- 文件：[tests/test_main.py](./tests/test_main.py)
- 重点理解：测试固定的是判断逻辑，不是某次偶然给出的建议。

## 建议运行命令
- `python -m app.main`
- `pytest`

## 建议最小实验
- 设计一个 hybrid 场景，看看推荐是否合理。
- 调整一个判断条件，观察结果如何变化。

## 最后把抽象迁回哪里
- 综合服务：[../../module-service/app/service.py](../../module-service/app/service.py)
- 对应抽象：`recommend()`

## 学完后你应该能回答
- 为什么模式选择应该先明确判断维度。
- 为什么很多任务其实 workflow 就足够了。
