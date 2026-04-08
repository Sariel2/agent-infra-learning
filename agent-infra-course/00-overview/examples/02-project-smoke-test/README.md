# 项目状态与 Smoke Test

这个实验用来证明：学习项目也需要最小验证机制，不是“能跑一次”就算准备完成。

## 这个实验要学会什么
- 区分“代码能执行”和“项目状态已就绪”。
- 用 smoke test 快速验证基础状态。
- 为后面所有模块建立最小验收意识。

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
- 把 `project_defined` 改成 `False`，观察状态如何变化。
- 新增一个检查项，并同步修正测试。

## 跑完之后要观察什么
- 为什么 smoke test 是最低成本的项目健康检查。
- 为什么“ready”状态必须有清晰定义，而不是口头判断。
- 这个实验如何映射到 [../../module-service/README.md](../../module-service/README.md) 里的就绪状态模型。

## 做完后回哪里
- 综合服务：[../../module-service/README.md](../../module-service/README.md)
- 练习手册：[../../exercises.md](../../exercises.md)
