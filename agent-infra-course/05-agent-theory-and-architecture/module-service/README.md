# architecture-lab

把 pattern 对比和边界判断组织成一个可演示的实验服务。

## 这个综合服务在模块里的位置
它不是一个额外 demo，而是这个模块知识点的收束点。你应该在跑完 examples 之后再来看它，这样你能看出哪些抽象是从 examples 提升而来的。

## 建议阅读顺序
- 先看 [app/service.py](./app/service.py)：先看 `compare()` 和 `recommend()`，理解“模式对比”和“场景判断”是两个互补维度。
- 先看 [app/main.py](./app/main.py)：再看如何用不同接口暴露它们。
- 先看 [tests/test_main.py](./tests/test_main.py)：最后看最小自动验证如何保护判断逻辑。

## 建议运行命令
- `uvicorn app.main:app --reload`
- `pytest`

## 学完后你应该能回答
- 这个服务如何把 `05 Agent 原理与架构` 的核心概念组合到一起。
- 为什么这些能力要按当前这种分层组织。
- 如果继续扩展，这个服务最先该从哪里演进。
