# 01 Python 与 Agent 基础任务安排

## Day 1：Python 工程基础
- 建立 `src/`、`tests/`、`app/` 分层认识
- 理解 `typing`、`dataclass`、`BaseModel`、`async/await`
- 写 3 个小练习：配置类、请求模型、响应模型

## Day 2：FastAPI 与配置管理
- 写一个 `/health` 接口
- 写一个 `/config-check` 接口
- 用 `pydantic-settings` 管理 `API key`、`model`、`timeout`

## Day 3：模型接入
- 读 Responses API 文档
- 写一个最小模型调用函数
- 支持 text input 和 structured output

## Day 4：抽象与封装
- 把模型调用封装成 provider
- 统一异常处理与日志
- 给请求加超时、重试、错误返回

## Day 5：测试与收尾
- 给 provider 写最小单元测试
- 给 FastAPI 路由写基础接口测试
- 输出一版阶段 README 和实验记录

## 退出条件
- 能从 API 请求拿到结构化响应
- 能定位 3 种常见错误：配置错误、调用错误、解析错误
