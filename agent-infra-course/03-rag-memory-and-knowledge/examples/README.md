# 03 RAG、Memory 与 Knowledge Examples

这里是本模块的代码实验室。两个 example 会把“检索与 citation”以及“短期 memory”拆成两个独立问题，让你先分清边界，再进入综合服务。

## 这两个实验分别在证明什么
- [01-local-retrieval/README.md](./01-local-retrieval/README.md)
  证明最小 RAG 链路至少要把检索结果和 citation 一起返回。
- [02-short-term-memory/README.md](./02-short-term-memory/README.md)
  证明 memory 应该被裁剪和建模，而不是把所有历史一股脑塞回去。

## 推荐实验顺序
1. 先做 [01-local-retrieval](./01-local-retrieval/README.md)
2. 再做 [02-short-term-memory](./02-short-term-memory/README.md)
3. 两个实验都完成后，再进入 [module-service/README.md](../module-service/README.md)

## 每个实验都按这个顺序做
1. 先看实验 `README.md`
2. 再看 `walkthrough.md`
3. 读 `app/main.py`
4. 跑测试
5. 做一个小改动，例如新增 citation 字段或调整 memory 长度
6. 再跑一次并记录差异

## 做实验前先回看
- 模块首页：[../README.md](../README.md)
- 学习地图：[../study-map.md](../study-map.md)
- 执行剧本：[../steps.md](../steps.md)
- 代码导读：[../resources/03-code-reading-guide.md](../resources/03-code-reading-guide.md)

## 跑完实验后你应该观察什么
- citation 为什么是质量治理能力。
- memory 和 retrieval 为什么不能混成同一层。
- 这两个实验怎样一起长成 `knowledge-agent`。

## 跑完之后回哪里
- 综合服务：[../module-service/README.md](../module-service/README.md)
- 练习手册：[../exercises.md](../exercises.md)
- 复盘模板：[../review.md](../review.md)
