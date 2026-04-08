# 05 Agent 原理与架构 Examples

这里是本模块的代码实验室。两个 example 会先把“模式差异”和“边界判断”拆开，让你从能看懂差异，走到能做出选择。

## 这两个实验分别在证明什么
- [01-pattern-comparison/README.md](./01-pattern-comparison/README.md)
  证明不同 agent pattern 的流程差异应该被显式比较，而不是只凭感觉。
- [02-boundary-checker/README.md](./02-boundary-checker/README.md)
  证明很多架构争论，本质上是在做任务边界判断。

## 推荐实验顺序
1. 先做 [01-pattern-comparison](./01-pattern-comparison/README.md)
2. 再做 [02-boundary-checker](./02-boundary-checker/README.md)
3. 两个实验都完成后，再进入 [module-service/README.md](../module-service/README.md)

## 每个实验都按这个顺序做
1. 先看实验 `README.md`
2. 再看 `walkthrough.md`
3. 读 `app/main.py`
4. 跑测试
5. 做一个小改动，例如加一个场景或调整判断条件
6. 再跑一次并记录你的选择变化

## 做实验前先回看
- 模块首页：[../README.md](../README.md)
- 学习地图：[../study-map.md](../study-map.md)
- 执行剧本：[../steps.md](../steps.md)
- 代码导读：[../resources/03-code-reading-guide.md](../resources/03-code-reading-guide.md)

## 跑完实验后你应该观察什么
- 模式选择为什么要先于框架选择。
- 任务确定性和风险为什么是最关键的判断信号。
- 这两个实验怎样汇合成 `architecture-lab`。

## 跑完之后回哪里
- 综合服务：[../module-service/README.md](../module-service/README.md)
- 练习手册：[../exercises.md](../exercises.md)
- 复盘模板：[../review.md](../review.md)
