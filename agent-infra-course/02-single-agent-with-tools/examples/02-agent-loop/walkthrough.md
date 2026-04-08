# 最小 Agent Loop 逐段读码讲义

这个实验在训练你把 agent 的一次运行拆成几个显式阶段，而不是把一切都看成一次黑盒调用。

## 先读前你要带着的问题
- 一个最小 agent loop 至少包含哪些阶段。
- 为什么“选择工具”和“执行工具”是两类不同问题。
- 这个实验怎样过渡到 `support-agent`。

## 第 1 步：先看决策函数
- 文件：[app/main.py](./app/main.py)
- 先看：`choose_tool`
- 重点理解：这里是 agent 的最小决策点，职责是把输入路由到合适工具，而不是做所有后续动作。

## 第 2 步：再看执行函数
- 文件：[app/main.py](./app/main.py)
- 先看：`run_agent`
- 重点理解：这个函数把“选工具 -> 执行 -> 返回结果”串起来，体现最小 loop。

## 第 3 步：最后回到测试
- 文件：[tests/test_main.py](./tests/test_main.py)
- 重点理解：测试让同一个 loop 在固定输入上保持稳定行为，这就是后续 trace 和 eval 的前提。

## 建议运行命令
- `python -m app.main`
- `pytest`

## 建议最小实验
- 增加一个新工具路径。
- 改变 `choose_tool` 规则，观察 loop 结果如何变化。

## 最后把抽象迁回哪里
- 综合服务：[../../module-service/app/service.py](../../module-service/app/service.py)
- 对应抽象：`run_agent()` 与最小 trace 返回

## 学完后你应该能回答
- 为什么 agent loop 不是“模型帮你调个函数”这么简单。
- 为什么 loop 越早被显式化，后面越容易做恢复和观测。
