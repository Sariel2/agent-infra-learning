# 06 转型、简历与面试 练习手册

## 这份练习怎么用
- 先按 [steps.md](./steps.md) 跑完 `project story api` 和 `interview qa pack` 两个 example。
- 本模块练习不是让你再学新概念，而是把前面所有能力整理成可表达、可展示、可面试的成果。
- 每题都要尽量引用你前面已经完成的项目、失败案例和优化动作。

## 做题前回看
- 学习路线：[study-map.md](./study-map.md)
- 概念讲义：[resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
- 原理细节：[resources/02-deep-dive.md](./resources/02-deep-dive.md)
- 代码导读：[resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md)
- 示例 1：[examples/01-project-story-api/app/main.py](./examples/01-project-story-api/app/main.py)
- 示例 2：[examples/02-interview-qa-pack/app/main.py](./examples/02-interview-qa-pack/app/main.py)
- 综合服务：[module-service/app/main.py](./module-service/app/main.py)
- 综合测试：[module-service/tests/test_main.py](./module-service/tests/test_main.py)

## 练习 1：为什么项目材料不能只写“接了大模型”
- 先回看：[resources/01-concepts-and-principles.md](./resources/01-concepts-and-principles.md)
- 题目：解释为什么 agent infra 转型材料不能只写“接了大模型”，而必须写出运行时、工具、检索、观测或评测。
- 输出要求：至少写 6 句。
- 完成标准：你的回答必须体现“工程复杂度来自系统治理，而不只是模型调用”。

## 练习 2：写一条业务版简历描述
- 先回看：[resources/02-deep-dive.md](./resources/02-deep-dive.md)
- 对应代码：[examples/01-project-story-api/app/main.py](./examples/01-project-story-api/app/main.py)
- 题目：把 `knowledge-agent` 写成一条 80-120 字的业务版简历描述。
- 输出要求：强调场景、价值、结果，不要堆名词。
- 完成标准：必须能让不熟悉 agent infra 的面试官也看懂项目价值。

## 练习 3：写一条 infra 版简历描述
- 先回看：[project.md](./project.md)
- 对应代码：[module-service/app/main.py](./module-service/app/main.py)
- 题目：把课程主项目写成一条 infra 版简历描述，强调架构、稳定性和可调试性。
- 输出要求：80-120 字。
- 完成标准：描述里至少出现 `structured output`、`tool calling`、`RAG`、`trace`、`eval` 中的三个。

## 练习 4：3 分钟项目讲解
- 先回看：[resources/03-code-reading-guide.md](./resources/03-code-reading-guide.md)
- 对应代码：[examples/02-interview-qa-pack/app/main.py](./examples/02-interview-qa-pack/app/main.py)
- 题目：写一份 3 分钟项目讲解提纲，至少覆盖目标、架构、失败案例、优化动作、结果。
- 输出要求：按 5 个小段组织。
- 完成标准：提纲里必须有一个真实失败案例，而不是只讲成功结果。

## 练习 5：技术追问应答
- 先回看：[resources/05-common-mistakes.md](./resources/05-common-mistakes.md)
- 题目：分别回答下面两个追问：
- 追问 A：为什么这里要 workflow，不直接让模型自由决策。
- 追问 B：为什么你说系统变稳定了，不是主观感觉。
- 输出要求：每个追问回答 5-8 句。
- 完成标准：你的回答要有边界判断和证据体系，而不是抽象态度。

## 练习 6：转型叙事设计
- 先回看：[module-service/README.md](./module-service/README.md)
- 对应代码：[module-service/app/main.py](./module-service/app/main.py)
- 题目：设计一段“从 Java 后端工程师转向 agent infra”的成长叙事，要求真实、具体、可被追问。
- 输出要求：分成“过去擅长什么”“为什么转向”“做了哪些具体建设”“现在能解决什么问题”四段。
- 完成标准：叙事必须建立在你课程里的真实项目和材料上，不能像套模板。

## 完成后自检
- 你能把一个技术项目讲成业务方也听得懂的故事。
- 你能把“做过 demo”与“做过工程化系统”区分开。
- 你已经准备好一版简历 bullet 和一版 3 分钟讲稿。
- 你已经能把前 5 个模块的内容组织成完整转型材料。
