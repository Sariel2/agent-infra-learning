# 00 总览与准备 Examples

这里不是“示例代码目录”，而是本模块的实验室。你在这里的目标不是多跑几个 demo，而是先建立课程后面都会反复使用的最小工程习惯：配置、日志、smoke test、实验记录。

## 这两个实验分别在证明什么
- [01-settings-and-logging/README.md](./01-settings-and-logging/README.md)
  证明“环境与日志上下文”应该先被建起来，否则后面实验很难排错。
- [02-project-smoke-test/README.md](./02-project-smoke-test/README.md)
  证明“项目是否处于可学习、可运行状态”也应该被快速验证。

## 推荐实验顺序
1. 先做 [01-settings-and-logging](./01-settings-and-logging/README.md)
2. 再做 [02-project-smoke-test](./02-project-smoke-test/README.md)
3. 两个实验都跑通之后，再进入 [module-service/README.md](../module-service/README.md)

## 每个实验都按这个顺序做
1. 先看该实验的 `README.md`
2. 再看 `walkthrough.md`
3. 跑代码
4. 做一个最小改动
5. 重新运行并记录结果
6. 把观察写进你的实验记录

## 做实验前先回看
- 模块首页：[../README.md](../README.md)
- 学习地图：[../study-map.md](../study-map.md)
- 执行剧本：[../steps.md](../steps.md)
- 代码导读：[../resources/03-code-reading-guide.md](../resources/03-code-reading-guide.md)

## 跑完实验后你应该观察什么
- 配置和日志为什么值得在课程一开始就建立。
- smoke test 为什么是最低成本的状态确认方式。
- 这些最小能力为什么会成为后续所有模块的通用底座。

## 跑完之后回哪里
- 综合服务：[../module-service/README.md](../module-service/README.md)
- 练习手册：[../exercises.md](../exercises.md)
- 复盘模板：[../review.md](../review.md)
