# 01 Python 与 Agent 基础资料

## 核心资料
- [OpenAI Responses API](https://platform.openai.com/docs/guides/responses)
  重点：输入模型、结构化输出、工具模式入口
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
  重点：path operation、dependency injection、error handling
- [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
  重点：BaseSettings、env file、类型转换
- [pytest](https://docs.pytest.org/en/stable/)
  重点：fixture、参数化、接口测试最小套路

## 推荐补充
- [httpx](https://www.python-httpx.org/)
  重点：异步调用和客户端抽象
- [OpenAI Python SDK](https://github.com/openai/openai-python)
  重点：请求封装方式和常见示例

## 这一阶段要解决的问题
- 如何把模型调用变成可维护的模块，而不是散落在业务代码里
- 为什么结构化输出比纯文本输出更适合工程系统
