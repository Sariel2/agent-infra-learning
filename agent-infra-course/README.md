# Agent Infra Learning Course

这是一个为后端工程师设计的 `6 周冲刺版` Agent Infra 学习课程，主线语言只用 Python，不夹带 Java 练习。课程核心目标不是“学几个框架名词”，而是用 6 周时间做出一套具备 `tool calling`、`RAG`、`workflow`、`observability`、`eval` 能力的工程化 Agent 系统，并在后两周补齐原理和转型表达。

## 课程定位
- 学习对象：有后端工程经验，想系统进入 Agent Infra 的工程师
- 节奏：每周 `8-12 小时`
- 周期：`6 周`
- 方法：`项目驱动 + 文档驱动 + 复盘驱动`
- 主项目：一个可运行的 `Python Agent API`，逐周叠加能力

## 学习结果
- 能独立搭建 Python-first 的 Agent 服务骨架
- 能实现单 Agent + Tools + RAG + Workflow 的完整链路
- 能给 Agent 系统加上 trace、eval、失败分析和回归验证
- 能把实践经验抽象成架构模式，并整理为面试和转型材料

## 课程结构
- [00-overview](./00-overview/README.md)：总览、环境、项目主线、学习机制
- [01-python-agent-foundations](./01-python-agent-foundations/README.md)：Python 工程基础与 LLM 接入
- [02-single-agent-with-tools](./02-single-agent-with-tools/README.md)：单 Agent 与工具调用
- [03-rag-memory-and-knowledge](./03-rag-memory-and-knowledge/README.md)：RAG、知识库、记忆
- [04-workflow-observability-and-evals](./04-workflow-observability-and-evals/README.md)：编排、可观测、评测
- [05-agent-theory-and-architecture](./05-agent-theory-and-architecture/README.md)：原理、模式、架构思维
- [06-career-transition-and-interview](./06-career-transition-and-interview/README.md)：项目包装、面试、转型表达

## 建议节奏
- `2 小时`：读文档和梳理原理
- `4-6 小时`：编码与实验
- `1-2 小时`：复盘、记错、补洞
- `1-2 小时`：整理输出物，例如图、笔记、讲稿、README

## 使用方式
1. 先读 [mindmap.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/mindmap.md)，建立总地图。
2. 再进入 `00-overview`，把环境、项目方向、学习日志模板搭好。
3. 之后按文件夹顺序推进，每完成一个阶段，就更新一次主项目和个人复盘。
4. 每周至少做一次失败案例分析，不要只记录“成功了什么”。

## 每个阶段固定文件
- `README.md`：阶段目标、范围、完成标准
- `tasks.md`：具体执行安排
- `resources.md`：推荐资料和阅读重点
- `project.md`：该阶段项目任务和验收要求
- `review.md`：复盘问题和自查清单
- `mindmap.md`：该阶段子思维导图

## 阶段完成定义
- 能跑：阶段项目可执行
- 能讲：你能用 3-5 分钟解释关键设计
- 能测：你知道成功与失败如何判断
- 能改：你知道下一步要优化哪里
