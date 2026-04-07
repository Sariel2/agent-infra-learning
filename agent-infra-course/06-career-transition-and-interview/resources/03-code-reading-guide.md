# 06 转型、简历与面试 代码导读

[返回学习地图](../study-map.md) | [返回模块首页](../README.md) | [上一篇：02-deep-dive.md](./02-deep-dive.md) | [下一篇：04-sources.md](./04-sources.md)

这一页要带你把“表达也可以工程化”这件事看成具体代码。第 06 模块并不是突然从技术跳到文档，而是在训练你把：
- 项目事实
- 项目故事
- 高频问答
- 展示资产
都做成稳定结构。

## 怎么读这一页
- 先看项目故事生成，再看问答模板，最后回到综合展示包。
- 每个文件都先看“输入对象是什么”，再看“输出骨架是什么”。
- 不要把这些代码当作“随便生成点文案”，它们在训练你把表达沉淀成可复用资产。

## 推荐总顺序
1. 看 `examples/01-project-story-api`
2. 看 `examples/02-interview-qa-pack`
3. 看 `module-service/app/service.py`
4. 看 `module-service/app/main.py`
5. 看 `module-service/tests/test_main.py`

## Example 1：`01-project-story-api`
入口文件：
- [examples/01-project-story-api/app/main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/06-career-transition-and-interview/examples/01-project-story-api/app/main.py)
- [examples/01-project-story-api/tests/test_main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/06-career-transition-and-interview/examples/01-project-story-api/tests/test_main.py)
- [examples/01-project-story-api/walkthrough.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/06-career-transition-and-interview/examples/01-project-story-api/walkthrough.md)

先看这几个点：
- `ProjectFacts`
- `build_story()`

第一眼应该理解什么：
- `ProjectFacts` 是表达层的输入契约。
- `build_story()` 同时生成 `business` 和 `infra` 两种版本，正好对应课程里“双口径表达”的主线。
- 这段代码在告诉你：表达不是临场发挥，而是对事实做结构化重组。

接着看测试时重点看：
- 输出是否稳定包含关键字段
- 同一组事实是否能稳定产出双版本表述

建议你动手改一次：
- 换成你自己的项目名和目标
- 再看两种口径是否都还能成立

## Example 2：`02-interview-qa-pack`
入口文件：
- [examples/02-interview-qa-pack/app/main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/06-career-transition-and-interview/examples/02-interview-qa-pack/app/main.py)
- [examples/02-interview-qa-pack/tests/test_main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/06-career-transition-and-interview/examples/02-interview-qa-pack/tests/test_main.py)
- [examples/02-interview-qa-pack/walkthrough.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/06-career-transition-and-interview/examples/02-interview-qa-pack/walkthrough.md)

先看这几个点：
- `FAQ`
- `answer_question()`

第一眼应该理解什么：
- `FAQ` 是高频追问的最小知识包。
- `answer_question()` 最重要的不是生成能力，而是“回答骨架可重复”。
- 这里训练的是一种非常实用的技能：把高频判断题做成稳定回答模板。

接着看测试时重点看：
- 已知主题是否返回稳定答案
- 未知主题是否返回通用回答骨架

建议你动手改一次：
- 增加一个新主题，比如 `tool-schema`
- 再给它补一个工程化回答

## 最后看综合服务：`showcase-pack`
入口文件：
- [module-service/app/service.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/06-career-transition-and-interview/module-service/app/service.py)
- [module-service/app/main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/06-career-transition-and-interview/module-service/app/main.py)
- [module-service/tests/test_main.py](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/06-career-transition-and-interview/module-service/tests/test_main.py)
- [module-service/README.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/06-career-transition-and-interview/module-service/README.md)

推荐读码顺序：
1. 先看 `StoryRequest`
2. 再看 `QARequest`
3. 再看 `FAQ`
4. 再看 `build_story()`
5. 最后看 `answer()`

第一眼应该理解什么：
- `StoryRequest` 和 `QARequest` 把两类表达任务分开了。
- `build_story()` 负责把项目事实变成展示资产。
- `answer()` 负责把高频面试问题变成稳定话术入口。
- 这正对应了第 06 模块的两条主线：项目叙事和追问应对。

接着再看 `app/main.py` 时重点看：
- `/story` 和 `/qa` 是否对应两类不同表达任务
- route 层是否只负责协议入口

最后看测试时重点看：
- 输出骨架是否被稳定保护
- 未知问题是否仍然能回到统一回答结构

## 这一页最容易读偏的地方
- 误区一：觉得这不是技术代码
  - 这里训练的是“把表达做成系统”的能力。
- 误区二：只看生成文案，不看输入对象
  - 真正关键的是事实如何被结构化收集。
- 误区三：觉得问答模板太死板
  - 对面试准备来说，稳定骨架比临场灵感更重要。

## 读完这一页后应该回哪里
- 如果你想继续执行：去 [steps.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/06-career-transition-and-interview/steps.md)
- 如果你想回顾原理：去 [02-deep-dive.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/06-career-transition-and-interview/resources/02-deep-dive.md)
- 如果你想看出处解释：去 [04-sources.md](/Users/tianqingxiang/Desktop/work/project/github/agent-infra-learning/agent-infra-learning/agent-infra-course/06-career-transition-and-interview/resources/04-sources.md)
