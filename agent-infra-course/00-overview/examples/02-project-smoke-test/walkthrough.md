# 项目状态与 smoke test 代码导读

这个 example 的核心目的：为什么学习项目也需要最小验证机制。

## 阅读顺序
- 先看 [app/main.py](./app/main.py)：看 `ProjectStatus` 与 `summarize_status`，理解“能运行”和“已准备好”不是一回事。
- 先看 [tests/test_main.py](./tests/test_main.py)：看 smoke test 如何把学习状态转成明确检查项。

## 建议运行命令
- `python -m app.main`
- `pytest`

## 建议实验
- 把 `project_defined` 改成 `False`，确认状态如何变化。

## 学完后你应该能回答
- 这个 example 为什么存在，它在整个模块里对应哪个关键知识点。
- 如果把这个 example 的抽象迁移到 `starter-workspace`，会迁移到哪一层。
