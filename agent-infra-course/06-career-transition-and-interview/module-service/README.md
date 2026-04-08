# showcase-pack

把项目故事、简历 bullet 和面试问答组织成可展示包。

## 这个综合服务的目标
- 把前面 6 个模块的工程成果转成可表达、可展示、可面试的材料。
- 让“项目讲解”也变成有结构的输出，而不是临场发挥。
- 演示技术表达同样可以被接口化、模板化和测试。

## 开始前先回看
- 模块首页：[../README.md](../README.md)
- 学习地图：[../study-map.md](../study-map.md)
- 概念讲义：[../resources/01-concepts-and-principles.md](../resources/01-concepts-and-principles.md)
- 原理细节：[../resources/02-deep-dive.md](../resources/02-deep-dive.md)
- 代码导读：[../resources/03-code-reading-guide.md](../resources/03-code-reading-guide.md)
- 示例 1：[../examples/01-project-story-api/app/main.py](../examples/01-project-story-api/app/main.py)
- 示例 2：[../examples/02-interview-qa-pack/app/main.py](../examples/02-interview-qa-pack/app/main.py)

## 先理解这 3 个文件
- 核心逻辑：[app/service.py](./app/service.py)
  先看 `build_story()` 和 `answer()`，理解“项目故事生成”和“面试追问应答”是两种不同表达任务。
- HTTP 入口：[app/main.py](./app/main.py)
  看 `/story` 和 `/qa` 为什么分开暴露。
- 最小验收：[tests/test_main.py](./tests/test_main.py)
  看测试如何锁住输出骨架，避免表达结构漂移。

## 推荐实现顺序
1. 先读 [app/service.py](./app/service.py)，理解 `StoryRequest`、`QARequest`、`FAQ`、`build_story()`、`answer()` 的角色。
2. 再看 [tests/test_main.py](./tests/test_main.py)，确认故事输出里至少要保留项目名。
3. 最后读 [app/main.py](./app/main.py)，看两个表达入口如何映射到不同服务函数。
4. 自己尝试增加一个新的 FAQ 主题，观察问答包如何扩展。

## 动手实现时每一步做什么
### Step 1：先固定项目故事模板
- 要改的文件：[app/service.py](./app/service.py)
- 要做的事：用 `build_story()` 稳定生成 `resume_bullet` 和 `pitch`。
- 验收标准：同一输入每次都能生成结构稳定的结果。

### Step 2：再整理面试高频问答
- 要改的文件：[app/service.py](./app/service.py)
- 要做的事：用 `FAQ` 和 `answer()` 承接高频技术追问。
- 验收标准：问答返回必须围绕目标、设计、失败、取舍和结果，而不是散答。

### Step 3：最后暴露接口与测试
- 要改的文件：[app/main.py](./app/main.py)
- 要改的文件：[tests/test_main.py](./tests/test_main.py)
- 要做的事：通过 `/story` 和 `/qa` 暴露表达能力，并用测试固定最小产出骨架。
- 验收标准：`/story` 的输出里必须保留项目名和改进方向。

## 建议运行命令
- `uvicorn app.main:app --reload`
- `pytest`

## 常见退化点
- 只讲“用了什么技术”，不讲为什么这样设计。
- 只讲成功结果，不讲失败案例和优化过程。
- 输出结构不稳定，导致简历描述和项目讲解无法复用。

## 扩展时优先做什么
- 为不同项目场景生成不同版本的故事模板。
- 给 FAQ 增加追问链路和反问示例。
- 把前面模块里的真实失败样本整理成面试素材库。

## 学完后你应该能回答
- 为什么“会做”和“会讲”是两种不同但都必须训练的能力。
- 如何把 agent infra 项目讲成业务方也能理解的故事。
- 如何把前面 5 个模块的工程能力组织成可信的转型材料。
