"""FastAPI 待办 API —— Python 工程化练习：类型注解 / pydantic 校验 / async。

运行方式（在 apps/fastapi_todo 目录下）:
    uvicorn main:app --reload

自动生成的接口文档: http://127.0.0.1:8000/docs
"""

from __future__ import annotations

import time
from typing import Annotated

from fastapi import FastAPI, HTTPException, Path, status
from pydantic import BaseModel, Field

app = FastAPI(title="Todo API", version="0.1.0")


# ---------- 数据模型（pydantic 负责请求/响应校验） ----------
class TodoCreate(BaseModel):
    """创建待办时客户端传入的字段。"""

    title: str = Field(min_length=1, max_length=200, examples=["学完 Transformer"])
    done: bool = False


class Todo(TodoCreate):
    """一条完整的待办记录（在请求字段基础上追加 id 和创建时间）。"""

    id: int
    created_at: float


# ---------- "数据库"：先用内存 dict 代替，后续可平滑换成真实数据库 ----------
_db: dict[int, Todo] = {}
_next_id = 1


def _next_todo_id() -> int:
    global _next_id
    current = _next_id
    _next_id += 1
    return current


# ---------- 路由 ----------
@app.post("/todos", response_model=Todo, status_code=status.HTTP_201_CREATED)
async def create_todo(payload: TodoCreate) -> Todo:
    """新建一条待办。"""
    todo = Todo(id=_next_todo_id(), created_at=time.time(), **payload.model_dump())
    _db[todo.id] = todo
    return todo


@app.get("/todos", response_model=list[Todo])
async def list_todos(done: bool | None = None) -> list[Todo]:
    """列出待办，可按完成状态过滤（?done=true / ?done=false）。"""
    todos = list(_db.values())
    if done is not None:
        todos = [t for t in todos if t.done is done]
    return sorted(todos, key=lambda t: t.created_at, reverse=True)


@app.get("/todos/{todo_id}", response_model=Todo)
async def get_todo(todo_id: Annotated[int, Path(ge=1)]) -> Todo:
    """查询单条待办，不存在返回 404。"""
    todo = _db.get(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail=f"todo {todo_id} 不存在")
    return todo


@app.put("/todos/{todo_id}", response_model=Todo)
async def update_todo(
    todo_id: Annotated[int, Path(ge=1)], payload: TodoCreate
) -> Todo:
    """更新待办的内容或完成状态。"""
    todo = _db.get(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail=f"todo {todo_id} 不存在")
    todo.title = payload.title
    todo.done = payload.done
    return todo


@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: Annotated[int, Path(ge=1)]) -> None:
    """删除一条待办。"""
    if todo_id not in _db:
        raise HTTPException(status_code=404, detail=f"todo {todo_id} 不存在")
    del _db[todo_id]
