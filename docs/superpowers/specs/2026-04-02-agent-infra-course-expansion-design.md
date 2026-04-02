# Agent Infra Course Expansion Design

## 背景

现有课程已经包含 6 周主线、每阶段说明文档、任务安排、资料链接、项目说明、复盘问题和思维导图，但还不满足“重度教学版”的要求。用户希望把课程扩展成真正可执行、可自学、可考核、可运行的学习系统。

## 目标

把现有 `agent-infra-course/` 扩展为一套面向 Python-first Agent Infra 学习的重度教学课程，满足以下要求：

- 每个模块把单文件 `resources.md` 升级为 `resources/` 目录
- 每个模块都要有更丰富的关键资料，并附带重点、总结、阅读说明
- 每个模块都要新增 `steps.md`，按步骤明确“每一步应该做什么”
- 每个知识点都要给出可运行的实例代码或示例项目
- 每个模块最终都要有一个综合本模块知识点的服务框架，实现模块内要求的所有核心功能
- 根目录新增一套汇总测试题，并提供详细参考答案与解析

## 非目标

- 当前阶段不直接实现整个 6 周主项目的最终生产版
- 不在这一轮中引入前端界面
- 不把每个知识点都做成完整独立中型项目，避免课程过度膨胀

## 整体结构

课程根目录保持为 `agent-infra-course/`，新增和调整后的结构如下：

```text
agent-infra-course/
├── README.md
├── mindmap.md
├── assessment/
│   ├── README.md
│   ├── final-exam.md
│   ├── final-exam-answers.md
│   └── scoring-rubric.md
├── 00-overview/
├── 01-python-agent-foundations/
├── 02-single-agent-with-tools/
├── 03-rag-memory-and-knowledge/
├── 04-workflow-observability-and-evals/
├── 05-agent-theory-and-architecture/
└── 06-career-transition-and-interview/
```

每个模块统一扩展为：

```text
<module>/
├── README.md
├── tasks.md
├── steps.md
├── project.md
├── review.md
├── exercises.md
├── mindmap.md
├── examples/
│   ├── README.md
│   ├── 01-<topic>/
│   ├── 02-<topic>/
│   └── ...
├── module-service/
│   ├── README.md
│   ├── pyproject.toml
│   ├── .env.example
│   ├── app/
│   └── tests/
└── resources/
    ├── README.md
    ├── key-resources.md
    ├── reading-notes.md
    └── concepts-summary.md
```

## 文件职责设计

### README.md

说明该模块学什么、范围边界、最终完成标准、推荐学习顺序。

### tasks.md

给出周/天级别节奏安排，解决“这一周怎么分配时间”的问题。

### steps.md

给出严格按顺序的执行说明。每一步都包含：

- 做什么
- 为什么现在做
- 具体动作
- 产出物
- 完成判断
- 常见卡点
- 卡住时优先排查什么

### project.md

描述本模块的综合项目目标、必做项、加分项、验收标准。

### review.md

给出复盘问题、自查清单、失败分析模板。

### exercises.md

给出本模块专属练习题，覆盖概念题、应用题、排错题和小型设计题。

### resources/

拆成 4 个文件：

- `README.md`：资料地图、必读/选读、推荐顺序
- `key-resources.md`：每篇资料的重点、总结、适用场景、阅读收益
- `reading-notes.md`：怎么读、读多久、带着什么问题去读、读完做什么
- `concepts-summary.md`：关键概念速记、混淆点对比、判断原则、常见误区

### examples/

每个知识点一个可运行示例。每个示例都包含：

- 简要说明文档
- 独立依赖配置
- 可启动或可测试的代码
- 最小测试
- 预期结果

### module-service/

每个模块的综合服务框架，用最小可维护方式覆盖本模块所有核心能力。它不是简单脚本，而是具备：

- 工程结构
- 配置管理
- 服务入口
- 核心模块实现
- 测试
- 运行说明

## 每个模块的综合服务设计

### 00-overview

综合服务：`starter-workspace`

目标：

- 给后续模块提供统一 Python 工程脚手架
- 包含目录结构、配置、日志、测试入口

### 01-python-agent-foundations

综合服务：`llm-gateway`

功能：

- FastAPI 服务
- Responses API 调用
- Structured output
- Provider 封装
- 配置与基础测试

### 02-single-agent-with-tools

综合服务：`support-agent`

功能：

- 单 Agent Loop
- Tool schema 定义
- 参数校验
- 失败恢复
- 执行轨迹记录

### 03-rag-memory-and-knowledge

综合服务：`knowledge-agent`

功能：

- 文档导入
- 检索
- citation
- 简单短期 memory
- 检索失败记录

### 04-workflow-observability-and-evals

综合服务：`agent-runtime`

功能：

- Workflow 编排
- Trace 记录
- Eval 数据集运行
- 基础回归比较

### 05-agent-theory-and-architecture

综合服务：`architecture-lab`

功能：

- 用统一接口演示不同 agent pattern
- 对比 ReAct、Router、Plan-and-Execute 的实现骨架
- 体现模式选型和边界

### 06-career-transition-and-interview

综合服务：`showcase-pack`

功能：

- 把前面模块的能力包装成演示资产
- 包含 README 模板、讲稿、问答库、项目对比表

## 每个模块的 examples 设计原则

示例必须满足：

- 可运行
- 单一知识点聚焦
- 不依赖复杂外部组件才能理解
- 与本模块综合服务存在清晰映射关系

例如：

### 01-python-agent-foundations

- `01-settings-and-config`
- `02-fastapi-minimal-app`
- `03-structured-output`
- `04-provider-abstraction`
- `05-basic-tests`

### 02-single-agent-with-tools

- `01-basic-tool-schema`
- `02-tool-validation`
- `03-tool-execution-loop`
- `04-tool-timeout-and-retry`
- `05-tool-trace-log`

### 03-rag-memory-and-knowledge

- `01-hosted-file-search`
- `02-qdrant-indexing`
- `03-retrieval-with-citations`
- `04-short-term-memory`
- `05-rag-failure-analysis`

## 汇总考试设计

根目录新增 `assessment/`：

- `README.md`：考试说明
- `final-exam.md`：完整试题
- `final-exam-answers.md`：详细答案与解析
- `scoring-rubric.md`：评分标准

题型采用混合版，包含：

- 选择题
- 判断题
- 简答题
- 场景分析题
- 系统设计题
- 项目讲解题

答案解析必须包括：

- 正确答案
- 原因说明
- 错误选项或常见错误思路解析
- 工程上的判断方法

## 数据流与学习流

每个模块的学习顺序固定为：

1. 看 `README.md`
2. 看 `mindmap.md`
3. 按 `resources/README.md` 和 `reading-notes.md` 读资料
4. 按 `steps.md` 跑 examples
5. 完成本模块 `module-service/`
6. 做 `exercises.md`
7. 用 `review.md` 复盘

## 错误处理与测试要求

由于课程包含可运行代码，所有代码示例和综合服务都应尽量满足：

- 有最小启动说明
- 有基础测试命令
- 不强依赖线上服务也能演示主要结构
- 对需要 API key 的模块，提供 mock 或 fake 模式说明

## 风险与取舍

### 风险 1：文件数量大幅增加

取舍：

- 统一模板，避免每个模块结构不一致
- 示例以最小可运行为主，不做无边界膨胀

### 风险 2：外部依赖导致示例难跑

取舍：

- 能用 mock 的地方优先提供 mock
- 把真实 API 集成留在综合服务中

### 风险 3：理论模块难以提供“服务框架”

取舍：

- 第 05 和第 06 模块的综合服务更偏“实验室”和“展示包”
- 保持“可运行/可交付”而不是强行伪造业务服务

## 实施范围

本轮实施将包括：

- 目录重构
- 所有模块资源目录扩展
- 所有模块新增 `steps.md`
- 所有模块新增 `exercises.md`
- 所有模块新增 `examples/`
- 所有模块新增 `module-service/`
- 根目录新增 `assessment/`

## 用户审阅点

重点请用户确认：

- 目录结构是否符合预期
- 每模块都同时包含文档、示例和综合服务的设计是否合理
- 第 05 和第 06 模块采用“实验室/展示包”形式而非传统 API 服务是否可接受
