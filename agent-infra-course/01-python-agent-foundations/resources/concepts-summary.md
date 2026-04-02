# 01 Python 与 Agent 基础 概念总结

    ## 关键概念
    - Structured Output：使用稳定 schema 约束模型输出的方式。
- Provider：统一封装模型接入的适配层。
- Service：组织业务逻辑并调度 provider 的层。
- Route：向外暴露 HTTP 接口的层。

    ## 容易混淆
    - 看起来能跑的 demo 不等于工程能力已经建立。
    - 会背术语不等于能做边界判断。
    - 有日志不等于有 trace；有试玩不等于有 eval。

    ## 判断原则
    - 优先做最小可运行版本，再补复杂度。
    - 所有知识点最终都要回到 examples 或 module-service 上验证。
    - 每个模块至少保留 1 条失败案例和 1 条改进思路。
