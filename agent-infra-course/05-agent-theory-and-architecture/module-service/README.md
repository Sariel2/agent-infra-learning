# architecture-lab

把 pattern 对比和边界判断组织成一个可演示的实验服务。

## 这个综合服务的目标
- 把“模式比较”和“模式推荐”拆成两个可验证能力。
- 让你学会先判断任务结构，再决定该用 workflow、agent 还是 hybrid。
- 用最小实验接口把抽象理论压到可运行代码里。

## 开始前先回看
- 模块首页：[../README.md](../README.md)
- 学习地图：[../study-map.md](../study-map.md)
- 概念讲义：[../resources/01-concepts-and-principles.md](../resources/01-concepts-and-principles.md)
- 原理细节：[../resources/02-deep-dive.md](../resources/02-deep-dive.md)
- 代码导读：[../resources/03-code-reading-guide.md](../resources/03-code-reading-guide.md)
- 示例 1：[../examples/01-pattern-comparison/app/main.py](../examples/01-pattern-comparison/app/main.py)
- 示例 2：[../examples/02-boundary-checker/app/main.py](../examples/02-boundary-checker/app/main.py)

## 先理解这 3 个文件
- 核心逻辑：[app/service.py](./app/service.py)
  先看 `compare()` 和 `recommend()`，前者负责展示模式差异，后者负责做场景判断。
- HTTP 入口：[app/main.py](./app/main.py)
  看 `/compare` 与 `/recommend` 为什么是两种不同接口。
- 最小验收：[tests/test_main.py](./tests/test_main.py)
  看测试如何把“固定步骤优先 workflow”固化为最小判断规则。

## 推荐实现顺序
1. 先读 [app/service.py](./app/service.py)，理解 `CompareRequest` 和 `RecommendRequest` 分别服务什么目的。
2. 重点看 `recommend()` 的三个布尔条件如何压缩成模式判断。
3. 再看 [tests/test_main.py](./tests/test_main.py)，理解为什么先固定一个最小推荐规则。
4. 最后读 [app/main.py](./app/main.py)，确认理论判断也可以被接口化。

## 动手实现时每一步做什么
### Step 1：先把模式差异写成可比较输出
- 要改的文件：[app/service.py](./app/service.py)
- 要做的事：用 `compare()` 明确展示 ReAct、Router、Plan-and-Execute 的最小流程差异。
- 验收标准：输出必须能让人一眼看出三种模式流程不同，而不是只有名词列表。

### Step 2：再做边界判断逻辑
- 要改的文件：[app/service.py](./app/service.py)
- 要做的事：用 `recommend()` 把任务特征映射成 `workflow`、`agent` 或 `hybrid`。
- 验收标准：固定步骤且非开放任务时，推荐结果必须是 `workflow`。

### Step 3：最后暴露接口和测试
- 要改的文件：[app/main.py](./app/main.py)
- 要改的文件：[tests/test_main.py](./tests/test_main.py)
- 要做的事：把比较与推荐分别暴露出来，并用测试锁住核心规则。
- 验收标准：`/recommend` 在典型确定性场景下返回 `workflow`。

## 建议运行命令
- `uvicorn app.main:app --reload`
- `pytest`

## 常见退化点
- 只会背模式定义，不会把场景映射成模式选择。
- 一上来就选 multi-agent，把复杂度提前抬高。
- 推荐逻辑没有明确判断条件，最后只能靠“经验感觉”。

## 扩展时优先做什么
- 增加更多任务特征，例如风险等级、人工审核、结果可验证性。
- 把推荐理由也结构化输出，而不只是返回一个模式名。
- 用前面模块的真实服务作为输入样本做模式复盘。

## 学完后你应该能回答
- 为什么模式选择先于框架选择。
- 为什么 workflow 往往是很多场景的更优起点。
- 哪些任务是真正需要 agent 自由度的。
