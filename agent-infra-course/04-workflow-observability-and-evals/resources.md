# 04 Workflow、Observability 与 Evals资料

## 核心资料
- [LangGraph Overview](https://docs.langchain.com/oss/python/langgraph/overview)
  重点：状态图、节点、边、持久化思路
- [LangGraph Observability](https://docs.langchain.com/oss/python/langgraph/observability)
  重点：如何把运行过程变得可读
- [OpenAI Agents SDK Tracing](https://openai.github.io/openai-agents-python/tracing/)
  重点：trace、span、运行分析
- [OpenTelemetry Python Instrumentation](https://opentelemetry.io/docs/languages/python/instrumentation/)
  重点：最小 tracing 概念与手动埋点方式

## 推荐补充
- [FastAPI Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/)
  重点：区分请求返回与后台任务的边界
- [PydanticAI Durable Execution](https://ai.pydantic.dev/durable_execution/overview/)
  重点：理解长流程和 durable runtime 的方向

## 这一阶段要解决的问题
- 为什么没有 trace 的 agent 系统几乎无法稳定迭代
- eval dataset 为什么要尽早建立，而不是最后补
