# 02 单 Agent 与 Tools资料

## 核心资料
- [OpenAI Tools Guide](https://platform.openai.com/docs/guides/tools)
  重点：工具声明、调用流程、模型与工具的关系
- [OpenAI Web Search Tool](https://platform.openai.com/docs/guides/tools-web-search?api-mode=responses&lang=python)
  重点：先理解 built-in tool 的使用方式，再类比自定义工具
- [OpenAI Agents SDK](https://platform.openai.com/docs/guides/agents-sdk/)
  重点：理解 agent orchestration 的主流官方路径

## 推荐补充
- [PydanticAI](https://ai.pydantic.dev/)
  重点：看它如何把类型约束和 agent 调用放一起设计

## 这一阶段要思考
- 工具描述写得不好，会怎样影响模型决策
- 为什么很多 Agent 问题其实是 schema 和执行治理问题
