# 00 总览与准备 关键资料重点与总结

## 1. OpenAI Responses API
- 为什么值得读：官方文档，帮助你建立统一的模型调用心智模型。
- 重点看哪里：请求结构、响应结构、structured outputs、tools 的入口。
- 一句话总结：模型调用、结构化输出和工具能力正逐渐收敛到统一接口。
- 读完你应该会：你能读懂后面示例里的 provider 和 response schema 设计。
- 阅读说明：第一遍只看总览即可。

## 2. FastAPI
- 为什么值得读：课程里几乎所有综合服务都以它为壳。
- 重点看哪里：路由、依赖注入、错误处理、测试。
- 一句话总结：FastAPI 让你可以低成本搭建结构清晰的 Python API。
- 读完你应该会：你能理解每个 module-service 的 HTTP 边界。
- 阅读说明：先学最小套路，不要一开始钻高级特性。

## 3. Pydantic Settings
- 为什么值得读：配置管理会影响所有模块的可维护性。
- 重点看哪里：BaseSettings、env file、类型转换。
- 一句话总结：配置治理越早做，后面项目越不容易乱。
- 读完你应该会：你能把 API key、模型名、超时和开关收进统一配置。
- 阅读说明：配合 .env.example 一起看最有感觉。

## 4. OpenTelemetry Python
- 为什么值得读：这是后面 tracing 的背景资料。
- 重点看哪里：trace、span、attribute 基本概念。
- 一句话总结：trace 是过程可见性的基础，而不是高级附加项。
- 读完你应该会：你能明白为什么日志不足以替代 trace。
- 阅读说明：当前模块只需理解概念。
