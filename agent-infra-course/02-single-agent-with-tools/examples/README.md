# 02 单 Agent 与 Tools Examples

这里是本模块的代码实验室。两个 example 会先把“工具契约”和“最小 agent loop”拆开演示，再把它们合起来进入综合服务。

## 这两个实验分别在证明什么
- [01-tool-schema/README.md](./01-tool-schema/README.md)
  证明 tool schema 设计质量会直接影响模型选择工具的稳定性。
- [02-agent-loop/README.md](./02-agent-loop/README.md)
  证明单 agent 的执行应该被看成一个状态过程，而不是一次黑盒调用。

## 推荐实验顺序
1. 先做 [01-tool-schema](./01-tool-schema/README.md)
2. 再做 [02-agent-loop](./02-agent-loop/README.md)
3. 两个实验都完成后，再进入 [module-service/README.md](../module-service/README.md)

## 每个实验都按这个顺序做
1. 先看实验 `README.md`
2. 再看 `walkthrough.md`
3. 读 `app/main.py`
4. 跑测试
5. 做一个小改动，例如改参数名、补 trace 字段或模拟失败
6. 再跑一次并记录现象

## 做实验前先回看
- 模块首页：[../README.md](../README.md)
- 学习地图：[../study-map.md](../study-map.md)
- 执行剧本：[../steps.md](../steps.md)
- 代码导读：[../resources/03-code-reading-guide.md](../resources/03-code-reading-guide.md)

## 跑完实验后你应该观察什么
- 工具边界为什么要先稳定，才能谈 agent 质量。
- trace 为什么应该从这个阶段开始成为一等产物。
- 这两个实验怎样自然汇合成 `support-agent`。

## 跑完之后回哪里
- 综合服务：[../module-service/README.md](../module-service/README.md)
- 练习手册：[../exercises.md](../exercises.md)
- 复盘模板：[../review.md](../review.md)
