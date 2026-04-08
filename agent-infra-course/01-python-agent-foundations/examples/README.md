# 01 Python 与 Agent 基础 Examples

这里是本模块的代码实验室。两个 example 会把后面所有 agent 工程都依赖的两个地基先立起来：结构化输出和 provider 抽象。

## 这两个实验分别在证明什么
- [01-structured-output/README.md](./01-structured-output/README.md)
  证明“输出结构稳定”比“文本看起来聪明”更重要。
- [02-provider-abstraction/README.md](./02-provider-abstraction/README.md)
  证明“模型接入边界”应该先被隔离出来，后面才有测试性和可替换性。

## 推荐实验顺序
1. 先做 [01-structured-output](./01-structured-output/README.md)
2. 再做 [02-provider-abstraction](./02-provider-abstraction/README.md)
3. 两个实验都完成后，再进入 [module-service/README.md](../module-service/README.md)

## 每个实验都按这个顺序做
1. 先看实验 `README.md`
2. 再看 `walkthrough.md`
3. 读 `app/main.py`
4. 跑测试
5. 做一个小改动，例如新增字段或替换 provider
6. 再跑一次并记录影响

## 做实验前先回看
- 模块首页：[../README.md](../README.md)
- 学习地图：[../study-map.md](../study-map.md)
- 执行剧本：[../steps.md](../steps.md)
- 代码导读：[../resources/03-code-reading-guide.md](../resources/03-code-reading-guide.md)

## 跑完实验后你应该观察什么
- schema 为什么是最早应该稳定的契约。
- fake provider 为什么能让你先把工程边界理顺。
- 这两个实验怎样自然过渡到 `llm-gateway` 综合服务。

## 跑完之后回哪里
- 综合服务：[../module-service/README.md](../module-service/README.md)
- 练习手册：[../exercises.md](../exercises.md)
- 复盘模板：[../review.md](../review.md)
