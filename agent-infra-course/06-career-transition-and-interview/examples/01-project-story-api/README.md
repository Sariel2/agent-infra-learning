# 项目故事生成

这个实验用来证明：同一个项目需要同时有业务版和 infra 版两种表达，而不是一套术语到处讲。

## 这个实验要学会什么
- 把项目事实压缩成稳定表达模板。
- 区分业务价值表达和 infra 价值表达。
- 理解为什么项目讲解也值得被结构化。

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
- 换一个项目目标，重写业务版和 infra 版表达。
- 调整模板字段，观察输出结构会怎样变化。

## 跑完之后要观察什么
- 为什么“做过项目”不等于“能把项目讲清楚”。
- 为什么同一项目需要不同口径。
- 这个实验如何映射到 [../../module-service/README.md](../../module-service/README.md) 里的 `build_story()`。

## 做完后回哪里
- 综合服务：[../../module-service/README.md](../../module-service/README.md)
- 练习手册：[../../exercises.md](../../exercises.md)
