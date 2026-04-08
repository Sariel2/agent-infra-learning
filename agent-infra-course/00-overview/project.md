# 00 总览与准备 模块综合项目说明

## 项目名
`starter-workspace`

## 项目定位
这个项目不是业务服务，而是整门课的最小工作区骨架。它要解决的问题不是“系统能不能回答”，而是“你的学习环境、配置、记录和 readiness 是否已经进入可持续演进状态”。

## 对应综合服务
- 服务入口：[module-service/app/main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/00-overview/module-service/app/main.py)
- 服务逻辑：[module-service/app/service.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/00-overview/module-service/app/service.py)
- 测试入口：[module-service/tests/test_main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/00-overview/module-service/tests/test_main.py)

## 项目目标
做一个最小的“工作区就绪检查服务”，能够结构化表达：
- 环境是否准备好
- 日志和记录机制是否准备好
- 主项目方向是否已经确定

## 你最终应该学到什么
- 为什么课程从骨架和记录开始
- 为什么状态对象值得先于复杂功能建立
- 为什么从第 00 模块就要有 `service + route + test` 的服务视角

## 必做项
- 提供一个最小 readiness 检查接口
- 用对象表达工作区状态，而不是散落布尔变量
- 把输出结构化成稳定响应
- 为 readiness 判断写最小测试
- 给工作区保留最基础的配置和日志上下文意识

## 推荐实现顺序
1. 先看 [resources/03-code-reading-guide.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/00-overview/resources/03-code-reading-guide.md)
2. 再跑 `examples/01-settings-and-logging`
3. 再跑 `examples/02-project-smoke-test`
4. 然后实现或阅读 `starter-workspace`
5. 最后回到 [review.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/00-overview/review.md) 做收束

## 实现清单
- `WorkspaceStatus` 之类的状态对象已经存在
- `summarize_workspace()` 能给出稳定结果
- HTTP 层只做协议边界
- 测试能验证“ready / needs-work”判断
- 你能在这个服务上继续扩展新的 readiness 条件

## 验收清单
- 我能跑起服务
- 我能解释每个 readiness 字段代表什么
- 我能新增一个状态字段并同步更新逻辑和测试
- 我能说清这个项目为什么是后面所有模块的起点

## 常见退化点
- 把第 00 模块当成“无聊准备工作”跳过
- 不写测试，觉得 readiness 太简单
- 仍然把配置、状态和日志当成零散变量

## 加分项
- 增加更多 readiness 字段，例如 `docs_ready`
- 给状态输出补简单 metadata
- 在响应里保留最小工作区摘要

## 交付物
- 一个能启动的最小工作区服务
- 一组最小测试
- 一份你自己的工作区 readiness 标准

## 进入下一模块前，你应该能回答
- 为什么课程必须先有骨架
- 为什么 readiness 也值得对象化
- 为什么从第一模块开始就要保留服务化和测试化意识
