# Agent Infra Course Expansion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Expand the existing course into a heavy-teaching format with richer resource packs, explicit step-by-step execution guides, per-module exercises, runnable knowledge-point examples, module-level service frameworks, and a final assessment with detailed answers.

**Architecture:** Keep `agent-infra-course/` as the root. For each module, replace the flat `resources.md` with a `resources/` directory, add `steps.md` and `exercises.md`, add an `examples/` folder with runnable mini-projects, and add a `module-service/` folder with a runnable service skeleton that integrates the module's key concepts. Add a root `assessment/` folder for the final exam and answer materials. Use consistent Python project structure across runnable examples and services so the learner experiences one coherent engineering style throughout the course.

**Tech Stack:** Markdown, Mermaid, Python 3.11, FastAPI, Pydantic, pytest, httpx

---

### Task 1: Prepare the expansion scaffolding

**Files:**
- Create: `docs/superpowers/plans/2026-04-02-agent-infra-course-expansion-implementation.md`
- Modify: `agent-infra-course/`

- [ ] **Step 1: Verify the current course tree**

Run: `find agent-infra-course -maxdepth 2 -type f | sort`
Expected: the original course files are present and ready for expansion

- [ ] **Step 2: Create the new shared directory targets**

Run: `mkdir -p agent-infra-course/assessment`
Expected: assessment directory exists

- [ ] **Step 3: Confirm replacement points for module resources**

Run: `find agent-infra-course -name resources.md | sort`
Expected: one `resources.md` per module, ready to be replaced by `resources/`

### Task 2: Expand the learning documents for every module

**Files:**
- Modify: `agent-infra-course/<module>/README.md`
- Create: `agent-infra-course/<module>/steps.md`
- Create: `agent-infra-course/<module>/exercises.md`
- Delete: `agent-infra-course/<module>/resources.md`
- Create: `agent-infra-course/<module>/resources/README.md`
- Create: `agent-infra-course/<module>/resources/key-resources.md`
- Create: `agent-infra-course/<module>/resources/reading-notes.md`
- Create: `agent-infra-course/<module>/resources/concepts-summary.md`

- [ ] **Step 1: Write the module step guides**

Each `steps.md` must include:

```md
## Step 1
- 要做什么
- 为什么现在做
- 具体动作
- 产出物
- 完成判断
- 常见卡点
```

- [ ] **Step 2: Write the module exercise packs**

Each `exercises.md` must include:

```md
## 概念题
## 应用题
## 排错题
## 设计题
```

- [ ] **Step 3: Replace `resources.md` with a richer `resources/` pack**

Each `resources/` must include:

```md
README.md
key-resources.md
reading-notes.md
concepts-summary.md
```

- [ ] **Step 4: Verify the module document expansion**

Run: `find agent-infra-course -maxdepth 3 -path '*/resources/*' -o -name steps.md -o -name exercises.md | sort`
Expected: every module has the new resources pack plus `steps.md` and `exercises.md`

### Task 3: Add runnable examples for every module

**Files:**
- Create: `agent-infra-course/<module>/examples/README.md`
- Create: `agent-infra-course/<module>/examples/<example>/README.md`
- Create: `agent-infra-course/<module>/examples/<example>/pyproject.toml`
- Create: `agent-infra-course/<module>/examples/<example>/app/*.py`
- Create: `agent-infra-course/<module>/examples/<example>/tests/*.py`

- [ ] **Step 1: Define focused examples per module**

For each module, create 2-5 examples that each demonstrate a single knowledge point:

```md
01-...
02-...
03-...
```

- [ ] **Step 2: Make each example runnable**

Each example must include:

```toml
[project]
name = "..."
dependencies = [...]
```

and a small `app/` plus `tests/`.

- [ ] **Step 3: Add run instructions**

Each example README must include exact commands such as:

```bash
uv run pytest
uv run python -m app.main
```

- [ ] **Step 4: Verify example coverage**

Run: `find agent-infra-course -path '*/examples/*/pyproject.toml' | wc -l`
Expected: multiple runnable examples across modules

### Task 4: Add integrated module services

**Files:**
- Create: `agent-infra-course/<module>/module-service/README.md`
- Create: `agent-infra-course/<module>/module-service/pyproject.toml`
- Create: `agent-infra-course/<module>/module-service/.env.example`
- Create: `agent-infra-course/<module>/module-service/app/*.py`
- Create: `agent-infra-course/<module>/module-service/tests/*.py`

- [ ] **Step 1: Create one service per module**

Service names:

```text
00 starter-workspace
01 llm-gateway
02 support-agent
03 knowledge-agent
04 agent-runtime
05 architecture-lab
06 showcase-pack
```

- [ ] **Step 2: Keep service scope aligned with module goals**

Each service README must clearly explain:

```md
## 功能
## 目录结构
## 如何运行
## 如何测试
```

- [ ] **Step 3: Add the minimal app and test entrypoints**

Each service must include:

```python
def create_app():
    ...
```

or equivalent runnable entrypoints.

- [ ] **Step 4: Verify service scaffolds**

Run: `find agent-infra-course -path '*/module-service/pyproject.toml' | wc -l`
Expected: one runnable service per module

### Task 5: Add the final assessment pack

**Files:**
- Create: `agent-infra-course/assessment/README.md`
- Create: `agent-infra-course/assessment/final-exam.md`
- Create: `agent-infra-course/assessment/final-exam-answers.md`
- Create: `agent-infra-course/assessment/scoring-rubric.md`

- [ ] **Step 1: Write the exam instructions**

Include:

```md
## 适用对象
## 建议时长
## 题型结构
```

- [ ] **Step 2: Write the mixed-format exam**

Include:

```md
## 选择题
## 判断题
## 简答题
## 场景分析题
## 系统设计题
```

- [ ] **Step 3: Write the detailed answer key**

Each answer must include:

```md
正确答案
原因
常见误区
工程判断
```

- [ ] **Step 4: Verify assessment files**

Run: `find agent-infra-course/assessment -type f | sort`
Expected: four assessment files exist

### Task 6: Validate the expanded course

**Files:**
- Modify: `agent-infra-course/README.md` if any links or structure notes are outdated

- [ ] **Step 1: Check the final file tree**

Run: `find agent-infra-course -maxdepth 4 -type f | sort`
Expected: document packs, resources packs, examples, services, and assessment files are all present

- [ ] **Step 2: Spot-check Python project consistency**

Run: `rg -n "name = |dependencies = |pytest|FastAPI|BaseModel|create_app" agent-infra-course`
Expected: examples and services share coherent Python conventions

- [ ] **Step 3: Review for stale references**

Run: `rg -n "resources.md" agent-infra-course`
Expected: no stale references to removed flat resource files
