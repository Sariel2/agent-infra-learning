# 本地检索与 Citation

这个实验用来证明：RAG 的最小链路不只是“找点文本”，而是要把检索结果和 citation 一起稳定地保留下来。

## 这个实验要学会什么
- 理解最小检索链路包含哪些对象。
- 为什么 citation 是系统能力而不是 UI 装饰。
- 为什么检索结果应该先结构化再进入回答阶段。

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
- 新增一条文档，观察排序结果如何变化。
- 修改 query，观察是否还能稳定命中。

## 跑完之后要观察什么
- 检索结果为什么应该带来源信息。
- 为什么 citation 一旦丢失，后面很难做质量治理。
- 这个实验如何映射到 [../../module-service/README.md](../../module-service/README.md) 里的 `retrieve()` 和 `citations`。

## 做完后回哪里
- 综合服务：[../../module-service/README.md](../../module-service/README.md)
- 练习手册：[../../exercises.md](../../exercises.md)
