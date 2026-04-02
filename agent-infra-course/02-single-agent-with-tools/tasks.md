# 02 单 Agent 与 Tools任务安排

## Day 1：理解工具调用
- 梳理工具调用和普通 API 调用的区别
- 设计 3 个工具接口：`search_docs`、`get_order_status`、`create_ticket`
- 定义每个工具的输入、输出、失败模式

## Day 2：实现工具层
- 用 Python 函数实现工具
- 给参数做类型校验
- 给每个工具加统一返回结构

## Day 3：接入 Agent Loop
- 写一个最小单 Agent 执行器
- 支持 `plan -> call tool -> observe -> continue`
- 记录每一步输入和输出

## Day 4：处理异常场景
- 模拟工具超时
- 模拟参数缺失
- 模拟工具返回空数据
- 设计重试和降级策略

## Day 5：打磨可解释性
- 输出工具调用轨迹
- 记录 tool name、args、result、latency
- 整理一份失败案例文档

## 退出条件
- Agent 能稳定执行至少 3 类任务
- 你能看日志判断问题出在模型、参数还是工具本身
