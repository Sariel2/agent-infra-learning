# 02 单 Agent 与 Tools 细节深挖

[返回学习地图](../study-map.md) | [返回模块首页](../README.md) | [上一篇：01-concepts-and-principles.md](./01-concepts-and-principles.md) | [下一篇：03-code-reading-guide.md](./03-code-reading-guide.md)

## 1. 最小 agent loop 是怎样工作的
用课程示例来拆，最小单 agent loop 可以理解成：
1. 收到问题
2. 根据问题类型选择工具
3. 执行工具
4. 把工具结果包装成 observation
5. 返回结果或继续循环

课程中的示例只实现了一轮，但这已经足够帮助你理解 agent 的骨架。多轮 loop 只是把这条链路继续迭代。

## 2. 为什么 trace 结构要从一开始就统一
当系统变复杂后，你真正关心的问题不是“工具有没有被调用”，而是：
- 调了哪个工具
- 参数是什么
- 成功还是失败
- 耗时如何
- 是否触发重试

如果这些字段没有统一结构，后面做 trace、eval 和失败分析时会非常痛苦。

## 3. 失败恢复的思路
tool calling 的失败可以分成三类：
- 选错工具
- 参数错
- 工具执行失败

三类失败的修复点不同：
- 选错工具通常要看 schema 描述、分类逻辑或上游上下文
- 参数错要看 schema 收紧和模型动作约束
- 执行失败要看工具实现、超时和 fallback
