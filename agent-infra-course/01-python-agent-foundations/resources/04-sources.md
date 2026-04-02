# 01 Python 与 Agent 基础 原始来源与出处详解

[返回学习地图](../study-map.md) | [返回模块首页](../README.md) | [上一篇：03-code-reading-guide.md](./03-code-reading-guide.md) | [下一篇：05-common-mistakes.md](./05-common-mistakes.md)


这一页不是“链接仓库”，而是本模块讲义的出处解释页。你可以把它理解成：我为什么引用这些来源、这些来源里最值得看的部分是什么、以及这些内容在本教程里被翻译成了哪一段讲义。

## 怎么使用这一页
- 先把本模块前面的讲义读完，再来看这里。
- 看每个来源时，不要试图通读整站，只看这里标出的重点。
- 把这一页当成“出处说明 + 精读提示”，不是新的主教程。

## 1. [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- 为什么这个来源重要：这个来源支撑了本模块对 route 层的讲解。你在课程里看到的“route 只做协议转换，不做业务执行”不是个人偏好，而是成熟服务设计的常见实践。
- 建议重点看：
  - 重点读 request body、response model、path operation 和 testing
  - 不用先读后台任务或部署章节
  - 阅读时把注意力放在“服务边界”而不是“功能列表”上
- 它在本教程里的对应位置：对应 `resources/01-concepts-and-principles.md` 里关于 route / service 分层的部分，以及 `module-service/app/main.py` 的组织方式。
- 我从原文里提炼出的关键结论：
  - HTTP 层最适合承担协议边界，而不是业务执行。
  - 请求模型和响应模型是系统契约，不只是输入输出样例。
  - 如果你先把 HTTP 层职责想清楚，后面接 provider 和 tools 会轻松很多。

## 2. [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
- 为什么这个来源重要：课程把配置治理放在前面，是因为 agent 系统的可调参数非常多，而不是因为这只是“代码整洁”问题。
- 建议重点看：
  - 理解 BaseSettings 为什么适合承接环境配置
  - 看 env file 的标准方式
  - 关注“统一入口”这个原则
- 它在本教程里的对应位置：对应讲义中“先 fake，再 real”和“配置不应该散落在业务代码里”的部分。
- 我从原文里提炼出的关键结论：
  - 配置对象是系统稳定性的组成部分。
  - 模型名、超时、开关一旦散落，测试和回放都会变得很痛苦。

## 3. [OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses/list?lang=python)
- 为什么这个来源重要：本模块围绕 structured output 和 provider 设计，这个来源提供了当前主流模型响应接口的官方背景。
- 建议重点看：
  - 建立响应对象的基本心智
  - 理解结构化输出为什么能进入系统契约
  - 先看核心接口，不急着深挖全部能力
- 它在本教程里的对应位置：对应 `01-structured-output` example 和 `llm-gateway` 服务中的响应模型设计。
- 我从原文里提炼出的关键结论：
  - 结构化输出不是额外装饰，而是系统接入的前提。
  - provider 之所以重要，是因为响应接口会演进，而业务逻辑不应该跟着散掉。

## 4. [pytest documentation](https://docs.pytest.org/en/stable/)
- 为什么这个来源重要：课程里的所有示例和综合服务都带测试，这不是形式，而是为了让你在重构 provider 和 service 时有可验证边界。
- 建议重点看：
  - 读最小测试写法、fixture 和断言习惯
  - 先会写最基础的行为测试
  - 不必现在钻高级插件
- 它在本教程里的对应位置：对应 examples 和 module-service 中的 `tests/test_main.py`。
- 我从原文里提炼出的关键结论：
  - 测试是结构演进的保护网。
  - 先测 schema 和最小行为，比一开始做复杂端到端更重要。

## 5. [HTTPX](https://www.python-httpx.org/)
- 为什么这个来源重要：虽然课程示例先用 fake provider，但未来接真实模型和内部服务时，HTTP 客户端抽象会自然成为 provider 的一部分。
- 建议重点看：
  - 理解 client、timeout 与请求封装心智
  - 不用现在把它接进课程所有代码
- 它在本教程里的对应位置：对应 provider 抽象的未来扩展方向。
- 我从原文里提炼出的关键结论：
  - provider 层经常是 HTTP 适配层的载体。
  - 理解 HTTP client 抽象，会帮助你后面接模型和内部工具服务。

## 读完这一页后回到哪里
- 如果你想回到主线：返回 [study-map.md](../study-map.md)
- 如果你想继续执行：去 [steps.md](../steps.md)
- 如果你想重新回顾概念：去 [01-concepts-and-principles.md](./01-concepts-and-principles.md)
