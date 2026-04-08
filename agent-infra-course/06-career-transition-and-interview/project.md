# 06 转型、简历与面试 模块综合项目说明

## 项目名
`agent-infra-showcase-pack`

## 项目定位
这是整门课的最终展示包。它不是再做一个新技术项目，而是把前 5 个模块的成果重新组织成可以用于求职、转岗、内部分享或技术面试的完整资产。

## 对应综合服务
- 服务入口：[module-service/app/main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/06-career-transition-and-interview/module-service/app/main.py)
- 服务逻辑：[module-service/app/service.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/06-career-transition-and-interview/module-service/app/service.py)
- 测试入口：[module-service/tests/test_main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/06-career-transition-and-interview/module-service/tests/test_main.py)

## 项目目标
把前 5 个阶段的成果打包成一套可展示、可追问、可复用的项目材料，至少包括：
- 一版项目 README
- 一张系统设计图
- 一份简历项目描述
- 一份高频问答清单
- 一份 3 分钟讲稿

## 你最终应该学到什么
- 为什么表达不是附属技能，而是交付的一部分
- 为什么同一项目要有业务版和 infra 版两套讲法
- 为什么失败案例会显著增强说服力
- 为什么表达也可以被工程化和模板化

## 必做项
- 生成项目故事骨架
- 生成高频问答骨架
- 把两类能力收束到 `showcase-pack`
- 明确区分业务版和 infra 版表述
- 保留至少 1 条完整失败案例

## 推荐实现顺序
1. 先跑 `examples/01-project-story-api`
2. 再跑 `examples/02-interview-qa-pack`
3. 再读 [resources/03-code-reading-guide.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/06-career-transition-and-interview/resources/03-code-reading-guide.md)
4. 再回到 `showcase-pack`
5. 最后做 [review.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/06-career-transition-and-interview/review.md)

## 实现清单
- `build_story()` 能生成项目故事骨架
- `answer()` 或等价函数能返回高频问答骨架
- `/story` 和 `/qa` 两类入口分开
- 测试保护项目故事和问答结构
- 你能把前 5 个模块中的真实例子填进这个服务

## 验收清单
- 我能直接拿这个展示包做项目讲解
- 我能用同一项目讲出业务版和 infra 版
- 我能拿出至少 1 条完整失败案例
- 我能回答常见追问，而不只会背术语
- 我能体现自己从后端工程师转向 agent infra 的成长路径

## 常见退化点
- 项目讲解只有功能，没有工程细节
- 简历描述只写用了什么框架
- 面试回答只有术语，没有案例
- 不敢讲失败，导致表达不真实
- 展示材料和真实代码脱节

## 加分项
- 录一段 demo 视频
- 做一页项目演进对比表
- 写一页“如果继续做，我下一步会做什么”
- 为常见问题准备更细的追问版本

## 交付物
- 一套可直接展示的项目材料
- 一个可运行的展示服务
- 一份你自己的业务版和 infra 版讲稿

## 进入总考试或真实面试前，你应该能回答
- 为什么这个项目值得做
- 为什么它的架构是这样设计的
- 你遇到了哪些失败，如何修复
- 为什么你是适合 agent infra 方向的人
