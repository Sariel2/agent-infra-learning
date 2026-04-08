# 04 Workflow、Observability 与 Evals Examples

这里是本模块的代码实验室。两个 example 会先分别证明“为什么 workflow 要显式建模”和“为什么 eval 必须基于固定样本”，然后再汇合到综合运行时。

## 这两个实验分别在证明什么
- [01-stateful-workflow/README.md](./01-stateful-workflow/README.md)
  证明流程状态、节点和分支应该被显式表达出来。
- [02-eval-runner/README.md](./02-eval-runner/README.md)
  证明没有固定数据集就很难做有效回归比较。

## 推荐实验顺序
1. 先做 [01-stateful-workflow](./01-stateful-workflow/README.md)
2. 再做 [02-eval-runner](./02-eval-runner/README.md)
3. 两个实验都完成后，再进入 [module-service/README.md](../module-service/README.md)

## 每个实验都按这个顺序做
1. 先看实验 `README.md`
2. 再看 `walkthrough.md`
3. 读 `app/main.py`
4. 跑测试
5. 做一个小改动，例如新增节点或新增样本 case
6. 再跑一次并记录结果变化

## 做实验前先回看
- 模块首页：[../README.md](../README.md)
- 学习地图：[../study-map.md](../study-map.md)
- 执行剧本：[../steps.md](../steps.md)
- 代码导读：[../resources/03-code-reading-guide.md](../resources/03-code-reading-guide.md)

## 跑完实验后你应该观察什么
- workflow 为什么适合固定步骤和高风险节点。
- eval 为什么必须和固定 dataset 绑定。
- 这两个实验怎样汇合成 `agent-runtime`。

## 跑完之后回哪里
- 综合服务：[../module-service/README.md](../module-service/README.md)
- 练习手册：[../exercises.md](../exercises.md)
- 复盘模板：[../review.md](../review.md)
