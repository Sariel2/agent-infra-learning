# 00 总览与准备资料

## 优先阅读
- [OpenAI Responses API](https://platform.openai.com/docs/guides/responses)
  重点：理解新的请求模型、输入输出结构、工具接入方式
- [FastAPI](https://fastapi.tiangolo.com/)
  重点：最小 API 服务、依赖注入、错误处理
- [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
  重点：配置管理、环境变量、类型安全

## 补充阅读
- [OpenAI New tools for building agents](https://openai.com/index/new-tools-for-building-agents/)
  重点：为什么现在讲 agent infra 要把 tools、tracing、runtime 放一起看
- [OpenTelemetry Python](https://opentelemetry.io/docs/languages/python/)
  重点：先知道它是干什么的，后面第 4 阶段再深入

## 这一阶段你要带着问题去读
- Agent 应用和普通 LLM 调用，工程差别到底在哪里
- 为什么 Python 成了当前 agent infra 主战语言
- 课程主项目后面需要哪些模块，哪些不需要现在做
