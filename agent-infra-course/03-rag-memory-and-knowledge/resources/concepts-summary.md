# 03 RAG、Memory 与 Knowledge 概念总结

    ## 关键概念
    - Chunking：把原始资料切成可检索片段的过程。
- Retrieval：从外部知识源取回候选上下文。
- Citation：答案引用来源证据。
- Short-term Memory：会话窗口内的压缩记忆。

    ## 容易混淆
    - 看起来能跑的 demo 不等于工程能力已经建立。
    - 会背术语不等于能做边界判断。
    - 有日志不等于有 trace；有试玩不等于有 eval。

    ## 判断原则
    - 优先做最小可运行版本，再补复杂度。
    - 所有知识点最终都要回到 examples 或 module-service 上验证。
    - 每个模块至少保留 1 条失败案例和 1 条改进思路。
