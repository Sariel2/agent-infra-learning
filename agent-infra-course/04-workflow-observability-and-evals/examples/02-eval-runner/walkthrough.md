# 固定数据集评测 逐段读码讲义

这个实验要让你真正看清：没有固定样本，所谓“优化”往往只是主观感受。

## 先读前你要带着的问题
- 为什么 eval 必须绑定固定 dataset。
- 为什么评测逻辑本身也应该可测试。
- 这个实验里的抽象会如何迁移到 `agent-runtime`。

## 第 1 步：先看样本集
- 文件：[app/main.py](./app/main.py)
- 先看：`DATASET`
- 重点理解：固定样本不是为了追求大规模，而是为了追求可比较性。

## 第 2 步：再看决策与评测函数
- 文件：[app/main.py](./app/main.py)
- 先看：`choose_tool()` 和 `run_eval()`
- 重点理解：评测就是把固定样本喂给稳定逻辑，再比较结果是否匹配预期。

## 第 3 步：最后回到测试
- 文件：[tests/test_main.py](./tests/test_main.py)
- 重点理解：测试在确认评测逻辑本身不会漂移。

## 建议运行命令
- `python -m app.main`
- `pytest`

## 建议最小实验
- 故意改坏 `choose_tool()`，看 eval 如何暴露退化。
- 增加一个新的样本 case，并观察 `run_eval()` 结果。

## 最后把抽象迁回哪里
- 综合服务：[../../module-service/app/service.py](../../module-service/app/service.py)
- 对应抽象：`DATASET`、`evaluate()` 和回归比较基线

## 学完后你应该能回答
- 为什么“同一批样本反复比较”是稳定迭代的前提。
- 为什么 eval 不只是上线前做一次的附属动作。
