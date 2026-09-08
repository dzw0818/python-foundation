# python-foundation

AI 转型学习计划 · 阶段一（基础重建）的代码仓库。

覆盖 Python 工程化进阶与 FastAPI 小服务，为后续 LLM 应用开发（RAG / Agent）打底。

## 目录结构

```
python-foundation/
├── exercises/          # 每日 Python 进阶练习（notebook / 脚本）
├── apps/
│   └── fastapi_todo/   # FastAPI 待办 API（第一个可运行的服务）
├── requirements.txt    # 依赖清单
└── README.md
```

## 快速开始

```bash
# 1. 创建虚拟环境（Windows）
python -m venv .venv
.venv\Scripts\activate

# 2. 安装依赖
pip install -r requirements.txt

# 3. 启动 FastAPI 服务（apps 目录下）
cd apps/fastapi_todo
uvicorn main:app --reload
```

浏览器打开 <http://127.0.0.1:8000/docs> 查看自动生成的接口文档（Swagger UI），
可以直接在页面上试调用接口。

## 练习方式（铁律）

1. 每天至少 1 次 `git commit`，让提交记录可追溯；
2. `exercises/` 下按日期建目录，例如 `exercises/2026-09-08_type_hints/`；
3. 每个练习写 2–3 行"今天学会了什么"的总结，沉淀到笔记仓库。

## 参考

- FastAPI 官方文档: <https://fastapi.tiangolo.com/zh/>
- 学习计划: 见《AI转型学习计划_2026-2028.md》
