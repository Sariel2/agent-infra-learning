# agent-runtime

集成 workflow、trace 与 eval 的最小运行时服务。

## 功能
- 提供一个可运行的最小服务入口
- 以统一工程结构展示本模块关键能力
- 自带基础测试，方便你边学边改

## 目录结构
- `app/main.py`：服务入口
- `app/service.py`：核心逻辑
- `tests/test_main.py`：基础接口与行为测试

## 如何运行
- `uvicorn app.main:app --reload`
- `pytest`
