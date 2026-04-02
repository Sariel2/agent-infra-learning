# 04 Workflow、Observability 与 Evals 概念总结

    ## 关键概念
    - Workflow：显式定义步骤与条件分支的执行图。
- Trace：单次运行的结构化过程记录。
- Eval Dataset：用于重复验证系统表现的一组固定输入。
- Regression：比较不同版本输出结果变化的过程。

    ## 容易混淆
    - 看起来能跑的 demo 不等于工程能力已经建立。
    - 会背术语不等于能做边界判断。
    - 有日志不等于有 trace；有试玩不等于有 eval。

    ## 判断原则
    - 优先做最小可运行版本，再补复杂度。
    - 所有知识点最终都要回到 examples 或 module-service 上验证。
    - 每个模块至少保留 1 条失败案例和 1 条改进思路。
