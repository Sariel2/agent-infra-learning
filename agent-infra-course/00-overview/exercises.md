# 00 总览与准备 练习手册

## 这份练习怎么用
- 先完成 [study-map.md](./study-map.md) 中的 Step 1 到 Step 4，再开始做这里的练习。
- 做题时不要只写结论，至少要写出你的判断依据、文件引用和下一步动作。
- 每做完一题，都回到 [review.md](./review.md) 记录一条“我现在真正理解了什么”和一条“我还没吃透什么”。

## 做题前回看
- 课程地图：[README.md](./README.md)
- 学习路线：[study-map.md](./study-map.md)
- 讲义主线：[resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
- 细节与原理：[resources/02-deep-dive.md](./resources/02-deep-dive.md)
- 读码说明：[resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md)
- 代码示例：[examples/01-settings-and-logging/app/main.py](./examples/01-settings-and-logging/app/main.py)
- 代码示例：[examples/02-project-smoke-test/app/main.py](./examples/02-project-smoke-test/app/main.py)
- 综合服务：[module-service/app/main.py](./module-service/app/main.py)

## 练习 1：一句话讲清课程主线
- 先回看：[resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
- 题目：用一句话解释 agent infra 与普通 LLM app 的区别，再用三句话说明这套课程为什么要从“工程骨架”开始。
- 输出要求：一句总定义，三句展开说明。
- 完成标准：你的回答里必须出现 `model`、`tool`、`workflow`、`trace`、`eval` 这五个词中的至少四个。

## 练习 2：画出学习对象地图
- 先回看：[resources/02-deep-dive.md](./resources/02-deep-dive.md)
- 对应代码：[examples/01-settings-and-logging/app/main.py](./examples/01-settings-and-logging/app/main.py)
- 题目：根据课程总览画一张最小 agent infra 地图，至少包含 `API 层`、`模型接入层`、`工具层`、`知识层`、`观测层`、`评测层`。
- 输出要求：用 Mermaid 或手绘图都可以，同时写 5 句说明。
- 完成标准：你能解释每一层在本课程后续哪个模块里会成为重点。

## 练习 3：给自己做一个 6 周节奏表
- 先回看：[tasks.md](./tasks.md)
- 题目：如果你每周只能投入 8-12 小时，请按“学习、编码、复盘、考核”四类活动拆一份你的周节奏表。
- 输出要求：按周写，至少覆盖 Week 1 到 Week 6。
- 完成标准：每周都要有一项可交付物，不能只写“读文档”。

## 练习 4：设计实验记录模板
- 先回看：[resources/02-deep-dive.md](./resources/02-deep-dive.md)
- 对应代码：[examples/02-project-smoke-test/tests/test_main.py](./examples/02-project-smoke-test/tests/test_main.py)
- 题目：设计一份实验记录模板，要求后续能同时承接 example 的小实验和 module-service 的综合实验。
- 输出要求：至少包含 `目标`、`输入`、`输出`、`失败现象`、`怀疑原因`、`下一步验证` 六个字段。
- 完成标准：模板字段能够支持后面模块的 trace 和 eval 记录。

## 练习 5：环境排错演练
- 先回看：[resources/05-common-mistakes.md](./resources/05-common-mistakes.md)
- 对应代码：[module-service/README.md](./module-service/README.md)
- 题目：回答“Python 环境能安装依赖但运行时报模块缺失”至少三种可能原因，并给出排查顺序。
- 输出要求：按 `症状 -> 原因 -> 检查动作` 的格式写。
- 完成标准：排查顺序必须先从环境与解释器边界开始，而不是直接改代码。

## 练习 6：综合小作业
- 先回看：[project.md](./project.md)
- 对应代码：[module-service/app/main.py](./module-service/app/main.py)
- 题目：基于本模块综合服务，写一份“后续模块如何在这个骨架上继续生长”的说明。
- 输出要求：至少覆盖配置、日志、测试、目录结构四部分。
- 完成标准：你的说明能自然衔接到 [01-python-agent-foundations](../01-python-agent-foundations/README.md)。

## 完成后自检
- 你能解释为什么课程不从“直接调真实模型”开始。
- 你能指出 example 和 module-service 的职责差异。
- 你已经写出自己的 6 周节奏和实验记录模板。
- 你知道卡住时先回哪几份讲义。
