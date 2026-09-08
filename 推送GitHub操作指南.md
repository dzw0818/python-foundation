# 第一个学习仓库：本地初始化 + 推送到 GitHub

仓库已经在你本地搭好并**通过了冒烟测试**（代码确认能跑）。现在把它变成 GitHub 上的正式项目。

## 一、本地初始化并提交（在你电脑的命令行里执行）

打开终端，进入项目目录（路径按你的实际情况）：

```bash
cd D:/1\ 失业人士的随手日志/学习AI/python-foundation

# 初始化 git 仓库（主线命名为 main）
git init -b main

# 把当前目录所有文件加入暂存区
git add .

# 第一次提交（提交信息建议写英文，专业感更好）
git commit -m "feat: init python-foundation with FastAPI todo app"
```

## 二、在 GitHub 上创建空仓库

网页操作：GitHub → 右上角 `+` → **New repository**

- Repository name: `python-foundation`（和本地文件夹同名，便于对应）
- 描述可写：`AI learning - Phase 1: Python engineering + FastAPI practice`
- **不要**勾选 Add a README（本地已经有了）
- 可见性选 Public（作品集需要公开）
- 点 Create repository

## 三、关联远程仓库并推送

创建完成后 GitHub 会显示命令，按下面的执行（把 `<你的用户名>` 替换为 dzw0818）：

```bash
git remote add origin https://github.com/dzw0818/python-foundation.git
git branch -M main
git push -u origin main
```

## 四、验证

刷新 <https://github.com/dzw0818/python-foundation>，能看到 README、代码、提交记录即成功。

之后每天练习：改代码 → `git add .` → `git commit -m "chore: ..."` → `git push`。
提交信息规范建议：`feat`(新功能) / `fix`(修bug) / `docs`(文档) / `chore`(杂务)。

## 五、（可选）本地跑起来试试

```bash
cd apps/fastapi_todo
pip install -r ../../requirements.txt   # 或用 venv
uvicorn main:app --reload
# 浏览器打开 http://127.0.0.1:8000/docs 可直接在 Swagger 页面点按钮调接口
```

> 提示：如果本地已有 Python 3.10+，建议先 `python -m venv .venv` 建虚拟环境再装依赖。
